"""
    Python中的一场处理try-except
    1- 多个异常python可以写在同一行，括号包括多个异常，逗号隔开
    2- 获取异常的信息描述通过 as e的方式
    3- 发生异常执行except，不发生异常执行else，两者对立
"""
try:
    file = open("Test.txt", "r")
except (FileNotFoundError, NameError) as e:
    print("捕获到了异常，异常信息%s, 准备补救工作..." % e)
    # file = open("Test.txt", "w")
except Exception as e:
    print("捕获到了超级异常")
else:
    print("如果try中的代码不发生异常执行else")
finally:
    print("Finally有没有异常都会执行的")

"""
    异常嵌套中的传递， 内部的异常搞不定就会传到外边一层去处理
"""
try:
    try:
        file = open("Test.txt", "r")
    finally:
        print("这里没有处理内部的异常")
except:
    print("外部一层捕获到了内部的异常")

"""
    函数中异常的传递,内部的异常向外传递
"""


def fun1():
    print(10 / 0)


def fun2():
    fun1()


def fun3():
    try:
        fun2()
    except:
        print("在最外层的函数中捕获到了异常")


fun3()

"""
    抛出自定义的异常,需要继承Exception, str方法显示的是信息的描述
    1- raise AgeError(age) 关键字进行自定义对象的抛出
    2- raise关键字的两个作用a:抛出自定义异常 b:将本异常不处理，进行抛出
"""


class AgeError(Exception):

    # 使用init的方法主要是要age的值， 此方法非必需
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return "你输入的年龄有误：age=%d" % self.age


class Person(object):

    def __init__(self, name, age):
        self.name = name
        if age <= 0 or age >= 150:
            raise AgeError(222)
        else:
            self.age = age

p1 = Person("小明", 222)

"""
    异常处理中的**不处理，抛出异常给下一层**
"""
class Test(object):

    def __init__(self, switch):
        self.switch = switch

    def calculate(self, a, b):
        try:
            return a / b
        except Exception as e:
            if self.switch:
                print("设置为自动捕获异常，异常如下：%s" % e)
            else:
                raise

Test(False).calculate(8, 0)