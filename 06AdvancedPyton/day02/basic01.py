"""

    多继承中的super和传统类型java有点不同

    1- Python中的C(A,B)是根据传入的父类顺序来规定的，所以A,B是有顺序的
    2- 具体的顺序是根据python使用C3算法，Grandson.mro() 方法返回的(<class '__main__.GrandSon'>, <class '__main__.Son1'>, <class '__main__.Son2'>, <class '__main__.Parent'>, <class 'object'>)
    3- Grandson()构造时候，super()调用的是mro返回元组的本身位置的下一个，即Grandon的下一个是Son1
    4- 然后去找Son1的构造方法，发现Son1的也调用了super()，所以还去**Grandson的mro**元组中招son1的下一个是son2
    5- son2的构造方法中super，去找son2在元组中的下一个是parent

    可以看出Son1的super方法竟然调用的是**Son2**的，所以很奇怪，一切根据C3算法的mro列表
    super(Parent, self).__init__()，是可以根据具体的类去调用某个父类的super
    super().init没有参数的super默认就是本事的类，类似super(自身的类, self).__init__()

    1- 单继承的情况下，并没有这样的**错误**，所以super()无惨，比较方便
    2- 多继承的情况下，还是推荐写有参数的super，来制定具体的父类是谁，该去mro列表中找谁
"""

class Parent(object):

    def __init__(self, name, *args, **kwargs):
        print("Parent的init方法开始调用")
        self.name = name
        print("Parent的init方法结束被调用")


class Son1(Parent):

    def __init__(self, name, age, *args, **kwargs):
        print("Son1的init方法开始调用")
        self.age = age
        super().__init__(name, args, kwargs)
        print("Son1的init方法结束被调用")


class Son2(Parent):

    def __init__(self, name, gender, *args, **kwargs):
        print("Son2的init方法开始调用")
        self.gender = gender
        super().__init__(name, args, kwargs)
        print("Son2的init方法结束被调用")


class GrandSon(Son1, Son2):

    def __init__(self, name, age, gender):
        print("GrandSon的init方法开始调用")

        super().__init__(name, age, gender)

        print("GrandSon的init方法结束被调用")


def test01():
    print(GrandSon.__mro__)     # --> 返回的是元组
    # print(GrandSon.mro())     # --> 返回的是列表

    gs = GrandSon("grandson", 11, "男")

    print("姓名: ", gs.name)
    print("年龄: ", gs.age)
    print("性别: ", gs.gender)


"""
    继承并不是子类**复制**父类的属性，而是子类中**访问**父类的属性
    实例对象中的x属性现在自身寻找，然后才去父类寻找，父类没有，就去父类的父类寻找
    继承不是复制，而是引用
"""
class A(object):
    x = 1


class B(A):
    pass


class C(A):
    pass


def test02():
    print(A.x, B.x, C.x)

    # python一看B中并没有自己的x，就自己添加了一个属性x=2
    B.x = 2
    print(A.x, B.x, C.x)

    # 父类中x进行了修改，C并不是复制的1，而是C可以使用A的x
    # C.x 一看自身并没有，就去引用父类
    A.x = 3
    print(A.x, B.x, C.x)        # 返回的是3 2 3 并不是3 2 1



"""
    1- 实例方法(self)指向的是调用的实例对象引用，所以需要self，可以读写**实例对象**的属性
    2- 类方法(cls)指向的是类对象引用，可以读写共享的数据**类属性**
    3- 所需要的既不是self实例对象引用也不需要cls类对象引用，就使用静态方法

"""
class D(object):

    def a(self):
        print("实例方法")


    @classmethod
    def b(cls):
        print("类方法")


    @staticmethod
    def c():
        print("静态方法")

"""
    家人之间共享苹果
"""
class Family(object):

    apple_num = 5

    def __init__(self, name):
        self.name = name

    # 需要使用共享的变量，说以设计为类方法
    # 这样son1和son2都吃了一个苹果后，还剩3个苹果
    @classmethod
    def eat_apple(cls):
        cls.apple_num -= 1

    # 这个吃苹果的实例方法会先查看self调用者有没有app_num，没有的话就会去找父类的，添加到自己的属性
    # 相当于每个成员都拥有5个苹果
    def eat_apple2(self):
        self.apple_num -= 1

    # 不需要self和类引用的静态方法
    @staticmethod
    def rule():
        print("每个人都必须遵守的约法三章")

def test03():
    pass


def test04():
    son1 = Family("老大")
    son2 = Family("小弟")

    son1.eat_apple()
    son2.eat_apple()

    print(son1.apple_num)
    print(son2.apple_num)


def main():

    # test01()
    # test02()
    # test03()
    test04()




if __name__ == '__main__':
    main()