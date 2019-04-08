from flask import render_template, current_app
from info.modules.index import index_blue


@index_blue.route('/')
def index():
    return render_template('news/index.html')


@index_blue.route('/favicon.ico')
def favicon():
    # 访问网站图标，send_static_file 是flask系统访问静态文件所调用的方法
    return current_app.send_static_file('news/favicon.ico')
