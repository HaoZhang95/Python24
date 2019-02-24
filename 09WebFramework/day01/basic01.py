"""
    web服务器返回灵活页面,根据制定的路径打开指定的页面
"""
import socket, threading, multiprocessing,gevent
import re
import time

# dynamic包中存放的是框架之类的东西，注意更新import的路径
import dynamic.mini_framework

from gevent import monkey
monkey.patch_all()


class WSGIServer(object):

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # socket优化，一个服务器的端口释放后会等待两分钟之后才能再被使用，SO_REUSEADDR是让端口释放后立即就可以被再次使用。
        # 参数1：设置socket所在的层级，SOL_SOCKET: 基本套接口
        # 参数2：设置socket的设置选项，地址重用选项
        # 参数3：设置还是取消，1/0
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定
        self.server_socket.bind(('', 9999))

        # 监听，设置已完成三次握手队列的长度
        self.server_socket.listen(128)

    def request_handler(self, client_socket):
        """ 为每个客户进行服务"""

        # 接收每个客户的请求报文,通过recv_data判断客户端是不是已经断开连接
        recv_data = client_socket.recv(4096)

        if not recv_data:
            print("客户端已经断开连接.")
            client_socket.close()
            return

        # 对请求报文进行切割，获取请求行中的请求路径：a.html
        request_str_data = recv_data.decode()

        # data_list = request_str_data.split("\r\n")

        # 使用正则表达式获取url
        ret = re.match(r"[^/]+([^ ]+)", request_str_data)
        if ret:
            path_info = ret.group(1)    # /index.html
        else:
            path_info = "/"

        print(" 用户的请求路径为: %s" % path_info)

        if path_info == "/":
            path_info = "/a.html"

        # 通过if判断区分动态请求/静态请求
        # 加入py结尾的为动态请求
        if not path_info.endswith(".py"):
            try:
                # 更改为with的安全打开文件方式，上下文管理器
                # 请求index.py返回的是index.html的内容，但是html中需要加载的css等，css请求是走这里的
                # 所以需要在这里设置静态文件的路径http://127.0.0.1:9999/css/bootstrap.min.css
                with open("../static/" + path_info, "rb") as f:
                    file_data = f.read()
                    print(len(file_data))

            except Exception as e:
                # 给客户端回复响应报文,、\r\n == 键盘上的Enter
                response_line = "HTTP/1.1 404 Not Found\r\n"
                # 响应头
                response_header = "Server: PythonWebServer2.0\r\n"
                # 响应体
                response_body = "Error!!!!!!"
                # 拼接豹纹
                response_data = response_line + response_header + "\r\n" + response_body
                # 发送报文,不能以str的方式方式，需要进行encode
                client_socket.send(response_data.encode())
            else:
                # 给客户端回复响应报文,、\r\n == 键盘上的Enter
                # 响应头,设置content_type告诉浏览器以utf-8形式解析，否则乱码
                response_header = "HTTP/1.1 200 OK\r\n"
                response_header += "Server: PythonWebServer2.0\r\n"

                """
                    经过多个版本的迭代，下面这句话需要注释掉，这个版本主要进入这里是处理css，js等文件的请求
                    所以不能以text/html的形式，否则会浏览器不能正常的加载css，js。
                    如果返回的是纯html文件，则可以告诉浏览器content——type为text/html
                """
                # response_header += "Content-Type: text/html; charset=UTF-8\r\n"
                response_header += "\r\n"
                # 响应体
                response_body = file_data
                # 拼接报文，response_body为二进制，所以header需要将字符串类型进行encode为二进制
                response_data = response_header.encode("utf-8") + response_body
                # 发送报文,不能以str的方式方式，**不再**需要进行encode
                client_socket.send(response_data)
            finally:
                # 关闭套接字
                client_socket.close()

        else:
            # 如果以.py结尾的请求
            # 给客户端回复响应报文,、\r\n == 键盘上的Enter
            # 响应头,设置content_type告诉浏览器以utf-8形式解析，否则乱码,要跟自己发送的响应体的编码格式相同
            # response_header = "HTTP/1.1 200 OK\r\n"
            # response_header += "Server: PythonWebServer2.0\r\n"
            # response_header += "Content-Type: text/html; charset=UTF-8\r\n"
            # response_header += "\r\n"

            env = dict()
            env["PATH_INFO"] = path_info

            # 响应体
            """
                使其符合WSGI协议，让框架去调用自己的set_header方法的传递
                env一个包含所有HTTP请求信息的dict对象：例如浏览器的版本，语言，请求path等
                env传递的字典是浏览器信息给服务器的，服务器的信息再把这些信息传递给框架
            """
            response_body = dynamic.mini_framework.application(env, self.set_headers)
            # 拼接报文，response_body此时为字符串，所以不需要encode，需要整体encode
            response = (self.response_header + response_body).encode("utf-8")
            # 发送报文,不能以str的方式方式，**不再**需要进行encode
            client_socket.send(response)

    # status --> "200 OK"
    # headers --> [("Content-Type", "text/html")]
    def set_headers(self, status, headers):

        response_header = "HTTP/1.1 %s\r\n" % status
        for temp in headers:
            response_header += "%s: %s\r\n" % (temp[0], temp[1])

        response_header += "\r\n"

        self.response_header = response_header

    def start(self):

        while True:

            # 队列中取出一个客户端套接字进行服务
            client_socket, client_addr = self.server_socket.accept()

            """
                线程处理每一个客户端的accept，线程你给的变量等是共享的
                所以传入的client_socket和主线程的client_socket是同一个东西，关一个即可
            """
            # thread = threading.Thread(target=request_handler, args=(client_socket,))
            # thread.start()

            """
                线程处理每一个客户端的accept
                在进程copy一份client_socket之后，关闭主进程的client_socket
                由于主进程和子进程互相独立，copy关系，两个都关闭网页左上角才不会一直转
            """
            # proc = multiprocessing.Process(target=self.request_handler, args=(client_socket,))
            # proc.start()
            # client_socket.close()

            """
                gevent协程的方式, join/joinAll就是保证主线程存活的作用，因为此处在while true死循环中，所以不需要join
            """
            gevent.spawn(self.request_handler, client_socket)


def test_web():

    wsgi_server = WSGIServer()
    wsgi_server.start()


def main():
    test_web()


if __name__ == '__main__':
    main()

