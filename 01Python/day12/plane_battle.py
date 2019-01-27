"""
    飞机大战游戏， settins-project intepretor—点击加号搜索第三方的模块，安装即可，安装后的文件出现在site-package文件夹内
"""
import pygame, sys

# 实例化pygame
pygame.init()

# 创建游戏窗口[宽，高] -> 窗口对象
window = pygame.display.set_mode([512,768])

# 设置窗口的title
pygame.display.set_caption("飞机大战")

# 设置窗口的图标icon,加载一个图片对象
logo_image = pygame.image.load("res/app.ico")
pygame.display.set_icon(logo_image)

# 游戏背景图片添加到窗口上, blit(需要添加的对象，(x坐标，y坐标))
bg_image = pygame.image.load("res/img_bg_level_1.jpg")
window.blit(bg_image, (0, 0))
# 记得刷新窗口来显示自己添加的元素
pygame.display.update()

# **死循环**中监听鼠标和键盘的事件
while True:
    # 获取所有窗口中的事件监听 -> 列表
    event_list = pygame.event.get()
    # 遍历所有的事件
    for event in event_list:
        # 如果是鼠标点击关闭事件
        if event.type == pygame.QUIT:
            # 停止游戏引擎
            pygame.quit()
            # 关闭窗口，退出游戏，
            sys.exit()

        # 监听按下事件
        if event.type == pygame.KEYDOWN:
            # 是否按下的是Esc
            if event.key == pygame.K_ESCAPE:
                # 停止游戏引擎
                pygame.quit()
                # 关闭窗口，退出游戏，
                sys.exit()

    # 监听键盘长按事件 -> 元组(0没按下，1长按了) 字母对应阿斯克码
    pressed_keys = pygame.key.get_pressed()

    # 判断向上是否被长按（1）
    if pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        print("向上")

    # 判断向下是否被长按（1）
    if pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        print("向下")

    # 判断向左是否被长按（1）
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        print("向左")

    # 判断向右是否被长按（1）
    if pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        print("向右")

