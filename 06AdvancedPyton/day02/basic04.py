"""
    with .. as
    一个类实现了__enter()__和__exit__两个魔法方法，就表示这个类有了context上下文管理器

    一般with配合上下文管理器使用， 上下文管理器就是给自己的类定义**鞍前马后**地处理

    with 返回的对象 as xxx:
        doSth()

    1- 获取返回的对象本身必须实现enter和exit魔法方法
    2- 获取该返回对象的时候就会触发enter鞍前方法
    3- 当with里面
    的代码执行完成后悔自动触发该对象的exit善后工作
"""
from contextlib import contextmanager


class MyFile(object):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # 上下文管理器的上文
    def __enter__(self):
        print("entering")
        self.file = open(self.filename, self.mode)
        return self.file

    # 上下文管理器的下文，用于处理善后清除工作
    def __exit__(self, *args):
        print("will exit...")
        self.file.close()


"""
    1- open("output.txt", "w") 如果成功，返回值给f
    2- 当with中的代码结束的时候，会**自动**调用close方法，实现原理就是默认实现了上下文管理器
    3- with后面不止可以写open文件类，还可以写自己实现上下文管理器的自定义类
"""


def test01():

    with open("output.txt", "w") as f:
        f.write("Hello World 1.0")

    with MyFile("output1.txt", "w") as f:
        f.write("Hello World 2.0")


"""
    使用contextmanager的模式, 方法前面加上@contextmanager的修饰器
    1- 方法的yield返回值之前的代码就相当于enter方法
    2- yield之后的代码就类似exit方法
"""


@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()


def test02():
    with my_open("output2.txt", "w") as f:
        f.write("Hello World 3.0")


def main():

    test01()
    test02()
    # test03()


if __name__ == '__main__':
    main()

# python中的函数都是从上到下执行的，即使写了main函数也一样,通常把main函数写在最后，不支持像js一样的预解析
# def test03():
#     print("......")