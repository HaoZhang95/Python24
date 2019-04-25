import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def test01():
    """36kr.com的内容是存放在script标签中"""

    class Kr36(object):

        def __init__(self):
            self.url = 'https://36kr.com/'
            self.headers = headers

        def get_data(self):
            resp = requests.get(url=self.url, headers=self.headers)

        def parse_data(self):
            pass

        def save_data(self):
            pass

        def run(self):
            data = self.get_data()
            parse_data = self.parse_data(data)


def test02():
    """
        selenium是一个测试工具，requests能做的这个测试工具也能做，类似于一个运行在浏览器上的测试工具
        这个测试工具模拟浏览器接受自己的指令来加载页面(模拟浏览器操作做)，甚至可以加载phantomJS这样无界面的浏览器

        phantomJS是无头浏览器，会把返回的js加载到内存中执行js处理
    """
    pass



def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

