# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class MyspiderPipeline(object):
    """pipeline文件手动控制数据的输出,需要在settings中设置取消注释ITEM_PIPELINES pipeline管道"""

    # 实现open_spider和close_spider方法
    # 类似于init方法
    def open_spider(self, item):
        self.file = open('itcast2.json', 'w', encoding='utf8')

    # 类似于del方法
    def close_spider(self, item):
        self.file.close()

    # item就是返回给引擎的模型对象
    def process_item(self, item, spider):
        # 把自己的对象模型转换为dict
        dict_item = dict(item)
        # dunps成str用于写入
        str_data = json.dumps(dict_item, ensure_ascii=False) + ',\n'
        self.file.write(str_data)
        # return给的是引擎
        return item
