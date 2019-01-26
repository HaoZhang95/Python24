"""
    警察vs土匪
"""

class Gun(object):

    def __init__(self, model, damage):
        # 型号
        self.model = model
        # 杀伤力
        self.damage = damage
        # 子弹数量，默认为0
        self.bullet_count = 0

    # 重写str
    def __str__(self):
        return "型号：%s, 杀伤力：%s, 子弹数量：%s" % (
            self.model, self.damage, self.bullet_count
        )

    # 填充子弹
    def add_bullets(self, bullet_count):
        self.bullet_count += bullet_count
        print("填充子弹完成，当前数量为：%s" % bullet_count)

    # 发射子弹打击土匪
    def shoot(self, enemy):
        # 判断当前枪是否有子弹
        if self.bullet_count <= 0:
            print("%s 没有子弹, 请填充子弹" % self.model)
        else:
            # 如果有子弹，更新子弹数量
            self.bullet_count -= 1
            # 判断是否击中土匪
            if enemy is not None:
                enemy.hurt(self)

            print("发射了一颗子弹 %s 剩余子弹：%d" % (self.model, self.bullet_count))





# 测试main()函数
def main():
    # 使用枪类创建一把AK47
    ak47 = Gun("AK47", 50)
    print(ak47)
    # 枪打土匪
    ak47.shoot(None)
    # 填充子弹
    ak47.add_bullets(50)


main()