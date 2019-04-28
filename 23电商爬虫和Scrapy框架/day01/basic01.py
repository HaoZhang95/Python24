import pymongo

"""
    MangoDB术语的对应表
    database --> database
    table    --> collection
    row      --> document
    column   --> field
"""

# 客户端对象
client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

# 数据库对象
db = client.get_database('Python24')

# 集合对象
collection = db.get_collection('Test')

def test01():
    """ python&mongo交互 """

    # 客户端中的数据库列表
    print(client.list_database_names())
    # 客户端连接信息
    print(client.address)

    # 使用db对象获得集合的方式和client的操作类似
    print(db.list_collection_names())
    # 创建删除集合
    # db.create_collection('Test2')
    # db.drop_collection('Test2')

    # 查询操作
    print(collection.find())    # find方法都会返回一个游标对象

    # 遍历这个游标对象
    for data in collection.find():
        print(data)

    # 或者直接把游标转换为list进行输出
    print(list(collection.find()))

    # find方法都是返回游标，需要for循环遍历获取
    print(collection.find_one({'name': 'Hao Zhang'}))
    # for data in collection.find({'name': 'Hao Zhang'}, {'age': '25'}):
    #     print(data)


def test02():
    """CRUD"""

    # insert
    collection.insert_many([
        {"item": "journal",
         "qty": 25,
         "tags": ["blank", "red"],
         "size": {"h": 14, "w": 21, "uom": "cm"}},
        {"item": "mat",
         "qty": 85,
         "tags": ["gray"],
         "size": {"h": 27.9, "w": 35.5, "uom": "cm"}},
        {"item": "mousepad",
         "qty": 25,
         "tags": ["gel", "blue"],
         "size": {"h": 19, "w": 22.85, "uom": "cm"}}])



def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

