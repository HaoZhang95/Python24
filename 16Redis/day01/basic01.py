"""
    Redis是一种非关系型数据库
    Nosql作为非关系型数据库，都是采用K-V的方式储存数据的，所以不支持sql语法
    相对于关系型数据库：nosql不适合关系复杂的数据库查询场景，只适合简单的关系，其次nosql不支持事务

    nosql类数据库中有：redis，mangodb等，
    Redis支持数据持久化，可以把内存中的数据保存在磁盘上，也支持备份
            同时还支持多种类型的存储，比如list, set, zset,hash等数据结构的存储

    Redis应用场景： 1- 缓存， redis所有数据都是存放在内存中，别名：内存数据库，读取快速
                    2- 在一些大型系统中，巧妙实现一些特定功能：session共享， 购物车等等

                    一般网站首页访问量是最大的，假如网站2个小时更新一次主页，那么久把从mysql读取的数据
                    存入到redis的缓存中，因为操作mysql获取太浪费时间。当用户请求浏览器的缓存时候，才会去数据库请求
                    redis的缓存有可能被用户删除，它只是提高访问体验的辅助工具，真是的数据是在mysql中



    redis-server redis.windows.conf 来启动服务端
    redis-cli -h XXX -p XXX 启动客户端,需要使用不同的终端打开，不能都使用git终端，否则卡住
"""

"""
    String类型
    
    添加：set key value EX 60 == setex key 60 value 单位是秒
        mset key1 value1 key2 value2 key3 value3   m表示mutable可变
    获取: get key1
        mget key1 key2
    追加: append key1 value
    
"""

"""
    键命令，通过获取相关的键keys来进行数据的删除
    
    获取所有的键：keys *
    获取a开头：keys a*
    获取包含a：keys 'a*'
    判断键是否存在：exists key1
    删除键: del key1 key2
    判断键所对用value的类型： type key1 
    设置某个键过期时间： expire key1 seconds
    查询有效时间: ttl key1
"""

"""
    Hash哈希类型，用来存储一个对象的不同属性值(一个key对应多个字段) hset key field value
    
    hast xiaoming name hao
    hast xiaoming height 180    给相同的key设置不同的属性值
    hmset xiaoming name hao height 180
    
    获取所有的属性： hkeys xiaoming
    获取所有的属性值： hvals xiaoming
    
    获取某个属性的值： hget xiaoming name
    获取某些属性的值： hmget xiaoming name height
    
    删除对象的某个属性： hdel key field1 field2

"""

"""
    List类型，是有序的
    
    添加：lpush key value1 value2 ... 左侧添加数据,右侧的rpush
            linsert key before或after 现有元素 新元素， l表示的是list
    获取: lrange key 0 2              l表示的是list，从0-2取出3个数据
            lrange key 0 -1 取出所有的数据
        
    修改某个index的值： lset key index value
    
    删除某个元素：lrem key count value count大于0表示从开头找进行删除， 等于0表示删除所有
                    lrem a2 -2 b    从'a2'列表右侧开始删除2个'b'
"""


"""
    set无序不重复类型，一旦定义只能获取和删除某个元素，set类型不能修改某个元素的值
    
    sadd key value1 value2 添加元素
    srem key value1  删除集合
    
    smembers key 获取集合中的所有元素
"""


"""
    zset类型，有序不重复，不能修改某个元素的值，通过权重将元素从⼩到⼤排序
    
    zadd key score1 value1 score2 value2 根据元素的score权重来设置
    
    zrange key 0 -1 获取所有的有序set
    zrangebyscore key 4 5   获取权重在4-5的元素
    zscore key value1 获取value1的权重
    zrem key value1 value2 删除元素

"""


"""
    select 0 选择d第一个数据库
    flushdb 清空当前数据库
    flushall 清空所以数据库
"""
from redis import *


def demo1():

    try:
        # 连接redis服务器可能网络错误，需要进行try
        # sr = StrictRedis() 如果是默认的配置，直接可以不传参数
        sr = StrictRedis(host='localhost', port=6379, db=0)

        sr.set('name', 'hao')

    except Exception as e:
        print(e)


def main():
    demo1()


if __name__ == '__main__':
    main()




















