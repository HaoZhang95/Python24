"""
    Reids中的主从，实际中读写比例10：1读取的多，降低某一台服务器的压力，提高效率
    主服务器同于写数据，从服务器用于读取主服务器的数据，实现了读写分离

    配置好redis-server a.conf 是根据不同的conf文件启动不同的服务器，设置好salveof
    从的服务器只能从主的服务器中get读取，不能写入修改，主服务器的数据是共享与所有的从服务器
"""

"""
    集群解决并发访问，防止服务器卡死，概念就是四川人访问四川的服务器，
    当请求到来首先由负载均衡服务器处理，把请求转发到另外的一台服务器上。负载均衡
    
    redis集群中，当一个master主服务器挂掉，才会启动一个其对应得salve服务器充当master

    python访问集群，需要安装redis-py-cluster插件
"""
if __name__ == '__main__':
    try:
        # 构建所有的主节点，Redis会使⽤CRC16算法，将键和值写到某个主服务器节点上
        startup_nodes = [
            {'host': '192.168.26.128', 'port': '7000'},
            {'host': '192.168.26.130', 'port': '7003'},
            {'host': '192.168.26.128', 'port': '7001'},
        ]
        # 构建StrictRedisCluster对象，并且将相应进行解码显示成string可读的形式
        src = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        # 设置键为name、值为itheima的数据
        result = src.set('name',' itheima')
        print(result)
        # 获取键为name
        name = src.get('name')
        print(name)
    except Exception as e:
        print(e)