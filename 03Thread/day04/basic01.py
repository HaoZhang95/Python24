"""
    协程：另外一种实现多任务的方式，占用更少的资源，也叫做微线程
    协程的特点就是**切换**着执行，使用yield关键字实现的
    1- yield的生成器函数就是一种简单的协程
    2- 协程是用户层面可以控制的，而进程是cpu控制的
"""
import time

def work1():

    while True:
        print("-----work1------")

        # 生成器被进行next的时候，yield返回一个空，在这里卡住，等待下一次next才继续执行
        yield
        time.sleep(0.5)


def work2():

    while True:
        print("-----work2------")
        yield
        time.sleep(0.5)

def test():
    w1 = work1()
    w2 = work2()

    # 死循环中next(w1)调用的时候，卡在yield屈服让步，然后程序执行next(w2)
    # next(w2)执行的时候，也会卡在yield屈服让步给next(w1)执行
    # 就这样，在死循环中来回yield关键字切换执行时间片段
    while True:
        next(w1)
        next(w2)


"""
    使用第三方的greenlet来实现协程
    1- 协程保存当前的执行环境比如变量等，在切换之前
    2- 恢复之前的执行环境，接着上次的继续执行

"""
from greenlet import greenlet

def work3():

    while True:
        print("-----work3------")
        g2.switch()
        time.sleep(0.5)

def work4():

    while True:
        print("-----work4------")

        # 手动切换到g1执行，底层封装了yield
        g1.switch()
        time.sleep(0.5)

g1 = None
g2 = None

def testGreenLet():
    # 创建两个协程对象

    g1 = greenlet(work3)
    g2 = greenlet(work4)

    # 切换到协程执行,就开始执行work3，因为work3函数中调用了g2.switch()实现来回切换
    g1.switch()

"""
    gevent是底层封装了greenlet的协程第三方模块，安装前必须安装greenlet，是其的增强版
    1- gevent自动切换的自动挡 2- greenlet需要手动切换的手动挡
    2- 使用gevent不会自动切换协程
    3- 导入gevent的monkey去破解使协程自动切换
    4- patch就是破解的意思，recv, recvfrom, sleep等函数(默认阻塞)变成不再阻塞
    5- joinall不能少，让其阻塞等待，不然main就执行完毕，就退出了
"""
from gevent import monkey
monkey.patch_all()

import gevent

def work5(num):

    for i in range(num):
        print("in work %s" % gevent.getcurrent())
        time.sleep(0.3)


def testGevent():

    # 创建一个协程对象，创建的时候就自动运行了，不需要手动启动
    g1 = gevent.spawn(work5, 10)
    g2 = gevent.spawn(work5, 10)
    g3 = gevent.spawn(work5, 10)

    # 阻塞等待协程执行完毕
    # 没使用monkey.patch_all()破解的时候不会自动切换，破解后就会随机协程
    # g1.join()
    # g2.join()
    # g3.join()

    # 程序从上到下执行，不管之前有没有异步代码，遇到join相当于一面墙，堵住下面的路
    gevent.joinall([g1,g2,g3])

    print("全部协程结束完毕.")

def main():
    # test()
    # testGreenLet()
    testGevent()


if __name__ == '__main__':
    main()