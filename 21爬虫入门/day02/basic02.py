import re

import requests


def test01():
    """
    爬虫有时候需要登陆后才能获取数据，不建议使用cookie，
    因为cookie的话会暴露自己的账号，会导致该账号因为爬虫被永久封禁
    1- 不要使用cookie
    2- 降低数据采集速度
    """

    url = 'http://www.renren.com/474692517'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
        # 'Cookie': "anonymid=juv3j19i-3t9bqx; depovince=GW; jebecookies=e3ef4064-90ed-4fd1-bf47-045da8caa0ae|||||; _r01_=1; ick_login=1ed70fae-db06-4a0a-a660-f0abdbe16703; _de=A9A895D4C2CE12CFDFBEC85DBF02707A; p=50430f0677fbafdde1e4b935a46e72497; first_login_flag=1; ln_uact=13463111974; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20150803/2335/h_main_C3Xl_9d590000b779195a.jpg; t=27d0e1b1de55cd027fa25bb42d5d942b7; societyguester=27d0e1b1de55cd027fa25bb42d5d942b7; id=474692517; xnsid=b1069884; ver=7.0; loginfrom=null; JSESSIONID=abcgD7CMSTTrladFw_oPw; wp_fold=0"
    }

    # 不放在请求头中的cookie
    temp = "anonymid=juv3j19i-3t9bqx; depovince=GW; jebecookies=e3ef4064-90ed-4fd1-bf47-045da8caa0ae|||||; _r01_=1; ick_login=1ed70fae-db06-4a0a-a660-f0abdbe16703; _de=A9A895D4C2CE12CFDFBEC85DBF02707A; p=50430f0677fbafdde1e4b935a46e72497; first_login_flag=1; ln_uact=13463111974; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20150803/2335/h_main_C3Xl_9d590000b779195a.jpg; t=27d0e1b1de55cd027fa25bb42d5d942b7; societyguester=27d0e1b1de55cd027fa25bb42d5d942b7; id=474692517; xnsid=b1069884; ver=7.0; loginfrom=null; JSESSIONID=abcgD7CMSTTrladFw_oPw; wp_fold=0"
    cookie = {}
    for i in temp.split('; '):
        cookie[i.split('=')[0]] = i.split('=')[-1]

    print(cookie)

    resp = requests.get(url, headers=headers)

    # 知乎不加header的话返回400 Bad Request
    print(resp.status_code)
    print(re.findall('张浩', resp.content.decode()))


def test02():
    """session的使用来模拟登陆后的获取数据信息"""
    url = "http://www.renren.com/PLogin.do"
    session = requests.session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }
    data = {
        "email": "13463111977",
        "password": "9941107288"
    }

    # 使用session进行post
    session.post(url, data=data, headers=headers)

    # 查看判断是不是登陆成功
    resp = session.get('http://www.renren.com/474692517')
    # 知乎不加header的话返回400 Bad Request
    print(resp.status_code)
    print(re.findall('张浩', resp.content.decode()))


def test03():
    url = "https://www.12306.cn/mormhweb/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36",
    }

    # 如果遇到ssl证书认证错误，设置verify=false即可
    resp = requests.get(url=url, verify=False, timeout=1)
    print(resp.status_code)
    # 使用requests对象中的将cookie的列表转换为字典
    print(resp.cookies)
    print(requests.utils.dict_from_cookiejar(resp.cookies))


def main():
    # test01()
    # test02()
    test03()


if __name__ == '__main__':
    main()


