"""BookManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, path
from Book import views


# 这里的pattern是有顺序的，从上到下匹配
urlpatterns = [

    # 使用正则来匹配路由，匹配到自己book中的视图view中的函数
    path('test', views.test),

    path('booklist', views.book_list, name='booklist'),
    re_path(r'booklist/(\d+)', views.people_list, name='details'),
]
