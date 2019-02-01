"""
    1- 网络就是用来**信息共享**和**数据传递**
    2- ip就是标识收件人和发件人的地址，跟发手快递类似
    3- ip = 网络号 + 主机号， 类似于身份证号130124XXXXXX
    4- 一个字节byte = 8 bit比特位， 比特位就是存放0/1的小格子
    5- ipv4 四个字节存放ip地址，32个格子， 共2^32次方
    6- ipv6 是ip的第六个版本，但是使用的是**8个字节**
    7- ping www.baidu.com 查看网络通不通，和查看百度的ip地址
    8- DNS域名解析系统 域名 <=> ip数字地址
    9- 一个程序运行起来就是一个进程，打开任务管理器查看各个进程
"""

"""
    1- encode编码成字节或者二进制类型, 默认参数就是encoding="utf-8"
    2- decode解码为原始数据
"""
a_str = "我是Python"
b_str = a_str.encode(encoding="utf-8")
print("数据类型：%s, 数值为：%s" % (type(b_str), b_str))

c_str = b_str.decode(encoding="utf-8")
print("数据类型：%s, 数值为：%s" % (type(c_str), c_str))

"""
    UDP Socket客户端编程
    1- socket发送的端口想要固定下来的话使用bind关键字
    2- 如果数据过大，recvfrom接收一部分，再次调用recvfrom才会返回剩余的data
    3- udp是广播接收，所以bind的是ip写的是空，而不是具体的ip地址
    4- 好友上线通知，一个好友上线就会往广播数据到所有的ip地址的某个端口
    5- 先进行bind绑定socket再进行sendto和recvfrom，不能乱序
"""
import socket

# 创建UDP的socket(ip协议类型ipv4 or ipv6， socket的类型) --> socket对象
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 将端口绑定到这个socket上, ip写""表示绑定本地所有的ip的数据
udp_socket.bind(('', 8888))

# 使用socket进行数据的发送
data = input("请输入你想要对服务器说的话：")
ip_address = "192.168.115.81"
port_num = 8080
udp_socket.sendto(data.encode(encoding="utf-8"), (ip_address, port_num))

# 进行数据的接收recvfrom --> 接收的data是一个元组类型（byte类型的data, (ip_address, port_num)）
recv_data, remote_address = udp_socket.recvfrom(1024)
recv_data = recv_data.decode("utf-8")
print("收到来自: %s 的数据：%s" % (str(remote_address),recv_data))

# 关闭socket
udp_socket.close()

