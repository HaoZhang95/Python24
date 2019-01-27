import pygame, plane_bullet

# 定义一个常量类，赋值后不能修改,Python中崇尚的是一切靠自觉
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768

# 英雄飞机类
class HeroPlane(object):

    def __init__(self):
        # 英雄飞机图片
        self.img = pygame.image.load("res/hero2.png")
        # 英雄飞机的外框矩形  -> (x,y, 宽像素，高像素)
        self.img_rect = self.img.get_rect()
        # 飞机的初始化位置
        self.img_rect.move_ip((WINDOW_WIDTH - self.img_rect[2])/2,
                              (WINDOW_HEIGHT - self.img_rect[3]) - 50)
        # 飞机移动的速度
        self.speed = 3

        # 子弹弹夹
        self.bullet_list = [plane_bullet.Bullet() for i in range(6)]

    #  向上移动
    def move_up(self):
        # 边缘检测
        if self.img_rect[1] >= 0:
            self.img_rect.move_ip(0, -self.speed)

    #  向下移动
    def move_down(self):
        if self.img_rect[1] <= WINDOW_HEIGHT - self.img_rect[3]:
            self.img_rect.move_ip(0, self.speed)

    #  向左移动
    def move_left(self):
        if self.img_rect[0] >= 0:
            self.img_rect.move_ip(-self.speed, 0)

    #  向右移动
    def move_right(self):
        if self.img_rect[0] <= WINDOW_WIDTH - self.img_rect[2]:
            self.img_rect.move_ip(self.speed, 0)

    # 发射子弹
    def shoot(self):
        # 遍历所有的子弹
        for bullet in self.bullet_list:
            if not bullet.is_shot:
                # 设置子弹发射的位置
                bullet.img_rect[0] = self.img_rect[0] + (self.img_rect[2] - bullet.img_rect[2]) / 2
                bullet.img_rect[1] = self.img_rect[1] - (bullet.img_rect[3] - 10)
                # 更新子弹的状态
                bullet.is_shot = True
                # 一次只能发射一次子弹
                break
