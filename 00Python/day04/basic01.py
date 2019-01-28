"""
    字符串string, 从左向右从0开始，从右向左-1，-2，-3.。。
"""
a = "abcdef"
print(a[2])
print(a[-2])

"""
    字符串的基本操作, python中的字符串是不可变的，会拷贝一份进行修改，原string不变
    切割,并没有slice函数直接中括号，中间使用**冒号**隔开 [起始：结束：步长]
"""
print(a[0:3])   # abc
print(a[0:5:2]) # ace 或者是省略直接写冒号
print(a[::2])   # ace 步长为2表示隔着读取
print(a[1:4:2])   # bd 从b开始读取
print(a[::-2])   # fdb 步长为负数表示从右到做，倒着读
print(a[-1:-4:-2])   # fd 步长为负数表示从右到做，倒着读
print("===========================")

"""
    self参数不用管，不填即可
    a.find(self, subStr, start, end) 检测a在start,end区间内是否包含subStr,返回值是subStr的index
    a.rfind(self, subStr, start, end) 从右边倒叙查找，但是没有lfind因为find()默认就是左边开始
    a.index(self, subStr, start, end) 方法和find一样，不建议使用，如果index找不到报错异常
    a.count("b") 检测b在a字符串中出现的次数
    a.replace(self, old, new, count) 该方法返回新的str，count指定的话，则替换不超过count次
    a.split(self,sep,maxSplit) 去除sep后的a返回一个[]
"""
print(a.find("c"))
print(a.rfind("c"))
print(a.index("c"))
print(a.count("c"))
print(a.replace("c","C",2))
print(a.split("c"))     # ['ab', 'def']

"""
    a.capitalize()  字符串**首字母**进行大写
    a.title()  字符串**每个单词的首字母**进行大写
    a.startswith()  字符串是否已某个字串开始
    a.endswith()  字符串是否已某个字串结尾
    a.lower()  字符串所有字母进行小写
    a.upper()  字符串所有字母进行大写
"""
b = "hello world"
print(a.capitalize())
print(b.title())
print(a.startswith("ab"))
print(a.endswith("ab"))
print(a.lower())
print(a.upper())
print(a.islower())
print(a.isnumeric())




