import pymongo

"""
    MangoDB术语的对应表
    database --> database
    table    --> collection
    row      --> document
    column   --> field
"""


def test01():
    """
    mongodb云服务链接
    注意点：登陆的用户和密码并不是Mongodb注册的账号密码，而是为这个数据库创建的用户的用户名和密码
   """

    client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

    # 使用python24这个数据
    db = client.get_database('Python24')
    # 获得试用的table表
    collection = db.get_collection('Test')
    print(collection.name)



def main():
    test01()


if __name__ == '__main__':
    main()

