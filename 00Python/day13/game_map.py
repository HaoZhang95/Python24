import pygame, random

# 定义一个常量类，赋值后不能修改,Python中崇尚的是一切靠自觉
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768

# 自定义一个地图类
class GameMap(object):

    def __init__(self):
        self.num = str(random.randint(1,5))
        # 图片1,2无缝连接，上下滚动
        self.img_1 = pygame.image.load("res/img_bg_level_" + self.num+".jpg")
        self.img_2 = pygame.image.load("res/img_bg_level_" + self.num+".jpg")
        # 记录背景图片的y轴坐标
        self.img1_y = -WINDOW_HEIGHT
        self.img2_y = 0
        # 背景移动的速度
        self.speed = 2

    # 背景向下移动
    def move_down(self):
        # 地图的y轴重置
        if self.img1_y >= 0:
            self.img1_y = -WINDOW_HEIGHT
            self.img2_y = 0

        self.img1_y += self.speed
        self.img2_y += self.speed