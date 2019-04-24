"""
    爬虫的用途:12306抢票，短信轰炸，数据获取
    分类：通用爬虫：是搜索引擎抓取系统的重要部分，主要是把互联网上的页面下载到本地作为一个镜像备份
        聚焦爬虫：对特定需求进行数据获取，会对页面的内容进行筛选，保证只抓取和需求相关的网页信息

    Http：端口号80
    Https： 端口号443

    使用第三方的requests进行请求：支持python2和3，在urllib中2和3的语法有些不一样
"""
import requests

kw = {'wd': '长城'}

# headers伪装成一个浏览器进行的请求
# 不加这个的话，网页会识别出请求来自一个python而不是浏览器的正常请求
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

response = requests.get("https://www.baidu.com/s?", params=kw, headers=headers)

# 返回的是unicode格式解码的str的数据
print(response.text)

# 返回字节流的二进制数据，并根据unicode进行解码
print(response.content)
print(response.content.decode())

# 返回完整的url地址
print(response.url)

# 返回字符编码
print(response.encoding)

# 返回状态吗
print(response.status_code)

# 保存响应结果
with open('baidu.html', 'wb') as f:
    f.write(response.content)

