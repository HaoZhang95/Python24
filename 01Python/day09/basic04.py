"""
    python中的类和对象, 所有的类的祖先都是object和java是一样的
    1- 前两种叫做经典类存在python 2.x中， 最后一种叫做新式类
    2- python 2中类并没有父类，自己就是父类
    3- 而python3中得class Person(object)存在父类，可以使用根类的方法
"""
class Person:
    pass

class Person():
    pass

class Person(object):
    pass

"""
    1- 实例方法的第一个形参是self自身,表示调用该方法的对象，谁调用谁就是self
    2- 给一个**对象**添加属性，并不是添加到类中的，有点奇怪
    3- 类的方法中，通过self获取对象的属性self.name
    4- 重写__init__() 用来给属性添加默认值，避免多个对象对共同的属性name赋值
    5- python中不能定义多个构造方法，只能定义一个，不然会报错
    6- 因为python对参数的类型没有限制，构造器中参数一般为字典{}用来处理不同数量参数的问题
"""
class Hero(object):

    # python提供的两个下划线的魔法方法，创建该类对象的时候自动调用，类似于构造方法
    # def __init__(self):
    #     self.name = "旺财"

    def __init__(self, age, my_name = "默认的名字"):     # 构造方法的参数也和kotlin一样可以默认参数
        self.name = my_name
        self.age = age

    def move(self):
        print(id(self))
        print("英雄会行走...")

    def print_info(self):
        print(self.name)
        print(self.age)
        print(self.hp)


hero01 = Hero(22)
print(id(hero01))   # 打印的id和move方法中的self的id是同一个地址

hero01.move()
hero01.name = "英雄名字01"
hero01.age = 22
hero01.hp = 4000
hero01.print_info()

hero02 = Hero(22)
print(hero02.name)

hero03 = Hero(18)
print(hero03.name)
print(hero03.age)

