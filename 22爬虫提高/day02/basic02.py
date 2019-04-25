import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}

"""
    Xpath是一门快速查找html,xml信息的语言
    安装第三方lxml库，是一款高性能的python html/xml解析器
"""


def test02():
    """使用lxml和xpath爬取贴吧"""

    class Baidu(object):
        """爬取旅游吧贴吧的帖子详情中的图片"""

        def __init__(self, name):
            self.url = 'http://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
            # 使用较老版本的请求头，该浏览器不支持js,
            # 不然获取的页面中部分html会被注释掉，这样xpath就不会获取到自己想要的元素
            self.headers = {
                'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0) '
            }
            self.file = open('baidu.html', 'wb')

        def get_data(self, url):
            resp = requests.get(url=url, headers=self.headers)
            return resp.content

        def parse_list_page(self, data):
            # 获取html对象
            html = etree.HTML(data)
            # 提取数据
            node_list = html.xpath('//*[@id="thread_list"]/li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')

            data_list = []
            for node in node_list:
                # 三元表达式 a = x if xxx else None
                temp = {}
                temp['url'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]
                temp['content'] = node.xpath('./text()')[0] if len(node.xpath('./text()')) > 0 else None
                data_list.append(temp)

            next_url = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')[0]
            next_url = 'http://tieba.baidu.com' + next_url

            return data_list, next_url

        def parse_detail_data(self, result_list):
            """提取详情页面的图片数据"""
            # 获取html对象
            html = etree.HTML(result_list)
            # 提取数据
            image_list = html.xpath("//cc/div[contains(@class,'d_post')]/img[@class='BDE_Image']/@src")

            return image_list

        def download(self, image_list):
            """创建文件夹保存 图片"""
            import os
            if not os.path.exists('images'):
                os.makedirs('images')

            for image_url in image_list:
                file_name = 'images' + os.sep + image_url.split('/')[-1]
                image_data = self.get_data(image_url)
                with open(file_name, 'wb') as f:
                    f.write(image_data)

        def run(self):
            next_url = self.url

            # while next_url:

            # 先爬取首页
            data = self.get_data(next_url)
            # 获取首页的数据和下一页链接
            data_list, next_url = self.parse_list_page(data)

            # 把每一页的帖子的标题和url获取
            for data in data_list:
                # 根据每个帖子的url进入详情页面
                url = data['url']
                # 获取详情页面的数据
                result_list = self.get_data(url)
                # 获取详情页面的图片url列表
                image_list = self.parse_detail_data(result_list)

                # 保存数据下载图片
                self.download(image_list)

    Baidu('旅游吧').run()


def test01():
    """lxml库的使用"""

    text = ''' 
            <div> 
                <ul> 
                    <li class="item-1"><a href="link1.html">first item</a></li> 
                    <li class="item-1"><a href="link2.html">second item</a></li> 
                    <li class="item-inactive"><a href="link3.html">third item</a></li> 
                    <li class="item-1"><a href="link4.html">fourth item</a></li> 
                    <li class="item-0"><a href="link5.html">fifth item</a> 
                    # 注意，此处缺少一个 </li> 闭合标签 
                </ul> 
            </div> 
        '''
    # 利用etrr.Html把html字符串转换为element对象
    html = etree.HTML(text)

    # element对象具有xpath方法用来获取指定的元素目标
    ele = html.xpath('//div/ul/li[1]/a')

    # /@href属性的值
    link = html.xpath('//div/ul/li[1]/a/@href')

    # /text()文本信息获取
    text = html.xpath('//div/ul/li[1]/a/text()')[0]
    print(ele)
    print(link)
    print(text)

    # 提取多条数据,返回的是一个列表
    print(html.xpath('//div/ul/li/a/@href'))    # ['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
    print(html.xpath('//div/ul/li/a/text()'))   # ['first item', 'second item', 'third item', 'fourth item', 'fifth item']

    data_list = html.xpath('//div/ul/li')


def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

