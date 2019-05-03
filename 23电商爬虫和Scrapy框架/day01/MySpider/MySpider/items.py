# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):

    # define the fields for your item here like:

    # 建模存储名字，标题，简介
    name = scrapy.Field()
    title = scrapy.Field()
    desc = scrapy.Field()
