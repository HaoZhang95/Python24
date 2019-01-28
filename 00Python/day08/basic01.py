"""
    python中的递归函数, time模块中的sleep(单位是秒s)
    1- 用现有的while循环来实现
    2- 递归实现，必须有一个停止的条件来调用自己
"""
import time
# def a_func(duration):
#     while duration > 0:
#         time.sleep(1)
#         print("重新发送(%ss)" % (duration -1))
#         duration -= 1
#
# a_func(3)

# def b_func(duration):
#     if duration > 0:
#         time.sleep(1)
#         print("重新发送(%ss)" % (duration -1))
#         duration -= 1
#
#         b_func(duration)
# b_func(3)

"""
    n! = {
            if   ->  n * (n - 1)!   if( n>=0)
            else ->  1              if( n=0)
         }
    
    1- f(3) -> 3*f(2)
    2- f(2) -> 2*f(1)
    3- f(1) -> 1*f(0)
    4- f(0) -> return 1
"""
def c_func(num):
    if num > 1:
        return num * c_func(num - 1)
    else:
        return 1

print(c_func(3))

"""
    递归的核心就是将表达式分部分，重复的部分和截至的部分
    递归求fib序列: 1 1 2 3 5 8
    fib(n) = {
                n = fib(n-2) + fib(n-1)   if n>2
                n = 1                     else (n=1 or n=2)    
             }
"""
def d_func(num):
    if num > 2:
        return d_func(num-2) + d_func(num-1)
    else:
        return 1

print(d_func(6))

"""
    youtube上跳楼梯的递归算法，求多少种可能性,实质答案就是fib序列
    主要关键是第一步跳1还是2，或者说迈大步还是迈小步
"""
def e_func(floor):
    if floor == 1 or floor == 0:
        return 1
    else:
        return e_func(floor-1) + e_func(floor-2)

print(e_func(4))

"""
    lambda关键字表示这是一个匿名函数，通过小括号来执行()
"""
# 无参数无返回值
def f_func():
    print("Hello World 1")

f_func()

a_lambda = lambda: {
    print("Hello World 2")
}
a_lambda()

(lambda: {print("Hello World 3")})()

# 无参数有返回值, lambda冒号后面不用写return
def e_func():
    return "Hello World 4"
print(e_func())

print((lambda: "Hello World 5")())

# 有参数，无返回值,参数写在lambda后面，冒号前面
def f_func(name):
    print(("Hello World 6 --> %s" % name))
f_func("张三")

(lambda name: {print(("Hello World 7 --> %s" % name))})("张三")

# 有参数，有返回值
def g_func(name):
    return "Hello World 8 --> %s" % name
print(g_func("李四"))

print((lambda name: {"Hello World 9 --> %s" % name})("李四"))

"""
    匿名函数lambda作为函数参数
    函数内a,b进行特定操作后，最后交给callback进行回掉
"""
def h_func(a,b,callback):
    print("result = %d" % callback(a,b))

# lambda a,b: a + b

h_func(3,5, lambda a,b: a + b)