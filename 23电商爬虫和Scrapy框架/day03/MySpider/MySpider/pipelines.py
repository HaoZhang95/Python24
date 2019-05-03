# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import pymongo
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from MySpider import settings
from MySpider.items import DoubanItem, DouyuItem


class SunPipeline(object):
    """把投诉的内容导入到mongodb数据库,settings中配置数据库"""

    def open_spider(self, item):

        # 客户端对象
        self.client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

        # 数据库对象
        self.db = self.client.get_database('Python24')

        # 集合对象
        self.collection = self.db.get_collection('Douban')



    def close_spider(self, item):
        self.client.close()


    def process_item(self, item, spider):
        if isinstance(item, DouyuItem):
            self.collection.insert_one(dict(item))

        return item


class DouyuPipeline(ImagesPipeline):
    """继承自ImagesPipeline专门用来下载图片的pipeline"""
    # 管道下载斗鱼主播的头像图片

    image_store = settings['IMAGES_STORE']

    def get_media_requests(self, item, info):
        """发送图片获取请求"""
        yield scrapy.Request(
            url=item['image_link']
        )

    def item_completed(self, results, item, info):
        """图片下载完毕后，如果不重写下面的方法，那么保存的就是full/一堆数字.jpg"""


        # result输出的是图片的连接信息，true， checksum
        # 遍历results获取图片的路径，会自动生成一个full文件夹
        image_path = [ data['path'] for ok, data in results if ok]

        # 原始图片文件名 full/12435465.jpg
        old_name = self.image_store + os.sep + image_path[0]
        # 新的图片文件文件名
        new_name = self.image_store + os.sep + image_path[0].split(os.sep)[0] + os.sep + item['nick_name'] + '.jpg'
        # 修改图片文件, os.rename直接把x/y.jpg重命名为x/z.jpg
        os.rename(old_name,new_name)
        return item

