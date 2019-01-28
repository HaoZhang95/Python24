
"""
    缺省函数，就是参数可以有默认值，跟kotlin一样
    返回值也可以简写，省略 -> int:
"""
def print_info(name, age=20):
    print("姓名：%s, 年龄：%s" % (name, age))

print_info("张三", 28)
print_info("李四")

"""
    元组[]不定长参数，参数的数量不确定， 调用类似于位置参数
    参数名之前加上*表示这个星号表明参数的类型为元祖，但是传入实参的时候不需要中括号[]
"""
def my_func01(*args):
    print(type(args))
    print(args[0])

my_func01(1, 3, 5)
my_func01(1, 3, 5, 7)

"""
    字典类型{}的不定长参数, 调用类似于关键字参数name=的形式
    参数名前面加上**两个星号，表明这个参数为一个字典,传入的时候不需要写{}，但是只能传入一个字典
"""
def my_func02(**kwargs):
    print(type(kwargs))
    print(kwargs["name"])
    print(kwargs["age"])

my_func02(name="小明", age=12)

"""
    一个函数的包含多return个
"""
def my_func03(score: int) -> str:
    if score >= 70:
        return "优秀"
    elif score >= 30:
        return "中性"
    else:
        return "差"

print(my_func03(50))

"""
    处理多个返回值的方式
    1- return ["小明"， 28]
    2- return {"name":"小明"，"age"：28]
    2- return 返回值1， 返回值2
"""
def my_func04(name, age):
    return name, age

print(my_func04("张三",28)[0])
print(my_func04("张三",28)[1])

"""
    python中的拆包(列表，字典，多个返回值): 一次性初始化多个变量的值
    如果返回值是列表，字典，或者多个返回值，可以直接用来赋值多个变量的方式就叫做拆包，简化代码量
"""
num01, num02, num03, num04 = 1, 3.14, True, "Hello World"
num05, num06, num07, num08 = [1, 3.14, True, "Hello World"]
name, age = my_func04("李四", 28)
print(name, "-->", age)

"""
    拆包中python快速交换两个变量的值, 免去了temp中间值
"""
a, b = 4, 5
a, b = b, a     # b的引用给a, a的引用给b，快速交换值

