from django.contrib import admin
from django.urls import path, re_path, include
from Book import views



urlpatterns = [
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3),
    path('test4/', views.test4),
    path('test41/', views.test41),
    path('test5/', views.test5),
    # path('test51/', views.verify_code),
    path('test52/', views.test52),


    # test6的a链接跳转到的链接，如果html中的链接不写死的话就是：反向解析，根据url的正则动态生成链接的地址
    # 给test61的路由起一个别名，用作反向解析
    path('test6/', views.test6),
    path('test61/', views.test61, name='test61'),
    path('test7/', views.test7),
    re_path('test8/(\d+)/(\d+)/', views.test8, name='test8'),

    # 访问test9的时候，重定向到test91
    path('test9/', views.test9),
    re_path('test91/(\d+)/(\d+)/', views.test91, name='test9'),

    # 反向解析中的关键字参数
    re_path('test10/(?P<num2>\d+)/(?P<num1>\d+)/', views.test10, name="test10"),

    # 重定向中的关键字参数
    path('test11/', views.test11),
    re_path('test111/(?P<num1>\d+)/(?P<num2>\d+)/', views.test111, name='test11'),

]
