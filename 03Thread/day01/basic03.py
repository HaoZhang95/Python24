"""
    创建线程的第二个方式：自定义的thread
    多个子线程的执行顺序是乱序的，不是固定的

    1- 一个任务创建出来：就绪状态
    2- cpu分配时间段： 运行状态
    3- 运行的代码中调用recv，join等方法时： 从运行状态 -> 阻塞状态
    4- recv，join等执行完成满足要求后就会变成就绪状态， 一个轮回三角关系
"""
import threading
import time


class MyThread(threading.Thread):

    def run(self):
        for i in range(3):
            print("这是在子线程中执行的...")
            time.sleep(1)


if __name__ == '__main__':
    thd = MyThread()
    thd.start()

    # while True:
    #     time.sleep(1)
    #     print("这是在主线程中执行的")
