import time
import re

"""
    业务逻辑的拆分，和服务器分开，框架进行中间人
    读取模板信息，返回自定义的前段模板
    open在没有指明参数的话，默认模式是r
"""


# 引用地址有一个坑，open的路径不是以当前mini_framework的路径算，而是以当前运行的py程序算
# 当前运行的是basic01.py所以open的是./当前路径下的template，而不是../富集目录下的templates
# open读取文件的时候，一定要告诉read的编码方式，不然windows当前电脑会以gbk的形式read，会报错
def index():

    with open("../templates/index.html", encoding='UTF-8') as f:
        html_content = f.read()

    return html_content


def center():

    with open("../templates/center.html", encoding='UTF-8') as f:
        html_content = f.read()

    # 使用正则表达式替换显示数据库的真正数据内容
    # {大括号在正则中有特殊含义，使用\{转义，使其显示字符表面的意思
    data = "这是数据库读取的数据..."
    html_content = re.sub(r"\{%content%\}", data, html_content)
    return html_content


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