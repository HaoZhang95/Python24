"""
    1- __str__()类似于toString方法，不能添加形参，因为是重写，必须返回一个str
    2- __del__()用来提前销毁对象内存管理, 使用“del 对象”的时候会触发该方法
    3- p1,p2,p3都指向同一个对象的地址张三，只有该类的引用数为0的时候“del 对象名”才会触发del魔法函数
    4- 所以说：“只要执行了del，就会执行__del__()”是错误的。
"""

class Person(object):

    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def __str__(self):
        return "姓名：%s 年龄: %s 学号: %s" % (self.name, self.age, self.num)

    def __del__(self):
        # 监听对象销毁，可以用来用户复活
        print("再见")

    def print_info(self):
        print("姓名：%s 年龄: %s 学号: %s" % (self.name, self.age,self.num))

p1 = Person("张三", 18, 1605477)
print(p1)

p2 = p1     # 引用计数+1
p3 = p1     # 引用计数+1

del p1      # 引用计数-1
del p2      # 引用计数-1
del p3      # 引用计数=0

# input()

"""
    1- 使用同一个类创建的不同对象，**属性**是需要单独开辟内存的，防止一损俱损
    2- 但是类的自定义方法是唯一的只有一份内存， 是通过self判断不同的调用对象是谁
"""

p4 = Person("张三", 18, 1605477)
p5 = Person("张三", 18, 1605477)
print(id(p4.name))              # name作为类属性，有单独的内存空间，id地址不同
print(id(p5.name))              # 但是因为小整数型原因，显示的id相同，但原理id是不同的
print(id(p4.print_info()))      # 类方法是唯一一份的，所以id相同
print(id(p5.print_info()))

