from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
"""
    视图就是应用app中的views.py中的视图函数，用来处理不同url的请求响应，中间人
    HttpResponse的子类有jsonResponse，HttpResponseRedirct,请求响应可以是:html页面,404错误,重定向,或者纯json    
    
"""


def book_list(request):

    return HttpResponse('ok...')
