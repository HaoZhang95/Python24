"""demo URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # 调用include函数，用来包含user.urls下面的所有路由
    # namespace的位置是在include函数里面的
    # 2。0之后需要在include第一个参数中设置一个元祖和制定app_name的值,应用的名字不能瞎写

    # {% url 'app_name: 该app_name下对应的路由中的name'%}
    path('user/', include(('user.urls', 'user'))),
    path('req/', include(('reqresp.urls', 'reqresp'), namespace='req')),
    path('drf/', include(('DRF.urls', 'DRF'))),

]
