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

    # redis配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session保存配置
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
