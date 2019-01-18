
"""
    print输出， input输入
    python3中只有input，无论用户输入什么都是string类型
    python2中的raw_input就是python3中的input， 但是python2中的input方法，反应的是用户输入的真实类型
"""

# num1 = input("请输入一个数字：")
# print(type(num1))
# print(num1)

"""
    算术运算符， + - * /
    // 取整除
    % 取余数
    ** 指数
    
    python中可以一行中赋值多个变量，比较pythonic
"""
num1 = 5
num2 = 2
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)
print(len(str(num1 ** num2)))

num3, num4, str1, str2 = 1, 2, "a1", "a2"

"""
    复合运算符 += /= //=，
    符合运算符可以减少一个变量的产生，但是会改变一个变量的值
    如果变量只会用到一次，可以使用复合运算符，否则不建议
"""
a = 9
b = 2
result = a // b
print("Result = %d" % result)
print("是否相等: %s" % (result == a // b))

