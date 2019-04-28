import pymongo

"""
    MangoDB术语的对应表
    database --> database
    table    --> collection
    row      --> document
    column   --> field
"""
client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

db = client.get_database('Python')

collection = db.get_collection('Test')

def test01():
    """  """

    print(collection.name)


def main():
    test01()


if __name__ == '__main__':
    main()

