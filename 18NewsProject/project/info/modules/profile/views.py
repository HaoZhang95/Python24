from flask import render_template, redirect, g, request, jsonify, current_app, abort

from info import db, constants
from info.models import Category, News, User
from info.modules.profile import profile_blue
from info.utils.common import user_login_data
from info.utils.image_store import storage
from info.utils.response_code import RET


@profile_blue.route('/other_news_list')
def other_news_list():
    # 获取页数
    p = request.args.get("p", 1)
    user_id = request.args.get("user_id")
    try:
        p = int(p)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    if not all([p, user_id]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    try:
        user = User.query.get(user_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询错误")

    if not user:
        return jsonify(errno=RET.NODATA, errmsg="用户不存在")

    try:
        paginate = News.query.filter(News.user_id == user.id).paginate(p, constants.OTHER_NEWS_PAGE_MAX_COUNT, False)
        # 获取当前页数据
        news_li = paginate.items
        # 获取当前页
        current_page = paginate.page
        # 获取总页数
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg="数据查询错误")

    news_dict_li = []

    for news_item in news_li:
        news_dict_li.append(news_item.to_review_dict())
    data = {"news_list": news_dict_li, "total_page": total_page, "current_page": current_page}
    return jsonify(errno=RET.OK, errmsg="OK", data=data)


@profile_blue.route("/other_info")
@user_login_data
def other_info():
    """查询其他人的用户信息"""
    user = g.user

    other_id = request.args.get("user_id")
    if not other_id:
        abort(404)

    # 数据库查询
    try:
        other = User.query.get(other_id)
    except Exception as e:
        current_app.logger.error(e)

    if not other:
        abort(404)

    # 判断当前登录用户是否关注过该用户
    is_followed = False
    if g.user:
        # if other.followers.filter(User.id == user.id).count() > 0:
        if other in user.followed:
            is_followed = True

    data = {
        "is_followed": is_followed,
        "user": g.user.to_dict() if g.user else None,
        "other_info": other
    }

    return render_template("news/other.html", data=data)


@profile_blue.route("/user_unfollow", methods=['POST'])
@user_login_data
def user_unfollow():
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg='未登录')

    # 获取参数
    user_id = request.json.get("user_id")
    # 验证参数
    if not user_id:
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    try:
        other = User.query.get(user_id)
    except Exception as e:
        return jsonify(errno=RET.DBERR, errmsg='数据库查询错误')

    if not other:
        return jsonify(errno=RET.DBERR, errmsg='未查询到该用户')

    # 取消当前关注用户
    if other in user.followed:
        user.followed.remove(other)
    else:
        return jsonify(errno=RET.PARAMERR, errmsg='当前用户还未被关注')

    return jsonify(errno=RET.OK, errmsg='操作成功')


@profile_blue.route("/user_follow")
@user_login_data
def user_follow():
    # 获取页数
    p = request.args.get("p", 1)
    try:
        p = int(p)
    except Exception as e:
        current_app.logger.error(e)
        p = 1

    user = g.user

    follows = []
    current_page = 1
    total_page = 1
    try:
        paginate = user.followed.paginate(p, constants.USER_FOLLOWED_MAX_COUNT, False)
        # 获取当前页数据
        follows = paginate.items
        # 获取当前页
        current_page = paginate.page
        # 获取总页数
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    user_dict_li = []

    for follow_user in follows:
        user_dict_li.append(follow_user.to_dict())

    data = {"users": user_dict_li, "total_page": total_page, "current_page": current_page}
    return render_template('news/user_follow.html', data=data)


@profile_blue.route("/news_list")
@user_login_data
def user_news_list():

    user = g.user

    page = request.args.get("p", 1)
    news_list = []
    current_page = 1
    total_page = 1
    try:
        paginate = News.query.filter(News.user_id == user.id).paginate(page, constants.USER_COLLECTION_MAX_NEWS, False)
        news_list = paginate.items
        current_page = paginate.page
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for news in news_list:
        news_dict_list.append(news.to_review_dict())

    data = {
        "news_list": news_dict_list,
        "current_page": current_page,
        "total_page": total_page,
    }

    return render_template("news/user_news_list.html", data=data)


