from flask import render_template, current_app, session

from info import constants
from info.models import News, User
from info.modules.news import news_blue


@news_blue.route('/<int:news_id>')
def logout(news_id):

    # 如果用户已经登陆，将登陆的数据传递到模板中
    user_id = session.get('user_id', None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    # 右侧的点击排行
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(constants.CLICK_RANK_MAX_NEWS)
    except Exception as e:
        current_app.logger.error(e)

    news_dict_list = []
    for model in news_list:
        news_dict_list.append(model.to_basic_dict())

    data = {
        "user_info": user.to_dict() if user else None,
        "news_dict_list": news_dict_list,
    }

    # 因为details.html继承自base.html，而base.html中使用了data数据，不传递的话渲染子模板的话会报错
    return render_template("news/detail.html", data=data)
