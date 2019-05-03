# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

from MySpiders.items import ZhiyoujiItem


class ZhiyoujiSpider(RedisCrawlSpider):
    name = 'zhiyouji'
    # 查看允许的域
    allowed_domains = ['jobui.com']
    # 起始url
    # start_urls = ['http://www.jobui.com/cmp?area=%E5%85%A8%E5%9B%BD&keyword=']
    redis_key = 'zhiyou'

    rules = (
        # 职友集列表页的提取规则 cmp\?area=%E5%85%A8%E5%9B%BD&n=\d+#listInter
        Rule(LinkExtractor(allow=r'cmp\?area=%E5%85%A8%E5%9B%BD&n=\d+#listInter'), follow=True),
        # 公司详情页的提取规则,需要使用结尾判断,不然页面中存在123123/review的链接
        Rule(LinkExtractor(allow=r'company/\d+/$'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        # 数据源、采集时间、企业名称、浏览次数、口号、公司性质、行业分类、企业简介、好评度、薪资、融资信息、地址信息、联系方式

        item = ZhiyoujiItem()
        # 数据源和采集时间/浏览次数
        item['data_source'] = response.url
        item['time_stamp'] = time.time()
        item['company_name'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first()
        try:
            item['browse'] = response.xpath('//div[@class="grade cfix sbox"]/div/text()').extract_first().split('人')[0].strip()
        except Exception as e:
            item['browse'] = None
        # 公司口号、公司性质、行业分类
        item['slogan'] = response.xpath('//p[@class="fs16 gray9 sbox company-short-intro"]/text()').extract_first()
        item['industry'] = response.xpath('//dl[@class="j-edit hasVist dlli mb10"]/dd[1]/text()').extract_first()
        item['category'] = response.xpath('//dd[@class="comInd"]/a/text()').extract()
        # 企业简介、好评度、薪资
        # 企业简介有多段内容，是多个p标签组合的desc，不需要for只需要''jpin一个列表，快速把列表中的元素使用字符串拼接， 使用字符串拼接,strip去除的是两端的空格，如果想要去除\r\n，\xa0的话需要replace
        item['desc'] = ''.join(response.xpath('//*[@id="textShowMore"]/text()').extract()).strip()
        item['praise'] = response.xpath("//div[@class='swf-contA']/div[@class='swf-info']/h3/text()").extract_first()
        item['salary'] = response.xpath("//div[@class='swf-contB']/div[@class='swf-info']/h3/text()").extract_first()
        # 获取融资信息的列表
        node_list = response.xpath('//div[@class="jk-matter jk-box fs16"]/ul[@class="col-informlist"]/li').extract()
        data_list = []
        for node in node_list:
            temp = {}
            temp['time'] = node.xpath('./span[1]/text()').extract_first()
            temp['status'] = node.xpath('./h3/text()').extract_first()
            temp['sum'] = node.xpath('./span[2]/text()').extract_first()
            temp['investor'] = node.xpath('./span[3]/text()').extract_first()
            data_list.append(temp)
        # 保存融资信息
        item['financing'] = data_list
        # 地址信息和联系方式
        item['address'] = response.xpath('//dl[@class="dlli fs16"]/dd[1]/text()').extract_first().strip()
        item['contact'] = response.xpath('//div[@class="j-shower1 dn"]/dd/text()').extract_first().strip()

        # 返回给引擎
        yield item
