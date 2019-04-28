# -*- coding: utf-8 -*-
import scrapy

from MySpider.items import MyspiderItemPlus


class TencentSpider(scrapy.Spider):
    name = 'tencentplus'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for node in node_list:
            item = MyspiderItemPlus()
            # extract用来序列化字符串
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_url'] = 'https://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()默认提取第一条，如果未提取到，给默认值，不会报异常
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = node.xpath('./td[5]/text()').extract()[0]

            # 为了获取详情页面的数据，这里不直接yield item(直接获取的是详情页面)
            # 而是进行request请求，在callback中获取详情信息后哦再yield item
            # meta传入一个字典，传参
            yield scrapy.Request(
                url=item['detail_url'],
                callback=self.parse_detail,
                meta={'meta1': item}
            )

        # scrapy只能实现start_url的请求，具体的详细页面的获取比如分页需要自己实现
        next_url = 'https://hr.tencent.com/' + response.xpath('//*[@id="next"]/@href').extract_first()
        # 判断是否下一页
        if 'javascript:;' not in next_url:
            # 手动发送请求,回掉函数不要加()
            """
                上面node_list获取第一页数据后，手动获取下一页的地址
                然后进行下一页请求，回掉函数是自己
                如果使用return的话就不会循环获取下一页数据了
            """
            yield scrapy.Request(
                url=next_url,
                callback=self.parse
            )


    """
        spider的作用就是解析数据，然后返回items给引擎
        之前的是直接返回items是列表页面的item，这次是在返回items之前多加了一个request获取detail_url页面
        在回掉函数中往items中多加了两个字段duty, require然后再返回
        总之就是MyspiderItemPlus模型中在第一个请求中没有获取模型中全部的数据需要再次请求另一个url完善模型再返回
    """


    def parse_detail(self, response):
        # 获取parse返回的item信息
        item = response.meta['meta1']
        # 提取详情页面的岗位职责和岗位要求信息
        item['duty'] = response.xpath('//tr[3]/td/ul/li/text()').extract()[0]
        item['require'] = response.xpath('//tr[4]/td/ul/li/text()').extract()[0]
        # 返回item给引擎
        yield item
