from flask import Flask, request, make_response, session, redirect, url_for

app = Flask(__name__)
# 设置session必须设置key
app.secret_key = 'Hao'

@app.route('/')
def hello_world():
    user_id = request.cookies.get('user_id')

    return 'Hello World! %s ' % user_id


# 处理上传的数据使用request,一定要使用post
# request可以获得的data,file,method等属性
@app.route('/demo1', methods=['POST'])
def demo1():
    file = request.files.get('pic')
    file.save('aaa.png')
    return 'ok...'


@app.route('/demo2')
def demo2():
    # 使用make_response函数返回一个response对象，不再返回一个str
    resp = make_response('success')
    # 通过res设置cookies,中间逗号隔开, 1个小时过期时间设置， delete_cookie('user_id')来删除cookie
    resp.set_cookie('user_id', '88', max_age=3600)
    return resp


@app.route('/demo3')
def demo3():
    # 访问该路由返回在服务器session中保存的username
    # session依赖于cookie的原因是session_id
    return "欢迎 %s " % session.get('username', '')


@app.route('/demo31')
def demo31():
    # 在服务器session保存username等敏感信息
    # 设置session之前需要给app设置app.secret_key = 'Hao'
    session['username'] = '张三'
    return redirect(url_for('demo3'))


@app.route('/demo32')
def demo32():
    # 删除服务器端的session.pop(), 没有username的话直接返回none
    session.pop('username', None)
    return redirect(url_for('demo3'))


if __name__ == '__main__':
    app.run()
