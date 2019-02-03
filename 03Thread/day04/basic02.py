"""
    多任务下载器，使用协程，本质就是使用**当前进程**在**不同**的函数代码内切换执行
    协程会在 urllib.request.urlopen(url_str)这行阻塞的代码中利用破解进行自动切换

    1- 进程切换需要的资源大，效率低
    2- 县城需要的资源一般，效率一般
    3- 协程切换需要的资源很少，效率高

    4- 进程：一条流水线
    5- 线程： 一条流水线中的不同工人  --> 单进程，多线程
    6- 一条流水线并不是线程越多越好: 多个流水线多个工人 --> 多进程，多线程
    7- 为再次提高效率，某条流水线的某个员工**临时没事，或者在等待的状态**，那么他就会去帮其他的人做事
        充分利用时间  --> 协程方式（微线程）
    总之： 协程就是尽可能的压榨硬件性能
"""

# 引入monkey进行阻塞破解
from gevent import monkey
monkey.patch_all()

import gevent

# 引入urllib，进行网页响应,下载网页的html代码
import urllib.request

# time用来及时
import time

def down_html(url_str):

    # 向远程服务器发起请求  -> 一个结果对象
    print("开始请求：%s" % url_str)
    response = urllib.request.urlopen(url_str)

    # io获取data
    data = response.read()
    print("获取网页数据成功 %s 共计 %d 字节" % (url_str, len(data)))


def main():

    start_time = time.time()

    # 不破解的话就会一个一个read网页，因为gevent默认是不会手动切换协程的
    g1 = gevent.spawn(down_html, "http://qq.com")
    g2 = gevent.spawn(down_html, "http://google.com")
    g3 = gevent.spawn(down_html, "http://twitter.com")

    gevent.joinall([g1, g2, g3])

    end_time = time.time()

    print("总共耗时: %s" % (end_time - start_time))

if __name__ == '__main__':
    main()