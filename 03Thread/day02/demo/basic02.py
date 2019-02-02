"""
    多个进程之间的全局变量的共享问题
    1- 多进程的执行顺序和线程一样是乱序的
    2- 每个进程互相独立，各有自己的一份全局变量，所以worker1中修改全局变量，worker2不受影响
    3- 进程之间变量独立不共享，这一点和thread完全不同
"""

import multiprocessing,time

g_num = 0

def worker1(num):

    global g_num
    print(g_num)
    # 这里修改全局变量
    g_num += 99
    while True:
        time.sleep(1)
        print("worker1获取到的g_num=%d" % g_num)

def worker2(num):

    while True:
        print("worker2获取到的g_num=%d" % g_num)
        time.sleep(1)

def main():
    pro1 = multiprocessing.Process(target=worker1, args=(0, ))
    pro1.start()

    pro2 = multiprocessing.Process(target=worker2, args=(1, ))
    pro2.start()

# if __name__ == '__main__':
#     main()

"""
    进程间如果想要共享全局变量的话使用中间商queue，每个进程都访问这个queue
    1- queue队列，先进先出， stack栈的话，先进后出
    2- 队列的存取原理是：放一个取一个， 取出队列就没有了
    3- 如果队列没有东西进行get，或者put放的超过长度，都会阻塞，一个萝卜一个坑
"""
from multiprocessing import queues

def testQueue():

    # 创建一个3个长度的队列
    queue = multiprocessing.Queue(3)

    # put放入数据
    # queue.put(1)

    # get读取数据
    queue.get()

testQueue()