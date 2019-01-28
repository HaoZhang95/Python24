import pygame, random

# 定义一个常量类，赋值后不能修改,Python中崇尚的是一切靠自觉
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768

# 敌机
class EnemyPlane(object):

    def __init__(self):
        self.num = str(random.randint(1, 7))
        # 敌机图片
        self.img = pygame.image.load("res/img-plane_" + self.num + ".png")
        # 外框矩形  -> (x,y, 宽像素，高像素)
        self.img_rect = self.img.get_rect()
        # 随机的初始化位置
        self.reset()

    # 敌机向下移动
    def move_down(self):
        self.img_rect.move_ip(0, self.speed)
        # 敌机位置重置，进行回收
        if self.img_rect[1] >= WINDOW_HEIGHT:
            self.reset()

    # 随机的初始化位置
    def reset(self):
        # 随机的初始化位置
        self.img_rect[0] = random.randint(0, WINDOW_WIDTH - self.img_rect[2])
        self.img_rect[1] = -self.img_rect[3]
        # 敌机移动的速度
        self.speed = random.randint(3,5)