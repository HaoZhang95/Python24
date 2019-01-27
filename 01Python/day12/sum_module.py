"""
    自定义的sum模块，需要自测成功后再使用
    1- 书写格式，如果在本模块下执行这个模块，python会自定义一个值为__main__的__name__变量
    2- main()可以直接写，但是开发时候常用if __name__ == '__main__'的方式
    3- if __name__ == '__main__': 类似于main函数的入口
    4- 如果在其他模块中引入并且调用这个模块任何方法和属性，那么__name__就变成了本函数名
"""
# 模块中的全局变量
name = "加法运算"

# 模块中自定义类
class Person(object):
    pass

# 加法运算函数
def my_sum(a, b):
    return a + b

# 自测函数
def main():
    result = my_sum(3, 5)
    print(result)

# main()

# 书写格式, __main__， 防止测试工程师使用这个模块的时候执行自己的自测函数
print(__name__)
if __name__ == '__main__':
    main()

"""
    __all__ = []只有列表中的元素才能被外部的模块使用
    但是__all__只能配合from 模块名 import * 这种格式下才有效
"""
__all__ = ["name", "Person", "my_sum"]