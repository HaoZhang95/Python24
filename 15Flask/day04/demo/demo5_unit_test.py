import unittest

from flask import json
from demo.demo5 import app


class LoginTestCase(unittest.TestCase):
    """为登陆页面进行的测试, 单元测试的自定义方法必须以test开头，否则会找不到测试方法"""

    # 在所测试的方法之前会调用的方法，可以做一些初始化操作，比如数据库操作
    def setUp(self):
        # 后面测试的时候直接使用self.client即可
        # 测试中的代码报错的话会显示出来哪一行
        app.testing = True
        self.client = app.test_client()

    # 测试传入的参数不足，会返回errcode = -2
    def test_empty_username_password(self):
        response = app.test_client().post('/login', data={})
        resp_data = response.data
        json_dict = json.loads(resp_data)

        print(json_dict)

        self.assertIsNotNone(json_dict, '未获取到相关的返回数据')
        self.assertIn('errcode', json_dict, '返回的数据格式不正确')
        errcode = json_dict['errcode']
        self.assertEqual(errcode, -2, '返回的状态码错误')

    # 测试用户名或者密码不正确，会返回errcode = -1


if __name__ == '__main__':
    # 在mian方法中使用unitest.main之后就可以命令行直接运行这个py文件了
    unittest.main()
