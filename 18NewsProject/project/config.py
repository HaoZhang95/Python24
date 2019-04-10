import logging

from redis import StrictRedis


class Config(object):
    """项目配置信息"""
    DEBUG = True

    # 随机产生import base64 >>> base64.b64encode(os.urandom(48))
    SECRET_KEY = 'V6nXzuKzkaJDYFTPiphjyVsIrHW7MVlHDC2Wwe4GyqY9B8prKhr8d6bfW7sWQHh6'

    # 数据库的配置信息
    SQLALCHEMY_DATABASE_URI = "mysql://root:haozhang@127.0.0.1:3306/information_news"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 在请求结束后，那么sqlchemy会自动执行一次db.session.commit()去更新模型的变化在数据库中，不需要手动
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    """
        session的建立过程：
        真正的session建立cookie注入是来自于这个方法CSRFProtect(app)，或者在session['xxx']=yyy赋值的时候也能建立
        
        1- 设置app.secret_key的值，并且在调用session['xxx'] = yyy赋值的时候才会在浏览器中存放session_id到cookie
            并不是只要设置了secret——key就会访问页面建立session链接。
        2- 这里修改了默认的session存储位置为redis，默认存储的位置就是服务器内存中，只要服务器关闭客户存储的session就会消失
        3- Flask-session插件是配合redis使用的，在第二步修改了session的存储位置后，调用Flask-Session中的Session(app)
            来将session存储到redis中
    
    """
    # session保存配置，这个StrictRedis用来保存的是session到redis中
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


# 根据不同的配置来设置不同的运行环境
# 来使用命令的方式指定app.config.from_object(XXX)中的值
class DevelopmentConfig(Config):
    DEBUG = True


# 比如，线上模式的话，可以使用不同的数据库
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:haozhang@127.0.0.1:3306/information_news"
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
}
