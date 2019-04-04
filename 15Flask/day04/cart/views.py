from flask import render_template

from . import cart_blue


# from . 的意思就是当前目录下寻找cart_blue函数，一般指的是__init__文件中寻找
@cart_blue.route('/list')
def cart_list():
    return render_template('cart.html')
