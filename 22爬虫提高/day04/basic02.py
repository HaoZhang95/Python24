import pymongo

"""
    MangoDB术语的对应表
    database --> database
    table    --> collection
    row      --> document
    column   --> field
"""


def test01():
    """mangodb云服务链接"""


    client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

    db = client.get_database('Python24')
    table = db.Test

    print(table.count_documents({}))


    # table.inventory.insert_one(
    #     {"item": "canvas",
    #      "qty": 100,
    #      "tags": ["cotton"],
    #      "size": {"h": 28, "w": 35.5, "uom": "cm"}})

    print(table.count_documents({}))



def main():
    test01()


if __name__ == '__main__':
    main()

