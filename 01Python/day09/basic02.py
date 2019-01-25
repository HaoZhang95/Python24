"""
    文件和文件夹的操作模块os
"""
import os

# 重命名
# os.rename("Test.txt","NewTest.txt")

# 删除
# os.remove("Test(备份).txt")

# 创建文件夹,  open的方式是创建文件
if not os.path.exists("MyFolder"):
    os.mkdir("MyFolder")

# 获取当前路径, getcwd()
myPath = os.getcwd()
print(myPath)

# 改变当前目录(类似于鼠标的返回上一级目录位置)
os.chdir("MyFolder")
print(os.getcwd())

# 无论是../或者是./都是相对路径
os.chdir("../")
print(os.getcwd())

# ../ 返回上一级目录， ./ 返回当前路径
os.chdir("./")
print(os.getcwd())

# 获取目录列表
result = os.listdir(os.getcwd())
print(result)

"""
    批量修改文件名
    1- 先创建模拟文件夹和10个文件
    2- 开始批量的重命名
"""
folder_name = "MyNewFolder"
if not os.path.exists(folder_name):
    os.mkdir("MyNewFolder")

# 创建文件之前先更改当前目录！
os.chdir(folder_name)

for i in range(1,11):
    open("Test%d.txt" % i,"w").close()

file_list = os.listdir()
for temp in file_list:
    new_name = temp.replace(".txt", "(新名字).txt")    # temp识别不出是字符串，需要手动敲
    os.rename(temp,new_name)        # os的任何操作都是在根据当前目录下完成的，用前先设置当前目录
