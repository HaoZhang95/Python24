"""
    主进程从队列中放入键盘输入的数据，紫禁城取出队列中的数据打印出来
"""

import multiprocessing

def proc_fun(queue):
    while True:
        data = queue.get()
        print("\n从队列中取出的数据是: %s" % data)

def main():
    queue = multiprocessing.Queue(3)

    # 进程的参数是一个queue队列
    proc = multiprocessing.Process(target=proc_fun, args=(queue,))

    proc.start()

    # 获取queue的大小,是否为空，是否已满
    print("队列的size= %d, 是否为空：%s, 是否满着：%s" % (queue.qsize(), queue.empty(), queue.full()))

    while True:
        data = input("请输入：")
        queue.put(data)

if __name__ == '__main__':
    main()