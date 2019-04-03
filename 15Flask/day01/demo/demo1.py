from flask import Flask, request, json, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/demo1')
def demo1():
    return 'demo1'


# 使用尖括号来包含传入的参数和规定的类型, 之间不能有空格
# 视图函数接收的参数，没有Int的话1234是str的格式, int=IntegerConverter 去处理 url 传入的参数
@app.route('/demo1/<int:user_id>')
def demo2(user_id):
    return 'demo1 %s' % user_id


# 设置该路由的请求方式, 路由中默认存在一个request对象
@app.route('/demo3', methods=['POST', 'GET'])
def demo3():
    return 'demo3 %s' % request.method


@app.route('/demo4')
def demo4():

    json_dict = {
        'name': 'zhangsan',
        'age': 18

    }

    # 使用falsk.json包下的dumps方法把一个字典对象转换为json格式的字符串
    json_str = json.dumps(json_dict)

    # 使用laod方法把json格式的字符串转换为一个字典对象
    # dict_obj = json.load('{ "name": "zhangsan","age": 18}')

    # json.dunps返回的json字符串在浏览器中Content-type是text/html
    # 但是使用jsonify来处理字典对象的话返回的也是str，但是浏览器的content-type就变成了application/json
    return jsonify(json_dict)


# 直接使用redirect函数进行重定向
# 重定向的反向解析：使用重定向路由的视图函数名字url_for(XXX),并且携带参数
@app.route('/demo5')
def demo5():
    # return redirect('/demo4')
    return redirect(url_for('demo2', user_id=12))


# falsk中自定义的状态吗，只需要在return中定义第二个参数即可
@app.route('/demo6')
def demo6():
    return 'ok...', 888


if __name__ == '__main__':

    # 打印所存在的路由，默认就会存在一个static的路由
    print(app.url_map)

    app.run()
