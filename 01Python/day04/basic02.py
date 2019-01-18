"""
    a.ljust(self, width, fillchar) 字符串进行左对齐，字符串占用的长度和需要填充的字符
    a.rjust(self, width, fillchar) 字符串进行右对齐，字符串占用的长度和需要填充的字符
    a.center(self, width, fillchar) 字符串进行居中，字符串占用的长度和需要填充的字符
    a.lstrip(char) 删除字符串左边的字符，不写参数的话去除的是左边空格，相当于左边trim()
    a.rstrip(char) 删除字符串右边的字符，不写参数的话去除的是右边空格，相当于右边trim()
    a.strip(char) 删除字符串两边的字符，不写参数的话去除的是两边空格，相当于java的trim()

"""
a = "abcdef"
print(a.ljust(10,"0"))      # abcdef0000
print(a.rjust(10,"0"))      # 0000abcdef
print(a.center(10,"0"))      # 00abcdef00
print(a.lstrip("0"))
print(a.rstrip("0"))
print(a.strip("0"))

"""
    a.partition("b") 将字符串以"b"字幕，分割，如果b在中间且只有一个b，那么返回一个数组[前,"b",后]
    a.splitlines()   将字符串逐行分割，返回一个list，非数组，按需求进行选择方法
    a.isalpha()      字符串是否全是字母，不论大小写，返回bool
    a.isdigit()      字符串是否全是数字，返回bool
    a.isalnum()      前两个的集合体al + num，判断字符串是否包含数字或者字母或者混合也行
    a.isspace()      字符串是否只包含空格
    a.join(["xxx","yyy"])      list中每个元素的后面都插入a字符串
    
"""
b = "ab\ncd\nef"
print(a.partition("b")[1])      # ('a', 'b', 'cdef') -> b
print(b.splitlines())      # ['ab', 'cd', 'ef']
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.isspace())
print("x".join(["1","2","3"]))      # 1x2x3
print("".join(["1","2","3"]))      # 123  将list迅速转换为一个字符串

# "abcbdbebf" -> "acdef"
c = "abcbdbebf"
d = c.split("b")    # 去除字符串中所有的b,返回一个list
result = "".join(d)    # list转换为字符串
print(result)
