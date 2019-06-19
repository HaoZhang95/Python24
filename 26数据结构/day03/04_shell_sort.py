
def shell_sort(alist):

    """
        希尔排序：是插入排序的增改版
        通过GAP增量来分组进行插入排序，排序好的小组进行到一起进行下一次排序
        下一次排序的时候GAP=2进行再次插入排序，GAP=1的时候就是纯粹的插入排序
    """
    n = len(alist)
    gap = n // 2    # 取整数

    # gap变化到0之前，插入算法执行的次数
    while gap >= 1:

        for j in range(gap, n):
            """
                通过一个for循环把几个分组都遍历到，从gap开始，类似于列表中间的一条竖线，gap,gap+1,gap+2...gap+n-1
                通过for j 中间后面的元素结合i-gap来插入排序中间线前面的元素
                时间复杂度O(n^2)，为不稳定排序，另一个分组的相同元素可能排到前面去
            """
            i = j

            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i], alist[i-gap] = alist[i-gap], alist[i]
                    i -= gap
                else:
                    break
        # 缩短gap接着计算
        gap //= 2

    # n = 9
    # i1 = n / 2
    # i2 = n // 2
    # print(i1)   # 浮点数触发 4.5
    # print(i2)   # 整数除法 4
