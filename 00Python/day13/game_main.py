import pygame, sys, hero_plane,game_map, enemy_plane, game_score

# 定义一个常量类，赋值后不能修改,Python中崇尚的是一切靠自觉
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 768

# 窗口管理类
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
        self.game_map = game_map.GameMap()

        # 创建一个英雄飞机对象
        self.hero_plane = hero_plane.HeroPlane()

        # 创建多架敌机
        self.enemy_list = [ enemy_plane.EnemyPlane() for i in range(6) ]

        # 加载背景音乐
        pygame.mixer.music.load("./res/bg2.ogg")
        pygame.mixer.music.play(-1)

        # 程序启动就开始加载碰撞音效
        self.boom_sound = pygame.mixer.Sound("./res/baozha.ogg")

        # 初始化分数文字
        self.score_text = game_score.GameScore(35)

    # 运行游戏程序, 一直死循环检测
    def run(self):
        while True:
            self.__action()
            self.__draw()
            self.__event()
            self.__update()
            self.__bullet_hit_enemy()

    # 1- 处理各种矩形坐标移动
    def __action(self):
        self.game_map.move_down()

        # 遍历子弹
        for bullet in self.hero_plane.bullet_list:
            if bullet.is_shot:
                bullet.move_up()

        # 敌机自由落体运动
        for enemy in self.enemy_list:
            enemy.move_down()

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

        # 添加敌机
        for enemy in self.enemy_list:
            self.window.blit(enemy.img, (enemy.img_rect[0], enemy.img_rect[1]))

        # 添加分数文字
        self.window.blit(self.score_text.text_obj, (10,10))

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
        # 停止背景音乐
        pygame.mixer.music.stop()
        # 停止音效
        self.boom_sound.stop()
        # 停止游戏引擎
        pygame.quit()
        # 关闭窗口，退出游戏，
        sys.exit()

    # 碰撞检测
    def __bullet_hit_enemy(self):
        # 遍历所有子弹
        for bullet in self.hero_plane.bullet_list:
            # 查看发射的子弹是否击中敌机之一
            if bullet.is_shot:
                for enemy in self.enemy_list:
                    is_hit = pygame.Rect.colliderect(bullet.img_rect, enemy.img_rect)
                    if is_hit:
                        # 子弹消失
                        bullet.is_shot = False
                        # 敌机消失
                        enemy.reset()
                        # 播放音效
                        self.boom_sound.play()
                        # 更新分数
                        self.score_text.set_text_obj()


def main():

    # 创建游戏窗口类
    game_window = GameWindow()
    # 运行游戏
    game_window.run()

if __name__ == '__main__':
    main()
