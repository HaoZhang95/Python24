from flask import Blueprint

# 把当前的模块注册成一个名为order的蓝图,蓝图就是视图函数路由加载在蓝图上，app直接和蓝图联系
# 没有蓝图的话@，app运行的时候rl_map显示不出来单独文件中的视图函数
order_blue = Blueprint('order', __name__)

# 1- 实例化蓝图模块
# 2- 使用该模块的实例对象去route注册路由
# 3- 在app.py中注册该蓝图，整体使用类似于django中的startapp应用
@order_blue.route('/order/list')
def order_list():
    return 'order list...'


