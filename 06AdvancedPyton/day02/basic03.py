"""
    魔法属性
    1- __doc__      获取类的描述信息
    2- __module__   表示当前操作的对象在哪个模块
    3- __class__    表示当前的操作的对象的类是什么
    4- __new__      创建这个对象，但是这个对象还没有
    4- __init__     python中的并不和java一样叫做构造器，只是new之后属性的添加
    5- __del__      对象在内存中被释放的时候，引用计数为0的时候，并不是自己手动调用del的时候
    6- __call__     对象后面加上()的时候被执行：obj = Foo() 执行 init
                                             obj()  执行call
    7- __dict__     获取实例对象的属性，输出为字典模式，无论私有还是共有的属性，私有的属性只不过进行了命名重整
    8- __str__       并不是print的时候才会调用，而是**打印**的时候都会调用eg: my_str = obj
    9- __getitem__  用于索引操作，如字典，获取数据
    9- __setitem__  设置数据
    9- __delitem__  删除数据


"""

class Foo(object):
    """这里是类的描述类信息，通过__doc__获取该信息"""
    def func(self):
        pass

    def __getitem__(self, item):
        return 0

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

def test01():

    print(Foo.__doc__)
    print(Foo.__module__)       # --> __main__
    print(Foo.__class__)        # --> <class 'type'>

    obj = Foo()
    result = obj["xxx"]         # 触发getitem
    obj["xxx"] = 2              # 触发setitem
    del obj["xxx"]              # 触发delitem


def main():
    test01()


if __name__ == '__main__':
    main()