@profile_blue.route("/news_release", methods=['GET', 'POST'])
@user_login_data
def news_release():

    if request.method == 'GET':
        # 加载新闻分类数据
        categories = []
        try:
            categories = Category.query.all()
        except Exception as e:
            current_app.logger.error(e)

        categories_dict_list = []
        for category in categories:
            categories_dict_list.append(category.to_dict())

        # 去除**最新**这个分类
        categories_dict_list.pop(0)
        return render_template("news/user_news_release.html", data={"categories": categories_dict_list})

    # 1. 获取要提交的数据
    title = request.form.get("title")
    source = "个人发布"
    digest = request.form.get("digest")
    content = request.form.get("content")
    index_image = request.files.get("index_image")
    category_id = request.form.get("category_id")
    # 1.1 判断数据是否有值
    if not all([title, source, digest, content, category_id]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

    # 1.2 尝试读取图片
    try:
        category_id = int(category_id)
        # index_image = index_image.read()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

    # 2. 将标题图片上传到七牛
    # try:
    #     key = storage(index_image)
    # except Exception as e:
    #     current_app.logger.error(e)
    #     return jsonify(errno=RET.THIRDERR, errmsg="上传图片错误")

    # 3. 初始化新闻模型，并设置相关数据
    news = News()
    news.title = title
    news.digest = digest
    news.source = source
    news.content = content
    news.index_image_url = constants.QINIU_DOMIN_PREFIX + "XXX"
    news.category_id = category_id
    news.user_id = g.user.id
    # 1代表待审核状态
    news.status = 1

    # 4. 保存到数据库
    try:
        db.session.add(news)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存数据失败")
    # 5. 返回结果
    return jsonify(errno=RET.OK, errmsg="发布成功，等待审核")


@profile_blue.route("/collection")
@user_login_data
def user_collection():

    # 获取参数
    page = request.args.get("p", 1)

    # 验证参数
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        # 非法页数将设置为1
        page = 1

    # 查询用户收藏的新闻
    user = g.user
    news_list = []
    total_page = 1
    current_page = 1

    try:
        paginate = user.collection_news.paginate(page, constants.USER_COLLECTION_MAX_NEWS, False)
        current_page = paginate.page
        total_page =  paginate.pages
        news_list = paginate.items
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for news in news_list:
        news_dict_list.append(news.to_basic_dict())

    data = {
        "current_page": current_page,
        "total_page": total_page,
        "collections": news_dict_list,
    }

    return render_template("news/user_collection.html", data=data)


@profile_blue.route("/pass_info", methods=['GET', 'POST'])
@user_login_data
def pass_info():
    """一个url根据不同的请求方法去执行不同的动作"""
    if request.method == "GET":
        return render_template('news/user_pass_info.html')

        # 1. 获取到传入参数
    old_password = request.json.get("old_password")
    new_password = request.json.get("new_password")

    if not all([old_password, new_password]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

    # 2. 获取当前登录用户的信息
    user = g.user

    if not user.check_passowrd(old_password):
        return jsonify(errno=RET.PWDERR, errmsg="原密码错误")

    # 更新数据
    user.password = new_password
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存数据失败")

    return jsonify(errno=RET.OK, errmsg="保存成功")


@profile_blue.route("/pic_info", methods=['GET', 'POST'])
@user_login_data
def pic_info():

    user = g.user
    # get请求进行头像的获取
    if request.method == 'GET':
        return render_template('news/user_pic_info.html', data={"user_info": g.user.to_dict()})

    # 获取上传的图片
    try:
        avatar = request.files.get("avatar").read()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 上传头像
    try:
        key = storage(avatar)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.THIRDERR, errmsg="上传头像失败")

    # 保存头像地址到数据库,不要存全链接，方便后期修改
    user.avatar_url = key
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存用户头像错误")

    return jsonify(errno=RET.OK, errmsg="OK", data={"avatar_url": constants.QINIU_DOMIN_PREFIX + key})


@profile_blue.route("/base_info", methods=['GET', 'POST'])
@user_login_data
def base_info():
    """一个url根据不同的请求方法去执行不同的动作"""

    # get请求进行资料的获取
    if request.method == 'GET':
        return render_template('news/user_base_info.html', data={"user_info": g.user.to_dict()})

    # 获取参数
    nick_name = request.json.get("nick_name")
    signature = request.json.get("signature")
    gender = request.json.get("gender")

    # 验证参数
    if not all([nick_name, signature, gender]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    if gender not in ('WOMAN', 'MAN'):
        return jsonify(errno=RET.PARAMERR, errmsg="参数错误")

    # 模型的修改
    user = g.user
    user.nick_name = nick_name
    user.gender = gender
    user.signature = signature

    return jsonify(errno=RET.OK, errmsg="用户信息修改成功")


@profile_blue.route('/info')
@user_login_data
def user_info():

    user = g.user

    if not user:
        return redirect("/")

    data = {
        "user_info": user.to_dict(),
    }
    return render_template("news/user.html", data=data)
