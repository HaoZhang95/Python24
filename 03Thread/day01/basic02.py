"""
    一个程序运行起来就是一个进程，线程就是一个进城内部的执行流程
    1- threading.Thread()实力方法中的参数target=方法名，注意方法名没有小括号
    2- 有小括号的话，表现的并不是多线程执行，而是单线程的形式
    3- 进程等多有子线程都结束后才会结束
"""

import time
import threading


def saySorry():
    print("sorry")
    time.sleep(1)

"""
    等所有子线程完成后的方法执行join，子线程在主线程的阻塞等待
    哪个线程调用join，那么等待这个子线程结束后才会调用之后的代码
"""
from time import sleep

def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        sleep(1)

if __name__ == '__main__':
    for i in range(5):

        # 创建一个线程，执行的计划，方法名没有小括号
        # thd = threading.Thread(target=saySorry())
        thd = threading.Thread(target=saySorry)

        # 启动线程
        thd.start()

    # 差查看当前进程中存货的所有线程列表
    print(threading.enumerate())
    print(len(threading.enumerate()))


    # =============================
    thd1 = threading.Thread(target=sing)
    thd1.start()

    thd2 = threading.Thread(target=dance)
    thd2.start()

    """
        join在主线程中阻塞等待
        thd1子线程执行完成后才会执行thd2.join
        thd2执行后表示两个子线程都执行结束，才会打印太棒了
    """
    thd1.join()
    thd2.join()

    print("演出结束，太棒了")

