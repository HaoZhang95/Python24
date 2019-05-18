import pymongo

client = pymongo.MongoClient("mongodb+srv://Hao:123456Hao@python24-urhj5.mongodb.net/test?retryWrites=true")

db = client.get_database('Python')

collection = db.get_collection('Test')

def test01():
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
    4- 引擎把收到的数据发送给spider进行数据解析
    5- 解析好的数据返回给scrapy引擎
    6- 引擎把解析好的数据发送给item pipeline进行数据持久化

    注意：引擎链接各个组件之间都有中间件的存在，类似于请求钩子，在请求或者响应的时候进行对数据额外操作
    比如：scheduler middleware, downloader middleware, spider middleware

    """

def main():
    test01()


if __name__ == '__main__':
    main()

