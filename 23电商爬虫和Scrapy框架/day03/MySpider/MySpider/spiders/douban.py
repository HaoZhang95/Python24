# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from MySpider.items import DoubanItem


class DoubanSpider(CrawlSpider):
    name = 'douban'
    allowed_domains = ['douban.com']
    # 修改起始的url
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        # 提取下一页的url
        # start=\d+&filter=
        Rule(LinkExtractor(allow=r'start=\d+&filter='), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        #  如果出现403的话，那么需要添加user-agent在settings中
        # print(response.url)

        node_list = response.xpath("//div[@class='info']")
        # print(len(node_list))
        # 遍历节点列表
        for node in node_list:
            item = DoubanItem()
            item['name'] = node.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['score'] = node.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['info'] = node.xpath('./div[2]/p[1]/text()').extract_first().replace('\xa0','').strip()
            item['desc'] = node.xpath('./div[2]/p[2]/span/text()').extract_first()

            # print(item)
            yield item

