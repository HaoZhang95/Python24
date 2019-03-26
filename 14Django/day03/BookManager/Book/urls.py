
from django.contrib import admin
from django.urls import path
from Book import views


urlpatterns = [

    # 不能在开始加反斜杠，推荐在结束加反斜杠
    # 如果url：http://127.0.0.1:8000/18/?a=10正则表达式只匹配的是18/的部分，并不是所有str
    path('booklist/', views.book_list),
]
