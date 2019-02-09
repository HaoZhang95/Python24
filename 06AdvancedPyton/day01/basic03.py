"""
    私有属性可以强制破解，但是一般**不这么使用**
    XX       **自定义**共有变量
    _X      前置下划线，私有属性或者方法，from somemodule import * 的情况下**禁止访问**，类对象和子类可以访问
    __XX    双前置下划线，避免与子类中的属性命名冲突，无法在外部直接访问私有变量
    __XX__  双前后下划线，用户名字空间的魔法方法或者属性，**系统自带**的公有变量
    XX_     单后置下划线，避免和python关键字冲突

    1- Python中重新命名了私有属性名，所以不能直接访问，可以通过t.__dict__获取所有的属性名t，私有属性的命名重整
    2- 命名重整的格式 ： _类名__属性名或者方法名  t._T__age

"""

class T(object):

    def __init__(self):
        self.num = 100
        self.__age = 18


    def __private(self):
        print("我的私有方法")

t = T()
print(t.num)
# print(t.__age)        私有属性不能直接方法
print(t.__dict__)       # {'num': 100, '_T__age': 18}
print(t._T__age)        # 利用新名字获取私有属性值
t._T__private()         # 也可以利用命名重整直接调用私有方法


"""
    import的问题
    
    1- sys.path列出一个列表的**搜索路径**，第一个就是当前py的目录
    2- import XX，先从列表从上到下搜索XX，也就是先从当前py路径搜索XX模块
    3- 如果想优先使用自己的模块，要么把该模块拷贝到当前路径下，要么修改搜索路径列表
        sys.path.append('/home/itcast/xxx')     或者      sys.path.insert(0, '/home/itcast/xxx')      
    
    
    1- 模块的reload，如果一个模块import XX，XX中某个方法有bug，但是不想退出此程序，需要重开XX进行方法的修改
    2- 那么当前文件中的方法并不会自动更新，因为import一次，就不会在随着XX的更新而更新
    3- 需要使用imp模块， from imp import reload  --> reload(xx)
    
    1- import XX的两层含义：a: 按照sys.path制定的路径去找XX.py 
                            b: 在本模块中定义一个XX变量，让这个对象指向被导入的模块
    
    2- from XX import FLAG  意味着: a：去sys.path制定的路径中招XX.py
                                    b: 定义一个变量名叫做FLAG，并且让这个变量指向XX模块中的Flag值，类似于a=100, a=200表示flag不在指向XX中的值，只是引用改变了
    3- 总结前者是XX.FLAG = TRUE更改的就是XX模块中真正的数值， 后者FLAG = TRUE只是引用不在指向XX模块中，from XX import FLAG方式的更改并**不会影响XX模块中原始值**                                
    
     
"""

import sys

print(sys.path)













