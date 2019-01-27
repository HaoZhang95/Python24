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

    # gun发射子弹打击土匪
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



class Player(object):

    def __init__(self, name, hp=100):
        # 玩家名字
        self.name = name
        # 血量
        self.hp = hp
        # 使用的枪械
        self.gun = None

    def __str__(self):
        # 如果土匪的学量小于0
        if self.hp <= 0:
            return "%s 已经挂掉了..." % self.name
        else:
            # 没枪是土匪，只有警察有枪
            if self.gun is None:
                return "%s [%d]没有佩戴枪" % (self.name, self.hp)
            else:
                return "%s [%d] 枪：%s" % (self.name, self.hp, self.gun)

    # 土匪受伤的方法
    def hurt(self, enemy_gun):
        # 击中更新血量
        self.hp -= enemy_gun.damage
        # 判断剩余血量
        if self.hp <= 0:
            print("%s 已经挂掉了..." % self.name)
        else:
            print("%s 被 %s 击中，剩余血量: %d" % (self.name, enemy_gun.model, self.hp))

    # 警察开火
    def fire(self, enemy):
        # 警察判断自己有无武器
        if self.gun is None:
            print("%s 没有佩戴枪, 请佩戴枪" % self.name)
            return

        # 判断有无子弹
        if self.gun.bullet_count <= 0:
            # 自动填充子弹
            self.gun.add_bullets(10)

        # 射击土匪
        self.gun.shoot(enemy)
        print("%s 正在向 %s 开火..." % (self.name, enemy.name))

# 测试main()函数
def main():

    # 创建一个警察
    police_man = Player("警察")
    # 创建一个土匪
    bad_man = Player("土匪", 70)
    # 枪打土匪(无枪)
    police_man.fire(bad_man)
    # 使用枪类创建一把AK47
    ak47 = Gun("AK47", 50)
    # 给警察配枪
    police_man.gun = ak47
    # 枪打土匪(有枪)
    police_man.fire(bad_man)
    police_man.fire(bad_man)

    # # 填充子弹
    # ak47.add_bullets(50)

main()
