"""
    UDP Socket 服务端编程
    1- echo回声服务器， 你给我发什么，我给你回什么
    2- UDP的特点： a:不保证不丢包 b:接收的data可能乱序
"""
import socket

# 创建服务器socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定接口
udp_server.bind(("", 8888))

while True:
    # 使用socket接收请求的数据
    recv_data, recv_address = udp_server.recvfrom(1024)

    # 回传数据
    udp_server.sendto(recv_data, recv_address)

# 服务器关闭socket并不重要
# udp_server.close()