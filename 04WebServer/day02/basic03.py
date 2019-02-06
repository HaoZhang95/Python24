"""
    io多路复用，好处在于单个process进程可以同时处理**多个网络连接**的io操作
    单进程，单线程，一般只能实现一个io发收操作，多路io复用在windows使用的是IOCP，在Linux上使用的就是epoll
    1- basic02.py我们使用的是for循环遍历服务器的client_socket列表去一一查看recv有没有数据，**不知道哪个socket收到信息**效率差，体验不好
    2- 在epoll模型中，每个socket都是由操作系统来监控，recv到信息，操作系统就会通知**用户进程**，不需要**一一查看**
    3- epoll的两种通知进程的模式
        LT模式：当epoll检测到描述的时间发生并将事件通知该进程，该应用程序可以**不立即处理**
                只要有数据就一直通知，直到没有数据
        ET模式：当epoll检测到描述的时间发生并将事件通知该进程，该应用程序**必须立即处理**
                只在有数据的一瞬进通知一次
    4- epoll只能认识文件描述符，EPOLLIN代表监听可读时间，EPOLLOUT可写事件
    5- 默认不设置就是LT模式
"""

"""
    因为epoll只能发在unix/linux下使用，所以windows下会出现module 'select' has no attribute 'epoll'，所以本代码不能被测试
    UNIX,LINUX中"一切皆文件"，文件描述符就是对**进程内部(才会有效)**所拥有文件资源的一种描述的符号
    1- 是一个无符号整数（0，1，2，3.。。）0(input)，1(output)，2(标准错误)默认被系统占有，通过sock.fileno()获取文件描述符
    2- 一个进程默认打开0,1,2三个文件，自己的socket就是为3的文件描述符
"""

"""
    epoll模式的服务器, epoll需要导入select模块
"""
import socket
import select

def testEpollServer():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.setblocking(False)

    server_socket.bind(("", 8888))

    server_socket.listen(128)

    # 创建epoll对象
    epoll = select.epoll()

    # 将服务器的socket添加到epoll的监听列表， fd = file descriptor文件描述符,
    # ET模式： select.EPOLLIN | select.EPOLLET
    epoll.register(server_socket.fileno(), select.EPOLLIN)

    # 保存客户端的socket字典, {fd: socket}
    client_socket_list = {}
    client_address_list = {}

    while True:

        # 死循环中向epoll对象获取监听结果
        epoll_list = epoll.poll()

        # 遍历列表，获取fd和是件
        for fd, events in epoll_list:

            # 服务器socket     accept()
            if fd == server_socket.fileno():
                new_client_socket, new_client_address = server_socket.accept()
                print("收到了来自%s的链接请求" % (str(new_client_address)))

                # 设置客户端socket非阻塞
                new_client_socket.setblocking(False)

                # 添加到epoll监听列表
                epoll.register(new_client_socket.fileno(), epoll.EPOLLIN)

                # 添加到集合
                client_socket_list[new_client_socket.fileno()] = new_client_socket
                client_address_list[new_client_socket.fileno()] = new_client_address

            # 客户端的socket    recv()
            elif events == select.EPOLLIN:
                recv_data = client_socket_list[fd].recv(4096)

                if recv_data:
                    print("收到了来自%s的数据：%s" % (str(client_address_list[fd]), recv_data.decode()))
                else:
                    print("收到了来自%s的断开请求" % (str(client_address_list[fd])))

                    # 从监听列表中移除
                    epoll.unregister(fd)

                    # 从字典中移除
                    del client_socket_list[fd]
                    del client_address_list[fd]

def main():
    testEpollServer()


if __name__ == '__main__':
    main()