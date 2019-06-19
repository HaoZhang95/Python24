
def bubble_sort(alist):

    n = len(alist)
    for j in range(0, n-1):
        # j表示需要n-1次冒泡过程， i表示一次冒泡过程中的交换

        count = 0
        for i in range(0, n-j-1):
            # 只需要到列表的n-1位置，因为从0开始正好range结尾是闭区间，所以只需要-1
            # 比如总共9个元素，需要遍历到第八个位置，让其跟8+1去比较，第八个元素的索引是7，所以range(0, 8)
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        """
            每次冒泡的过程count都为0来记录这次冒泡过程中是否有交换发生
            如果只要有一次冒泡过程中没有交换发生直接结束循环，表示前面的都是有序的
            [1,2,3,9,8]第三次循环的时候发现count没变，直接return
        """
        if 0 == count:
            """
                break, continue, return的区别主要表现在终止循环的层数上面
                break终止的是当前循环层，因为这里正好处于最外层的for j循环中，所以下面的return可以被break替换
                return终止所有循环层，表示此函数终止
                continue跳过本次循环
            """
            return

