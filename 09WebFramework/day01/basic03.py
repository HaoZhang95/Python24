"""
    装饰器, @static等等
    在定义的时候，*和**告诉python解释器，args是以元组的方式存储多余的数据， kwargs是以字典的形式存储

    *和**在定义的时候，都意味着**解包**
    1- *args 将(100, 200) 变为 100, 200
    2- *kwargs 将("num1": 100, "num2": 200) 变为 num1 = 100, num2 =200

    没有*和**就代表两个参数类型，一个元组，一个字典，不拆包
    3- fun(*args, **kwargs) --> fun(100,200, num1=100, num2=200)
    4- fun(args, kwargs) --> fun((100,200), {"num1": 100, "num2": 200})
"""

# 通用装饰器，整合了*args, **kwargs，没有ret返回的就是none
def super_set_func(func):

    def call_func(*args, **kwargs):
        print("====这是执行func函数之前的功能====")
        ret = func(*args, **kwargs)    # 无参数，无返回值
        print("****这是执行func函数之后的功能****")
        return ret
    return call_func


def set_func(func):
    print("Python解释器，从上到下遇到@符号就自动装饰，并不是等调用时候才装饰")

    def call_func():
        print("====这是执行func函数之前的功能====")
        func()    # 无参数，无返回值
        print("****这是执行func函数之后的功能****")
    return call_func


def set_func1(func):

    def call_func():
        print("====这是执行func函数之前的功能====")
        num = func()      # 无参数，有返回值
        print("****这是执行func函数之后的功能****")
        return num  # 无参数，无返回值
    return call_func


def set_func2(func):

    def call_func(*args, **kwargs):
        print("====这是执行func函数之前的功能====")
        func(*args, **kwargs)      # 有参数，无返回值, 防止多个参数，不传值，就是空元组和空字典
        print("****这是执行func函数之后的功能****")
    return call_func


def set_func3(func):

    def call_func(temp):
        print("====这是执行func函数之前的功能====")
        num = func(temp)      # 有参数，有返回值
        print("****这是执行func函数之后的功能****")
        return num
    return call_func


@set_func
def test01():
    print("----test01----没有参数，没有返回值")


@set_func1
def test02():
    print("----test02----没有参数，有返回值")
    return 100


@set_func2
def test03(num):
    print("----test03----有参数num：%d，没有返回值" % num)


@super_set_func
def test04(num):
    print("----test03----有参数num：%s，没有返回值" % num)
    return 88888888


"""
    下面的test01()方法的执行，并不在指向上面的print函数，而是更改为set_func(test01)返回的函数内存空间，来进行调用
    直接在test01()上面写上装饰器@set_func 等价于 test01 = set_func(test01)
    装饰器装饰的时间：并不是test01()调用的时候才装，而是python解释器从上到下遇到@符号的时候，就自动装饰test01 = set_func(test01)，来执行装饰器set_func中的代码
    
    1- 对加了装饰器的原函数test01()在执行前后添加了额外的功能
    2- @set_func，test01函数名传递给set_func当参数，set_func的返回值给test01接收,test01被@set_func进行装饰，装饰完重新赋值给test01
    3- 当调用test01()的时候，就会把test01函数名传递给set_func当参数，执行set_func方法
"""
# test01 = set_func(test01)
# test01()


class T(object):
    @staticmethod       # 装饰器，就等价于 test = staticmethod(test)
    def test():
        pass


def main():
    # test01()          # 无参数，无返回值
    # num = test02()    # 无参数，有返回值
    # print(num)

    # test03()          # 有参数，无返回值
    num = test04(123)            # 有参数，有返回值
    print(num)


if __name__ == '__main__':
    main()