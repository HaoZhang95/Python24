from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.urls import reverse


def test1(request):
    return HttpResponse('OK...')


def test2(request):
    return render(request, 'test2.html')


def test3(request, a, b):
    return HttpResponse("%s ---> %s" % (a, b))


def test4(request, a, b):
    return HttpResponse("%s ---> %s" % (a, b))


def test5(request):

    # 反向解析，可以用来模板中指定路由 {% url 'user:test1' %}
    # 或者在函数中使用reverse函数获取请求该视图函数的url地址
    str = reverse('user:test1')
    return HttpResponse("OK... %s" % str)
