"""
    状态保持
    一般浏览器请求服务器是无状态的，请求一次后不会在认识客户端之前做过什么，每一次都是新的请求
    无状态的原因是：底层的实现是socket，一次客户端请求后socket及时关闭，服务器端对应的socket对象也会被及时销毁

    实现状态保持主要有两种方式：
    在客户端储存信息的方式叫做cookie(再次访问会带着客户端的cookie来让服务器匹配识别)，而在服务器端储存信息的方式叫做session
    关于Session的使用会在Redis数据库中介绍，因为Session信息是储存在redis数据库中

    cookie的应用：登陆和非登陆状态下的购物车的商品，网站根据浏览信息进行的广告推荐，还有记录登陆信息，比如未来3天免登陆之后cookie会过期
"""


"""
    为什么有了cookie还会有session，肯定是cookie有弊端:只能存储明文信息，不安全
    session可以存储暗文，可以存储多种地方：缓存(服务器内存中,读取快速)，数据库，缓存和数据库
    session默认存储在数据库中的django_session默认数据库中的，该表结构是session_key, session_data, expire_date(默认存储两个星期)
    但是也可以自定义位置SESSION_ENGINE = 'django.contrib.sessions.backends.cache (db or cache_db 三种方式)'
    
    在使用Session后，会在Cookie中存储一个sessionid的数据，
    每次请求时浏览器都会将这个数据发给服务器，服务器在接收到sessionid后，会根据这个值找出这个请求者的Session
    类似于你的信息存储在俱乐部的电脑中，你需要拿着你的卡号去健身(session的机制：依赖于cookie)
"""