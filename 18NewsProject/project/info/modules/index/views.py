from flask import render_template, current_app, session, request, jsonify, g

from info import constants
from info.models import User, News, Category
from info.modules.index import index_blue
from info.utils.common import user_login_data
from info.utils.response_code import RET


@index_blue.route('/news_list')
def news_list():
    # 获取参数
    cid = request.args.get("cid", "1")
    page = request.args.get("page", "1")
    per_page = request.args.get("per_page", "10")

    # 验证参数
    try:
        cid = int(cid)
        page = int(page)
        per_page = int(per_page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1
        per_page = 10

    # 默认加载cid=1的新闻，如果用户点击种类cid=2，那么就添加一个过滤器列表
    filters = [News.status == 0]
    if cid != 1:
        filters.append(News.category_id == cid)

    # 查询数据，使用传入一个过滤器列表, 并且分页
    try:
        paginate = News.query.filter(*filters).order_by(News.create_time.desc()).paginate(page, per_page, False)
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DBERR, errmsg='数据查询错误')

    news_model_list = paginate.items
    current_page = paginate.page
    total_pages = paginate.pages

    news_dict_list = []
    for news in news_model_list:
        news_dict_list.append(news.to_basic_dict())

    data = {
        "current_page": current_page,
        "total_pages": total_pages,
        "news_dict_list": news_dict_list,
    }

    return jsonify(errno=RET.OK, errmsg="OK", data=data)


@index_blue.route('/')
@user_login_data
def index():
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

    # 查询分类数据
    try:
        category_list = Category.query.all()
    except Exception as e:
        current_app.logger.error(e)

    category_dict_list = []
    for category in category_list:
        category_dict_list.append(category.to_dict())

    data = {
        # 如果user不存在的话，那么“user” = None
        "user_info": user.to_dict() if user else None,
        "news_dict_list": news_dict_list,
        "category_dict_list": category_dict_list,
    }

    return render_template('news/index.html', data=data)


@index_blue.route('/favicon.ico')
def favicon():
    # 访问网站图标，send_static_file 是flask系统访问静态文件所调用的方法
    return current_app.send_static_file('news/favicon.ico')
