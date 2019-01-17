
# ==============================
# 单行注释以警号开始
# 注释一般是用在有意义的代码上，hello world大家都看得懂，没必要注释
"""
    多行注释内容， 三个双引号或者单引号都可以
    '''多行注释内容'''
"""
print("Hello World！")

# ==============================
# 变量（变量名是没有意义的，用来临时保存数据的，箭头指向内存空间）

num1 = 10
num2 = 20
result = num1 + num2
print(result)

# ==============================
# 变量的类型， int,long,float,complex复数
# python中没有double的双精度类型
# bool(没有ean),string,list,tuple（元组==数组），dictionary（字典）
name = "老王"
print(type(name))   # <class 'str'>

is_man = True
is_woman = False
print(type(is_man))

# ==============================
# 标识符 == 自己定义的变量名，函数名等等， 有命名规则