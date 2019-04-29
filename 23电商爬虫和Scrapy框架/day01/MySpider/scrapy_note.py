"""
    Scrapy框架主要的组件有：
        scheduler调度器：封装url列表，压入队列
        scrapy engine引擎：连接各个组件的中转中心
        downloader下载器：类似于get_data方法，接受url获取数据的请求,接受请求，返回响应
        spiders：类似于parse_data解析downloader的数据
        item pipeline: 用于save_data，可以以数据模型的方式保存到数据库

    1- scheduler调度器接受不同的url，传递给scrapy引擎
    2- 引擎发送url请求给downloader进行下载数据
    3- downloader下载好的数据返回给scrapy引擎
    4- 引擎把收到的数据发送给spider进行数据解析,此时scrapy有两个选择1-解析数据返回给引擎  2= 解析中有url，再次跟进的话把url返回给调度器再次循环
    5- 解析好的数据返回给scrapy引擎
    6- 引擎把解析好的数据发送给item pipeline进行数据持久化

    注意：引擎链接各个组件之间都有中间件的存在，类似于请求钩子，在请求或者响应的时候进行对数据额外操作
    比如：scheduler middleware, downloader middleware, spider middleware
"""

"""
    scrapy startproject 项目名称
    scrapy genspider renren 创建一个叫做renren的爬虫 (需要cd到spider的目录下创建spider)
    scrapy crawl renren 运行renren这个爬虫获取数据
    scrapy crawl renren --nolog 不显示多余的log信息
    scrapy crawl renren -o itcast.json 根据items中的模型输出到json文件
    scrapy crawl renren -o itcast.csv 输出csv文件或者xml
"""

"""
    项目结构目录:
    items           --> 数据建模
    pipelines       --> 决定数据的后续操作，如果写入数据库的话那么就需要用到items建模
    settings        --> scrapy项目的配置文件
    scrapy.cfg      --> 远程部署的配置文件
"""

