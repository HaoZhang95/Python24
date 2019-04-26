import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def test01():
    """斗鱼平台获取直播房间和的信息"""

    class Douyu(object):

        def __init__(self):
            self.url = 'https://www.douyu.com/'
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



def main():
    test01()


if __name__ == '__main__':
    main()

