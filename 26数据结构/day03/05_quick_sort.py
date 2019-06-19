
def quick_sort(alist, first, last):

    """
        快速排序不像之前的那样把序列分成两部分
        而是第一个元素通过一个low一个high游标相夹， low的左边都比第一个元素小，high的右边都比第一个元素大
        以此来确定第一个元素在序列中的位置
        时间复杂度O(nlogn) 第一次分成2部分，2部分分成4部分，也就是 2*2*2*...=n 也就是logn次才能变成一个个单独元素的数组推出递归
        如果9个元素的话，n = log2为底9，结果为3，横向为n，纵向为logn总体最优复杂度为O(nlogn)，最坏为O(n^2)
    """

    # 递归终止条件，如果递归的数组只有一个元素的时候
    if first >= last:
        return

    low = first
    high = last
    mid_value = alist[first]

    while low < high:
        """遇到相等元素，等号放在随便的一遍，这里放在了high移动的一边"""
        while low < high and alist[high] >= mid_value:
            """如果low和high在向中间走的过程中没有相遇，并且high的元素大于当前mid_value就继续向左移动"""
            high -= 1
        # 移动完发现不大于，那么就交换一下位置，high暂停移动，low开始移动
        alist[low] = alist[high]
        # low += 1

        while low < high and alist[low] < mid_value:
            """如果low和high在向中间走的过程中没有相遇，并且low的元素小于当前mid_value就继续向右移动"""
            low += 1
        alist[high] = alist[low]
        # high -= 1

    alist[low] = mid_value

    # 把一个元素放在正确的位置之后，递归左边和右边的部分
    # 但是切片返回的是一个新的数组，不合适，需要手动更新low，high的位置
    # quick_sort(alist[:low])
    # quick_sort(alist[low:])

    # 对low左边和右边的数组递归
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)