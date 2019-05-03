# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from MySpider.items import MyspiderItem, MyspiderItemPlus

"""
    spider返回items模型后，引擎把items模型给pipeline管道进行处理的时候，
    因为在settings中有可能项目会用到多个管道，如果不做处理的话，那么items模型会被多个管道进行处理，会生成多个一样的.json文件
    所以在process_item的时候要判断item的类型，做不同的处理
"""

class MyspiderPipeline(object):
    """数据的管道，不要忘记在settings中解注释，否则默认的数据输出是命令行打印"""

    def open_spider(self, item):
        self.file = open('tencent.json', 'w', encoding='utf8')

    def process_item(self, item, spider):

        # 如果引擎给的是MyspiderItem类型的话，那么才保存写入
        if isinstance(item, MyspiderItem):
            dict_item = dict(item)
            str_item = json.dumps(dict_item, ensure_ascii=False) + ',\n'
            self.file.write(str_item)

        return item

    def close_spider(self, item):
        self.file.close()


class MyspiderPipelinePlus(object):
    """数据的管道，不要忘记在settings中解注释，否则默认的数据输出是命令行打印"""

    def open_spider(self, item):
        self.file = open('tencent2.json', 'w', encoding='utf8')

    def process_item(self, item, spider):
        if isinstance(item, MyspiderItemPlus):
            dict_item = dict(item)
            str_item = json.dumps(dict_item, ensure_ascii=False) + ',\n'
            self.file.write(str_item)

        return item

    def close_spider(self, item):
        self.file.close()
