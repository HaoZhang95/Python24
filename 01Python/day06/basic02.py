
"""
    python定义函数， 对代码进行封装，python也是引用传递，而不是值传递
    1- 如果函数名一样，python并不会报错，而是会覆盖
    def 函数名(参数)
"""
def my_print():
    print("HAHAHHA")

def my_print():
    print("HAHAHHA22222")

for i in range(5):
    my_print()

# 如果提示shadows in xxx build in是因为你定义的函数名和内置的函数名一样，比如sum()
def my_sum(a, b):
    print("a + b = %d" % (a + b))

my_sum(1,5)

# 带有返回值的函数， 使用 -> 的方式，和typescript类似
def my_sum(a, b) -> int:
    return (a + b)
print("a + b = %d" % my_sum(1, 5))

"""
    函数的嵌套调用，就是函数中调用另一个函数
    1- my_func02 必须定义在My_func01之前，真正调用的时候才会加载，并不会全局预加载
    2- 内置函数的作用域，不会自动调用
"""
def my_func02():
    print("C")
    print("D")

def my_func01():
    print("A")
    my_func02()
    print("B")

my_func01()


def my_func03():
    print("A")
    # 内置def函数，注意作用域， 注意内置函数不会自动调用
    def my_func04():
        print("C")

    my_func04()
    print("D")
    print("B")

my_func03()

# 函数参数的乱序位置，也可以像kotlin一样添加关键字参数
# 注意： 如果某个参数使用了关键字参数，那么之后的参数必须都必须使用关键字参数
#        换句话说，就是参数可以合理的一一对应，开发中一般很少使用关键字参数，看懂即可
def get_info(name, age) -> str:
    return "name: %s, age: %s" % (name, age)

print(get_info(age= "26", name="张三"))
