"""
    list列表使用lambda自定义排序, list.sort(lambda)
    lambda中拿出alist中的每一项temp，按照temp["name"]进行排序
"""
a_list = [
            {"name": "张三", "age":19},
            {"name": "李四", "age":18},
            {"name": "王五", "age":20}
        ]

a_list.sort(key=lambda temp: temp["age"],reverse=True)
print(a_list)

# list中包含多个list，嵌套list,按照元素的第二个数字进行排序
b_list = [[5, 3, 5], [1, 1, 3], [9, 1, 12]]
b_list.sort(key=lambda temp:temp[1])
print(b_list)

"""
    列表推导式只能创建**有规律**的列表：
    列表名 = [temp for temp in range(100) if temp % 2 == 0], temp是要往list中添加的值
"""
c_list = []
for i in range(100):
    c_list.append(i)
print(c_list)

d_list = [temp for temp in range(100)]  # 列表推导式
print(d_list)

e_list = [temp for temp in range(100) if temp % 2 == 0]
print(e_list)

# 添加3个形同的元素
f_list = ["Hello World %i" % i for i in range(3)]
print(f_list)

# 列表中装有三个元祖()
g_list = []
for i in range(3):
    for j in range(2):
        g_list.append((i,j))
print(g_list)

h_list = [(i, j) for i in range(3) for j in range(2)]
print(h_list)

# 列表的切片 list[start: end]
j_list = [temp for temp in range(1, 12)]
print(j_list[0: 3])     # [1,2,3]
print(j_list[3: 6])     # [4,5,6]

"""
    将[1,2,3,4,5,6,7,8,9,10,11,12] -> list中套用三个一组的小list
    列表中的每一项为j_list[temp: temp+3]， 三个一组的小列表
    temp每一次的取值为range(0, len(j_list), 3) -> 0,3,6,9
    导致小列表的切片们j_list[0: 3], j_list[3: 6], j_list[6: 9]等规律
    输出结果为： [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11]]
"""
k_list = [temp for temp in range(1,13)]
l_list = [k_list[temp: temp + 3] for temp in range(0, len(k_list), 3)]
print(l_list)

"""
    引用，int是不可变的数据类型
    不可变的数据类型，函数内进行修改的话是重新开一个房间，不会影响全局变量的值
    可变的话，就直接在本身进行修改，只有一个房间
    1- 如果要避免[1],[1,1],[1,1,1]的话要在程序运行的时候不能使用同一个m_list去append
    2- 做法是：将缺省的形参设置为None类型，None类型也是会开辟空间的id()
    3- 每次进入都直接创建新的[]去append，这样就不会重复使用同一个[]
"""
def a_func(m_list=[]):
    a_list.append(1)
    print(m_list)

a_func()
a_func()
a_func()

def b_func(n_list=None):
    if n_list is None:
        n_list = []

    n_list.append(1)
    print(b_list)

b_func()
b_func()
b_func()

