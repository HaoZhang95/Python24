import json

import requests

"""
    对称加密：客户端和服务器使用一个密钥进行，密钥容易被获取，但是加密效率高，传输快
    非对称加密：公钥和私钥都可以加密，一般公钥对数据进行加密形成密文，密文经过私钥解析成明文给服务器
"""

"""
    数据：结构化数据和非结构化数据主要是指数据有无规律
    比如xml数据和json数据都是结构化数据，转换为python对象即可获取数据
    非结构化数据html(数据可能在不同的标签中)，文本等属于非结构化数据，使用正则/xpath获取
"""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/73.0.3683.75 Safari/537.36 "
}

"""
    json之一个基于键值对格式的**字符串**，字典则是一个对象类型
    json字符串 --> json.loads(str) --> python数据类型
    python数据类型 --> json.dumps(dict) --> json字符串
    
    json.load不加s的是用来将数据进行转换并且写入文件的时候才会使用不带s的方法
"""

def test01():
    # python中支持单引号,但是转换为数据类型的时候，需要使用双引号，json字符串必须外单内双
    dict_data = {"name": "Hao浩"}
    # 转换为json字符串
    json_str = json.dumps(dict_data)

    # 转成json字符串的时候默认编码为ascii编码，需要设置ensure_ascii=false
    print(json_str)

    print(type(dict_data))
    print(type(json_str))


    # load,dump写文件如果遇到编码，可以在写文件的时候制定编码格式utf-8
    f = open('data.json', 'w', encoding='utf8')
    json.dump(dict_data, f, ensure_ascii=False)
    f.close()

    # # 读取文件中的json
    f1 = open('data.json', 'r', encoding='utf8')
    dict_data1 = json.load(f1)
    print(dict_data1)
    f1.close()


def test02():

    class Douban(object):

        # 构建请求头和url
        def __init__(self):
            self.url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8' \
                        '&sort=recommend&page_limit=20&page_start=0'
            self.headers = headers
            self.file = open('douban.json', 'w', encoding='utf8')

        # 发送请求
        def get_data(self):
            resp = requests.get(url=self.url, headers=self.headers)
            return resp.content.decode()

        # 解析数据
        def parse_data(self, data):
            # 把返回的json字符串转换为字典
            dict_data = json.loads(data)
            result_list = dict_data['subjects']

            # 获取电影列表数据
            # data_list = []
            # for result in result_list:
            #     temp = {}
            #     temp['title'] = result['title']
            #     temp['rate'] = result['rate']
            #     temp['url'] = result['url']
            #     data_list.append(temp)

            # 返回数据列表
            return result_list

        # 保存到文件
        def save_data(self, data_list):
            """文件以str的方式写入"""
            for data in data_list:
                str_data = json.dumps(data, ensure_ascii=False) + ',\n'
                self.file.write(str_data)

        def __del__(self):
            """在douban这个对象无引用的时候进行file关闭"""
            self.file.close()

        # 执行
        def run(self):
            self.save_data(self.parse_data(self.get_data()))


    Douban().run()


def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

