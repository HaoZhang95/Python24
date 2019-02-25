import time
import re
import urllib

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
@route(r"/index\.html$")       # 更改.py为.html为伪静态url
def index(ret):

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
                        <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
                    </td>
                </tr>
    """
    code_html = ""
    for temp in data_from_mysql:
        code_html += line_html % (temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[0])

    html_content = re.sub(r"\{%content%\}", code_html, html_content)

    # 返回数据
    return html_content


# 第一步将center.html作为实参执行route()函数，返回的是set_func代码块
# 第二部center = set_func(center)，返回的是一个闭包，里面包含call_func，并且对dict添加了一个key-value
# 第三部，当在application中调用的时候，call_func调用，返回的是func(参数)，也就是center(参数)方法被执行
@route(r"/center\.html$")
def center(ret):

    with open("../templates/center.html", encoding='UTF-8') as f:
        html_content = f.read()

    # 查询mysql
    db = pymysql.connect(host='localhost',port=3306,user='root',password='haozhang',database='stock_db',charset='utf8')
    cursor = db.cursor()
    sql = """select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i
            inner join focus as f on i.id=f.info_id;"""
    cursor.execute(sql)
    data_from_mysql = cursor.fetchall()
    cursor.close()
    db.close()

    # 这是一行的模板
    line_html = """<tr>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>%s</td>
                        <td>
                        <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
                        </td>
                        <td>
                        <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
                        </td>
                    </tr>
                """

    code_html = ""
    for temp in data_from_mysql:
        code_html += line_html % (temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6], temp[0], temp[0])

    # 3. 替换数据
    html_content = re.sub(r"\{%content%\}", code_html, html_content)

    return html_content


@route(r"/register\.html$")
def register(ret):
    return "----注册主页----current time is %s" % time.ctime()


@route(r"/login\.html$")
def login(ret):
    return "----登陆主页----current time is %s" % time.ctime()


# @route("/add/000007.html")
# def add_focus():
#     return "----添加关注页----current time is %s" % time.ctime()

# 使用正则表达式，匹配不同的url，使用正则分组获取股票代码
# 所有带有装饰器的函数，都需要加上ret一个参数，或者使用不定长参数，接受匹配上的path
@route(r"^/add/(\d+)\.html$")
def add_focus(ret):

    # 获取股票代码
    stock_code = ret.group(1)

    # 判断这只股票是否存在
    db = pymysql.connect(host='localhost',port=3306,user='root',password='haozhang',database='stock_db',charset='utf8')
    cursor = db.cursor()
    sql = """select * from info where code=%s"""
    cursor.execute(sql, [stock_code])
    data_from_sql = cursor.fetchall()
    if not data_from_sql:
        cursor.close()
        db.close()
        return "没有这只股票..."

    # 判断是否已经关注了此股票
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cursor.execute(sql, [stock_code])
    data_from_sql = cursor.fetchall()
    if data_from_sql:
        cursor.close()
        db.close()
        return "请误重复关注...."

    # 写入数据到mysql
    # 除了查询意外，python操作数据库都需要commit生效,查询需要fetch
    sql = """insert into focus (info_id) select id from info where code=%s"""
    cursor.execute(sql, [stock_code])
    db.commit()
    cursor.close()
    db.close()

    return "----添加关注成功----"


# 删除对应的股票代码
@route(r"^/del/(\d+)\.html$")
def del_focus(ret):

    # 获取股票代码
    stock_code = ret.group(1)

    # 删除股票
    db = pymysql.connect(host='localhost',port=3306,user='root',password='haozhang',database='stock_db',charset='utf8')
    cursor = db.cursor()

    # 2. 判断是否有这支股票
    sql = """select * from info where code=%s;"""
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchall()
    if not data_from_mysql:
        # 如果要是没有这个股票，那么就退出
        cursor.close()
        db.close()
        return "没有这支股票...."

    # 3. 判断是否之前关注过这支股票
    sql = """select * from info as i inner join focus as f on i.id=f.info_id where i.code=%s;"""
    cursor.execute(sql, [stock_code])
    data_from_mysql = cursor.fetchall()
    if not data_from_mysql:
        # 如果之前没有关注过这个股票，那么就退出
        cursor.close()
        db.close()
        return "请先关注，然后在取消关注...."

    # 4. 删除股票对应的关注信息
    sql = """delete from focus where info_id = (select id from info where code=%s);"""
    cursor.execute(sql, [stock_code])
    db.commit()
    cursor.close()
    db.close()

    return "----删除关注成功----"


@route(r"^/update/(\d+)\.html$")
def show_edit_noteinfo_page(ret):

    # 提取股票代码
    stock_code = ret.group(1)

    # 1- 打开模板
    with open("../templates/update.html", encoding='UTF-8') as f:
        html_content = f.read()

    # 2- 从数据库中查找股票的备注信息
    db = pymysql.connect(host='localhost',port=3306,user='root',password='haozhang',database='stock_db',charset='utf8')
    cursor = db.cursor()
    sql = """select note_info from focus where info_id=(select id from info where code=%s);"""
    cursor.execute(sql, [stock_code])
    # data_from_mysql = cursor.fetchall()  # ((备注信息,),)
    data_from_mysql = cursor.fetchone()  # (备注信息,)
    cursor.close()
    db.close()

    # 3- 打合并数据
    html_content = re.sub(r"\{%note_info%\}", data_from_mysql[0], html_content)
    html_content = re.sub(r"\{%code%\}", stock_code, html_content)

    # 4- 返回数据给http服务器
    return html_content


@route(r"/update/(\d+)/(.*)\.html")
def save_edit_noteinfo(ret):
    # 1. 提取股票代码以及备注信息
    stock_code = ret.group(1)  # 股票代码

    # 因为浏览器url编码问题，防止存入数据库中文乱码问题
    # 浏览器和服务器通信时http协议中规定将地址栏中的中文按照**url编码**转换为乱码
    # quote("中文") --> url编码形式的乱码
    # unquote("url编码形式的乱码 ") --> 中文
    note_info = urllib.parse.unquote(ret.group(2))  # 备注

    # 2. 修改数据
    conn = pymysql.connect(host='localhost',port=3306,user='root',password='mysql',database='stock_db',charset='utf8')
    cursor = conn.cursor()
    sql = """update focus as f inner join info as i on i.id=f.info_id set f.note_info=%s where i.code=%s;"""
    cursor.execute(sql, [note_info, stock_code])
    conn.commit()
    cursor.close()
    conn.close()

    return "修改备注成功..."


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
        # 此时的字典样子如下: {
        #     r"/add/\d+\.html": add_focus,
        #     r"/index\.html": index,
        # }

        for r_url, func in url_func_dict.items():
            ret = re.match(r_url, path_info)
            if ret:
                response_body = func(ret)       # 将匹配出来的/add/00822.html作为参数传递，用来获取股票代码
                break
        else:
            # else属于for循环的，找不到url
            response_body = "----Not Found 这个url----"

        # 因为add方法中装饰器参数为正则表达式，字典中的key是r"/add/\d+\.html"，是不可能匹配到任何的"/add/00822\.html"的
        # url_func_dict[path_info]永远找不到add_focus函数，所以正确的是使用re匹配
        # print(url_func_dict)
        # response_body = url_func_dict[path_info]()
    except Exception as e:
        response_body = "----Not Found----current time is %s" % time.ctime()

    # 通过return将body返回
    return response_body





