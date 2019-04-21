"""
    中间件是把所有的请求和相应进行修改
    装饰器只是给个别视图路由进行修改的

    自定义的中间件需要继承自MiddlewareMixin的扩展类
"""
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None):
        super(MyMiddleware, self).__init__(get_response)
        print('init中间件,只会在服务器启动的时候初始化一次中间件')

    def process_request(self, request):
        print('before 视图')
        # 注意：可以返回None或者response对象，如果返回response对象，则视图函数就不会再执行了

    # 需要返回一个response
    def process_response(self, request, response):
        print('after 视图')
        return response

