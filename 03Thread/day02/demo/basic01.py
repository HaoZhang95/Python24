"""
    死锁：没有成功释放锁，解决：
    1- 用户规范，用完一定要关闭
    2- 获取锁的时候，使用非阻塞的方式acquire(False)获取锁 或者 阻塞 + 超时acquire(True,1)的方式获取锁

    acquire()锁门时候的参数,默认是死等
    lock.acquire(True,1) blocking = true表示锁是阻塞等待，false为非阻塞等待
    第二个参数表示等待的时间， acquire返回值为true表示成功获取了锁
"""

"""
    程序：xxx.py就是一个程序，是一个静态的，占用的是硬盘空间
    进程：程序运行起来，代码+用到的资源叫做进程，占用的是内存，cpu的空间
    
    1- 就绪状态，万事俱备，只差cpu
    2- 执行状态： cpu分配时间段cpu，时间段用完就返回到就绪状态
    3- 等待状态： 如果存在阻塞recvfrom, recv, sleep等进入阻塞状态，满足条件后进入就绪状态
"""

"""
    定义一个子进程使用multiprocessing模块，方法使用和threading模块差不多
    1- 在命令行中运行这个py文件的话，在任务管理器就能查看到来给多个进程在运行了
    2- PID：任务管理器中的进程id， 使用os。getpid获取运行该方法的进程id
    3- PPID：使用os.ppid获取当前进程的*父进程*的id
"""
import time
import multiprocessing
import os


def proc_func(num, age):

    print("这是命名参数 age = %s" % age)
    print("这是子进程 %d, pid = %d，父进程ppid = %d" % (num, os.getpid(), os.getppid()))
    for i in range(3):
        print("这是子进程")
        time.sleep(1)

def main():

    # 创建一个进程,kwargs={"age": 18} 命名参数
    proc = multiprocessing.Process(
        target=proc_func, args=(100, ), name="我的进程X1",
        kwargs={"age": 18})

    # 启动这个进程
    proc.start()

    # 判断进程是否活着
    print(proc.is_alive())

    # 获取进程的名字
    print("进程的name = %s pid = %d" % (proc.name, proc.pid))

    # 和thread一样，这个进程结束后再执行下面的代码
    # join(1) 有参数表示阻塞等待超时1秒，只等待1s就不再阻塞
    proc.join()
    print(proc.is_alive())

    # terminate()立即强制进程推出
    proc.terminate()

    # while True:
    #     print("这是主进程 pid = %d" % os.getpid())
    #     time.sleep(1)

if __name__ == '__main__':
    main()