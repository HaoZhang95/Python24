"""
    使用**多进程**完成文件夹的copy案例
    主进程统计完成的进度，使用进程间的通信queue，子进程完成后放入queue中，主进程去拿
"""
import os
import multiprocessing
import time

def copy_file(src, file_name, dest, queue):
    # 打开一个源文件， 读取文件
    src_file = open(src + "/" + file_name, "rb")
    # 打开一个目标文件，写入文件
    dest_file = open(dest + "/" + file_name, "wb")

    file_data = src_file.read()
    dest_file.write(file_data)

    # 关闭文件资源
    src_file.close()
    dest_file.close()

    # 通过队列告诉主进程，该子进程已经完成这个文件的copy
    queue.put(file_name)

def main():
    # 用户输入需要copy的文件名
    src = input("请输入你要copy的目录名：")
    # 创建一个目的地文件夹名
    dest = src + "_备份"
    os.mkdir(dest)

    # 创建一个queue，用来统计进度条
    queue = multiprocessing.Queue()

    # 获取原目录下的文件列表, 遍历获取各个文件名字
    for file_name in os.listdir(src):
        print(file_name)
        # 未每一个文件创建一个单独的进程为其负责copy
        proc = multiprocessing.Process(target=copy_file, args=(src, file_name, dest, queue))
        proc.start()

    # 使用死循环不停的从queue中读取
    count = 0
    while True:
        queue.get()
        count += 1

        # 转义2个百分号代表一个, \r的作用是每次用这一行输出，配合end=""，效果表现为每一次同一行进行文字的更新
        print("\r当前进度是 %f%%" % (count / len(os.listdir(src))),end="")
        time.sleep(0.6)

        if count == len(os.listdir(src)):
            print("\n已完成拷贝100%")
            break

if __name__ == '__main__':
    main()