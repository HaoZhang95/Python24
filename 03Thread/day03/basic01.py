"""
    queue(data, blocking=True, timeout=-1)默认为阻塞和永久不超时
    1- 如果超出长度，或者超时等待之后都没有获取到数据，则会**抛出异常**
    2- put(data, False)不等待，不阻塞，直接判断能不能放入，不能直接报错 == put_nowait(data)
    3- get(block=true, timeout=-1),默认就是一直等待get阻塞
    4- get(true, 3)阻塞3秒取不到直接异常， get(False) == get_nowait()
"""

"""
    进程池， 1- 可以重复使用池中的进程 2- 效率高，池中的进程都是已经准备好的进程
    1- 有请求提交到pool时候，如果池中没满，就会新建一个进程去服务，满了话，就让该请求等待，直到池中有资源释放才会去服务该请求    
    2- 池中apply方式添加的方式是阻塞式的,该任务执行完成，才会执行apply之后的代码
    3- apply_async非阻塞的添加任务，不会等待任务结束，可以直接执行之后的代码
    4- 进程池中只要主进程已退出，所以正在执行的任务全部终止
    5- 池join的阻塞等待，只能在pool。close之后才能执行
    6- 进程池的close的含义是：不在接收新的任务请求
    7- 进程之前的通信，使用的是multiprocessing.Queue(),而进程池中的通信使用的是multiprocessing.Manager().Queue()
"""
import multiprocessing, time, os, random

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为%d" % (msg, os.getpid()))
    # 随机生成0-1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg,  "执行完毕，耗时%0.2f" % (t_stop - t_start))

def processPool(max_size):

    # 创建一个进程池
    pool = multiprocessing.Pool()

    # apply——async添加任务请求
    pool.apply_async(func=worker, args=("111",))
    print("111任务执行完成")

    # apply添加任务请求
    pool.apply(func=worker, args=("222",))
    print("222任务执行完成")

    # apply——async添加任务请求
    # 如果该方法的下面没有代码，表示main进程已经结束，那么可能这个async的请求会终止
    pool.apply_async(func=worker, args=("333",))
    print("333任务执行完成")

    # 关闭进程池,正常关闭，不再允许添加新的任务
    pool.close()

    # 立即终止进程池，暴力终止
    # pool.terminate()

    # 等待所有任务执行完成
    pool.join()
    print("所以任务执行完毕")

def main():
    processPool(3)


if __name__ == '__main__':
    main()


