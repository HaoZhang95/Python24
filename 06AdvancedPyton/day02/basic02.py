"""
    property装饰器,不需要为每一个属性分别定义set/get，并且添加属性的权限判断
    1- 看上去是属性的获取，其实是方法的执行，但是并没有小括号:p1.name
"""


class Person(object):
    def __init__(self, name, age):
        self.__age = age
        self.__name = name

    def get_age(self):
        print("这里是对私有属性获取的权限验证")
        if 1 == 1:
            return self.__age

    def set_age(self, age):
        print("这里是对私有属性获取的权限验证")
        if 1 == 1:
            self.__age = age

    """
        1- @property的方法名可以自定义，不一定必须和属性名一样
        2- @name.setter必须和之前@property的get中的name方法名一样
        3- @name.deleter删除属性，在del obj.name的时候被调用
        
    """

    @property
    def name(self):
        print("这里是对私有属性获取的权限验证")
        if 1 == 1:
            return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name


def test01():

    p1 = Person("老王", 18)

    print(p1.get_age())
    print(p1.name)
    p1.name = "王五"

    del p1.name
    print(p1.name)


"""
    property(获取的方法，设置的方法，删除的方法，说明文字)的第二种使用方式，和前面的方式效果相同
    1- 使用property定义的类属性
    2- 当使用obj.属性的时候就会调用property(get_bar, set_bar, del_bar)中的第一个参数的方法
"""


class Foo(object):
    def get_bar(self):
        print("getter...")
        return "老王"

    def set_bar(self, value):
        print("setter...")
        return "set value" + value

    def del_bar(self):
        print("deleter...")
        return "老王"

    # 使用property定义的类属性
    BAR = property(get_bar, set_bar, "This is description...")


def test02():

    obj = Foo()

    print(obj.BAR)  # 自动调用property第一个参数的方法get_bar
    obj.BAR = "New Name"  # set_bar
    desc = obj.BAR.__doc__  #获取第四个参数desc
    print(desc)


def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()