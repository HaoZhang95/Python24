"""
    字典数据类型dictionary表示方法： 花括号{}
    list获取元素有些问题： 如果某个元素的名字错了， 然后list的顺序也发生了变化
    因为list的有序index问题，都某一个元素进行修改会比较麻烦

    这样就出现了字典的形式key-value，无序， 方便的进行某一元素的修改
"""

a_dict = {"name": "张三", "age": 20, "id": "007"}
print(a_dict)
b_dict = {}
c_dict = dict()


"""
    字典的常见操作
    字典的key必须是**不可变**，可以是任意类型，元组也可以为key，因为元组是不可变的
    注意字典的key必须不可变但是可以重复， 重复的话获取的是最后一个
"""
d_dict = {(1,2,3): "元组value01",
          "name": "张三",
          "info": {"address": "石家庄", "country": "中国"},
          (1,2,3): "元组value02"}

print(d_dict[(1,2,3)])
print(d_dict["info"]["country"])

"""
    字典修改元素的value, 前提是key存在，
    添加元素： 否则就会新增一个key-value
    删除元素： del python内置函数可以用在list, tuple和字典都可以用
"""
d_dict["name"] = "李四"
d_dict["name2"] = "王五"  # name2 不存在， 直接就会添加进去
del d_dict["name2"]
d_dict.clear()
print(d_dict)

"""
    len() 字典的长度
    keys()  返回字典中所有的key的集合, 转化为list类型
    values() 返回字典中所有的value的集合, 转化为list类型
    items()  返回的是一对对key-value以元组的形式
"""
print(len(a_dict))
print(list(a_dict.keys()))    # dict_keys(['name', 'age', 'id']) -> ['name', 'age', 'id']
print(list(a_dict.values()))
print(list(a_dict.items())[1][1])     # [('name', '张三'), ('age', 20), ('id', '007')]

"""
    python3中取消了字典的has_key方法，使用的是setdefault
    使用的是setdefault("key", "找不到的默认值")， 找不到的话会修改添加新的key到字典中
    get(key, 默认值) 和setdefault的作用基本一样， 但是不会添加新的key，原来dict不会变
"""
if "name" in a_dict:
    print("有一个key为name的。")
else:
    print("字典中没有一个key叫做name")

print(a_dict.setdefault("name1", "name的默认值"))    # 找不到name1， 添加进去
print(a_dict)
print(a_dict.get("name2", "name的默认值"))    # 找不到name2， 但是不会添加进去
print(a_dict)



