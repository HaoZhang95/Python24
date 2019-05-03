# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    """
        使用formrequest进行post请求
    """

    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    # 实现post请求需要重写start_request方法,不重写的话，默认的start_requests方法使用的GET请求
    def start_requests(self):
        url = self.start_urls[0]
        post_data = {
            'email': '18949599846',
            'password':'shengjun'
        }

        # 发送post
        yield scrapy.FormRequest(url=url, formdata=post_data, callback=self.parse)

    def parse(self, response):
        # 获取post请求的响应数据
        with open('renren.html','wb') as f:
            f.write(response.body)
