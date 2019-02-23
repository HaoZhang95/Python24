"""
    用class的形式处理y=kx+b的问题是一种很好的解决方式
    但是如果需要计算2万条一次函数的话，需要不断更新k，b的值，来创建2万个内存对象空间
    更重要的是，自定义的类默认都集成了大量的魔法方法从object中，累赘， 类的方式占用大量内存
"""


class Line(object):

    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


"""
    闭包closure,就是一个空间：包含外部函数定义的变量k=1,b=2和其里面的get_y函数
    line1 = line(1,2)，中的line方法并不会return之后就销毁，因为这个函数中包含另一个内部函数
    只有当line1这个内部函数没有引用指向或者执行完毕的时候，line方法才算完成，进行空间销毁
    
    闭包：类似于轻量化的类处理,并不是函数中嵌套函数叫做闭包，而是一个空间中既有变量数据，又有功能函数
        只是函数嵌套函数并且返回函数只是实现闭包的形式(之一probably)， 
    nonlocal 类似于全部变量在def函数中使用的global
"""


def line(k, b):
    count = 0

    count1 = [0]

    def get_y(x):
        # global count  会报错，找不到全局变量的count，提示未定义
        nonlocal count  # 不是本地的count，会寻找外部方法的count
        count1[0] += 1  # python2中没有nonlocal，可以使用count1这样曲线救国的方法
        count += 1
        print("这是第%d次执行, 当x=%d时, y=%d" % (count, x, k*x+b))

    return get_y


line1 = line(1, 2)      # 创建一个新的闭包，让line1指向一个函数空间

line1(0)
line1(1)
line1(2)

line2 = line(11, 22)        # 旧闭包空间不再引用，开始销毁，创建另一个闭包
line2(0)
line2(1)
line2(2)


"""
    函数：不可以使用另外一个函数作用域中的变量的函数。而闭包可以
   xx(函数名)      普通函数能够完成较为复杂的功能， 传递的是这个函数的引用，只有功能
   xx(匿名函数名)   匿名函数能够完成基本的简单功能，传递的是函数的引用，只有功能
   xx(闭包)        闭包能够完成较为复杂的功能，传递的是闭包中的函数和数据，功能+数据
   xx(实例对象)     对象能完成复杂的功能，传递的是数据+很多功能函数
"""