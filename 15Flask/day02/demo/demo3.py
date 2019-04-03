from flask import Flask, request, current_app
from flask_script import Manager

app = Flask(__name__)

"""
    flask-script用来使用命令行的方式传入参数配置app.run,此时不能使用pycharm运行了
    使用flask-script中的manager对象来关联app和Manager(app)，把当前app传入到manager，并且启动manager.run

"""


manager = Manager(app)


"""
    请求上下文：用来保存浏览器和服务器之间的数据，request和session
    应用上下文：保存一些app的config配置信息，数据库连接等，
                也就是应用的属性信息，类似于app的全局变量， current_app和g变量
"""


@app.route('/')
def hello_world():
    """上下文：请求上下文和应用上下文，相当于一个容器，保存flask运行的数据"""

    # 上下文中包含了请求前后的相关数据并且封装成了对象，请求上下文的意思是只有在请求发生的时候才会保存前后文
    # 比如request和session对象
    print(request.url)

    # 应用上下文current_app，应用run之后才会有相应的数据对象，但是应用上下文并不是一值存在的
    # 使用应用上下文获取config信息，只能在app.run之后才能获取应用上下文
    print(current_app.config['DEBUG'])

    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
