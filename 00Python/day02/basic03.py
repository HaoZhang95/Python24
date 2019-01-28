"""
    数据类型之间的互相转换
    int(对象,x进制) 将对象**先看作**x进制的对象，再转换为十进制的输出， 默认不写就是十进制
"""
str1 = "11"
int_str1 = int(str1,8)  # 11（8） = 9 （10）代表八进制的11，转换为十进制输出=9
print(type(int_str1))
print(int_str1)

str2 = "3.14"
float_str2 = float(str2)
print(type(float_str2))
print(float_str2)

"""
    str(x) 将对象x转换为字符串，给程序员看的，ide进行了处理，不会带引号
    repr(x) 将对象x转换为表达式字符转，给python看的，cmd下带引号
"""

"""
    eval(str) 用来计算字符串中的有效python表达式，
    去除双引号去看真实的数据类型，并返回一个对象
    
    但是"int1" -> int1发现该行之前有int1的变量为int类型的123456，那么久返回该int类型
    或者说，1，3.14类型python都能认出是什么类型的，但是拔掉引号的abc就不知道了，如果前面变量没有叫做abc的，那么就会报错not defined
"""
int1 = 123456
str1 = "abc"
num1 = eval(input("请输入："))  # "1" -> 1 返回的对象就是int类型的1
print(num1, "type = %s" % type(num1))