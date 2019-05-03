# -*- coding: utf-8 -*-
import time

import scrapy

from MySpiders.items import AqiItem


class AqiSpider(scrapy.Spider):
    name = 'aqi'

    # ----3 注销允许的域名和起始的url
    # allowed_domains = ['www.aqistudy.cn']
    # host = 'https://www.aqistudy.cn/historydata/'
    # start_urls = [host]

    # ----4 编写__init__()动态获取允许的域名
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop('domain', '')
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(AqiSpider, self).__init__(*args, **kwargs)

        # ----5 编写redis_key
    redis_key = 'aqi'

    # 解析起始url对应的响应d
    def parse(self, response):
        #获取城市url列表
        url_list = response.xpath('//div[@class="bottom"]/ul/div[2]/li/a/@href').extract()

        # 遍历列表
        for url in url_list[45:48]:
            city_url = 'https://www.aqistudy.cn/historydata/' + url
            # 发起对城市详情页面的请求
            yield scrapy.Request(city_url, callback=self.parse_month)

    # 解析详情页面请求对应的响应
    def parse_month(self, response):
        # 获取每月详情url列表
        url_list = response.xpath('//ul[@class="unstyled1"]/li/a/@href').extract()
        # 遍历url列表中的部分
        for url in url_list[30:35]:
            month_url = 'https://www.aqistudy.cn/historydata/' + url
            # print month_url,'**************'
            # 发起详情页面请求
            yield scrapy.Request(month_url, callback=self.parse_day)

    # 在详情页面解析数据
    def parse_day(self, response):
        # print response.url,'######'
        # 获取所有的数据节点
        node_list = response.xpath('//tr')

        city = response.xpath('//div[@class="panel-heading"]/h3/text()').extract_first().split('2')[0]
        # 遍历数据节点列表
        for node in node_list:
            # 创建存储数据的item容器
            item = AqiItem()

            # 先填写一些固定参数
            item['city'] = city
            item['url'] = response.url
            item['timestamp'] = time.time()

            # 数据
            item['date'] = node.xpath('./td[1]/text()').extract_first()
            item['AQI'] = node.xpath('./td[2]/text()').extract_first()
            item['LEVEL'] = node.xpath('./td[3]/span/text()').extract_first()
            item['PM2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['PM10'] = node.xpath('./td[5]/text()').extract_first()
            item['SO2'] = node.xpath('./td[6]/text()').extract_first()
            item['CO'] = node.xpath('./td[7]/text()').extract_first()
            item['NO2'] = node.xpath('./td[8]/text()').extract_first()
            item['O3'] = node.xpath('./td[9]/text()').extract_first()

            # for k,v in item.items():
            #     print k,v
            # print '##########################'

            # 将数据返回给引擎
            yield item

