import pygame, sys, random

# 定义一个常量类，赋值后不能修改,Python中崇尚的是一切靠自觉
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768

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
        self.bullet_list = [Bullet() for i in range(6)]

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


# 游戏窗口管理类
class GameWindow(object):

    def __init__(self):
        # 实例化pygame
        pygame.init()

        # 创建游戏窗口[宽，高] -> 窗口对象
        self.window = pygame.display.set_mode([WINDOW_WIDTH,WINDOW_HEIGHT])

        # 设置窗口的title
        pygame.display.set_caption("飞机大战")

        # 设置窗口的图标icon,加载一个图片对象
        logo_image = pygame.image.load("res/app.ico")
        pygame.display.set_icon(logo_image)

        # 创建一个地图对象，渲染背景图片
        self.game_map = GameMap()

        # 创建一个英雄飞机对象
        self.hero_plane = HeroPlane()

    # 运行游戏程序
    def run(self):
        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()

    # 1- 处理各种矩形坐标移动
    def __action(self):
        self.game_map.move_down()

        # 遍历子弹
        for bullet in self.hero_plane.bullet_list:
            if bullet.is_shot:
                bullet.move_up()

    # 2- 根据矩形坐标，对元素进行回测
    def __draw(self):
        # 添加背景图片
        self.window.blit(self.game_map.img_1, (0, self.game_map.img1_y))
        self.window.blit(self.game_map.img_2, (0, self.game_map.img2_y))
        # 添加英雄飞机
        self.window.blit(self.hero_plane.img, (self.hero_plane.img_rect[0], self.hero_plane.img_rect[1]))
        # 添加子弹
        for bullet in self.hero_plane.bullet_list:
            if bullet.is_shot:
                self.window.blit(bullet.img, (bullet.img_rect[0], bullet.img_rect[1]))

    # 3- 处理窗口中的监听事件
    def __event(self):
        # 获取所有窗口中的事件监听 -> 列表
        event_list = pygame.event.get()
        # 遍历所有的事件
        for event in event_list:
            # 如果是鼠标点击关闭事件
            if event.type == pygame.QUIT:
                self.game_over()

            # 监听按下事件
            if event.type == pygame.KEYDOWN:
                # 是否按下的是Esc
                if event.key == pygame.K_ESCAPE:
                    self.game_over()
                # 是否按下的是空格
                if event.key == pygame.K_SPACE:
                    self.hero_plane.shoot()

        # 监听键盘长按事件 -> 元组(0没按下，1长按了) 字母对应阿斯克码
        pressed_keys = pygame.key.get_pressed()

        # 判断向上是否被长按（1）
        if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
            self.hero_plane.move_up()

        # 判断向下是否被长按（1）
        if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
            self.hero_plane.move_down()

        # 判断向左是否被长按（1）
        if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
            self.hero_plane.move_left()

        # 判断向右是否被长按（1）
        if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
            self.hero_plane.move_right()

    # 4- 刷新窗口
    def __update(self):
        pygame.display.update()

    # 结束游戏
    def game_over(self):
        # 停止游戏引擎
        pygame.quit()
        # 关闭窗口，退出游戏，
        sys.exit()

def main():

    # 创建游戏窗口类
    game_window = GameWindow()
    # 运行游戏
    game_window.run()

if __name__ == '__main__':
    main()
