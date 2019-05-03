# -*- coding: utf-8 -*-
import json

import scrapy

from MySpider.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    """根据斗鱼的api返回的json，从json中获取主播的头像"""

    name = 'douyu'
    allowed_domains = ['douyucdn.cn']
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset=']

    def parse(self, response):
        # 如果获取纯json的api返回的话，如果loads resp.body出错的话试试resp.text
        data_list = json.loads(response.body)['data']
        for data in data_list:
            item = DouyuItem()
            item['nick_name'] = data['nickname']
            item['image_link'] = data['vertical_src']
            item['uid'] = data['room_id']
            item['city'] = data['anchor_city']
            print(item)
            # yield item

