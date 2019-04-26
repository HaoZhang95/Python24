import json
import time

import requests
from PIL import Image
from pytesseract import pytesseract
from selenium import webdriver

"""
    selenium和xpath的使用区别
    selenium使用不需要自己写headers，只需要导入webdriver.Chrome().get(url)就会打开浏览器，使用find_xxx_by_xpath
    写入自己的xpath语句即可
    
    传统的xpath使用，需要导入etree.Html(url),然后写入自己的html.xpath(‘xxx’)
"""


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def test01():
    """斗鱼平台获取直播房间和的信息
    1、爬取房间名称、类型、房主、关注人数、封面信息等
    2、使用selenium进行爬取
    """
    class Douyu(object):

        def __init__(self):
            self.url = 'https://www.douyu.com/directory/all'
            # 实例化浏览器对象
            self.driver = webdriver.Chrome()
            # 创建文件
            self.file = open('douyu.json','w')

        # 解析数据
        def parse_data(self):
            # 提取房间列表，必须使用elements
            node_list = self.driver.find_elements_by_xpath('//*[@id="listAll"]/section[2]/div[2]/ul/li')
            # 测试节点列表
            # print(len(node_list))
            # 定义存储数据的容器
            data_list = []
            # 遍历节点列表
            for node in node_list:
                temp = {}
                # 提取房间的标题/房间类型/房间主人/关注人数/封面
                temp['title'] = node.find_element_by_xpath('./div/div/h3').text
                temp['category'] = node.find_element_by_xpath('./div/div/span').text
                temp['owner'] = node.find_element_by_xpath('./div/p/span[1]').text
                temp['num'] = node.find_element_by_xpath('./div/p/span[2]').text
                temp['cover'] = node.find_element_by_xpath('./span/img').get_attribute('data-original')
                # temp['link'] = node.get_attribute('href')
                data_list.append(temp)
                # print(temp)
            # 返回数据
            return data_list

        # 保存数据
        def save_data(self,data_list):
            # 遍历列表数据,因为里面存储的是字典类型
            for data in data_list:
                str_data = json.dumps(data,ensure_ascii=False) + ',\n'
                self.file.write(str_data)


        def __del__(self):
            # 关闭浏览器对象
            self.driver.close()
            self.file.close()

        def run(self):
            # 构造url
            # 构造webdriver浏览器对象
            # 发送请求
            self.driver.get(self.url)
            while True:
                # 解析数据,返回数据列表
                data_list = self.parse_data()
                self.save_data(data_list)
                # 提取下一页链接,模拟点击
                try:
                    ele_next_url = self.driver.find_element_by_xpath('//*[@class="shark-pager-next"]')
                    ele_next_url.click()
                    time.sleep(3)
                except:
                    break

            # 保存数据
    Douyu().run()


def test02():
    from PIL import Image
    import pytesseract

    """谷歌图片识别的包：tesseract"""

    # 使用pil加载一张图片到内存中，返回图片对象
    img = Image.open('test.jpg')

    # 调用tesseract进行识别，返回一个data
    data = pytesseract.image_to_string(img)

    # 输出结果
    print(data)


def test03():
    """图片识别验证码进行豆瓣登陆"""
    # 创建浏览器对象
    driver = webdriver.Chrome()
    # 发送请求
    driver.get('https://accounts.douban.com/login')

    # 定位元素位置，账号
    ele_email = driver.find_element_by_id('email')
    # 把账号发送给表单
    ele_email.send_keys('371673381@qq.com')

    # 定位元素，密码
    ele_pswd = driver.find_element_by_id('password')
    # 把密码发送给表单
    ele_pswd.send_keys('123456shengjun')


    # # 1、手动输入获取图片验证码
    # 定位图片验证码所在的元素位置
    # ele_captcha = driver.find_element_by_id('captcha_field')
    # data = input('请输入图片验证码：')
    # ele_captcha.send_keys(data)

    # 2 使用ocr系统识别图片验证码
    ele_image_captcha = driver.find_element_by_id('captcha_image')
    image_url = ele_image_captcha.get_attribute('src')
    print(image_url)
    # 获取图片文件
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    }

    # 发送get请求，获取图片文件bytes类型
    # data = requests.get(image_url,headers=headers).content
    # 保存图片文件
    # with open('douban.jpg','wb') as f:
    #     f.write(data)
    # time.sleep(3)
    # 使用ocr系统
    img = Image.open('douban.jpg')
    image_str = pytesseract.image_to_string(img)
    print('-------',image_str,'-------')


    # 定位登录按钮
    ele_submit = driver.find_element_by_name('login')
    # 模拟点击
    ele_submit.click()


def main():
    # test01()
    # test02()
    test03()


if __name__ == '__main__':
    main()

