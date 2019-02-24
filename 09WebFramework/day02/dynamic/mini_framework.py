import time
import re
import pymysql

"""
    业务逻辑的拆分，和服务器分开，框架进行中间人
    读取模板信息，返回自定义的前段模板
    open在没有指明参数的话，默认模式是r
"""
#
# url_func_dict = {
#     # 字典的方式，比较好一点，但是使用装饰器的话会更简洁
#     "/index.html": index,
#     "/center.html": center,
#     "/login.html": login
# }


url_func_dict = dict()


def route(url):
    def set_func(func):
        # "/index.html" --> index()方法的引用
        # 这样不再需要手动定义并且添加字典了
        url_func_dict[url] = func

        # 因为在application函数中调用的是dict[path_info]()来调用的，而不是直接index()调用的
        # 所以下面的代码可以省略，直接调用字典中的方法引用即可

        # def call_func(*args, **kwargs):
        #     return func(*args, **kwargs)
        # return call_func
    return set_func


# 引用地址有一个坑，open的路径不是以当前mini_framework的路径算，而是以当前运行的py程序算
# 当前运行的是basic01.html所以open的是./当前路径下的template，而不是../富集目录下的templates
# open读取文件的时候，一定要告诉read的编码方式，不然windows当前电脑会以gbk的形式read，会报错
@route("/index.html")       # 更改.py为.html为伪静态url
def index():

    with open("../templates/index.html", encoding='UTF-8') as f:
        html_content = f.read()

    # 查询mysql
    db = pymysql.connect(host='localhost',port=3306,user='root',password='haozhang',database='stock_db',charset='utf8')
    cursor = db.cursor()
    sql = """select * from info;"""
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()
    cursor.close()
    db.close()

    # 将mysql中的数据替换到模板中,fetchAll取出的是元组，直接sub会报错，需要转换为str
    line_html = """
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>
                        <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007">
                    </td>
                </tr>
    """
    code_html = ""
    for temp in data_from_mysql:
        code_html += line_html % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7])

    html_content = re.sub(r"\{%content%\}", code_html, html_content)

    # 返回数据
    return html_content


# 第一步将center.html作为实参执行route()函数，返回的是set_func代码块
# 第二部center = set_func(center)，返回的是一个闭包，里面包含call_func，并且对dict添加了一个key-value
# 第三部，当在application中调用的时候，call_func调用，返回的是func(参数)，也就是center(参数)方法被执行
@route("/center.html")
def center():

    with open("../templates/center.html", encoding='UTF-8') as f:
        html_content = f.read()

    # 使用正则表达式替换显示数据库的真正数据内容
    # {大括号在正则中有特殊含义，使用\{转义，使其显示字符表面的意思
    data = "这是数据库读取的数据..."
    html_content = re.sub(r"\{%content%\}", data, html_content)
    return html_content


@route("/register.html")
def register():
    return "----注册主页----current time is %s" % time.ctime()


@route("/login.html")
def login():
    return "----登陆主页----current time is %s" % time.ctime()


def application(env, set_header):
    """使其mini框架符合WSGI协议, 通过路由的形式处理界面，代替if/else"""
    # 调用set_header指向的函数，将response_header传递进去
    # 框架中设置参数，将这些参数返回给web服务器调用自己的set_header方法处理
    status = "200 OK"
    response_headers = [("Content-Type", "text/html; charset=UTF-8")]
    set_header(status, response_headers)

    path_info = env["PATH_INFO"]

    try:

        # 打印url_func_dict验证是否通过装饰器添加了key-value
        print(url_func_dict)
        response_body = url_func_dict[path_info]()
    except Exception as e:
        response_body = "----Not Found----current time is %s" % time.ctime()

    # 通过return将body返回
    return response_body