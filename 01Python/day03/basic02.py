"""
    for循环
    range(0,5) 默认index为0， 循环5次，[0,5)
    range(1,6) 默认index为1， 循环5次，[1,6)
"""
name = "张三"
for temp in name:
    print(temp)

for temp in range(5):
    print(temp)

for temp in range(1,6,2):
    print(temp)

print("================")

"""
    for循环应用,打印三角形
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

"""
    break和continue,是配合循环才能使用
"""
for i in range(1,6):
    if i == 2:
        continue
    if i == 3:
        break
    print(i)

print("================")

"""
    for-else-break 和 while-else，比较pythonic， 主要用来判断循环是不是以break的方式结束
    for循环**正常**结束之后，执行else块中的代码, continue不影响else块中的执行代码
    for循环**非正常**结束之后，就是循环中是以break方式结束的，就不会执行else块中的代码
"""
for i in range(1,6):
    print(i)
else:
    print("else")
print("测试结束")

for i in range(1,6):
    if i == 2:
        break
    print(i)
else:
    print("else")
print("测试结束")
