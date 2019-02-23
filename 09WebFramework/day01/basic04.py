"""
    多个装饰器对同一个函数进行装饰，有关装饰器装饰的时间问题
"""


def set_permission(func):

    def call_func(*args, **kwargs):
        print("====这是添加权限验证的功能====")
        ret = func(*args, **kwargs)
        return ret
    return call_func


def set_log(func):

    def call_func(*args, **kwargs):
        print("====这是添加log功能====")
        ret = func(*args, **kwargs)
        return ret
    return call_func


"""
    哪个装饰器在上面，就先执行哪一个装饰器
    但是装饰的时候是倒着装饰，先装饰set_log在装饰permission，装的时候是从下到上装，执行的时候是从上到下运行

"""
@set_permission     # test = set_permission(test)
@set_log
def test():
    print("----test----")


test()
