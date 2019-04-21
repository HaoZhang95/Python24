"""
    服务器端包含服务器程序+框架
    服务器程序比如flask中的GunXX和django使用的uwsgi这两个斗志服务器程序，用来通过WSGI协议链接不同的Web框架
    框架就是符合WSGI协议的web代码，通过服务器程序来对外提供高性能的web服务
    默认的flask和django中的app.run只是简单的服务器程序，性能只是用来开发测试，线上的产品则需要专业的服务器软件来支持
"""


"""
    序列化是指将计算机中的数据结构转换为可用于传输的格式:xml,json等，django响应的时候，从数据库读取数据模型对象，然后
        通过一个空列表append添加多个字典对象进去，然后jsonresponse将这个列表序列化成json格式的字符串
        
    反序列化就是用户请求的参数为json，进行request.body.decode()成json_str然后进行json.loads()把json转换为字典对象的过程
    
    序列化：  模型对象 --> python字典，用于输出发，返回给前端使用的
    反序列化: 前段数据 --> 经过验证 --> python字典，用于输入
    序列化器：帮助进行序列化和反序列化
    
    django rest framework（DRF）主要帮我们做了：就是序列化和反序列化，具体的就是不需要手动的append一个个字段
        使用这个rest framework框架的serialize方法就可以把ORM对象转化为一个json，省去自己创建空列表，一个个append添加字典的字段
"""

"""
    Serializer(instance=None, data=empty, **kwarg)
    用于序列化时，将模**型类对象**传入instance参数
    用于反序列化时，将要被反序列化的数据传入data参数
    除了instance和data参数外，在构造Serializer对象时，还可通过context参数额外添加数据
    
"""

