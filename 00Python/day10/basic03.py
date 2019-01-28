"""
    类中的私有属性和方法
    1- 父类中的money不想让子类继承，进行私有self.__属性名
    2- 方法前加上两个下划线使方法私有化， 私有的属性和方法只能在类内使用
    3- # 私有属性子类不能使用,相当于java中的对象不能加点来获取private的属性值
"""

class Master(object):

    def __init__(self):
        self.kongfu = "古法"
        self.__money = 100000   # 两个下划线开头表示私有属性

    def make_cake(self):
        print(self.__money)     # 私有属性可以在类自己种使用
        print("制作古法煎饼果子")

    def __hello_python(self):
        print("你好python")

lishifu = Master()
lishifu.make_cake()
print(lishifu.kongfu)
# print(lishifu.money)


"""
    子类不能继承父类的私有属性和方法
    因为根本没有继承下来，所以子类内部方法中根本就不能调用父类的私有属性和方法
"""
class Prentice(Master):

    def xx(self):
        print("xx")
        # self.__hello_python()


damao = Prentice()
print(damao.kongfu)
# damao.__hello_python
damao.xx()