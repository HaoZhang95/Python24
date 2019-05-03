# -*- coding: utf-8 -*-
import scrapy


class RenrenproSpider(scrapy.Spider):
    """不重写start_request的进行post请求"""

    name = 'renrenpro'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']


    def parse(self, response):
        post_data = {
            'email': '18949599846',
            'password':'shengjun'
        }

        # 发送post请求
        # from_response()方法会自动查看请求的url中是不是有表单，有的话会根据post_data自动填充表单
        yield scrapy.FormRequest.from_response(
            response=response,
            formdata=post_data,
            callback=self.parse_login
        )


    def parse_login(self, response):
        # 获取post请求的响应数据
        with open('renren2.html','wb') as f:
            f.write(response.body)