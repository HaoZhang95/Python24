# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdItem(scrapy.Item):
    # 书名，大分类，大分类页面url，小分类，小分类页面url，封面图片链接，详情页面url，作者，出版社，出版时间，价格
    name = scrapy.Field()
    big_category = scrapy.Field()
    big_category_url = scrapy.Field()
    small_category = scrapy.Field()
    small_category_url = scrapy.Field()
    cover_url = scrapy.Field()
    detail_url = scrapy.Field()
    author = scrapy.Field()
    publisher = scrapy.Field()
    pub_date = scrapy.Field()
    price = scrapy.Field()
