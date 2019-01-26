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

# 测试main()函数
def main():
    # 使用枪类创建一把AK47
    ak47 = Gun("AK47", 50)
    print(ak47)
    ak47.add_bullets(50)

main()