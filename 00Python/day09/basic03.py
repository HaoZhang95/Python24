"""
    学生管理系统： 文件操作和函数的综合应用
    1- 用文件写入一个字典，持久化保存数据， 启动系统的时候用内存中的all_dict而不是每次读取文件，效率问题
    2- 只有点击保存的时候才会写入到文件中，期间一直是内存中的all_dict
    3- 注意： 全局变量在函数内部修改的话需要使用global
"""
import os

all_dict = {
    # "小明": {"name":"小明", "age": 22},
    # "小红": {"name":"小红", "age": 28}
}

file_name = "StudentManageSystem.txt"

def load_info():
    if not os.path.exists(file_name):
        file = open(file_name, "w", encoding="utf-8")
        file.write("{}")
        file.close()

    file = open(file_name, "r", encoding="utf-8")

    global all_dict       # 不写globe的话直接定义一个新的变量，这是一个坑，并不会自动使用全局变量
    all_dict = eval(file.read())       # 不能直接往文件中写入字典，需要转换为字符串
    file.close()


def print_menu():
    print("-------------------------------")
    print("         学生管理系统 V1.0")
    print(" 1-添加学生")
    print(" 2-删除学生")
    print(" 3-修改学生")
    print(" 4-查询学生")
    print(" 5-显示所以学生")
    print(" 6-保存数据")
    print(" 7-退出系统")
    print("-------------------------------")

    index = input("请输入你的选择:")
    if index.isdigit() and (0 < int(index) < 8):
        return int(index)
    else:
        print_menu()       # 递归重新显示自己，知道正确才会有返回值


# 1- 添加学生
def add_info():
    my_name = input("请输入你的名字：")
    my_age = input("请输入你的年龄：")
    my_dict = {"name":my_name, "age": my_age}
    all_dict[my_name] = my_dict
    print("保存数据成功...")

# 2- 删除学生
def delete_info():
    my_name = input("请输入需要删除的名字：")

    if my_name in all_dict:
        del all_dict[my_name]
        print("删除数据成功...")
    else:
        print("你输入的名字不存在...")

# 3- 修改学生
def update_info():
    my_name = input("请输入需要修改的名字：")

    if my_name in all_dict:
        my_age = input("请输入你的年龄:")
        all_dict[my_name]["age"] = my_age
        print("修改数据成功...")
    else:
        print("你输入的名字不存在...")

# 4- 查询学生
def select_info():
    my_name = input("请输入需要查询的名字：")

    if my_name in all_dict:
        print("查询数据成功... %s" % all_dict[my_name])
    else:
        print("你输入的名字不存在...")

# 5- 查询所以学生
def select_all_info():
    print("查询全部数据成功... %s" % all_dict)

# 6- 保存数据
def save_info():
    file = open(file_name, "w", encoding="utf-8")
    file.write(str(all_dict))       # 不能直接往文件中写入字典，需要转换为字符串
    file.close()

def main():
    load_info()
    while True:
        index = print_menu()
        if index == 1:
            add_info()
        elif index == 2:
            delete_info()
        elif index == 3:
            update_info()
        elif index == 4:
            select_info()
        elif index == 5:
            select_all_info()
        elif index == 6:
            save_info()
        elif index == 7:
            break

main()