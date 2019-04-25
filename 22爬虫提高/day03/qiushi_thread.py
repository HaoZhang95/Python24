#coding:utf-8
import requests
from lxml import etree
import json
from queue import Queue
import threading

class Qiushi(object):
    """
        使用queue的存取形式取代了return
        启动的时候启动三个线程，每个线程分别进行while true的向队列中放url, resp_data, data
        第一个线程不停的存url队列，第二个线程不停的区url队列进行生产resp_data，
        第三个线程不停的从第二个队列中区resp_data进行save
        总结就是生产消费模式

    """

    def __init__(self):
        self.url = 'https://www.qiushibaike.com/hot/page/{}/'
        self.url_list = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.file = open('qiushi.json','w', encoding='utf8')
        # 创建三个队列对象
        self.url_queue = Queue()
        self.response_queue = Queue()
        self.data_queue = Queue()

    def generate_url_list(self):
        for i in range(1, 14):
            self.url_queue.put(self.url.format(i))

    def get_data(self):
        while True:
            # 获取队列中的url
            url = self.url_queue.get()
            print('正在获取{}对应的响应'.format(url))
            response = requests.get(url, headers=self.headers)
            if response.status_code == 503:
                self.url_queue.put(url)
            else:
                # 往响应队列中添加数据
                self.response_queue.put(response.content)

            # 每task_down一次就会从queue队列中移除一个
            # url_queue.join()就会判断队列中是不是为0，为0的话才会去执行主线程的其他任务
            self.url_queue.task_done()

    def parse_data(self):
        while True:
            data = self.response_queue.get()
            print('正在解析数据')
            # 创建element对象
            html = etree.HTML(data)

            # 定位出帖子节点列表
            node_list = html.xpath('//*[contains(@id,"qiushi_tag_")]')
            # print(len(node_list))

            # 构建存放返回数据的列表
            data_list = []

            # 遍历节点列表，从没一个节点中抽取数据
            for node in node_list:
                temp = dict()
                try:
                    temp['user'] = node.xpath('./div[1]/a[2]/h2/text()')[0].strip()
                    temp['link'] = 'https://www.qiushibaike.com' + node.xpath('./div[1]/a[2]/@href')[0]
                    temp['age'] = node.xpath('./div[1]/div/text()')[0]
                    temp['gender'] = node.xpath('./div[1]/div/@class')[0].split(' ')[-1].replace('Icon', '')
                except:
                    temp['user'] = '匿名用户'
                    temp['link'] = None
                    temp['age'] = None
                    temp['gender'] = None
                # 将数据加入数据列表
                data_list.append(temp)

            self.data_queue.put(data_list)
            self.response_queue.task_done()

    def save_data(self):
        while True:
            data_list = self.data_queue.get()
            print('正在保存数据')
            for data in data_list:
                print(data)
                str_data = json.dumps(data, ensure_ascii=False) + ',\n'
                self.file.write(str_data)
            self.data_queue.task_done()

    def __del__(self):
        self.file.close()

    def run(self):
        # 创建存储线程的列表
        thread_list = []
        # 创建生成url列表的线程
        t_generate_url = threading.Thread(target=self.generate_url_list)
        thread_list.append(t_generate_url)

        # 创建获取数据的线程
        for i in range(3):
            t = threading.Thread(target=self.get_data)
            thread_list.append(t)

        # 创建解析数据的线程
        for i in range(3):
            t = threading.Thread(target=self.parse_data)
            thread_list.append(t)

        t_save_data = threading.Thread(target=self.save_data)
        thread_list.append(t_save_data)

        # 开启线程
        for t in thread_list:
            # 守护线程，主线程结束后结束
            t.setDaemon(True)
            t.start()
        # 关闭队列
        for q in [self.url_queue, self.response_queue, self.data_queue]:
            q.join()


if __name__ == '__main__':
    qiushi = Qiushi()
    qiushi.run()