from flask import Flask

app = Flask(__name__)

"""
    Werkzeug工具箱中的routing模块：rule(保存的是视图函数和url路由的关系)
                                Map(包含一大堆rule)
                                BaseConverter(路由的匹配转换器)
                                MapAdapter(负责协调Rule做具体的匹配的工作)
                                others
"""

"""
    请求钩子类似于django中的中间件，避免每个视图函数中都写同样的代码，比如CSRF验证，或者黑名单检查
"""


@app.before_first_request
def before_first_request():
    """在第一次请求之前会访问该函数"""
    print('before_first_request')


@app.before_request
def before_request():
    """在每次请求的之前会触发， 进入视图函数之前"""
    print('before_request')

    # 一旦在before_request中return的话，就不会触发被请求的url的视图函数，例如黑名单的检测就在这里
    # 根据不同的if条件，来return不同的试图
    # return 'HAHAHA...'


@app.after_request
def after_request(response):
    """需要一个response参数进行返回，该参数是视图函数返回的response对象，进入视图函数之后"""
    # 在返回给客户端之前对response进行统一的二次修改，再返回给客户端
    print('after_request')
    return response


@app.teardown_request
def teardown_request(error):
    """在视图函数之中发生异常触发的error，进行统一处理"""
    print('teardown_request %s' % error)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
