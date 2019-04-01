
from django.contrib import admin
from django.urls import path, re_path
from Book import views


urlpatterns = [

    # 不能在开始加反斜杠，推荐在结束加反斜杠
    # 如果url：http://127.0.0.1:8000/18/?a=10正则表达式只匹配的是18/的部分，并不是所有str
    path('booklist/', views.book_list),


    # url位置参数取值-使用正则的分组
    re_path('test1/(\d+)/(\d+)/$', views.test1),

    # 正则的关键字取值在分组括号内?P<num1>
    re_path('test2/(?P<num1>\d+)/(?P<num2>\d+)/$', views.test2),

    # 获取request中的method, path, GET
    re_path('test3/$', views.test3),

    # 获取post中的表单信息
    re_path('test4/$', views.test4),

    # 获取post中的表单信息
    re_path('test41/$', views.test41),

    # ajax局部刷新需要使用jsonresponse返回一个json
    re_path('test5/$', views.test5),

    # 响应json给ajax,ajax一般和jsonResponse组合使用
    re_path('test51/$', views.test51),

    # login
    re_path('test6/$', views.test6),

    # 响应login的redirect
    re_path('^test61/$', views.test61),

    # 响应的时候写入cookie
    re_path('^test7/$', views.test7),

    # session
    re_path('^test8/$', views.test8),


]
