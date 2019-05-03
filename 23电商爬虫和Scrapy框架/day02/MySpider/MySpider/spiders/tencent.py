# -*- coding: utf-8 -*-
import scrapy

from MySpider.items import MyspiderItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')

        for node in node_list:
            item = MyspiderItem()
            # extract用来序列化字符串
            item['name'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['detail_url'] = 'https://hr.tencent.com/' + node.xpath('./td[1]/a/@href').extract()[0]
            # extract_first()默认提取第一条，如果未提取到，给默认值，不会报异常
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract()[0]
            item['address'] = node.xpath('./td[4]/text()').extract()[0]
            item['pub_date'] = node.xpath('./td[5]/text()').extract()[0]

            # 返回item给引擎，return item的话下面就不会执行了
            yield item



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
