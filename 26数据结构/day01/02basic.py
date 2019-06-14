def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


from timeit import Timer

# setup中是从从__main__也就是当前文件名02basic中找到test1
# 创建一个timer对象
t1 = Timer(stmt="test1()", setup="from __main__ import test1")
print("concat ", t1.timeit(number=1000), "seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append ", t2.timeit(number=1000), "seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension ", t3.timeit(number=1000), "seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range ", t4.timeit(number=1000), "seconds")

# ('concat ', 1.7890608310699463, 'seconds')
# ('append ', 0.13796091079711914, 'seconds')
# ('comprehension ', 0.05671119689941406, 'seconds')
# ('list range ', 0.014147043228149414, 'seconds')

"""
    一个int类型占用4个字节，内存就是一系列连续的存储单元，单元是以字节表示，int a = 1,二进制就是00000000 00000000 00000000 00000001
    顺序表就是将类型一致的变量存在连续的存储单元中，li = [1,2,3]这样的物理地址是连续的为0x01, 0x05, 0x09 c是指该类型的存储大小,int类型的话就是4
    
    顺序表中的元素外置可以解决列表中的不同数据类型，每个列表的存储都是4个字节4个字节的格子，每个格子存储的是地址指向不同的数据类型的外置元素
    列表中的地址存储就是占用4个字节的存储单元
    
    顺序表中的表头区和数据区，表头信息包含该数据表中的整体信息，比如容量和实际元素个数都存储在表头信息中，一般使用分离式的存储表头信息
    表头信息可以使用一体式的存储方式或者外链式的存储，具体表头存储采用哪一种方式，主要的区别就是扩容的时候，一体式的方式表头信息的地址会变化
    
    扩容的策略：固定的每次扩容增加10个位置，线性增长，不过需要频繁的进行扩容操作
                或者倍增的方式，减少扩容的请求，空间换取时间
"""

"""
    链表的原理就是node节点，每个元素的存储地址不连续，使用前一个节点记录下一个元素的位置进行串起来，就像手链一样
    单向链表LinkedList中只有数据区和下一个节点物理地址，双向链表是记录着上一个节点的位置，单向链表并没有记录上一个节点的物理地址
    
    python是弱类型语言，因为a = 10中a这个变量名也占用一份内存，不像java中的int a = 10 a只是10这个物理地址的别名，a也不能赋值其他类型的值
"""
