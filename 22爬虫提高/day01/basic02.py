import json
import re

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def test01():
    """正则表达式"""

    # 匹配字符串自身
    data = 'python24'
    print(re.findall('py', data))

    # . 匹配除了换行符之外的任意字符
    data1 = 'a\nb'
    print(re.findall('a.b', data1))
    # .的情况下，识别换行符,下面两个都可以
    print(re.findall('a.b', data1), re.DOTALL)
    print(re.findall('a.b', data1), re.S)
    print(re.findall('a\nb', data1))

    # [] 匹配容器中的内容
    data2 = 'abc_adc'
    print(re.findall('a[bd]c', data2))

    # | 或操作
    data3 = 'itcast|python'
    print(re.findall('t|p', data3))     # ['t', 't', 'p', 't']
    print(re.findall('t\|p', data3))    # ['t|p']

    # 匹配数字, 正则默认开启贪婪模式(尽可能多的匹配)， ？写在\d的后面表示非贪婪模式
    data4 = 'itcast 2018 python24'
    print(re.findall('\d', data4))      # ['2', '0', '1', '8', '2', '4']
    print(re.findall('\d+', data4))     # ['2018', '24']
    print(re.findall('\d+?', data4))    # ['2', '0', '1', '8', '2', '4']

    # * 尽可能的匹配，匹配不到返回空字符串
    print(re.findall('\d*', data4))    # ['', '', '', '', '', '', '', '2018', '', '', '', '', '', '', '', '24', '']

    # 编译一个正则,python中尽量使用compile来确认一个正则的pattern
    # 和直接re.findall相比，下面的性能提高很多，先编译一次后，可以匹配n次
    pattern = re.compile('\d')
    print(pattern.findall(data4))


class Neihan(object):

    # 构造url，请求头
    def __init__(self):
        self.url = 'http://neihanshequ.com/'
        # 用来加载下一页的url
        self.ajax_url = 'http://neihanshequ.com/joke/?'
        self.headers = headers
        self.file = open('neihan.json', 'w', encoding='utf8')

    # 发送请求
    def get_data(self, url, params=None, headers=None):
        if params is None:
            resp = requests.get(url=url, headers=self.headers)
        else:
            resp = requests.get(url=url, headers=headers, params=params)
        return resp.content.decode()

    # 解析数据
    def parse_data(self, data):
        # 使用正则匹配想要的段子数据
        result_list = re.findall('<a target="_blank" class="image share_url" '
                                 'href="(.*?)" .*?<p>(.*?)</p>', data, re.S)
        # 获取分组后的数据
        data_list = []
        for result in result_list:
            temp = {}
            temp['url'] = result[0]
            temp['content'] = result[1]
            data_list.append(temp)

        # 获取时间戳,注意引号的位置，否则匹配不到
        max_time = re.findall("max_time: '(\d+)'", data)[0]

        # 返回结果
        return data_list, max_time


    # 解析ajax数据
    def parse_ajax_data(self,data_list):
        # 转成字典
        dict_data = json.loads(data_list)
        # print (dict_data)
        result_list = dict_data['data']['data']
        # 定义容器存储下一页的数据
        data_list = []
        for result in result_list:
            temp = {}
            temp['url'] = result['group']['share_url']
            temp['content'] = result['group']['content']
            # print(temp)
            data_list.append(temp)
        # 获取时间戳
        max_time = dict_data['data']['max_time']
        # print (max_time)
        # 返回数据
        return data_list, max_time


    # 保存文件
    def save_data(self, data_list):
        for data in data_list:
            json_str = json.dumps(data, ensure_ascii=False) + ',\n'
            self.file.write(json_str)

    # 关闭文件
    def __del__(self):
        self.file.close()

    # 第一页首页会生成时间戳，会用来加载下一页的时候用到，需要保存上一页的时间戳
    def run(self):
        data = self.get_data(self.url)
        data_list, max_time = self.parse_data(data)
        self.save_data(data_list)

        # 不断循环加载下一页的数据
        while True:
            # 构造请求下一页的参数
            params = {
                "is_json": "1",
                "app_name": "neihanshequ_web",
                "max_time": max_time
            }

            # 加载第一页的时候是没有cookie信息的，所以区分开
            # 加上cookie的原因是防止反扒
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
                'Cookie': 'csrftoken=245c0765ecede1727127ddaf7e3d6ef9; tt_webid=6539038376715929095; uuid="w:04341f3c529a49b8ac51c54443bc0467"; _ga=GA1.2.2055694696.1522488515; _gid=GA1.2.1500670035.1522488515'
            }

            # 发送ajax请求，获取下一页数据
            data_lists = self.get_data(self.ajax_url,params=params, headers=headers)
            data_list, max_time = self.parse_ajax_data(data_lists)
            # 保存文件
            self.save_data(data_list)
            # 判断下一页是否有数据
            if len(data_list) is 0:
                break


def test02():
    """爬取非结构数据的案例html中循环标签中的内容"""
    Neihan().run()


def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

