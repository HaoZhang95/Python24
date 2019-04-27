import pymongo

client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

db = client.get_database('Python')

collection = db.get_collection('Test')

def test01():
    """  """


def main():
    test01()


if __name__ == '__main__':
    main()

