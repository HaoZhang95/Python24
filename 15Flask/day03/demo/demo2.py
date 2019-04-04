import base64
import os

from flask import Flask

app = Flask(__name__)
app.config['WTF_CSRF_ENABLED'] = True


"""
    CSRF伪造流程：1- 用户登录信任的网站，验证通过后信任网站给用户设置官方cookie
        2- 用户在没有登出的情况下，访问了不安全的网站，该网站会发送一个请求要求用户访问那个受信任的网站(带着恶意的参数或者修改了转账地址)
        3- 客户端会根据伪造的请求带着官方的cookie引狼入室，但是网站并不知道该请求的来源，达到模拟用户操作的目的

    在请求后服务器设置cookkie中会包含CSRF-TOKEN，同样的表单中也会有一个隐藏的input标签，value也是这个token
    两个token进行比较，一样的话表示正常操作
    
    1- 模板中添加<input type="hidden" name="csrf_token" value="{{ csrf_token }}">
    2- 基于base64产生一个csrf，传入到模板中的隐藏input
    4- 回复的resp中把token添加到cookie中
    3- 在视图函数中判断请求网页中的隐藏input的token和携带cookie中的csrf是否相等
    
    flask中只需要在form中添加wtforms中的实例对象的token方法即可{{ register_form.csrf_token() }}
    
"""


def generate_csrf():
    return bytes.decode(base64.b64decode(os.urandom(48)))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
