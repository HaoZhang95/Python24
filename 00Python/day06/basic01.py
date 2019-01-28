"""
    应用：列表中的最大值和最小值
"""

import random

a_list = []
for i in range(8):
    a_list.append(random.randint(-100, 100))
print(a_list)

max = a_list[0]     # max初始化不能为0， 要为列表元素之一
for temp in a_list:
    if temp > max:
        max = temp
print("最大值为：%d" % max)

"""
    字符串的字幕出现次数的统计
    1- 利用list装，但是需要判断是否已经在list中存在
    2- set集合（传入可迭代的string），则不需要判断是否已经存在 
"""
a_str = "Hello World"
b_list = []
for temp in a_str:
    if temp != " " and temp not in b_list:
        a_str.count(temp)
        b_list.append(temp)
        print("%s : %d" % (temp, a_str.count(temp)))

a_set = set(a_str)
print(a_set)
for temp in a_str:
    if temp != " ":
        a_str.count(temp)
        print("%s : %d" % (temp, a_str.count(temp)))

"""
    应用： 名片查询系统，三个双引号可以用来保存带有格式的字符串
    [
        {"小明"：{"name"： "小明"， "age":18}},
        {"小明"：{"name"： "小明"， "age":18}},
        {"小明"：{"name"： "小明"， "age":18}}
    ]
    input()无论输入什么都是str类型，并不是真实类型
    1- if语句中也可以使用数学的 0 < int(index) < 6 来表示范围
    2- if语句或者表达式中若逻辑没有想清楚，可以先试用pass保证编译通过
"""
str_info = """请选择
1-添加名片
2-删除名片
3-修改名片
4-查询名片
5-退出系统
"""
all_dict = dict()

while True:
    index = input(str_info)
    if index.isdigit() and (0 < int(index) < 6):
        # 添加名片
        if index == "1":
            my_name = input("请输入你的名字：")
            my_age = input("请输入你的年龄：")
            my_dict = {"name": my_name, "age": my_age}
            all_dict[my_name] = my_dict
            print("保存数据成功")
        # 删除名片
        elif index == "2":
            my_name = input("请输入删除的名字：")
            if my_name in all_dict:
                del all_dict[my_name]
                print("删除数据成功")
            else:
                print("你输入的名字不存在。")
        # 修改名片
        elif index == "3":
            my_name = input("请输入需要修改的名字：")
            if my_name in all_dict:
                my_age = "请输入修改的年龄："
                all_dict[my_name] = my_age
                print("数据修改成功")
        # 查询名片
        elif index == "4":
            my_name = input("请输入需要查询的名字：")
            if my_name in all_dict:
                print(all_dict[my_name])
            else:
                print("你输入的名字不存在。")
        # 退出系统
        elif index == "5":
            print("欢迎下次使用.")
            break
    else:
        print("输入错误")
