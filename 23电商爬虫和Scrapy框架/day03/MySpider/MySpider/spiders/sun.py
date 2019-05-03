# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from MySpider.items import SunItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    rules = (
        # 提取列表页的url(第一页的url, 第二页的url...)： php/question/questionType
        Rule(LinkExtractor(allow=r'php/question/questionType'), follow=True),
        # 提取详情页的url：html/question/\d+/\d+.shtml
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )


    def parse_item(self, response):
        """列表页不需要callback,因为需求提取的内容列表页并没有，但是需要follow跟进进行下一页列表的获取"""
        # 编号，详情url，标题，投诉内容

        # 返回符合规则的url
        # print(response.url)

        item = SunItem()
        item['number'] = response.xpath('//tr/td[2]/span[2]/text()').extract_first().split(':')[-1].strip()
        item['detail_url'] = response.url
        item['title'] = response.xpath('/html/head/title/text()').extract_first().split('_')[0]
        item['content'] = response.xpath('/html/head/meta[@name="description"]/@content').extract_first()
        # print(item)
        yield item
