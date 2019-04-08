import redis
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# 制定session保存的位置，一般保存在redis数据库的nosql数据库
# 注意使用的是扩展中的session，并不是flask中的session，需要添加扩展
from flask_session import Session
from redis import StrictRedis


class Config(object):
    """项目配置信息"""
    DEBUG = True

    # 随机产生import base64 >>> base64.b64encode(os.urandom(48))
    SECRET_KEY = 'V6nXzuKzkaJDYFTPiphjyVsIrHW7MVlHDC2Wwe4GyqY9B8prKhr8d6bfW7sWQHh6'

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:haozhang@127.0.0.1:3306/information_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session保存配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开启csrf保护， 源代码中显示，如果不符合csrf直接return请求
CSRFProtect(app)
# 设置session保存制定位置
Session(app)


@app.route('/')
def index():
    # 这个session是flask自带的session
    session['name'] = 'Hao'
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
