import json

import requests


def test01():
    url = 'http://www.zhihu.com/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
    }

    resp = requests.get(url, headers=headers)

    # 知乎不加header的话返回400 Bad Request
    print(resp.status_code)


def test02():
    class Baidu(object):

        def __init__(self, keyword, pn):
            self.keyword = keyword
            self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}&pn='.format(self.keyword)
            self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
            }

            # 根据传入的页数构成一个url——list,贴吧默认就是一页显示50
            # 主要注意传入的pn必须是int类型，否则pn*50的时候会报错
            self.url_list = [self.url + str(pn*50) for pn in range(pn)]
            print(self.url_list)

        def get_data(self, url):
            resp = requests.get(url, headers=self.headers)
            return resp.content

        def save_data(self, data, index):
            file_name = 'tieba_{}.html'.format(index)
            with open(file_name, 'wb') as file:
                file.write(data)

        def run(self):

            for url in self.url_list:
                data = self.get_data(url)
                index = self.url_list.index(url)
                print(index)
                self.save_data(data, index)

    Baidu('李毅', 5).run()


def test03():
    """模拟post请求, 获取翻译结果"""
    class JinShanFanYi(object):

        def __init__(self, text):
            self.url = 'http://fy.iciba.com/ajax.php?a=fy'
            self.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
            }
            self.post_data = {
                'f': "auto",
                't': "auto",
                'w': text,
            }

        def get_data(self):
            # get请求的话参数是params，post使用的是data
            resp = requests.post(self.url, data=self.post_data, headers=self.headers)
            return resp.content.decode()

        def parse_data(self, data):
            # 把响应数据转换为字典
            dict = json.loads(data)
            # 判断key是否存在,out是中译英，word_mean是英译中
            if 'out' in data:
                print(dict['content']['out'])
            else:
                print(dict['content']['word_mean'][0])

        def run(self):
            data = self.get_data()
            self.parse_data(data)

    JinShanFanYi('python').run()


def test04():
    """代理的使用方法，代理网站比如：快代理, mimvp代理"""
    url = 'http://www.baidu.com/'

    proxies = {
        # 免费代理
        'http': 'http://117.69.99.82:37862',
        # 付费代理格式
        # 'http': 'http://user:pwd@111.177.166.47:9999'
    }

    resp = requests.get(url=url, proxies=proxies)
    print(resp.status_code)


def main():
    # test01()
    # test02()
    # test03()
    test04()


if __name__ == '__main__':
    main()


