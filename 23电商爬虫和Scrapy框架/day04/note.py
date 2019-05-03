"""
    集群是指一个任务在多个地方运行(一个服务器在多个地方运行)
    分布式是指一个任务分成多个子任务共同完成(爬虫中多个人爬取同一个网站，但是需要去重)
    scrapy-redis分布式：实现多人获取数据去重，scrapy并不支持分布式
    scrapy-redis分布式原理：结合了redis和scrapy

    scrapy和scrapy-redis区别：
    1- 请求的处理，前者是在调度器中处理，后者实在redis数据库队列中处理
    2- duplication filter重复过滤器，前者是在python的集合中去重，后者是在redis数据库中的set中去重
    3- itempipeline管道，前者使用管道来处理数据的后续，后者把数据自动放到redis数据库队列中，读写的时候直接从内从中读取数据
    4- spider,前者使用的是普通的scrapy类，后者从redis中读取url，获取的跟进url也是在redis中共其他人来继续跟进
"""

"""
    先实现scrapy版本的爬虫，然后添加redis更改为分布式爬虫即可
    
    spider中定义的start_url传递给调度器封装请求，请求发送给引擎，引擎把请求交给下载器去下载把相应通过引擎交给spider解析，
    如果解析中存在需要跟进的url则返回给调度器循环，不然的话交给items管道进行数据持久化操作
    
    分布式的区别就是：1- start_url交给redis去封装请求，把封装好的请求交给调度器，分担了调度器的职能
                2- spider中解析的数据或者响应中的跟进url不在返回给调度器去循环，而是交给redis进行数据持久化
                    还有url的封装去重操作，进行跟进url的循环请求
    
"""

"""
    master端负责request去重和人物的分配
    master一声令下让多个slave去爬取，哪个slave先拿到，那么就执行把跟进的url返回给master去去重，并且剩下的slave去拿这个跟进的url去执行
    
    具体更改的步骤：
    1- 拷贝适合redis分布式的settings中的配置
    2- 导入分布式爬虫类
    3- 修改累的集成
    4- 注销allowed_domains和start_url(url使用redis进行输入)
    5- 重写init方法(可选) 
    6- redis中添加redis_key

"""
print('aaa')


