# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    """职位列表的模型"""
    name = scrapy.Field()
    detail_url = scrapy.Field()
    category = scrapy.Field()
    number = scrapy.Field()
    address = scrapy.Field()
    pub_date = scrapy.Field()


class MyspiderItemPlus(scrapy.Item):
    """职位详情页面的模型"""
    name = scrapy.Field()
    detail_url = scrapy.Field()
    category = scrapy.Field()
    number = scrapy.Field()
    address = scrapy.Field()
    pub_date = scrapy.Field()
    duty = scrapy.Field()
    require = scrapy.Field()
