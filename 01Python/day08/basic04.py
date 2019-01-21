"""
    应用： 文件的备份copy
"""

old_file = open("Test.txt", "r")
result = old_file.readlines()
print(result)

# for循环开始进行copy写入
new_file = open("Test(附件).txt", "w")
for line in result:
    new_file.write(line)

old_file.close()
new_file.close()

"""
    上面的例子直接readlines()，并不是完美的copy方法
    如果文件过大，一点点的读取写入，内存问题，防止电脑变卡
    在读取的时候，可以按行读取或者按照公司的字节读取（2014）
"""