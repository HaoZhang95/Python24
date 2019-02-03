"""
    Tcp 面向连接(必须先建立连接)，可靠的数据传输方式，类似于打电话,可靠的3个原因
    1- TCP采用的发送应答机制  2- 超时重传 3- 错误校验

    1- tcp使用的是send & recv
    2- udp使用的是sendto & recvfrom
    3- 涉及到网络发送接收都是byte的类型需要解码的类型
    4- 设计的网络地址都是元组类型
    5- tcp的close方法作用有两个1- 断开链接(因为tcp有链接) 2- 释放资源
"""
import socket

# 创建一个tcp的socket使用的是sock_stream， udp使用的类型是数据棒sock_dgram
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立目的地链接
tcp_socket.connect(("192.168.115.128", 8888))

# 发送数据
data = input("请输入要跟服务器说的话: ")
tcp_socket.send(data.encode(encoding="utf-8"))

# 接收数据,因为tcp已经建立了链接，所以知道目的地地址，recv返回的直接就是data
recv_data = tcp_socket.recv(1024)
print("收到的数据：%s" % (recv_data.decode(encoding="utf-8")))

# 挂机关闭
tcp_socket.close()



"""
    TCP 服务器端的实现
    recv的作用：
    1- 如果链接正常，返回的就是data
    2- 如果突然断开连接，返回的是一个0字节长度的str,byte类型 --> b'' **就不会阻塞了**
"""

# 创建一个总机，用来接收不同客户端的请求转发到分机
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 使用固定号码
tcp_server.bind('', 8888)

# 安装服务系统，设置等待服务区大小,能够连接的最大客户端数量
tcp_server.listen(128)

# 从等待服务区，取出一个客户,用来转到分机，处理客户端的服务
# 返回值: 一个元组(和客户端关联的socket，客户端地址)
client_socket, client_address = tcp_server.accept()
print("收到来自: %s 的链接请求." % client_address)

while True:
    # 服务,完成后，挂掉分机的socket
    # 判断recv返回的是不是0字节的str
    data = client_socket.recv(1024)
    if data:
        print("收到的数据: %s." % data.decode("utf-8"))
        client_socket.send(data)
    else:
        client_socket.close()
        break

# 挂掉总机的socket
# tcp_server.close()