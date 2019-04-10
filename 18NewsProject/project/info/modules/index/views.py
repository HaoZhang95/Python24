from flask import render_template, current_app, session

from info.models import User
from info.modules.index import index_blue


@index_blue.route('/')
def index():
    # 如果用户已经登陆，将登陆的数据传递到模板中
    user_id = session.get('user_id', None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    data = {
        # 如果user不存在的话，那么“user” = None
        "user_info": user.to_dict() if user else None,
    }

    return render_template('news/index.html', data=data)


@index_blue.route('/favicon.ico')
def favicon():
    # 访问网站图标，send_static_file 是flask系统访问静态文件所调用的方法
    return current_app.send_static_file('news/favicon.ico')
