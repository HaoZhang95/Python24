
def quick_sort(alist):

    """
        快速排序不像之前的那样把序列分成两部分
        而是第一个元素通过一个low一个high游标相夹， low的左边都比第一个元素小，high的右边都比第一个元素大
        以此来确定第一个元素在序列中的位置
    """
    n = len(alist)
    low = 0
    high = n-1
    mid_value = alist[0]

    while low < high:
        """如果low和high在向中间走的过程中没有"""
        if alist[high] > mid_value:
            high -= 1

        alist[low] = alist[high]
