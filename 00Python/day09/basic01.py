"""
    文件按照字节数量来一步步读取
"""

# 写入一个文件
file = open("Test.txt", "w")
file.write("Hello World, My Name is Hao.")
file.close()

# 读取文件到新的文件中
old_file = open("Test.txt", "r")
new_file = open("Test(备份).txt", "w")

while True:
    temp = old_file.read(5)
    if len(temp) > 0:          # 读取字节大于0就写入
        new_file.write(temp)
    else:                      # 等于0或者小于0就表示无字节可以读取
        break

old_file.close()
new_file.close()