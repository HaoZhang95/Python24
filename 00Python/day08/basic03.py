"""
    文件操作,open()返回一个file对象，r+主模式为读，但也可以写。 w+主模式为写，但也可以读
    1- 如果"r"的方式打开，不存在会报错异常，存在的话会打开并且返回该对象
    2- 如果"w"的方式open，不存在的文件不会报错，但是会**创建**一个新的文件
    3- 读取和写入的时候不能write多次和read多次，只能open-close之后再次操作，否则无效
"""
# 文件的打开
a_file = open("Test.txt", "w+")
# 文件的读写
a_file.write("Hello World!")
# 关闭文件
a_file.close()

"""
    1- read(2) 读取2个字节， 无参表示读取全部
    2- readline() 读取一行，再次readline()就会光标读取下一行
"""
b_file = open("Test.txt", "r")
result = b_file.read()
print(result)
b_file.close()

"""
    中文的问题，可以在open的时候关键字参数指定编码open(encoding="utf-8")
    file的访问模式：
    1- "w" 先清空再写入，以文本的方式写入保存
    2- "r" 不存在会直接异常报错
    3- "a" -> append追加，也是写入的一种
    4- "rb" 读取进制数据,显示的都是16进制的数字，需要解码decode
    5- "wb" 以二进制的方式写入， 保存方式的不同，直接保存文本会报错，需要.encode("utf-8")保存
"""
c_file = open("Test.txt","wb")
c_file.write("中国".encode("utf-8"))  # 文本.encode压缩
c_file.close()

d_file = open("Test.txt","rb")     # 中文只能read(3)显示一个汉字
result = d_file.read().decode(encoding="utf-8")     # 二进制读取的解码
print(result)


