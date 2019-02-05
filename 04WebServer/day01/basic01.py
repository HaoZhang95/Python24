"""
    Web服务器基础, 模拟服务器使用socket去监听网页请求

"""
import socket

def testResponse():
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


def testRequest():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.connect(("103.235.46.39", 80))

    # 模拟浏览器发送http请求报文
    request_data = "GET / HTTP/1.1\r\nHost: www.baidu.com\r\n\r\n"
    tcp_socket.send(request_data.encode())

    # 接受http响应报文
    recv_data = tcp_socket.recv(4096)
    print(request_data)

    # 解码获取字符串，并且切割获取网页的响应体
    recv_str_data = recv_data.decode()
    index = recv_str_data.find("\r\n\r\n")
    print(recv_str_data[index+4: ])

    tcp_socket.close()

"""
    网页链接的tcp建立需要三次握手，四次挥手拜拜，中大型网站都是长连接
    响应头的connection：keep-alive长连接类似于公交卡，短链接类似于一次性的单程票
    1- 长连接：再次连接，不需要排队买票，节约时间
    2- 短链接：发起链接，建立连接，发送消息，server回应，链接关闭，实现简单，不需要保存socket，省内存，但是不能快速响应用户请求
    3- 一般客户端连接代理，代理连接数据库，代理不需要断开数据库，客户端不需要重复的断开数据库，客户端直接和代理进行连接/等待链接
    4- 一个百度首页，需要请求多次服务器获取多个资源，长连接不需要频繁建立，效率高
"""

def main():
    # testResponse()
    testRequest()

if __name__ == '__main__':
    main()



