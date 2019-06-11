"""
    算法就类似于兵法, test1的执行时间为110s， 第二个执行时间为1s
    但是不能淡出的以时间来衡量，因为执行程序的机器配置不同，所以时间不能全面的反应算法的优劣
"""
import time


def test1():
    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            for c in range(0, 1001):
                if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                    print("a, b, c: %d, %d, %d" % (a, b, c))

    end_time = time.time()
    print("finished: %s" % (end_time - start_time))


"""
    如果a+b+c=1000，且a^2+b^2=c^2的a,b,c的组合
    N是程序的规模，例子中N就是1000， a+b+c=N，描述的一类问题
    时间复杂度：就是程序执行的步骤， T(n) = N^3 * (1+1) 也就是1000的三次方
    大O记法：时间复杂度的简化分析，算法分析的是数量级和趋势，不计较规模函数中的常量因子，简化为O(n)=N^3,图线特征和趋势，类似于渐进函数
    
    Test2中：T(n) = n * n * (1 + max(1, 0))
                  = n ^2 *2
                  = O(n^2)
"""


def test2():

    start_time = time.time()
    for a in range(0, 1001):
        for b in range(0, 1001):
            # 此时c就已经确立了，不需要循环1000次了
            c = 1000 - a - b
            if a + b + c == 1000 and a ** 2 + b ** 2 == c ** 2:
                print("a, b, c: %d, %d, %d" % (a, b, c))

    end_time = time.time()
    print("finished: %s" % (end_time - start_time))


def test3():
    list1 = [1, 23, 4, 1, 4, 6]
    list2 = [1, 2, 3, 4, 5, 6]

    """
        如果排序list1和list2的话，list1的时间复杂度和N^2，最坏时间复杂度(一种保证)，一般使用的就是最坏时间复杂度
        list2碰巧为有序的列表，遍历一次即可，时间复杂度为最优时间复杂度，没意义
        
        基本操作算一个时间复杂度O(1) 即只有常数项
        顺序结构采用加法
        循环结构使用乘法
        分支结构采取最大值，if和else中谁的步骤多，if中的条件判断不加进去
        只关注数量级的最高项，一般忽略常量
        
    """


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    pass
