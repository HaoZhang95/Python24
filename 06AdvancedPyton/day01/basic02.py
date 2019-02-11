"""
    浅拷贝: 类似于新建快捷链接，复制的是指向文件的**箭头链接**，在程序中的就是**指向的地址**
    深拷贝: 拷贝的就是数据本身
"""
"""
    验证思路，a: 根据id b:修改其中一个，查看另一个变不变
    当 b = a的时候，就是b**指向**a的地址，不涉及深拷贝和浅拷贝，只是引用的层级
"""
a = [11, 22]

b = a

print(id(a))
print(id(b))

a.append(33)
print(a)
print(b)

c = [11, 22]
d = [33, 44]
e = [c, d]
"""
    拷贝引入copy模块
    1- d = e 是d指向了e的引用地址， d = copy.copy(e) 则是copy了e
    2- copy的两种情况，浅拷贝：创建了e，但是e中的c,d并没有赋值，c,d还是使用的引用地址
                      深拷贝: 创建了e，同时也copy了e中的c,d

    3- c中进行了改变，浅拷贝导致层中层的d，e都发生了改变
    4- copy中的copy方法，只是复制一层，并没有**递归**进行深度复制
    5- copy中的deepcopy方法，会**递归**着进行深度复制
"""
import copy

# d = copy.copy(e)
d = copy.deepcopy(e)
print("c的地址是和d中的c相等：%s" % c == d[0])
print("d的地址是和d中的d相等：%s" % c == d[1])

c.append(88)
print(e)
print(d)
"""
    n是一个不可变的元组，里面包含一个可变的列表
    1- 如果浅拷贝的是一个不可变的元素的时候，假如真的把最外层的copy一份，这就意外这n和n1都指向的空间都不能修改，这样就浪费了空间
    2- 结论就是：浅拷贝的是一个不可变的lexington的时候，连最外层的那一层都不会被copy
                深拷贝：如果只是一层不可变的类型的话，那么深浅拷贝不会copy，只是**引用指向**
                        如果最外边是不可变，里面的是可变类型，那么只要里面有一层是可变的，那么深拷贝就拷贝
    3- c = b[:]列表的从头到尾切，是浅拷贝
    4- 字典dict可以直接使用copy方法，字典默认的copy方法和切片都是**浅拷贝**,只拷贝最外一层
"""
m = [11, 22]
n = (m, )

# n1 = copy.copy(n)
n1 = copy.deepcopy(n)
print("n的地址是和n1相等：%s" % (id(n) == id(n1)))

a_dict = {"name": "张三", "age": 18, "family": ["father", "mother", "brother"]}
b_dict = a_dict.copy()
a_dict["family"].append("Children")
print(a_dict)  # 浅拷贝，只拷贝最外一层，dict里面的列表并没有修改，只是引用同一个
print(b_dict)
print("a_dict的地址是和b_dict相等：%s" % (a_dict == b_dict))
