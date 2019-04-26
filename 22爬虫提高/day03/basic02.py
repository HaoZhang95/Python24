import time

import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"
}


def test01():
    """36kr.com的内容是存放在script标签中"""

    class Kr36(object):

        def __init__(self):
            self.url = 'https://36kr.com/'
            self.headers = headers

        def get_data(self):
            resp = requests.get(url=self.url, headers=self.headers)

        def parse_data(self):
            pass

        def save_data(self):
            pass

        def run(self):
            data = self.get_data()
            parse_data = self.parse_data(data)

from selenium import webdriver

def test02():
    """
        selenium是一个测试工具，requests能做的这个测试工具也能做，类似于一个运行在浏览器上的测试工具
        这个测试工具模拟浏览器接受自己的指令来加载页面(模拟浏览器操作做)，甚至可以加载phantomJS这样无界面的浏览器

        phantomJS是无头浏览器，会把返回的js加载到内存中执行js处理
    """

    # 创建浏览器对象,需要单独pip install并且下载selenium对应的浏览器驱动
    driver = webdriver.Chrome()

    # 脚本使其打开一个网页
    driver.get("http://www.baidu.com")

    # 保存截图需要使用png格式
    # driver.save_screenshot('baidu.png')
    # driver.get_screenshot_as_png()

    # 通过xpath寻找元素
    # driver.find_element_by_xpath('//div/a')

    # 获取包含特定文本的标签，但是这个标签必须有link
    # driver.find_element_by_link_text('hao')   # 使用文本定位
    # driver.find_element_by_partial_link_text('hao')   # 使用部分文本定位

    # 通过id定位百度的搜索框
    ele_kw = driver.find_element_by_id('kw')

    # 元素定位后可以调用的方法get_attr, send_keys(), click(),submit, clear
    ele_kw.get_attribute()

    # 往制定的搜索框填写数据
    ele_kw.send_keys('python')

    # 定位搜索按钮
    ele_su = driver.find_element_by_id('su')
    # 模拟点击进行搜索
    ele_su.click()

    # 获取网页源码
    driver.page_source

    # 获取cookie信心
    print(driver.get_cookies())

    # 获取当前url
    print(driver.current_url)

    # 获取网页title
    print(driver.title)


    # 关闭浏览器
    # driver.close()


def test03():
    """使用selenium控制58窗口的切换"""

    url = 'http://sh.58.com/'
    # 构建浏览器对象
    dr = webdriver.Chrome()

    # 加载url对相应的响应
    dr.get(url)

    # 获取当前的url，窗口
    print(dr.current_url)
    print(dr.window_handles)
    # 模拟点击房屋出租

    el = dr.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/span[1]/a')
    el.click()

    # 点击房屋出租后，会打开新的标签页，需要传入新打开标签页的索引
    dr.switch_to.window(dr.window_handles[-1])
    print(dr.current_url)
    print(dr.window_handles)

    # 定位所有帖子的title
    node_list = dr.find_elements_by_xpath('/html/body/div[5]/div/div[5]/div[2]/ul/li[1]/div[2]/h2/a')
    for node in node_list:
        print(node.text, node.get_attribute('href'))


def test04():
    """QQ空间中嵌套iframe的处理"""

    # Iframe的嵌套html处理，首先必须定位到这个iframe框架，然后再获取iframe中的火元素，不能一步到位
    url = 'https://qzone.qq.com/'

    # 构建浏览器对象
    dr = webdriver.Chrome()

    # 访问url
    dr.get(url)

    # 首先必须要进入内部框架iframe!!!!
    # 进入框架的两种方式
    # 通过id
    # dr.switch_to.frame('login_frame')
    # 通过元素定位
    el_1 = dr.find_element_by_xpath('//*[@id="login_frame"]')
    dr.switch_to.frame(el_1)

    # 尝试点击账号密码登录按钮
    el = dr.find_element_by_id('switcher_plogin')
    el.click()

    # 输入账号密码
    el_user = dr.find_element_by_id('u')
    el_user.send_keys('371673381')
    el_pwd = dr.find_element_by_id('p')
    el_pwd.send_keys('123+456shengjun')

    # 强制设置一个等待时间用来加载html，不然的话理解寻找id会找不到元素，或报错
    time.sleep(10)
    # 点击登录
    el_sub = dr.find_element_by_id('login_button')
    el_sub.click()

    # 需要设置一个sleep等待，不带点击后立马就结束了
    time.sleep(10)

    dr.close()
    dr.quit()


def main():
    # test01()
    # test02()
    # test03()
    test04()


if __name__ == '__main__':
    main()

