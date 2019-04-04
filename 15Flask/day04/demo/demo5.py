from flask import Flask, request, jsonify

app = Flask(__name__)


"""
    单元测试：类似于一个手机的组装过程中需要对摄像头，屏幕，硬盘等单元器件进行测试
    asset就是判断一个函数是否返回自己的期望值，true/false
"""


def div(num1, num2):

    # 断言不符合int类型给出的提示抛出AssertError
    assert isinstance(num1, int), '值类型不正确'
    assert isinstance(num2, int), '值类型不正确'

    assert num2 != 0, '除数不能为0'
    return num1/num2


@app.route('/')
def index():

    print(div(100, "HAHA"))

    return 'index'


@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # 判断参数是否为空
    if not all([username, password]):
        result = {
            "errcode": -2,
            "errmsg": "params error"
        }
        return jsonify(result)

    # a = 1 / 0
    # 如果账号密码正确
    # 判断账号密码是否正确
    if username == 'hao' and password == 'zhang':
        result = {
            "errcode": 0,
            "errmsg": "success"
        }
        return jsonify(result)
    else:
        result = {
            "errcode": -1,
            "errmsg": "wrong username or password"
        }
        return jsonify(result)


if __name__ == '__main__':
    app.run()
