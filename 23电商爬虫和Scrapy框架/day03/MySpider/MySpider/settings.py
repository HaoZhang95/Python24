# -*- coding: utf-8 -*-

# Scrapy settings for MySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MySpider'

SPIDER_MODULES = ['MySpider.spiders']
NEWSPIDER_MODULE = 'MySpider.spiders'

# 创建自定义文件存储的地方, IMAGES_STORE名字需要固定，因为imagespipeline中用到
IMAGES_STORE = 'C:\Users\HaoZhang\Documents\PythonAndMachineLearning\23电商爬虫和Scrapy框架\day03\MySpider\MySpider\images'

# 默认是开启log的
LOG_ENABLED = True
# 创建log信息存放的位置
lOG_FILE = 'douyu.log'
LOG_LEVEL = 'INFO'

# 下载超时,超时的话就会跳过该下载，或者切换下一个代理ip
DOWNLOAD_TIMEOUT = 3



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MySpider (+http://www.yourdomain.com)'
# 下面还有一个地方指定user-agent
# 自定义请求池
USER_AGENT = [
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; MathPlayer 2.0; .NET CLR 1.1.4322) ",
   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; {FF0C8E09-3C86-44CB-834A-B8CEEC80A1D7}; iOpus-I-M) ",
   "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; i-Nav 3.0.1.0F; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
   "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040616 ",
   "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; rv:1.5) Gecko/20031007 ",
]

PYTHON_PROXY = [
   # 付费代理的格式
   # {'ip_port':'121.58.17.52:80', 'user_passwd':"账号:密码"},

   {'ip_port':'121.58.17.52:80'},
   {'ip_port':'190.57.147.138:3128'},
   {'ip_port':'218.26.217.77:3128'},
   {'ip_port':'221.4.133.67:53281'},
   {'ip_port':'180.104.62.188:9000'},
   {'ip_port':'60.168.206.90:18118'},
   {'ip_port':'114.99.31.218:18118'}
]


# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 默认是接受cookie响应的，一般是不建议使用cookie信息，容易暴露，scrapy建议false
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   # 添加自己的user-agent
   # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
   'Accept-Language': 'en',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
   'MySpider.middlewares.DoubanRandomUserAgentMiddleware': 543,
   'MySpider.middlewares.DoubanRandomProxyMiddleware': 544,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html

# 、、

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'MySpider.pipelines.SunPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
