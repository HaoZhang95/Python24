from flask import Flask, session, render_template

# 创建一个Flask实例对象
from flask_session import Session
from redis import StrictRedis
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__,   # 决定Flask所对应的模板/静态文件从哪个位置开始找，__name__表示从当前模块中找
            static_url_path='/python27',    # 类似于django设置中的static-urls用来隐藏真实的静态文件目录
            static_folder='static',     # 默认存放的静态文件目录
            template_folder='templates'     # 模板的存放地址
            )


class Config(object):
    # 注意在falsk 1.0之后，这种方法失效，只能在右上角编辑环境中设置debug和端口等信息
    DEBUG = True

    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host="127.0.0.1", port=6379)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2


# ===========FLASK从对象中加载配置=============
app.config.from_object(Config)
app.secret_key = 'Hao'
CSRFProtect(app)
Session(app)

# ===========FLASK从文件中加载配置, ini格式=============
# app.config.from_pyfile('config.ini')


# ===========FLASK从环境中加载配置(了解)=============
# app.config.from_envvar('')

# 一般常用的配置信息，可以直接通过属性的方式设置
# 默认是线上模式，开启debug之后，可以实时更改不需要重启，可以看到报错信息
# app.debug = True
# app.config['DEBUG'] = True


# 使用@app装饰器来和视图函数hello_world进行关联
@app.route('/')
def hello_world():
    # session['user_id'] = '888'
    # user_id = session.get('user_id', None)

    data = {
        'user': 'Hao'
    }
    print(app.config['DEBUG'])
    print(session)
    return render_template('news/test.html', data=data)


if __name__ == '__main__':
    app.run()
    # app.run(host='192.168.1.102', port=8000, debug=True)
