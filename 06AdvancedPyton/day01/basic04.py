"""
    多态：调用方在不变得情况下，传入的实例对象不同，如果实例对象重写了父类方法，那么就使用自己本身子类的重写方法，否则直接使用父类的方法

    类似：go(Car), 自行车继承了父类的Car，摩托车继承了Car类， go(Car)方法中的Car.start()方法的时候，
    传入的是自行车那么就使用自行车的start()方法，传入的是摩托车那么就使用摩托车的start()，如果都重写了父类Car的start()方法
    java中叫做延迟绑定，一开始go(Car)调用的时候，绑定的是Car的start方法，后来认出传入的类型是bicycle，就会再次绑定到bicycle的start()方法，这就叫做多态

"""

class MiniOS(object):

    def __init__(self, name):
        self.name = name
        self.apps = []

    def __str__(self):
        return "%s 安装的软件列表：%s." % (self.name, str(self.apps))

    def install_app(self, app):
        if app.name in self.apps:
            print("已经安装了 %s 无需再次安装." % app.name)
        else:
            # 方法传入的是父类的类型，总的类型
            # 这里会根据传入的具体类型去调用具体类型的install方法
            # 具体类型如果没有重写父类app.install()方法的话，那么久直接使用父类的install方法
            app.install()
            self.apps.append(app.name)


class App(object):

    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return "%s 的当前版本是 %s - %s" % (self.name, self.version, self.desc)

    def install(self):
        print("将 %s [%s] 的执行程序复制到程序目录..." % (self.name, self.version))


class PyCharm(App):
    pass


class Chrome(App):

    # super关键字来调用父类方法
    # 通过自身的self获得父类的属性值
    def install(self):
        print("正在解压缩安装程序...")
        super().install()


def main():

    linux = MiniOS("Linux")
    print(linux)

    pycharm = PyCharm("PyCharm", "1.0", "python开放的IDE环境")
    chrome = Chrome("Chrome", "2.0", "谷歌浏览器")

    linux.install_app(pycharm)
    linux.install_app(chrome)
    linux.install_app(chrome)


if __name__ == '__main__':
    main()
