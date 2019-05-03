

# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
# 爬虫文件存放位置
SPIDER_MODULES = ['JD.spiders']
NEWSPIDER_MODULE = 'JD.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 启用scrapy-redis重复过滤器，把scrapy的去重取消
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 启用scrapy-redis的调度器，把scrapy中的调度器取消
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# scrapy-redis断点续爬
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

# 配置redis数据库的链接
REDIS_URL = 'redis://127.0.0.1:6379'





# # -*- coding: utf-8 -*-
#
# # Scrapy settings for JD project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     https://doc.scrapy.org/en/latest/topics/settings.html
# #     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# #     https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'JD'
#
# SPIDER_MODULES = ['JD.spiders']
# NEWSPIDER_MODULE = 'JD.spiders'
#
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'JD (+http://www.yourdomain.com)'
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True
#
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
#
# # Configure a delay for requests for the same website (default: 0)
# # See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# #DOWNLOAD_DELAY = 3
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
#
# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False
#
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
#
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #}
#
# # Enable or disable spider middlewares
# # See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    'JD.middlewares.JdSpiderMiddleware': 543,
# #}
#
# # Enable or disable downloader middlewares
# # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    'JD.middlewares.JdDownloaderMiddleware': 543,
# #}
#
# # Enable or disable extensions
# # See https://doc.scrapy.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# #}
#
# # Configure item pipelines
# # See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    'JD.pipelines.JdPipeline': 300,
# #}
#
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
#
# # Enable and configure HTTP caching (disabled by default)
# # See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = 'httpcache'
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
