"""
    list列表元素的修改操作
"""
a_list = [1,2,3,4]
a_list[2] = "双击666"
print(a_list)

"""
    查询list元素 （in, not in, index, count）
    为了避免index方法找不到的报错，解决方案：
    1， 先判断是否in，然后再list.index进行获取
    2， 判断count非零即真，-1等负数也是真，再进行获取
"""
if 1 in a_list:
    print("存在")
if 88 not in a_list:
     print("不存在list中")

print(a_list.index(2))  # 查询某个元素的index， 找不到的话不返回-1，直接报错
print(a_list.count(2))  # 查询某一个元素出现的次数

if a_list.count(22):
    print("22元素存在可以安全的获取索引：%d" % a_list.index(22))
else:
    print("元素不存在列表中")


"""
    list删除元素
    del 是一个内置函数，并不是属性， del 函数直接销毁对象
    pop 是属性，pop()默认删除最后一个，pop(1)删除索引为1的元素，并且返回该元素
    remove 是属性， pop是知道索引进行删除，remove是知道obj进行删除
    clear 清空为[]
"""
b_list = [1, 2, 3, 4]
del b_list[2]   # del b_list的话会直接删除b_list整个list，销毁对象，再print的话就话undefined
print(b_list)

print(b_list.pop(0))
b_list.remove(2)    # remove不存在的元素会抛异常报错
b_list.clear()
print(b_list)