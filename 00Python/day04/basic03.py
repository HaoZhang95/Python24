"""
    help(str)
"""
help(str)   # 查看str数据类的所有方法和说明
help(str.count)   # 查看str数据类的某个具体方法,方法说明文档

"""
    list列表**有序**数据结构，python中的list可以装任何类型的元素在同一个list中
    如果遍历list的时候想要获取index，好像只能使用while小于len的方法
"""
a_list = [1, 3.14, "hello world", True, [1,2,3] ]
b_list = []
c_list = list()
print(len(c_list))  # 返回0表示这个list是一个空的list

for temp in a_list:
    print(temp)

i = 0
while i < len(a_list):
    print(a_list[i])
    i += 1

"""
    list添加元素是在原list进行修改的,列表是可变的，和str的操作不同，str是不可变的
    list.append -> 追加
    list.extend(obj) -> 继承一个可迭代的对象，将obj中的每一个元素拿出来进行追加append
    list.insert(index, obj) -> 在index的位置上插入一个obj, 如果index越界，不会报错，直接在末尾append
"""
d_list = [1, 2, 3]
d_list.append("4")
d_list.extend("abcd")   # 字符串本身就是一个可迭代的对象 -> [1, 2, 3, '4', 'a', 'b', 'c', 'd']
d_list.insert(1,"abcd")   # [1, 'abcd', 2, 3, '4', 'a', 'b', 'c', 'd']
print(d_list)

"""
    
"""