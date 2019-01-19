"""
    list元素的排序
    sort() 默认无参数是从小到大
    reversed(list) 整个列表直接反过来，返回值是一个新的list
"""
import random

a_list = []
for i in range(10):
    a_list.append(random.randint(0, 200))
print(a_list)
a_list.sort()
print(a_list)

a_list.sort(reverse=True)   # 降序，从大到小
print(a_list)

new_list = reversed(a_list)     # [12,10,7,9] -> [9,7,10,12]
print(new_list)


"""
    一个学校，三个办公室， 八位老师进行随机分配办公室
"""
school = [[], [], []]
teacher_list = list("ABCDEFGH")

for name in teacher_list:
    index = random.randint(0,2)
    school[index].append(name)
print(school)

"""
    字符串表示："", '', """"""
    list表示：[]， 可修改
    元组的表示：(), 元组的元素不能进行修改，
    元组中如果只有一个元素的话，后面加上逗号表明是一个tuple，否则就是元素真实类型
"""
a_tuple = (1, 3.14, "Hello", True)
empty_tuple = ()
empty_tuple2 = tuple()

# 特例
b_tuple = (1)    # type = int
c_tuple = (1,)    # type = tuple

"""
    访问元组tuple
    查询的话和list一样使用count， index
"""
print(a_tuple[2])
# a_tuple[1] = "哈哈" 元组的元素不能重新赋值和修改，因为tuple是不可变的

print(a_tuple.count(1))    # 元组中1对象出现的次数是2， 因为Ture在计算机眼中就是1
print(a_tuple.index(3.14))
