"""
    io多路复用，好处在于单个process进程可以同时处理**多个网络连接**的io操作
    单进程，单线程，一般只能实现一个io发收操作，多路io复用在windows使用的是IOCP，在Linux上使用的就是epoll
    1- basic02.py我们使用的是for循环遍历服务器的client_socket列表去一一查看recv有没有数据，**不知道哪个socket收到信息**效率差，体验不好
    2- 在epoll模型中，每个socket都是由操作系统来监控，recv到信息，操作系统就会通知**用户进程**，不需要**一一查看**

"""