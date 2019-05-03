# -*- coding: utf-8 -*-
import scrapy

from MySpider.items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    # 允许的域名必须和下面的start_url中的www后面的一样，不然可能获取不到
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 提取数据使用xpath
        # 如果请求不到数据，检查是不是robot.txt协议问题或者url问题，url的最后不能加/
        node_list = response.xpath("//div[@class='li_txt']")

        # 传统的方式
        # data_list = []
        # for node in node_list:
        #     temp = {}
        #
        #     # 使用xpath后面的extract方法序列化字符串，不然返回：
        #     # {'name': [<Selector xpath='./h3/text()' data='肖老师'>]}
        #     temp['name'] = node.xpath('./h3/text()').extract()[0]
        #     temp['title'] = node.xpath('./h4/text()').extract()[0]
        #     temp['desc'] = node.xpath('./p/text()').extract()[0]
        #     data_list.append(temp)
        #
        # # 即使没有print，但是return的data返回给了引擎，引擎在命令行自动的就会打印处理啊data_list
        # return data_list

        # 使用items中的模型,temp不再等于一个{}
        for node in node_list:
            temp = MyspiderItem()
            # 前往不能使用temp.name，这样不会输出数据的！！！
            temp['name'] = node.xpath('./h3/text()').extract()[0]
            temp['title'] = node.xpath('./h4/text()').extract()[0]
            temp['desc'] = node.xpath('./p/text()').extract()[0]

            # yield生成器，当有列表或者详情页面的时候，需要再次发送请求下载内容，return的话该方法就直接完毕
            # yield的话下次有数据的话会从yeild的地方重新for循环执行，不会中断
            # 传统的方法是while true根据内置调用self.get_data()
            # 直接return的话，直接就给了引擎，就不能根据这个temp获取详情信息了
            yield temp
