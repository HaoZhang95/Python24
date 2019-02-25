"""
    globals()['__buildins__']返回的是一个字典，表示python的内建模板，解释器默认加载的功能
    例如print，通过globals()['__buildins__'].__dict__查看这个内建的模板

    python解释器运行之后，会创建一个内存空间，这个空间里面存储的是一个字典，这个字典可以看到所有的全局变量，eg：a = 100
    存储方式：key：a value:100

    不管定义的是全局变量，函数，还是对象，实际上就是往globals这个字典中添加一个变量名->函数，对象的引用
    import XXX, 1- 寻找XXX.py 文件，从上到下执行 2- 在当前的文件中向字典中添加一个XXX的全局变量，只想这个模块文件

    对象和对象之间的关联是通过：globals返回的字典可以当作一个链接的源头，一个链接指向另一个对象，一个对象指向其对象方法内存空间

"""

"""
    元类(用来创建类对象) --> 创造了 person这个类对象 --> 创造了p1,p2等实例对象
    元类就是一种特殊的类，这个类可以创建类对象，元类指的就是type！！！，通过type()函数定义的类和class 穿件创建的类一样
"""


class T(object):
    pass


def test01():

    # type(object) -> the object's type
    # type(name, bases, dict) -> a new type
    # help(type)

    # type("类名", 包含了父类名的元组, 包含了属性的字典)
    a = type("TT", (), {})      # 创建了一个a类对象，并不是TT类对象，一般命名成一致的TT

    help(T)
    help(a)


class A(object):
    num = 1

    def test(self):
        print("----A-test----")


# 实例方法
def test_1(self):
    print("----AA-test-1----")


@classmethod
def test_2(cls):
    print("----AA-test-2----")


@staticmethod
def test_3(cls):
    print("----AA-test-3----")


def test02():

    # 字典的key-value链接,globals字典中添加了一个key为AA的变量名，指向元类type创建的类对象AA
    # 类对象AA中也有字典，key-value指向的实例属性或者方法
    AA = type("AA", (object, ), {"num": 1,
                                 "test_1": test_1,
                                 "test_2": test_2,
                                 "test_3": test_3,
                                 })

    help(AA)


"""
    1- 当python解释器在创建class T(object)的时候，如果解释器在括号中没有找到metaclass的命名参数，那么就用type()
    来创建这个T类，实质就是type()创建的这个class T()
    python解释器会把当前class定义的类名和父类以及这个class中的所有方法和属性会特殊的方式传递到type中当参数

    2- 如果class T(object, metaclass=upper_attr)那么python解释器就用指定的东西来创建类对象，而不是使用默认的type来创建
    此时就意味着调用upper_attr函数，并且解释器会自动把类名，父类名组成的元祖以及属性方法组成的字典传递给upper_attr
    
    3- 元类的作用:可以修改类对象定义时候的样子，进行偷梁换柱，批量将小写的类属性变为大写的类属性
"""


def upper_attr(class_name, class_parents, class_attr):

    # 此时的class_name=Foo,parent=object,但是class_attr中不只有bir，还有__class__等隐藏的魔法方法
    # 遍历属性字典，把不是__开头的属性名字变为大写
    new_attr = {}
    for name,value in class_attr.items():
        if not name.startswith("__"):
            new_attr[name.upper()] = value

    # 调用type来创建一个类，metaclass等于谁就用哪个方法和创建对象，不在是type
    return type(class_name, class_parents, new_attr)


class UpperAttrMetaClass(type):
    # __new__ 是在__init__之前被调用的特殊方法
    # __new__是用来创建对象并返回之的方法
    # 而__init__只是用来将传入的参数初始化给对象
    # 你很少用到__new__，除非你希望能够控制对象的创建
    # 这里，创建的对象是类，我们希望能够自定义它，所以我们这里改写__new__
    # 如果你希望的话，你也可以在__init__中做些事情
    # 还有一些高级的用法会涉及到改写__call__特殊方法，但是我们这里不用
    def __new__(cls, class_name, class_parents, class_attr):
        # 遍历属性字典，把不是__开头的属性名字变为大写
        new_attr = {}
        for name, value in class_attr.items():
            if not name.startswith("__"):
                new_attr[name.upper()] = value

        # 方法1：通过'type'来做类对象的创建
        return type(class_name, class_parents, new_attr)

        # 方法2：复用type.__new__方法
        # 这就是基本的OOP编程，没什么魔法
        # return type.__new__(cls, class_name, class_parents, new_attr)


# metaclass调用的时候会自动把Foo相关的参数传递给upper_attr
# metaclass可以传递一个函数，或者一个class，通过类的__new__方法来处理
class Foo(object, metaclass=upper_attr):
    bar = 'bip'


def test03():

    print(hasattr(Foo, 'bar'))
    print(hasattr(Foo, 'BAR'))


def main():

    # test01()
    # test02()
    test03()


if __name__ == '__main__':
    main()