"""
    非阻塞客户端
    非阻塞模式的socket设置， 默认的socket都是阻塞的模式
"""
import socket,time


def testNoBlockingClient():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_socket.connect(("127.0.0.1", 8888))

    # 在connect连接之后，如果没有数据，就不会等待，直接抛出异常
    tcp_socket.setblocking(False)

    while True:

        try:
            # 先接收服务器信息，自己再发送, 默认的就是阻塞在这里了
            recv_data = tcp_socket.recv(4096)
        except Exception as e:
            print("no data")
            time.sleep(1)
        else:
            print(recv_data)

"""
    非阻塞服务器，能实现多线程的功能，但是非阻塞实用性不强
    1- server_socket.setblocking(False) 解决服务器的accept阻塞
    2- client_socket.setblocking(False) 解决服务器接收链接的recv阻塞
"""
def testNoBlockingServer():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 一般socket是服务器的话，都需要加入这行解决客户端重启后的地址重用问题
    # SOL_SOCKET: 基本套接口
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

    server_socket.bind(("", 8888))

    server_socket.listen(128)

    # 服务器在listen之后，如果accept没有数据，就不会等待，直接抛出异常
    server_socket.setblocking(False)

    client_socket_list = []
    while True:

        try:
            # 先接收服务器信息，自己再发送, 默认的就是阻塞在这里了
            client_socket, client_addr = server_socket.accept()
        except Exception as e:
            print("没有客户端连接，1秒后重新查看")

            """
                时间间隔小，下面for循环次数增多，CPU 空转，资源浪费
                时间间隔大，用户体验不好
            """
            time.sleep(1)
        else:
            print("接收来自客户端%s的链接请求" %str(client_addr))

            # 将客户端的socket设置为非阻塞的，用于解决recv
            client_socket.setblocking(False)
            client_socket_list.append(client_socket)
        finally:
            for client_socket, client_addr in client_socket_list:
                try:
                    # 先接收服务器信息，自己再发送, 默认的就是阻塞在这里了
                    recv_data = client_socket.recv(4096)
                except Exception as e:
                    print("当前客户端%s没有数据" % str(client_addr))
                else:
                    if recv_data:
                        print("接受来自客户端%s的数据%s" % (str(client_addr), recv_data.decode()))
                    else:
                        print("客户端%s断开连接" & client_addr)
                        client_socket_list.remove(client_socket)

def main():
    testNoBlockingServer()
    # testNoBlockingClient()


if __name__ == '__main__':
    main()
