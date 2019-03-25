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
from django.contrib import admin
from django.urls import path, re_path, include

# 这里的pattern是有顺序的，从上到下匹配
# url的写法已经废弃，取代的是path，path中的url不能正则匹配，使用re_path可以使用正则，re代表的是regex
urlpatterns = [

    path('admin/', admin.site.urls),

    # 如果不是admin，匹配到自己book中的urls.py文件
    re_path(r'^', include('Book.urls'))

]
