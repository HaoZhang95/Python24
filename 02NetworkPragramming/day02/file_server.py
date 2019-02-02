"""
    文件下载的服务器端
    Python中如果函数中没有return的话，默认的是返回return None
"""
import socket, os


def read_file_data(file_name):
    """获取指定的文件数据"""
    try:
        file = open(file_name, "rb")
    except Exception as e:
        print("文件不存在.")
        return None
    else:
        # 如果文件过大，会有隐患
        file_data = file.read()
        file.close()
        return file_data


# 创建一个服务器socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置socket断开连接的选项,close的时候会立即释放，答应断开分手，1表示确定，0为取消
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定端口
server_socket.bind("", 8888)

# 将socket设置为监听模式（被动）
server_socket.listen(128)

while True:
    # 取出一个客户端用来服务
    client_socket, client_address = server_socket.accept()

    # 接收文件名，读取本地的文件数据
    file_name = client_socket.recv(4096)
    file_data = read_file_data(file_name)

    # 将本地读取的一系列文件名发送给客户端
    if file_data:
        client_socket.send(file_data)

    # 关掉用来服务的socket
    client_socket.close()

# 关掉服务器的socket
# server_socket.close()
