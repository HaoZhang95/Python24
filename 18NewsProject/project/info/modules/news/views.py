from flask import render_template, current_app, session, g, abort, request, jsonify

from info import constants, db
from info.models import News, User, Comment, CommentLike
from info.modules.news import news_blue
from info.utils.common import user_login_data
from info.utils.response_code import RET


@news_blue.route('/followed_user', methods=['POST'])
@user_login_data
def followed_user():

    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg='未登录')

    # 获取参数
    user_id = request.json.get("user_id")
    action = request.json.get("action")
    # 验证参数
    if not all([user_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    if action not in ("follow", "unfollow"):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')
    try:
        other = User.query.get(user_id)
    except Exception as e:
        return jsonify(errno=RET.DBERR, errmsg='数据库查询错误')

    if not other:
        return jsonify(errno=RET.DBERR, errmsg='未查询到该新闻作者用户')

    # 用当前用户的关注列表添加一个值
    if action == "follow":
        if other not in user.followed:
            user.followed.append(other)
        else:
            return jsonify(errno=RET.DATAEXIST, errmsg='当前作者已被关注')
    else:
        if other in user.followed:
            user.followed.remove(other)
        else:
            return jsonify(errno=RET.PARAMERR, errmsg='当前用户还未被关注')

    return jsonify(errno=RET.OK, errmsg='操作成功')


@news_blue.route('/comment_like', methods=['POST'])
@user_login_data
def comment_like():
    # 获取用户登陆信息
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg='用户未登陆')

    # 接收参数
    comment_id = request.json.get('comment_id')
    news_id = request.json.get('news_id')
    action = request.json.get('action')

    if not all([news_id, comment_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    if action not in ["add", "remove"]:
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    try:
        news_id = int(news_id)
        comment_id = int(comment_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    # 查询被点赞的评论模型是否存在
    try:
        comment = Comment.query.get(comment_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询错误')

    if not comment:
        return jsonify(errno=RET.NODATA, errmsg='未查询到该评论')

    # 点赞
    if action == "add":
        comment_like_model = CommentLike.query.filter(CommentLike.user_id==user.id,
                                                      CommentLike.comment_id==comment.id).first()

        # 先查询，防止用户知道url接口后多次点赞
        if not comment_like_model:
            comment_like_model = CommentLike()
            comment_like_model.user_id = user.id
            comment_like_model.comment_id = comment_id
            db.session.add(comment_like_model)

            comment.like_count += 1
    else:
        comment_like_model = CommentLike.query.filter(CommentLike.user_id==user.id,
                                                      CommentLike.comment_id==comment.id).first()
        if comment_like_model:
            db.session.delete(comment_like_model)
            # comment_like_model.delete()
            comment.like_count -= 1

    # 下面的try可以不需要，tear——down给完成
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.OK, errmsg='点赞数据库操作失败')

    return jsonify(errno=RET.OK, errmsg='点赞数据库操作成功')


@news_blue.route('/news_comment', methods=['POST'])
@user_login_data
def news_comment():
    """评论新闻或者回复某条的评论"""

    # 获取用户登陆信息
    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg='用户未登陆')

    # 接收参数
    news_id = request.json.get('news_id')
    comment_content = request.json.get('comment')
    parent_id = request.json.get('parent_id')

    if not all([news_id, comment_content]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    try:
        news_id = int(news_id)
        if parent_id:
            parent_id = int(parent_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    # 查询新闻区判断该news_id是否存在
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询错误')

    if not news:
        return jsonify(errno=RET.NODATA, errmsg='未查询到新闻数据')

    # 添加评论到数据库
    comment = Comment()
    comment.user_id = user.id
    comment.news_id = news_id
    comment.content = comment_content
    if parent_id:
        comment.parent_id = parent_id

    # 添加到数据库
    # 因为在return之前需要用到comment的id(用于显示前段评论是否嵌套),因为自动的commit_tear_down是发生在return之后
    # 因为是在数据库插入一个新的模型，而不是get获取，所以甭能直接返回comment=comment，因为这样的话前段只知道comment的user_id和comemnt.comment_content
    # comment表因为是子关联的所以其id很重要，需要在return之前获取该comment
    try:
        db.session.add(comment)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
        return jsonify(errno=RET.DBERR, errmsg="保存评论数据失败")

    return jsonify(errno=RET.OK, errmsg="评论成功", data=comment.to_dict())


@news_blue.route('/news_collect', methods=['POST'])
@user_login_data
def collect_news():

    user = g.user
    if not user:
        return jsonify(errno=RET.SESSIONERR, errmsg='用户未登陆')

    # 接受参数, get请求使用的是request.args.get, post请求使用的是request.json.get()
    news_id = request.json.get('news_id')
    action = request.json.get('action')

    if not all([news_id, action]):
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    if action not in ["collect", "cancel_collect"]:
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    try:
        news_id = int(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.PARAMERR, errmsg='参数错误')

    # 查询新闻区判断该news_id是否存在
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询错误')

    if not news:
        return jsonify(errno=RET.NODATA, errmsg='未查询到新闻数据')

    # 收藏
    if action == "collect":
        if news not in user.collection_news:
            user.collection_news.append(news)
    else:
        if news in user.collection_news:
            user.collection_news.remove(news)

    return jsonify(errno=RET.OK, errmsg='操作成功')


@news_blue.route('/<int:news_id>')
@user_login_data
def news_detail(news_id):

    # 如果用户已经登陆，将登陆的数据传递到模板中
    user = g.user

    # 右侧的点击排行
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for model in news_list:
        news_dict_list.append(model.to_basic_dict())

    # 查询新闻详情,get方法默认就是根据该数据模型的id去查询的
    news = None

    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)

    if not news:
        abort(404)

    # 更新新闻的点击次数, 因为设置了Commit_tear_down自动更新数据库的数据模型
    news.clicks += 1

    # 判断用户是否收藏了该新闻
    is_collected = False

    if user:
        # 这里不需要user.collection_news.all()，因为模型中使用了lazy，用到的时候自动查询所有，不过加上也行
        if news in user.collection_news:
            is_collected = True

    # 查询评论数据
    comments = []
    try:
        comments = Comment.query.filter(Comment.news_id==news_id).order_by(Comment.create_time.desc()).all()
    except Exception as e:
        current_app.logger.error(e)

    # 查询用户在当前新闻中都点赞了哪些评论
    comment_like_ids = []
    if g.user:
        # 1. 查询当前新闻评论的所有comment_ids
        comment_ids = [comment.id for comment in comments]
        # 2. 查询当前新闻评论下进行过滤，选择那些当前新闻的评论，并且点击人id就是user.id
        comment_likes = CommentLike.query.filter(CommentLike.comment_id.in_(comment_ids),
                                                                            CommentLike.user_id == g.user.id).all()
        # 3. 第二步得到的是CommentLike模型，因为是多对多，所以根据模型获得被点赞的comment模型的id
        comment_like_ids = [comment_like.comment_id for comment_like in comment_likes]

    comments_dict_list = []
    for comment in comments:
        comment_dict = comment.to_dict()

        # 设置每条评论的点赞状态
        comment_dict['is_like'] = False

        if comment.id in comment_like_ids:
            comment_dict['is_like'] = True

        comments_dict_list.append(comment_dict)

    # 如果当前新闻有作者，并且当前登录用用户已关注这个用户
    is_followed = False

    if news.user and user:
        if news.user in user.followed:
            is_followed = True

    data = {
        "user_info": user.to_dict() if user else None,
        "news_dict_list": news_dict_list,
        "news": news.to_dict(),
        "is_collected": is_collected,
        "comments": comments_dict_list,
        "is_followed": is_followed,
    }

    # 因为details.html继承自base.html，而base.html中使用了data数据，不传递的话渲染子模板的话会报错
    return render_template("news/detail.html", data=data)
