import time
from datetime import datetime, timedelta

from flask import render_template, request, current_app, session, redirect, url_for, g

from info import constants
from info.models import User, News
from info.modules.admin import admin_blue
from info.utils.common import user_login_data


@admin_blue.route('/news_review_detail/<int:news_id>')
def news_review_detail(news_id):

    # 通过id查询新闻
    news = None
    try:
        news = News.query.get(news_id)
    except Exception as e:
        current_app.logger.error(e)

    if not news:
        return render_template('admin/news_review_detail.html', data={"errmsg": "未查询到此新闻"})

    # 返回数据
    data = {"news": news.to_dict()}
    return render_template('admin/news_review_detail.html', data=data)


@admin_blue.route('/news_review')
def news_review():
    """返回待审核新闻列表"""

    page = request.args.get("p", 1)
    keywords = request.args.get("keywords", None)
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    news_list = []
    current_page = 1
    total_page = 1

    filters = [News.status != 0]
    if keywords:
        filters.append(News.title.contains(keywords))

    try:
        # *args就是把列表中的[A,B]放在参数中(A,B)
        paginate = News.query.filter(*filters) \
            .order_by(News.create_time.desc()) \
            .paginate(page, constants.ADMIN_NEWS_PAGE_MAX_COUNT, False)

        news_list = paginate.items
        current_page = paginate.page
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for news in news_list:
        news_dict_list.append(news.to_review_dict())

    data = {"total_page": total_page, "current_page": current_page, "news_list": news_dict_list}

    return render_template('admin/news_review.html', data=data)


@admin_blue.route('/user_list')
def user_list():

    page = request.args.get("p", 1)
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    user_model_list = []
    current_page = 1
    total_page = 1

    try:
        paginate = User.query.filter(User.is_admin == False).paginate(page, constants.ADMIN_USER_PAGE_MAX_COUNT, False)
        user_model_list = paginate.items
        current_page = paginate.page
        total_page = paginate.pages
    except Exception as e:
        current_app.logger.error(e)

    user_dict_list = []
    for user in user_model_list:
        user_dict_list.append(user.to_admin_dict())

    data = {
        "users": user_dict_list,
        "current_page": current_page,
        "total_page": total_page,
    }

    return render_template("admin/user_list.html", data=data)


@admin_blue.route('/user_count')
def user_count():

    total_count = 0
    mon_count = 0
    day_count = 0

    # 总人数
    try:
        total_count = User.query.filter(User.is_admin == False).count()
    except Exception as e:
        current_app.logger.error(e)

    # 月增用户
    try:
        now = time.localtime()
        mon_begin = '%d-%02d-01' % (now.tm_year, now.tm_mon)
        mon_begin_date = datetime.strptime(mon_begin, '%Y-%m-%d')
        mon_count = User.query.filter(User.is_admin == False, User.create_time >= mon_begin_date).count()
    except Exception as e:
        current_app.logger.error(e)

    # 日增用户
    try:
        now = time.localtime()
        day_begin = '%d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday)
        day_begin_date = datetime.strptime(day_begin, '%Y-%m-%d')
        day_count = User.query.filter(User.is_admin == False, User.create_time >= day_begin_date).count()
    except Exception as e:
        current_app.logger.error(e)

    # 折线图数据,从今天开始算之前31天的数据
    active_date = []
    active_count = []
    now_date = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')

    # 依次添加数据，再反转
    for i in range(0, 31):
        begin_date = now_date - timedelta(days=i)       # 2019-04-14 00:00:00
        end_date = now_date - timedelta(days=(i - 1))   # 2019-04-15 00:00:00
        active_date.append(begin_date.strftime('%Y-%m-%d'))  # 将时间对象转换为str
        count = 0
        try:
            count = User.query.filter(User.is_admin == False, User.last_login >= begin_date,
                                      User.last_login < end_date).count()
        except Exception as e:
            current_app.logger.error(e)

        active_count.append(count)

    active_date.reverse()
    active_count.reverse()

    data = {
        "total_count": total_count,
        "mon_count": mon_count,
        "day_count": day_count,
        "active_date": active_date,
        "active_count": active_count,
    }
    return render_template("admin/user_count.html", data=data)


@admin_blue.route('/index')
@user_login_data
def index():
    user = g.user
    return render_template("admin/index.html", user=user.to_dict())


@admin_blue.route('/login', methods=['GET', 'POST'])
def login():
    """因为后台的login需要登陆成功后跳转页面，所以不需要ajax局部刷新"""

    if request.method == 'GET':
        # 判断是否已经登陆，登陆的话直接跳转到index
        user_id = session.get('user_id', None)
        is_admin = session.get('is_admin', False)

        if user_id and is_admin:
            return redirect(url_for('admin.index'))
        return render_template("admin/login.html")

    # 获取参数，没用到ajax使用的是html中的form表单
    username = request.form.get('username')
    password = request.form.get('password')

    # 验证参数，因为没用到ajax，所以不能返回一个jsonify
    if not all([username, password]):
        return render_template("admin/login.html", errmsg="参数错误")

    # 数据库查询
    try:
        user = User.query.filter(User.mobile == username, User.is_admin == True).first()
    except Exception as e:
        current_app.logger.error(e)
        return render_template("admin/login.html", errmsg="用户信息查询失败")

    if not user:
        return render_template("admin/login.html", errmsg="未查询到用户信息")

    if not user.check_passowrd(password):
        return render_template("admin/login.html", errmsg="用户名或者密码错误")

    # 保存用户信息
    session['user_id'] = user.id
    session['mobile'] = user.mobile
    session['nick_name'] = user.nick_name
    session['is_admin'] = user.is_admin

    return redirect(url_for('admin.index'))