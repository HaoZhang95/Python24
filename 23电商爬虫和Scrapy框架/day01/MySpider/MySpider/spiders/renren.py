# -*- coding: utf-8 -*-
import scrapy

class RenrenSpider(scrapy.Spider):

    # 爬虫的名字(scrapy crawl 的时候会用到)
    name = 'renren'
    # 允许的域名
    allowed_domains = ['renren.com']
    # 开始的url
    start_urls = ['http://renren.com/']

    def parse(self, response):
        # 解析相应，提取数据
        # print(response.body)

        with open('renren.html', 'wb') as f:
            f.write(response.body)

        pass
