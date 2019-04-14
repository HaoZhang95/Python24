import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, render_template, g
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect, generate_csrf
from redis import StrictRedis
from config import config

# 制定session保存的位置，一般保存在redis数据库的nosql数据库
# 注意使用的是扩展中的session，并不是flask中的session，需要添加扩展
from flask_session import Session

db = SQLAlchemy()

# redis_store: StrictRedis = None
redis_store = None  # type: StrictRedis


def setup_log(config_name):
    # 设置日志的记录等级,调试debug级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    # 自建log文件夹，不能把log日志传到github，但是需要上传这个空文件夹，否则报错，所以自建一个.keepgit文件在里面
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):

    # 配置日志，根据不同的模式配置不同的log等级
    setup_log(config_name)

    # 初始化FLASK对象
    # 因为静态文件static目录和当前app的__name__同级，所以不需要额外设置，templates也是
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])
    # 初始化数据库, 需要被manage.py外界访问，需要提取到外面
    # db = SQLAlchemy(app)
    db.init_app(app)

    # 初始化redis，这个StrictRedis是用来保存项目中的K-V，并不是保存session的redis
    global redis_store
    redis_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)

    # 开启csrf保护， 源代码中显示，如果不符合csrf直接return请求
    # 配合ajax的post请求必须在html中设置<meta name="csrf-token" content="{{ csrf_token() }}">
    # 并且在相应的js文件中设置 ，否则ajax的请求一直400 BAD REQUEST
    # var csrftoken = $('meta[name=csrf-token]').attr('content')
    #
    # $.ajaxSetup({
    #     beforeSend: function(xhr, settings) {
    #         if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
    #             xhr.setRequestHeader("X-CSRFToken", csrftoken)
    #         }
    #     }
    # })

    """
        真正的session建立cookie注入是来自于这个方法CSRFProtect(app)，或者在session['xxx']=yyy赋值的时候也能建立
        一个是全局url保护，一个只是部分的
        
        1- Flask-wtf扩展中的CSRF保护，设置在Session(app)之前，因为先产生session_id才能保存在redis中
        2- CSRF的保护会在访问页面的时候，生成session_id进行cookie注入，CSRFProtect开启的话，
        <meta name="csrf-token" content="{{ csrf_token() }}">中的csrf_token()方法的调用是来自CSRFprotect中，也就是来自flask-wtf中
        在html中获取了生成的csrf-token才能在js中进行请求的时候带上token，也就是session_id进行验证，不然400错误码
        
        CSRFProtect(app)做了两件事：1-从cookie中取出随机值  2- 进行验证，返回响应
        我们需要做： 1- 在界面加载的时候，在cookie中设置一个csrf-token  
                    2- 表单提交的时候带上自己生成的token
                    3- 因为我们登陆注册中使用的是ajax请求，并不是表单，所以不需要在表单中添加{{XXX}}，需要在ajax中设置header
        上面的方法也可行，就是meta的那种方法，二选一
    """
    CSRFProtect(app)

    # 设置session保存制定位置
    Session(app)

    # 在蓝图之前添加自定义过滤器,过滤器的import也是何时注册何时调用，否则会循环依赖错误
    # 初始化数据库, 需要被manage.py外界访问，需要提取到外面
    # 在flask中的很多扩展中都可以先初始化对象，然后再去调用init.app方法去关联app
    from info.utils.common import do_index_class
    app.add_template_filter(do_index_class, "index_class")

    # 设置全局的404页面,errorhandler去捕获制定状态吗的错误
    from info.utils.common import user_login_data

    @app.errorhandler(404)
    @user_login_data
    def page_not_found(error):
        user = g.user
        data = {"user_info": user.to_dict() if user else None}
        return render_template('news/404.html', data=data)

    # 响应客户端的时候添加上token到cookie
    @app.after_request
    def after_request(response):
        # 通过flask-wtf中生成csrf
        csrf_token = generate_csrf()
        # 设置cookie
        response.set_cookie("csrf_token", csrf_token)
        # 返回被装饰后的response
        return response

    # 注册蓝图, 如果下面的import放在上面的话，那么卡启动的时候就会报错
    # 因为一个包去导入另一个包然会最后一个views.py去导入redis_store的时候就发现当前的文件还有有执行到redis_store = None
    # 这个循环导入，就会还没定义这个redis_store，因此以后何时注册蓝图，何时导入这个蓝图，蓝图的导入不要放在顶部
    from info.modules.index import index_blue
    app.register_blueprint(index_blue)

    from info.modules.passport import passport_blue
    app.register_blueprint(passport_blue)

    from info.modules.news import news_blue
    app.register_blueprint(news_blue)

    from info.modules.profile import profile_blue
    app.register_blueprint(profile_blue)

    from info.modules.admin import admin_blue
    app.register_blueprint(admin_blue)

    return app
