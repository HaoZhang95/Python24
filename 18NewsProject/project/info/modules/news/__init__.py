"""
    news的蓝图
"""
from flask import Blueprint

# 创建蓝图对象
news_blue = Blueprint('news', __name__, url_prefix='/news')

# 导入一个文件，就会从上到下执行一遍，就会使用index_blue去给views中的方法进行装饰器修饰，达到两者关联的目的
from . import views
