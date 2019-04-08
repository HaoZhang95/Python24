from info.modules.index import index_blue


@index_blue.route('/')
def index():
    # 这个session是flask自带的session
    # session['name'] = 'Hao'

    # 测试打印日志，使用python中的logging模块
    # logging.debug('测试debug')
    # logging.warning('测试warning')
    # logging.error('测试error')
    # logging.fatal('测试fatal')

    # flask种的logger输出日志
    # current_app.logger.error('flask中的测试error')
    return 'Hello World!'
