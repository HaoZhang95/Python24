import pygame

# 子弹类
class Bullet(object):

    def __init__(self):
        # 图片
        self.img = pygame.image.load("res/bullet_10.png")
        # 图片矩形
        self.img_rect = self.img.get_rect()
        # 子弹状态
        self.is_shot = False
        # 子弹移动的速度
        self.speed = 5

    #  向上移动
    def move_up(self):
        self.img_rect.move_ip(0, -self.speed)
        # 设置为未发射状态
        if self.img_rect[1] <= -self.img_rect[3]:
            self.is_shot = False
