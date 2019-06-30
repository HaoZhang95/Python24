"""
    树分为好多种，二叉树就是一个父节点最多只能包含两个子节点，树的度最多为2

    完全二叉树：如果有n层，那么除了最底层之外的节点都挂满了子节点，父节点都达到了最大的度
    满二叉树：所有节点都达到最大的度，包含最底层
    平衡二叉树：当且仅当任意一个节点的**两颗子树**的高度差不大于1的二叉树
    有序二叉树：树的每一个节点都是有序的，根节点左边的节点都比根节点小，右边的都比根节点大
"""

"""
    树的存储：
    如果采用顺序存储的话,那么以数组的方式，装完一层之后去装下一层的节点，虽然遍历上有优势，但是占用空间大，非主流的存储方式
    一般采用的就是链式的存储方式，树常用在xml,html的解析中，mysql的索引，路由协议，文件系统的目录结构
"""


class Node(object):
    """树的结构类似于链表的扩充，也需要节点"""

    def __init__(self, elem=None, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):

    def __init__(self, root):
        self.root = root

    def add(self, item):
        """完全二叉树的添加，那一层缺元素的话那么就直接添加到该层的节点，那一层的节点没满就添加到此处"""
        node = Node(item)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            # 只要队列存在元素，就pop判断
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return

        queue = [self.root]
        while queue:

            cur_node = queue.pop(0)
            print(cur_node)

            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def pre_order(self, node):
        """深度遍历中的先序便利，根节点先， 根 -> 左 -> 右"""

        if node is None:
            return

        print(node.elem)
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node):
        """深度遍历中的中序便利，根节点在中，  左 -> 根 -> 右"""

        if node is None:
            return

        self.in_order(node.lchild)
        print(node.elem)
        self.in_order(node.rchild)

    def post_order(self, node):
        """深度遍历中的后序便利，根节点在后， 左 -> 右 -> 后"""

        if node is None:
            return

        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem)
