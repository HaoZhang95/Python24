
def select_sort(alist):

    """
        选择排序：从无序队列中选择最小的放到前面去，有序部分和无序部分
        首先认为最小的元素就是第一个元素，不断比较更新这个min的数值
    """
    for j in range(0, len(alist)-1):

        min_index = j
        # 因为j要和剩余的部分作比较也就是从j+1到最后一个元素，n的索引为n-1，闭区间所以到n
        for i in range(j+1, len(alist)):
            if alist[min_index] > alist[i]:
                min_index = i

        alist[j], alist[min_index] = alist[min_index], alist[j]

    """
        j从0开始比较到倒数第二个元素，总共9个元素，最后让8和8+1比较，所以range：9-1=8,闭区间只能到7
        内层循环中让j和j+1比较，更新min_index和剩余无序部分的数值
        时间复杂度为O(n^2)
    """

    """
        排序中的稳定性，如果列表中两个元素相等，排序如果可能出现这两个相等元素的位置不固定的话，则为不稳定排序
        [1, 3, 2, 2]
    """


