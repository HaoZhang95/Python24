import time

"""
    业务逻辑的拆分，和服务器分开，框架进行中间人
"""


def index():
    return "----主页----current time is %s" % time.ctime()


def center():
    return "----中心主页----current time is %s" % time.ctime()


def register():
    return "----注册主页----current time is %s" % time.ctime()


"""
    使其mini框架符合WSGI协议
"""


def application(env, set_header):

    # 调用set_header指向的函数，将response_header传递进去
    # 框架中设置参数，将这些参数返回给web服务器调用自己的set_header方法处理
    status = "200 OK"
    response_headers = [("Content-Type", "text/html; charset=UTF-8")]
    set_header(status, response_headers)

    path_info = env["PATH_INFO"]
    if path_info == "/index.py":
        response_body = index()
    elif path_info == "/center.py":
        response_body = center()
    elif path_info == "/register.py":
        response_body = register()
    else:
        response_body = "----Not Found----current time is %s" % time.ctime()

    # 通过return将body返回
    return response_body