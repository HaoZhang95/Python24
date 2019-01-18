
"""
    python中的else if语句使用的是elif, python中并没有switch
    if语句的嵌套
"""
score = 80
if score >= 90:
    print("优")
elif score >= 80:
    print("良")
elif score >= 60:
    print("合格")
else:
    print("差")

daoLength = 10
ticket = 1
if daoLength <= 10:
    print("你可以进入火车站")
    if ticket == 1:
        print("你有车票可以上车")
    else:
        print("请买票后再上车")
else:
    print("你携带管制刀具，禁止上车")


"""
    while循环的使用和应用
"""
i = 0
while i < 5:
    print("媳妇，我错了")
    i += 1

x = 1
result_x = 0
while x <= 100:
    result_x += x
    x += 1
print("1-100的和总共为：%d" % result_x)

y = 1
result_y = 0
while y <= 100:
    if y % 2 == 0:
        result_y += y
    y += 1
print("1-100的偶数和总共为：%d" % result_y)

"""
    while循环的嵌套，打印三角形
"""
z = 1
while z <= 5:
    colum = 1
    while colum <= z:
        print("*", end=" ")
        colum += 1
    print()
    z += 1

"""
    while循环的嵌套，打印九九乘法表
    多个占位符的表达方式： "%d + %d = %d" % (1,2,(1*2))
    
    %-2d,两位数左对齐， %2d两位数右对齐， 保持层次对齐
"""
row = 1
max = 9
while row <= max:
    colum = 1
    while colum <= row:
        print("%d*%d=%-2d" % (colum, row, (colum * row)), end=" ")
        colum += 1
    print()
    row += 1

"""
    if语句猜拳游戏
    random模块产生随机数, randint(0,2)相当于区间[0,2]
"""
import random

will_continue = True
while will_continue:
    player = int(input("请输入： 剪刀（0） 石头（1） 布（2）："))
    computer = random.randint(0,2)
    print("player: %s, computer: %d, type = %s" %(player,computer,type(player)) )
    # 以用户为第一视角： 胜 平 负

    if (player == 0 and computer == 2) \
            or (player == 1 and computer == 0) \
            or (player == 2 and computer == 1):
        print("你赢了")
    elif player == computer:
        print("平局")
    else:
        print("你输了")

    if input("继续请按(y): ") == "y":
        will_continue = True
    else:
        will_continue = False






