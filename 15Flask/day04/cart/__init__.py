from flask import Blueprint

# 每一个模块蓝图可以拥有自己的静态文件夹，默认的app会设置好系统级别的static
# 但是蓝图需要自己手动设置注册静态文件的路径
# 为了区分加载的是主应用下的static还是模块下的static，给模块初始化的时候添加url前缀
# 添加前缀后，那么该蓝图.route的时候就自动添加了该前缀， 加载img的时候使用/cart/static/xxx.img

# 如果模块模板和主营业模板下都拥有相同的html名字，则优先加载主营业下的模板
cart_blue = Blueprint('cart', __name__,
                      static_folder='static',
                      template_folder='templates',
                      url_prefix='/cart')

# 只能在蓝图初始化之后再倒入views，因为.views使用了蓝图
from .views import *
