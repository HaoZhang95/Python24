from flask import Flask

from cart import cart_blue
from demo import demo4

app = Flask(__name__)

# 把order相关的蓝图注册到app上
app.register_blueprint(demo4.order_blue)
app.register_blueprint(cart_blue)


@app.route('/')
def index():
    return 'index'


@app.route('/list')
def list():
    return 'list'


@app.route('/detail')
def detail():
    return 'detail'


if __name__ == '__main__':
    app.run()
