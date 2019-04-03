from flask import Flask, request, json, jsonify, redirect, url_for, abort
from werkzeug.routing import BaseConverter

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


"""
    转换器： init方法用来重写regex属性，自定义匹配的正则规则
            to_python方法用来把url路由中用户输入的/demo3/1,2,3转换为一个列表[1,2,3]，方便后台使用
            to_url方法用来重定向的时候，参数传入user_ids=[1,2,3,4]转换为重定向地址的1，2，3，4字符串
"""


class RegexConverter(BaseConverter):
    """自定义的转换器，根据自己的正则表达式,重写父类的regex属性"""
    # 转换器就是用来定义url路由的匹配规则
    regex = "[0-9]{6}"


class RegexConverter1(BaseConverter):
    """自定义的转换器，根据传入的正则来定义转换器"""
    def __init__(self, url_map, *args):
        # 父类处理url_map
        super(RegexConverter1, self).__init__(url_map)
        # 自己重写父类的regex属性
        self.regex = args[0]


class ListConverter(BaseConverter):
    """重写to_python方法用来匹配url中的列表"""
    regex = "(\\d+,?)+\\d$"

    def to_python(self, value):
        # 当匹配到的时候对参数进行处理，进行返回给路由，url参数的二次加工赋值给user_ids
        return value.split(',')

    def to_url(self, value):
        """对url_for的重定向参数进行处理，处理后能够路由匹配，否则的话直接回在地址栏进行encode乱码"""
        return ','.join(str(v) for v in value)


# 注册自己的转换器到app中,命名为re,使用的时候直接re1('正则表达式'):user_id
app.url_map.converters['re'] = RegexConverter
app.url_map.converters['re1'] = RegexConverter1
app.url_map.converters['list'] = ListConverter


# 使用正则匹配路由，使用转换基类baseConverter, 比如int
@app.route('/demo1/<re:user_id>')
def demo1(user_id):
    return 'demo1 %s' % user_id


@app.route('/demo2/<re1("[0-9]{6}"):user_id>')
def demo2(user_id):
    return 'demo2 %s' % user_id


@app.route('/demo3/<list:user_ids>')
def demo3(user_ids):
    return 'demo3 %s' % user_ids


@app.route('/demo4')
def demo4():
    # 不重写to_url的话，那么地址栏不会显示/demo3/[1,2,3,4]，而是把[1,2..]变成乱码，导致不能被匹配
    return redirect(url_for('demo3', user_ids=[1, 2, 3, 4]))


# abort(404)主动抛出制定错误状态吗的错误, 有一个error的参数对象
@app.route('/demo5')
def demo5():
    abort(404)
    return 'demo5'


# 全局补货404状态错误,不仅可以捕获状态码，也可以捕获制定的错误
@app.errorhandler(404)
def demo6(error):
    return '页面不见了...'


@app.errorhandler(ZeroDivisionError)
def demo7(error):
    return '除数为0的错误捕获...'


if __name__ == '__main__':

    app.run()
