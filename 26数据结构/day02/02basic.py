class Node(object):
    """单链表的节点"""

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleCycleLinkedList(object):
    """单链表的结构"""

    def __init__(self, node=None):
        # 头节点不需要暴露，使用私有属性
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):

        if self.is_empty():
            return 0

        cur = self.__head
        # while的循环条件变了，count不能从0开始，否则缺少最后一个节点
        count = 1
        while cur.next is not self.__head:
            count += 1
            cur = cur.next

        return count

    def travel(self):
        # 游标用来移动遍历节点
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next

        # 退出循环后，cur指向最后节点，但是最后节点没被打印
        print(cur.elem)
        print('\n')

    def add(self, item):
        """头部插入元素，把尾节点的next指向第一个节点"""
        node = Node(elem=item)
        if self.is_empty():
            self.__head = node
            node.next = node
            return

        cur = self.__head
        while cur.next is not self.__head:
            cur = cur.next
        # 注意下面两行的顺序
        node.next = self.__head
        self.__head = node
        cur.next = self.__head

    def append(self, item):
        """尾部插入节点"""
        node = Node(elem=item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            # 注意cur和cur.next的不同使用
            while cur.next is not self.__head:
                cur = cur.next

            node.next = self.__head
            cur.next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() - 1:
            self.append(item)
        else:
            pre = self.__head
            count = 0

            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 循环推出后pre指向pos-1位置
            node = Node(elem=item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        if self.is_empty():
            return

        cur = self.__head
        pre = None

        while cur.next is not self.__head:
            if cur.elem == item:
                # 判断是不是头节点
                if cur == self.__head:
                    rear = self.__head
                    while rear.next is not self.__head:
                        rear = rear.next
                    self.__head = cur.next
                    rear.next = self.__head

                else:
                    pre.next = cur.next
                return
            else:
                pre = cur
                cur = cur.next

        if cur.elem == item:
            if cur is self.__head:
                # 链表只有一个节点
                self.__head = None
            else:
                pre.next = cur.next

    def search(self, item):

        if self.is_empty():
            return False

        cur = self.__head
        while cur.next is not self.__head:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        # 此时的cur指向最后一个元素
        if cur.elem == item:
            return True

        return False


def main():
    ll = SingleCycleLinkedList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.travel()


if __name__ == '__main__':
    main()
