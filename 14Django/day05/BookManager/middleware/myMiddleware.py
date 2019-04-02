

class Middleware01(object):

    def __init__(self):
        print('--------------init')

    def process_request(self, request):
        print('--------------request')

    def process_view(self, request, view_func, view_args, view_kwargs):
        print('--------------view')

    def process_template_response(self, request, response):
        print('--------------template')
        return response

    def process_response(self, request, response):
        print('--------------response1111111')
        return response
    #
    # def process_exception(request,exception):
    #     pass

#
# class Middleware02(object):
#     """
#         自定义的中间件，至少实现1-6个父类方法，从init创建中间件到请求再到响应一整套流程
#
#         自定义的中间件还需要在settins中注册，多个中间件如果都执行相同的重写方法，那么先注册的后执行，也就是说后注册的先响应
#
#     """
#     def __init__(self):
#         print('--------------init')
#
#     def process_request(self, request):
#         print('--------------request')
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('--------------view')
#
#     def process_template_response(self, request, response):
#         print('--------------template')
#         return response
#
#     def process_response(self, request, response):
#         print('--------------response22222222')
#         return response
#
#     def process_exception(request,exception):
#         pass






