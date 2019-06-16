"""
    堆栈就像水杯一样，一种容器，类似于顺序表结构但是只有push和pop，一端进出，后进的先出去
    队列就像排队一样，先来的先出去
"""


class Stack(object):
    def __init__(self):
        self.__list = []

    def push(self, item):
        self.__list.append(item)
        # 可以选择append和insert0的方式，不过insert的方式时间复杂度为O(n)
        # self.__list.insert(0)
        # self.__list.pop(0)

    def pop(self):
        self.__list.pop()

    def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        # return not self.__list
        # return self.__list == []
        return self.size() == 0

    def size(self):
        return len(self.__list)


class Queue(object):
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        self.__list.append(item)
        # 可以选择append和insert0的方式，不过insert的方式时间复杂度为O(n)
        # self.__list.insert(0, item)
        # self.__list.pop()

    def dequeue(self):
        self.__list.pop(0)

    def is_empty(self):
        # return not self.__list
        # return self.__list == []
        return self.size() == 0

    def size(self):
        return len(self.__list)


class Deque(object):
    """
        double-ended-queue双端队列，两端都可以进行push和pop，类似于两个堆栈底部合起来

    """
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list.insert(0, item)

    def ad_rear(self, item):
        self.__list.append(item)

    def remove_front(self):
        self.__list.pop(0)

    def remove_rear(self):
        self.__list.pop()

    def is_empty(self):
        # return not self.__list
        # return self.__list == []
        return self.size() == 0

    def size(self):
        return len(self.__list)