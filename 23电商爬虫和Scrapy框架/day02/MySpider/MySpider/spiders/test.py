# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TestSpider(CrawlSpider):
    """
        CrawlSpider的创建命令： scrapy genspider -t crawl XXX XXX.com
        crawlspider的特点就是：自动提取网页中的符合自己定义规则的link，使用链接提取器**自动发送请求跟进**，适合整站爬取信息
        并且link会自动补全根url，不需要自己手动拼接url

        和scrapy.Spider类的区别：
        这个类不能重写父类的parse方法，crawlspider类在parse方法中实现了自身的逻辑，重写的话逻辑会直接raise error
        后者不能自动提取link链接
    """


    name = 'test'
    allowed_domains = ['test.com']
    start_urls = ['http://test.com/']

    rules = (
        # 根据不同的规则提取链接，并且发送请求跟进
        # allow 满足该正则的链接将会被提取
        # deny  满足该正则的链接不会被提取
        # allow_domain  允许的域名
        # deny_domain   不允许的域名
        # restrict_xpaths   规定的xpath节点
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
