from flask import Flask, render_template


"""
    需要注意模板的路径和当前app的关系
    当前app找不到系统根目录下的templates文件夹，因为不再统一目录下面，只能加载自己本目录下的模板文件夹
    下面的template_folder='templates'指的并不是系统的templates文件夹
"""


app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    my_int = 10
    my_str = 'Hao'
    my_num_list = [1, 2, 3, 4, 5]
    my_dict = [
        {'name': "apple", 'price': 20},
        {'name': "juice", 'price': 68},
    ]

    return render_template('demo4.html',
                           my_dict=my_dict,
                           my_num_list=my_num_list,
                           my_int=my_int,
                           my_str=my_str)


# 自定义列表反转过滤器，装饰器的添加方式
@app.template_filter('list_reverse')
def list_reverse(li):

    # 通过原列表创建一个新列表,不能直接temp_li = li，只能通过list()函数
    temp_li = list(li)
    # 将新列表进行返转
    temp_li.reverse()
    return temp_li


# 自定义过滤器的第二种添加方式
# app.add_template_filter(list_reverse, 'list_reverse')


if __name__ == '__main__':
    app.run()
