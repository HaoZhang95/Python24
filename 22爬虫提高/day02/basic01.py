import hashlib
import json
import random
import re
import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    "Referer": "http://fanyi.youdao.com/"
}


def test01():
    """36kr.com的内容是存放在script标签中"""

    class Kr36(object):

        def __init__(self):
            self.url = 'https://36kr.com/'
            self.headers = headers
            self.file = open('36kr.json', 'w', encoding='utf8')

        def get_data(self):
            resp = requests.get(url=self.url, headers=self.headers)
            return resp.content.decode()

        def parse_data(self, data):

            # 将html页面提取内容，发现内容都是包含在script中
            result = re.findall('<script>var prop=(.*?)</script>', data, re.S)[0]
            # 提取到的内容发现直接loads报错，原因是包含=等， 去除不标准的json字符串
            result_list = re.sub(',locational={.*', '', result)

            dict_data = json.loads(result_list)['feedPostsLatest|post']

            # 提取需要的数据
            data_list = []
            for data in dict_data:
                temp = {}
                temp['cover'] = data['cover']
                temp['title'] = data['title']
                data_list.append(temp)

            return data_list

        def save_data(self, data_list):
            for data in data_list:
                str_data = json.dumps(data, ensure_ascii=False) + ",\n"
                self.file.write(str_data)

        def __del__(self):
            self.file.close()

        def run(self):
            data = self.get_data()
            parse_data = self.parse_data(data)


    Kr36().run()


def test02():
    """有道词典翻译"""
    class Youdao(object):

        def __init__(self):
            self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
            self.headers = headers
            self.post_data = None

        def generate_post_data(self, word):
            now = int(time.time() * 1000)
            random_num = random.randint(0, 9)
            salt = str(now + random_num)
            S = 'fanyideskweb'
            n = word
            r = salt
            D = ''

            md5Str = S + n + r + D
            # 生成md5对象
            md5 = hashlib.md5()
            # 填充数据
            md5.update(md5Str.encode())
            # 生成16进制
            o = md5.hexdigest()


            self.post_data = {
                'i': word,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': dict,
                'client': 'fanyideskweb',
                'salt': '15561745799005',
                'sign': '69aad56937660f19b95143d9f9164165',
                'ts': '1556174579900',
                'bv': '8738acdfb64ced94051e576f287e2052',
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_CLICKBUTTION',
            }

        def get_data(self):
            resp = requests.post(url=self.url, headers=self.headers, data=self.post_data)
            print(resp.content.decode())
            return resp.content.decode()

        def parse_data(self, data):
            dict_data = json.loads(data)
            result = dict_data['translateResult'][0][0]['tgt']
            print(result)

        def run(self):
            # import sys
            # word = sys.argv[1]
            self.generate_post_data('黄金')
            data = self.get_data()
            self.parse_data(data)

    Youdao().run()


def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

