"""
    分布式把数据去重存储到redis之后，把数据转存到mongodb中
"""
import json

import pymongo
import redis

# 实例化redis客户端
redis_client = redis.Redis(host='127.0.0.1', port=6379)

# 实例化mongodb客户端
mongo_client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

db = mongo_client.get_database('Python')

collection = db.get_collection('Redis_Mongo')

while True:
    # 从redis中取出名为book:items的数据,从左端pop
    key, value = redis_client.blpop('book:items')
    print(key)
    print(value)

    # 转存到mongodb中,需要把redis中的数据decode，因为redis去重使用了hash二进制
    item = json.loads(value.decode())
    collection.insert_one(item)

# 关闭mongodb
mongo_client.close()
