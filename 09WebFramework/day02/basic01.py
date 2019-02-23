def set_log(log_level):
    def super_set_func(func):
        def call_func(*args, **kwargs):
            log_level_info_dict = {
                1: "Warning",
                2: "Error"
            }

            # 根据闭包内存空间的log——level的不同，处理不同业务
            print("****Log日志：%s****" % log_level_info_dict[log_level])
            return func(*args, **kwargs)

        return call_func

    return super_set_func  # 多嵌套一层，返回这个装饰器


@set_log(1)
def test01():
    """
        @super_set_func(1) 带有参数的装饰器，用来区分多个函数都被同一个装饰器装饰，用来区分函数
        实现的原理是，把装饰器外边包上一层函数，带有参数

        这种特殊的带有参数的装饰器，并不是直接test01 = set_log(1, test01)的，并非直接把函数名传递给set_log
        1- @装饰器(参数) 会先**调用**set_log函数，把1当作实参进行传递，此时跟函数名没有关系，先调用带有参数的set_log函数
        2- 把set_log函数的返回值，当作装饰器进行装饰，此时才是test01 = super_set_func(test01)
    """
    print("----test01----没有参数，没有返回值")


@set_log(2)
def test02():
    print("----test02----没有参数，有返回值")
    return 100


class Log(object):

    """
        类装饰器，装饰器加载在类上，不在是传统上的加载在方法上面
        作用就是:不同于方法装饰器，类装饰器可以在被装饰的方法的前后添加多个自己类的实力方法进行装饰，self.xxx()，self.yyy()
        1- @Log 等价于 Log(test03) 初始化Log的init方法，test03函数名作为参数传递
        2- 此时test03就指向一个类对象，等test03()调用的时候，相当于调用了类中的call方法
    """

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("---在方法执行前添加的功能---")
        ret = self.func(*args, **kwargs)
        print("---在方法执行后添加的功能---")
        self.xxx()
        self.yyy()
        return ret

    def xxx(self):
        pass

    def yyy(self):
        pass


@Log
def test03():
    print("----test02----")


def main():
    # test01()
    # num = test02()
    # print(num)

    test03()


if __name__ == '__main__':
    main()
