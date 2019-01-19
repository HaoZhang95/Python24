"""
    字典的遍历,
"""
a_dict = {"name": "张三", "age": 20, "id": "007"}

for key in a_dict.keys():
    print(key)

for value in a_dict.values():
    print(value)

for item in a_dict.items():     # 遍历字典的元素，返回一个个元组（），（）
    print(item)

for key, value in a_dict.items():     # 遍历字典的键值对
    print(key, "->", value)

str1 = "xxx"
str2 = "yyy"
print(str1, str2)   # print多个变量， 第二个参数默认是一个空格：xxx yyy
print(str1, "--->", str2)   # xxx ---> yyy

"""
    enumerate(list / tuple等带有索引的数据结构)可以获得index
"""
a_list = ["张三", "李四", "王五"]
a_tuple = ("张三", "李四", "王五")

for index, temp in enumerate(a_list):
    print(index, "-->", temp)


"""
    集合set表示花括号{}， 无序不可重复,重读的话只保留一份，python自动去重操作
    add() 添加到set中， 相当于list中的append
    update(可迭代对象)， 类似于list中的extend， 将可迭代的最小单元add到set中
"""
a_set = {1,3,5,7,3}
print(a_set)       # {1, 3, 5, 7} 去重操作

b_set = set()
c_set = {}  # 指的是空的字典，并不是集合set类型

a_set.add(11)
a_set.update("abcd")
print(a_set)

"""
    set中的删除
    remove(obj), set无序，只能根据obj进行删除，找不到obj的话异常
    pop(), 因为set无序， 删除的并不是最后一个，而是随机的删除一个元素
    discard(), 元素存在删除， 不存在则不会发生异常
"""
a_set.remove(1)
a_set.pop()
a_set.discard(111)   # set中的discard安全一点，不会异常
print(a_set)

"""
    多个set集合的操作, 交集并集主要用在多个set的去重
    & -> 交集
    | -> 并集
"""
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print(set1 & set2)
print(set1 | set2)

# 去重的话讲list转换为set的话直接迅速， 不需要手动判断
a_list = [1, 3, 4, 3, 4, 5, 6]
print(set(a_list))

# 利用set集合的特点，进行多个list的去重, 将每一个list转换为set求交集即可，一行代码搞定
b_list = [1, 2, 3, 4]
c_list = [3, 4, 5]
print(set(b_list) | set(c_list))


"""
    字符串， list， 元组， 字典等运算符公共方法
"""
print([1,2] + [3,4])    # [1, 2, 3, 4]
print([1,2] * 4)        # [1, 2, 1, 2, 1, 2, 1, 2]
print(3 in [1,2,3])     # True
print(3 not in [1,2,3]) # False


