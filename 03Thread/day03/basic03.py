"""
    迭代器计算费布纳奇数列,  0 1 1 2 3 5 某一项的值等于前两项的和

"""

class Fib(object):

    def __init__(self, num):
        # 计算次数
        self.num = num
        # 当前下标
        self.index = 0

        self.num1 = 0
        self.num2 = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.num:
            temp = self.num1

            # 同时交换两个变量的简写
            # self.num1 = self.num2
            # self.num2 = self.num1 +  self.num2

            self.num1, self.num2 = self.num2,(self.num1 +  self.num2)
            self.index += 1
            return temp
        else:
            raise StopIteration

def testFib():
    # for i in Fib(10):
    #     print(i)

    # 可迭代对象也可以用在list(迭代器),或者tuple(迭代器)并不只是for循环中
    print(list(Fib(10)))


"""
    生成器是一种特殊的迭代器，使用小括号类似的列表推导式
    1- 生成器，可以直接用来next(迭代器)
    2- 使用了yeild的函数叫做生成器函数
    3- 调用生成器函数才能产生生成器iterator
    4- 生成器内部实现了iter，next，抛出异常的方法
"""


def testGenerator():
    data1 = [x for x in range(100000)]
    data2 = (x for x in range(100000))

    print(type(data1))  # list
    print(type(data2))  # type = generator

    print(next(data2))
    print(next(data2))
    print(next(data2))

"""
    yield的作用：
    1- 将yield后面的值作为**返回值**给调用生成器的地方
    2- 把当前函数挂起，在下一次调用生成器的时候，从上一次结束的地方开始
"""
def hello():
    yield 1
    yield 2
    yield 3
    yield 4

def testYield():
    generator = hello()
    print(next(generator))
    print(next(generator))

    # 挂起继续执行
    print(next(generator))
    print(next(generator))

"""
    使用yeild的计算fib
    1- while循环中不使用return返回值，因为是returm的不会产生生成器
    2- yield在循环中挂起，生成器迭代的时候，会从此行继续执行代码，判断while
    3- 如果使用send唤醒的话，yield还有一个作用就是收数据
"""
def testFib2(num):

    index = 0

    num1 = 0
    num2 = 1


    while index < num:
            temp = num1
            num1, num2 = num2,(num1 +  num2)
            index += 1
            # return temp
            extra = yield temp
            print("接收到了send发送的额外的数据:%s" % extra)

"""
    第一次调用生成器必须使用next，之后才可以使用send发送额外的数据
    send和next的作用类似，都是恢复生成器的挂起，但是send唤醒的时候可以传入额外的数据
"""
def main():
    # testFib()
    # testGenerator()
    # testYield()
    generator = testFib2(10)
    print(next(generator))
    print(generator.send("这是给yield额外的数据"))

if __name__ == '__main__':
    main()

