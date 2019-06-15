"""
    双向链表
"""


class Node(object):
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self, node=None):
        # 头节点不需要暴露，使用私有属性
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        count = 0

        while cur is not None:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        # 游标用来移动遍历节点
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print('\n')

    def add(self, item):
        """头部插入元素"""
        node = Node(elem=item)
        # 注意下面两行的顺序
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """尾部插入节点"""
        node = Node(elem=item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            # 注意cur和cur.next的不同使用
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            cur = self.__head
            count = 0

            while count < pos:
                count += 1
                cur = cur.next
            # 循环推出后pre指向pos-1位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        cur = self.__head

        while cur is not None:
            if cur.elem == item:
                # 判断是不是头节点
                if cur == self.__head:
                    self.__head = cur.next
                    if cur.next is not None:
                        # 如果链表不是只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next is not None:
                        cur.next.prev = cur.prev
                break
            else:
                cur = cur.next

    def search(self, item):
        cur = self.__head
        while cur is not None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False
