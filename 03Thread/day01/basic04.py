"""
    多线程下的全局变量共享问题
    1- 互斥锁：就是为变量引入一个状态：锁定和非锁定状态，类似于上厕所的锁门
    2- 多个线程互相互斥，只有厕所门开锁之后才能让下一个进去，多个线程**协同配合**
    3- 互斥锁：保证每次只有一个线程读写变量
"""
import threading, time

global_num = 0

# 创建一把全局互斥锁
global_lock = threading.Lock()

def worker1():

    global global_num
    for i in range(100000):

        # 修改资源前，尝试获取并加锁，如果没有被锁定，就可以被我锁定
        # 如果进入厕所之前，已经锁门，就会阻塞等待，直到成功获取并锁定
        global_lock.acquire()
        global_num += 1
        # 用完资源，释放锁,锁定状态 -> 未锁定状态
        global_lock.release()

def worker2():

    global global_num
    for i in range(100000):
        global_lock.acquire()
        global_num += 1
        global_lock.release()


def worker3(lock):

    global global_num
    for i in range(100000):
        lock.acquire()
        global_num += 1
        lock.release()


def worker4(lock):

    global global_num
    for i in range(100000):
        lock.acquire()
        global_num += 1
        lock.release()

if __name__ == '__main__':
    thd1 = threading.Thread(target=worker1)
    thd1.start()

    thd2 = threading.Thread(target=worker2)
    thd2.start()

    """
        非线程安全：数据在多线程情况下没有按照一定的顺序进行数据的读写
        1- 取消下面的两个join，global_num就会随机的打印一个数字
        2- 但是即使加上join的话，global_num也是随机的而不是10万+10万=20万
        3- 原因是thread中进行global_num += 1的时候，分成三步，取值，计算，赋值
        4- 假如：两个线程区的时候都是100，都开始计算100+1，最后赋值的时候成了双份的101，存在数据计算的丢失，所以产生的也是随机小于20万的数字
        5- 简单说，即使join，但是一份变量同时被多个线程读写
    """
    thd1.join()
    thd2.join()

    print("最终的num = %d" % global_num)

    """
        以参数的形式传入一把锁，使用args参数接收一个元祖，如果只有一个参数，注意加上逗号
    """
    lock = threading.Lock()
    thd3 = threading.Thread(target=worker3, args=(lock,))
    thd3.start()

    thd4 = threading.Thread(target=worker4, args=(lock,))
    thd4.start()

    thd3.join()
    thd4.join()

    print("最终的num = %d" % global_num)


"""
    死锁：类似于一个人上完厕所直接爬出来，但是不释放锁，其他线程只能等待，主线程进行阻塞
"""