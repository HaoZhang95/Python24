"""
    单继承,class B(A) 括号里面的是相对B来说的B的父类，集成了A的属性和方法
    1- python中类的属性是直接写在init方法中的
"""
class A(object):

    def __init__(self):
        self.num = 10

    def print_num(self):
        print(self.num + 10)

class B(A):

    def my_func(self):
        print("我自己B类的自定义方法")

b = B()
print(b.num)
b.print_num()
b.my_func()

"""
    多继承class D(C, A),如果多个父类C,A中都含有相同的方法和属性print_num那么子类D继承的是就是C的，注意继承的先后顺序
    1- 父类中的属性和方法如果相同的话，会继承第一个父类的属性和方法，按照集成的顺序走init构造方法
    2- D类中重写父类的方法,如果自己d类中重写了init方法，那么就不会继承任何的父类属性从init方法中
    3- 换句话，子类重写了父类的方法，那么不在使用父类同名的方法，包括init构造方法
    4- 子类中重写了父类的方法但是还是想调用父类的方法，
"""
class C(object):

    def __init__(self):
        self.num = 28

    def print_num(self):
        print(self.num + 10)

class D(C, A):

    def __init__(self):
        self.age = "这是D类自己的属性age"
        self.num = "这是D类重写父类的属性num"

    def print_num(self):
        self.__init__()     # 再将self.num更改回来
        print("这是D自己重写父类的方法")

    # 但是子类还是想使用**父类的属性**调用父类重名的print_num方法
    # 使用A.__init__(self)方法来更改self.num的值
    def print_a_num(self):
        print(d.num)        # 本来D对象中self.num = "这是D类重写父类的属性num"
        A.__init__(self)    # 把self传进去，当前的self.num = 10
        A.print_num(self)

    # 或者使用super在子类方法中调用父类的方法
    def print_c_num(self):
        # super(D, self).print_num()    或者下面的简写形式
        super().print_num()

    def my_func(self):
        print("我自己D类的自定义方法")

d = D()
d.print_a_num()
print(d.num)
d.print_num()

