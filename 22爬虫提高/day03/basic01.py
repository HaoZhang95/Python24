import json
import threading
from queue import Queue

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def test03():

    class Qiushi(object):
        """
        获取糗事百科1-13页短暂数据和作者数据
        """

        def __init__(self):
            self.url = 'https://www.qiushibaike.com/hot/page/{}/'
            self.url_list = None
            self.headers = headers
            self.file = open('qiushi.json', 'w', encoding='utf8')

        def generate_url_list(self):
            """用来生成1-13页的url列表"""
            self.url_list = [self.url.format(i) for i in range(1, 14)]
            print(self.url_list)


        def get_data(self, url):
            resp = requests.get(url=url, headers=self.headers)
            return resp.content

        def parse_data(self, data):
            # 实例化etree对象
            html = etree.HTML(data)
            # 提取相应数据的节点列表
            node_list = html.xpath('//*[contains(@id,"qiushi_tag_")]')

            data_list = []
            for node in  node_list:
                temp = {}
                # strip去除多余隐藏的不可见的换行符
                try:
                    temp['username'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                    temp['link'] = 'https://www.qiushibaike.com' + node.xpath('./div[1]/a[2]/@href')[0]
                    temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon', '')
                    temp['age'] = node.xpath('./div[1]/div/text()')[0]
                except:
                    temp['username'] = '匿名用户'
                    temp['link'] = None
                    temp['gender'] = None
                    temp['age'] = None
                print(temp)
                data_list.append(temp)

            return data_list

        def save_data(self, data_list):
            for data in data_list:
                str_data = json.dumps(data, ensure_ascii=False) + ',\n'
                self.file.write(str_data)

        def __del__(self):
            self.file.close()

        def run(self):
            self.generate_url_list()

            # 循环多页
            # for url in self.url_list:
            #     data = self.get_data(url)
            #     data_list = self.parse_data(data)
            #     self.save_data(data_list)

            # 只获取第一页
            data = self.get_data(self.url_list[0])
            data_list = self.parse_data(data)
            self.save_data(data_list)

    Qiushi().run()


def test01():
    """queued队列的使用"""

    queue = Queue()

    # 队列中添加数据
    queue.put(1)

    print(queue.get())

    print(queue.full())

    print(queue.empty())

    # 关闭队列task_done一般配合join使用
    queue.task_done()

    # 阻塞主线程，让主线程等待*队列操作*执行完毕后再关闭
    queue.join()


def test02():
    """线程的使用"""
    thread = threading.Thread(target=test01)
    thread.start()

    # 设置进程守护：类似redis服务器启动后，命令行可以隐藏在后台关闭进行输入其他命令
    # 生产环境下如果遇到主线程意外的话，该线程会随着主线程的推出而推出
    thread.setDaemon(True)



def main():
    # test01()
    # test02()
    test03()


if __name__ == '__main__':
    main()

