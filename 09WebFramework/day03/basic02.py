"""
    http服务器和web框架的分离，python中使用的就是WSGI协议

    使用app这个参数，指向dynamic.mini_framework.application中的application函数
    更加解耦，不然mini_framework文件名变，还需要修改多处，甚至源代码

    如果执行一个py文件时，print("模拟攻击127.0.0.1")，如果想要更改攻击的ip，则需要更改源代码里面，比较繁重
    使用运行时参数的话，就能在运行py文件时传入一个参数，python3 test.py 127.0.0.2 这样就能方便的更改，print(sys.argv[1])

    pycharm是不能执行运行时传参的，只有使用命令行的方式
    运行时参数就能保证服务器随意的选择运行时框架：python3 basic01.py django:application
                                             python3 basic01.py flask:application
"""

# response_body = dynamic.mini_framework.application(env, self.set_headers)
# response_body = app(env, self.set_headers)


import sys

print(sys.argv)     # 返回的是一个列表[]，第一个元素总是当前文件路径