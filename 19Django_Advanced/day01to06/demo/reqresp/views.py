import json

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

"""
    request.GET.get ---> request.args.get类似于flask
    request.POST.get ---> request.form.get类似于flask
    
    HttpResponse常用的子类：JsonResponse和HttpResponseRedirect
"""


# Create your views here.
def test1(request):
    # 客户端传参的方式： 1- 查询字符串?a=1&b=2  2- url路径传参/news/1/2
    #                  3- body中使用form，键值对,ajax中json等形式传参
    #                  4- header中

    # 类似字典的 QueryDict 对象，包含 GET 请求的所有参数
    query_dict = request.GET

    # get返回最后一个，同名情况下
    query_dict.get('a')

    # getlist返回一个同名的列表
    query_dict.getlist('a')

    return HttpResponse('OK...')


def test2(request):
    # body请求提中的数据如果是表单的话，可以通过request.POST.get()的方式获取
    # 如果body中的数据是json等的花，则需要使用request.body获取再进行decode获得参数
    # 非表单提交的数据，POST.get返回的是none

    x = request.POST.get("x")
    y = request.POST.get("y")
    xlist = request.POST.getist('x')

    return HttpResponse('OK...')


def test3(request):
    # body中发送的是json文本,返回的类似是一个byte的str类型
    str_bytes = request.body
    json_str = str_bytes.decode()

    # python 3.6以后，不需要此步骤,参数类型可以直接是str_byte类型
    # 3.5之前的版本json.laods接受的是参数类型str,需要先decode
    dict = json.loads(json_str)
    x = dict.get('x')
    y = dict.get('y')

    return HttpResponse("OK...")


def test4(request):
    # request.META获取请求头中的数据，比如CONTENT_TYPE
    dict = request.META
    content_type = dict.get("CONTENT_TYPE")

    return HttpResponse("OK...")


def test5(request):

    # 自定义响应体
    data = '{"name":"python"}'
    resp1 = HttpResponse(content=data, content_type='application/json', status=404)
    resp2 = JsonResponse({
        "name": "python"
    })

    # 重定向和reverse配合使用解决url硬编码的问题
    resp3 = HttpResponseRedirect(reverse("user:test1"))

    return resp3


def test6(request):

    resp = HttpResponse('OK...')
    resp.set_cookie('key1', 'value1', max_age=3600)

    cookie1 = request.COOKIES.get('key1')

    return resp


def test7(request):

    return None


"""
    这个装饰器用来装饰类视图的话，需要在路由中设置check_ip(views.RegisterView.as_view())
    装饰器@符号的添加就是执行了test = my_decorator(test)，返回一个wrapper, 也就是test = wrapper
    当被装饰的test()方法被调用的时候，也就是wrapper方法被执行
    
    路由中设置check_ip(views.RegisterView.as_view())原理就是手动的模拟@符号的添加来添加一个装饰器
    as_view返回的就是一个根据不同请求方式dispatch分发的视图函数，然后check_ip(这个函数) ==  my_decorator(test)
    
    缺点：从代码中看不出check_ip这个装饰器和RegisterView的联系，可读性不强，因为没有@符号，只能在url路由中查看
"""


def check_ip(func):
    # 实现禁止ip黑名单访问发帖界面。 解决： 可以通过在视图函数中使用装饰器实现
    def wrapper(request, *args, **kwargs):
        # 在视图函数执行前做额外的操作：
        # 禁止ip黑名单访问
        IP = request.META.get('REMOTE_ADDR')
        if IP not in ['192.168.210.160']:
            return HttpResponse('IP禁止访问')

        # 一切正常，返回该返回的
        return func(request, *args, **kwargs)

    return wrapper


# 方式4， 直接把装饰器定义成适合类视图函数的装饰器，添加一个self参数，这样就能直接在类视图函数中不需要method_decorator了
def check_ip_for_class(func):
    # 实现禁止ip黑名单访问发帖界面。 解决： 可以通过在视图函数中使用装饰器实现
    def wrapper(self, request, *args, **kwargs):
        # 在视图函数执行前做额外的操作：
        # 禁止ip黑名单访问
        IP = request.META.get('REMOTE_ADDR')
        if IP not in ['192.168.210.160']:
            return HttpResponse('IP禁止访问')

        # 一切正常，返回该返回的
        return func(self, request, *args, **kwargs)

    return wrapper


""""
    使用method_decorator把原来适用于python函数的装饰器修改**转换**为适合类视图函数的修饰器
    method_decorator装饰器作用：为类视图函数添加一个self参数，使其和as_view()函数中的dispatch方法的参数一一对应
    不能直接在get方法上添加@check_ip装饰器，因为缺少一个self参数，参数个数不符合，会直接把传进来的request当作self
"""


"""
    扩展类中重写as_view方法中添加装饰器，其他类视图直接继承自这个基类类视图，这样其他类视图中就不用使用method_decorator转换器了
    
    扩展类不要继承自View，扩展类1和扩展类2如果都继承自同一个父类的话，那么super的时候会先指向扩展1，再指向扩展2
    如果两个扩展类不是集集成自同一个父类的话，那么扩展1的super指的就是object，然后就return了，扩展2中的添加装饰器并不会执行
    
    为了防止这种情况，两个装饰器扩展类mixin都继承自object，但是在使用具体的类视图的时候让其继承自(Mixin1, Mixin2,View)
    最后一个继承自View来兜底，确保最后super执行到View中的as_view方法    
"""


class BaseViewMixin(object):

    @classmethod
    def as_view(cls, *args, **kwargs):
        view = super().as_view(*args, **kwargs)
        # 在这里添加自己的装饰器
        view = check_ip(view)
        return view


# 方式3， name=dispatch的话就是给所有的函数添加装饰器
# @method_decorator(check_ip, name='get')
# @method_decorator(check_ip, name='dispatch')
class RegisterView(BaseViewMixin, View):
    # 类视图的使用，用来继承提高复用和可读性, url中定义的话需要使用view.RegisterView.as_view()
    # 试图函数和类视图二选一

    """"
        如果要为类视图中所有函数都添加装饰器的话，需要重写dispatch方法，在dispatch方法上添加method_decorator
    """""

    # 方式2
    # @method_decorator(check_ip)
    # def dispatch(self, request, *args, **kwargs):
    #     return super(RegisterView, self).dispatch(request, *args, **kwargs)

    # 不同的方法处理不同的请求方式，函数的名字一定要正确
    # 方式1
    # @method_decorator(check_ip)
    def get(self, request):
        return render(request, 'test2.html')

    # 直接加上check_ip的话，第一个参数传递的是self这个类视图对象，第二个才是request
    def post(self, request):
        return HttpResponse("注册的操作成功...")


