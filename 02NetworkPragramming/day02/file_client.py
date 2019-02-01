"""
    文件下载的客户端,文件的上传下载都是采用tcp的形式

"""
import socket
import os

# 创建一个套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 链接服务器
ip_address = input("请输入服务器的ip地址:")
port_num = int(input("请输入服务器的端口号:"))
tcp_socket.connect((ip_address, port_num))

# 发送文件下载请求 --- 文件名
file_name = input("请选择一个下载的文件名:")
tcp_socket.send(file_name.encode(encoding="utf-8"))

# 通过链接，接受文件数据，写到本地wb的方式写进，省去转码
file = open("new_" + file_name, "wb")
had_written_len = 0

while True:
    data = tcp_socket.recv(4096)
    if data:
        file.write(data)
        had_written_len += len(data)
    else:
        # 关闭文件和链接

        file.close()
        if had_written_len > 0:
            print("文件传输完成")
        else:
            # 删除空文件
            print("服务器没有这个文件")
            os.remove("new_" + file_name)
        tcp_socket.close()
        break

