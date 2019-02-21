"""
    WSGI就是一种服务器和web框架之间的规定协议，插座和插头的关系

    不修改服务器和架构代码而确保可以在多个架构下运行web服务器呢？
    答案就是 Python Web Server Gateway Interface (或简称 WSGI，读作“wizgy”)。

    主要就是WSGI允许开发者将选择web框架和web服务器分开
    Nginx服务器，apache服务器可以运行django， flask等不同的框架，这些框架可以动态的返回响应体response_body
"""

"""
    web服务器调用web框架,
    第一个参数目的是传递浏览器信息给web框架，以字典的形式告诉web框架path_info等信息，让web框架返回不同的界面
    第二个参数是服务器不知道返回的界面是否成功等信息，无法确定响应头，比如返回的状态码，通知浏览器的解析方式等等，
    所以将服务器的方法名传递给web框架，在web框架中得知具体的响应头信息后，以参数的形式调用web服务器的set_header方法，进行web服务器的响应头拼接
"""


def application(env, set_header):
    pass