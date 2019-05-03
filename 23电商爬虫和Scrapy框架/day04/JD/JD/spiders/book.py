# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy_redis.spiders import RedisSpider

from JD.items import JdItem

"""
    有时候xpath写的对，但是层层获取不到得到none发生错误，需要判断none
    直接xpath获取的是一个selector对象，[<Selector xpath='./td[1]/a/text()' data='22989-腾讯云虚拟化高级研发工程师（深圳）'>] 技术类 2 深圳 2018-07-11
    通过extract()获取其中的数据，返回的是一个列表对象，extract_first返回列表中的第一个
"""

class BookSpider(RedisSpider):
    name = 'book'
    allowed_domains = ['jd.com', 'p.3.cn']
    # start_urls = ['https://book.jd.com/booksort.html']
    redis_key = 'book_url'

    def parse(self, response):
        # 读取列表页，大分类节点列表标题和每个大分类的url
        big_category_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt/a')

        # 遍历大分类列表获取小分类节点
        for big_category in big_category_list:
            # dd标签是在big_list上级目录的下一个节点sibling中
            big_category_name = big_category.xpath('./text()').extract_first()
            big_category_url = 'https:' + big_category.xpath('./@href').extract_first()

            # 当前大分类下的小分类列表
            small_category_list = big_category.xpath('../following-sibling::dd[1]/em/a')
            for small_category in small_category_list:
                # 获取小分类的链接

                small_category_name = small_category.xpath('./text()').extract_first()
                small_category_url = 'https:' + small_category.xpath('./@href').extract_first()

                temp = {}
                temp['big_category'] = big_category_name
                temp['big_category_url'] = big_category_url
                temp['small_category'] = small_category_name
                temp['small_category_url'] = small_category_url

                yield scrapy.Request(
                    url=temp['small_category_url'],
                    callback=self.parse_book_list,
                    # 把当前的temp当作参数使用meta进行传递
                    meta={'meta1': temp}
                )

    def parse_book_list(self, response):
        """解析图书小分类下面的书籍列表"""
        # 获取parse方法传递的meta数据，传递temo的作用是为了构建模型的时候传递oarse中获得的大小分类的name和url
        temp = response.meta['meta1']

        book_list = response.xpath('//*[@id="plist"]/ul/li/div')
        # 遍历图书列表
        for book in book_list:
            # 实例化item
            item = JdItem()
            # 书名信息、分类信息，出版社只有在鼠标滑过的时候才会显示
            item['name'] = book.xpath('./div[3]/a/em/text()').extract_first().strip()
            item['big_category'] = temp['big_category']
            item['big_category_url'] = temp['big_category_url']
            item['small_category'] = temp['small_category']
            item['small_category_url'] = temp['small_category_url']
            item['author'] = book.xpath('./div[@class="p-bookdetails"]/span[@class="p-bi-name"]/span[@class="author_type_1"]/a/text()').extract_first()
            item['publisher'] = book.xpath('./div[@class="p-bookdetails"]/span[2]/a/text()').extract_first()
            item['pub_date'] = book.xpath('./div[@class="p-bookdetails"]/span[3]/text()').extract_first().strip()

            try:
                item['cover_url'] = 'https:' + book.xpath('./div[1]/a/img/@src').extract_first()
            except:
                item['cover_url'] = None
            try:
                item['detail_url'] = 'https:' + book.xpath('./div[3]/a/@href').extract_first()
            except:
                item['detail_url'] = None


            # 获取价格的url，价格的保存并不在html中而是在jquery进行请求一个p.3.cn的接口，
            # 并且需要skuid等等参数，发现参数的值藏在html页面中，传入参数来获取当页价格的json list

            # https://p.3.cn/prices/mgets?skuIds=J_11757834%2CJ_10367073%2CJ_11711801%2CJ_12090377%2
            # CJ_10199768%2CJ_11711801%2CJ_12018031%2CJ_10019917%2CJ_11711801%2CJ_10162899%2CJ_110816
            # 95%2CJ_12114139%2CJ_12010088%2CJ_12161302%2CJ_11779454%2CJ_11939717%2CJ_12026957%2CJ_12
            # 184621%2CJ_12115244%2CJ_11930113%2CJ_10937943%2CJ_12192773%2CJ_12073030%2CJ_12098764%2CJ
            # _11138599%2CJ_11165561%2CJ_11920855%2CJ_11682924%2CJ_11682923%2CJ_11892139&pduid=1523432
            # 585886562677791

            # 获得skuid=11757834的价格链接，pduid是固定的
            # https://p.3.cn/prices/mgets?skuIds=J_11757834&pduid=1523432585886562677791
            skuid = book.xpath('./@data-sku').extract_first()

            pduid = '&pduid=1523432585886562677791'
            # print(item)
            # 再次发送请求，获取价格信息
            if skuid is not None:

                # 如果打印不出价格，是因为获取价格的时候惊醒了跨域请求的域名已经发生了改变
                url = 'https://p.3.cn/prices/mgets?skuIds=J_' + skuid + pduid
                yield scrapy.Request(
                    url=url,
                    callback=self.parse_price,
                    meta={'meta2':item}
                )

    def parse_price(self, response):
        """解析价格json"""
        item = response.meta['meta2']
        data = json.loads(response.body)
        item['price'] = data[0]['op']

        # 所有的模型字段填充完毕，进行yield
        yield item