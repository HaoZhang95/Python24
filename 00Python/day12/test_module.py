"""
    自建一个文件测试sum_module的自定义模块
    1- 引入A模块后，无论调用A模块中的任何属性和方法，A模块都会从上到下将可执行的代码执行一遍
    2- from...import选择性的导入模块的一部分（全局变量，函数名，类）
    3- import 模块后的as将模块名**别名**为自定义的名字来使用,防止命名冲突
"""

# 测试工程师做的事情
import sum_module as bie_ming             # 导入这个模块下的所以东西，需要写模块名来调用
from sum_module import *                  # 导入模块的全部，但是不需要写模块名来调用
from sum_module import my_sum as super_sum           # 只导入模块下的my_sum方法，不需要写模块名来调用

# 定义一个函数测试
def main():
    result = bie_ming.my_sum(3, 5)
    print(result)
    print(bie_ming.name)
    print(bie_ming.Person())

main()

# 部分导入后使用，不需要写模块名，直接调用该方法即可，可能会和自己类的方法名冲突
print(my_sum(3, 5))