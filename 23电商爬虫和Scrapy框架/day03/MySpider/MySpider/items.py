# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # 名字，uid, 图片链接， 所在城市，图片保存路径
    nick_name = scrapy.Field()
    uid = scrapy.Field()
    image_link = scrapy.Field()
    city = scrapy.Field()
    image_path = scrapy.Field()


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # 投诉编号、投诉详情url、投诉标题，投诉内容
    number = scrapy.Field()
    detail_url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    score = scrapy.Field()
    info = scrapy.Field()
    desc = scrapy.Field()


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
