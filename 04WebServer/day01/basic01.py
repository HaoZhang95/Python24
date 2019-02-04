"""
    Web服务器基础, 模拟服务器使用socket去监听网页请求

"""
import socket

def testRequest():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("", 8080))

    server_socket.listen(128)

    while True:

        client_socket, client_addr = server_socket.accept()

        print("接收来自%s的连接请求" % str(client_addr))

        recv_data = client_socket.recv(4096)

        if not recv_data:
            print("对方已经断开连接")
        else:
            print(recv_data)

        client_socket.close()

"""
    重定向的状态码是30X开头的， 200是(正常) 503(服务器错误)，请求http:形式的百度，会被重定向到https的百度
"""

def main():
    testRequest()

if __name__ == '__main__':
    main()



