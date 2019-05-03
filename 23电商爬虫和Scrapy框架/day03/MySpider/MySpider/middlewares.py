# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import base64
import random

from scrapy import signals

from MySpider import settings


class DoubanRandomUserAgentMiddleware(object):
    """自定义中间件类，动态添加请求头"""

    def process_request(self, request, spider):
        """process_request方法中重新赋值请求头中的user-agent"""

        # 获取请求头列表
        us = settings['USER_AGENT']
        # random中的choice方法随机从列表中取出一个
        us = random.choice(us)

        # 更新请求头
        request.headers['User-Agent'] = us


# 自定义ip代理池
class DoubanRandomProxyMiddleware(object):
    def process_request(self, request, spider):
        # 获取请求头
        proxy = settings['PYTHON_PROXY']
        ps = random.choice(proxy)
        # 设置请求头
        # 如果使用代理ip，需要指定的请求参数为meta
        request.meta['proxy'] = ps['ip_port']

        # 付费代理的格式, 可选项，如若不想让headers中打印出账号密码的话
        # proxy = settings['PYTHON_PROXY']
        # ps = random.choice(proxy)
        # # 对账号密码进行编码
        # b64_user_pwd = base64.b64encode(ps['user_passwd'].encode())
        # # 设置账号密码，Basic后面必须有空格
        # request.headers['Proxy-Authorization'] = 'Basic ' + b64_user_pwd.decode()
        # request.meta['proxy'] = ps['ip_port']



class MyspiderSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class MyspiderDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
