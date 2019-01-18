# 查看关键字的模块 keyword

import keyword
print(keyword.kwlist)

# 格式化输出print, %d代表占位符是一个整数
age = 12
print("我的年龄是%d岁" % age)

age += 1
print("我的年龄是%d岁" % age)

# 常用的格式符号
# %s -> string
# %d -> int (digit)
# %f -> float (%f占位符默认是显示小数点后6位的)
# bool数值的格式化输出比较特殊（%s进行打印True/False, 或者%d打印1，非零即真）
my_name = "小明"
my_age = 25
is_man = True
my_height = 180.88

print("我的姓名：%s" % my_name)
print("我的年龄：%d" % my_age)
print("我的身高：%f" % my_height)
print("我的身高：%.2f" % my_height)
print("我的性别为男：%s" % is_man)
print("我的性别为男：%d" % is_man)

# 在python百分号已经作为特殊符号，如果想表达一个%使用两个百分号替代一个百分号
purity = 86
print("纯度为：%d%%" % purity)

# 换行输出只能使用\n
print("Hello")
print("Hello", end="\n")    # 等同于上面的写法

print("Hello", end=" ")    # 两个print同行
print("World")
print("Hello\nWorld")





