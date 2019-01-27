import pygame, random

# 分数模块
class GameScore(object):

    __cls_score = 0

    def __init__(self, font_size):
        # 设置字体的大小
        self.font = pygame.font.SysFont("SimHei", font_size)
        # render方法返回一个控件对象
        self.text_obj = self.font.render("分数：0",1,(255,255,255))

    # 设置显示的文字和颜色
    def set_text_obj(self):
        # 每次加一分
        self.__cls_score += 1
        # 随机颜色
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        # 更新赋值
        self.text_obj = self.font.render("分数: %d" % self.__cls_score, 1, (r,g,b))
