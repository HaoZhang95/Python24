"""
    __new__()方法, 对象创建的过程，
    1- new方法返回一个对象 2- init利用new返回的对象进行属性的添加
"""


class Person(object):

    # 监听创建一个实例对象的过程，需要返回一个对象赋值给xiaoming
    # new中不return的话，那么久不会执行init方法
    def __new__(cls, *args, **kwargs):
        print("new")
        print((object.__new__(cls)))
        return object.__new__(cls)

    # 构造方法，当执行init方法的时候对象**已经创建成功**，剩下的是将属性添加到对象中
    def __init__(self, name):
        print("init")
        self.name = name

    # 类的toString方法
    # def __str__(self):
    #     return "我的名字是: %s" % self.name

    # 监听引用计数为0的时候，python会执行del方法
    def __del__(self):
        print("再见")


# xioaming的地址和new中return的obj的地址一样，说明new中返回的obj就是xiaoming
xiaoming = Person("小明")
print(xiaoming)
print("=" * 28)

"""
    python的单例模式，需要使用到new关键方法
    1- 保证返回的对象是同一个，在new中修改
    2- 保证对象的属性只能赋值一次，在init方法中修改
    3- 一般单例模式中的包含静态方法， 类似于Tools.XX, 不需要创建多个对象来调用同一个静态方法
"""
class Student(object):
    # 定义一个类属型保存实例对象
    __instance = None

    # 类属型保证实例属性只能被赋值一次
    __is_first = True

    # s1,s2要保证使用一份内存， 需要new的时候返回同一个对象
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)

        return cls.__instance

    def __init__(self, name, age):
        if self.__is_first:
            self.name = name
            self.age = age
            self.__is_first = False

    # 静态方法
    @staticmethod
    def add_num(a, b):
        return a + b

s1 = Student("小明", 25)
s2 = Student("小红", 28)

print(s1)
print(s2)
print(s1.name)
print(s2.name)
