"""
    queue(data, blocking=True, timeout=-1)默认为阻塞和永久不超时
    1- 如果超出长度，或者超时等待之后都没有获取到数据，则会**抛出异常**
    2- put(data, False)不等待，不阻塞，直接判断能不能放入，不能直接报错 == put_nowait(data)
    3- get(block=true, timeout=-1),默认就是一直等待get阻塞
    4- get(true, 3)阻塞3秒取不到直接异常， get(False) == get_nowait()
"""
import multiprocessing

queue = multiprocessing.Queue(3)



