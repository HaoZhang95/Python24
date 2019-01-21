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