def binary_search(alist, item):
    """二分法查找，递归方法"""

    n = len(alist)
    mid = n // 2

    if n > 0:

        if alist[mid] == item:
            return True
        elif item < alist[mid]:
            # 产生新的列表进行递归
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid:], item)

    return False


"""
    二分法查找的折半查找，操作的对象必须有序，其次计算mid需要index需要顺序表才行
    时间复杂度为 折半2的几次方等于n，最坏所以为 O(logn)，最好就是O(1)
"""


def binary_search_2(alist, item):
    """二分法查找，非递归方法"""

    n = len(alist)
    first = 0
    last = n - 1

    while first <= last:

        mid = (first + last) // 2

        if item == alist[mid]:
            return True
        elif item < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False
