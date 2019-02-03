"""
    产品迭代的含义：不是功能的增加，而是功能的**增强**
    1- 轮子 -> 车筐 -> 发动机 -> 整车完成， 并不是产品的迭代，只是功能的增加
    2- 滑板车 -> 自行车 -> 摩托车 -> 轿车，这个才是产品的迭代，产品功能的增强

    代码中的迭代器：记录位置信息的东西iterator
    1- 判断是不是可迭代对象 isinstance(x, int)
    2- Python中的迭代器，引入collections， 获取迭代器和next方法使用都是方法开头
"""
from collections import Iterable, Iterator

data = [1, 2, 3, 4, 5]

"""
    1- 定义自己的可迭代对象，需要在自己的class中重写__iter__的魔法方法
    2- 定义自己的迭代器，next()方法调用的时候，魔法方法__next__被调用
    3- 迭代器本身就是可迭代的对象，判断一个对象是不是迭代器使用
    4- 迭代器本身也必须重写__iter__方法
"""
class MyListIterator(object):

    # 构造器传入需要迭代的数据
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        print("当前的下标是: %d" % self.index)
        if self.index < len(self.data):
            data = self.data[self.index]
            self.index += 1
            return data
        else:
            # 抛出一个stopIteration的异常，告诉for循环停止next
            raise StopIteration

    # Python规定，迭代器本身也是可迭代对象
    # 所以迭代器本身也必须重写__iter__方法
    def __iter__(self):
        return self

class MyList(object):

    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    # 将本class定义为可迭代的，需要自定义迭代器,调用iter()方法返回的对象
    def __iter__(self):
        return MyListIterator(self.data)

def testMyIteratableObj():
    myList = MyList()
    print("iterator是迭代器：%s" % isinstance(iter(myList), Iterator))

    print("myList是可迭代的对象：%s" % isinstance(myList, Iterable))

    for temp in myList:
        print(temp)

def testIteratable():
    print("data是可迭代的对象：%s" % isinstance(data, Iterable))

    # 获取可迭代对象的迭代器iter(data)
    iterator = iter(data)

    # 死循环next，超出的话，会报错stopIterator的异常
    while True:
        try:
            temp = next(iterator)
            print(temp)
        except Exception as e:
            break


def main():
    # testIteratable()
    testMyIteratableObj()


if __name__ == '__main__':
    main()
