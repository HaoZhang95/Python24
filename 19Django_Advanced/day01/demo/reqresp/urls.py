from django.urls import path

from reqresp import views
from reqresp.views import check_ip

urlpatterns = [
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3),
    path('test4/', views.test4),
    path('test5/', views.test5),

    path('test6/', views.test6),
    path('test7/', views.test7),

    # 类视图的注册，通过调用as_view方法来把一个类转换为url视图函数
    # as_view()方法的调用会把类转换为一个函数，如果url的请求方式的话i是get的话就会调用类视图中的get方法函数
    # 如果请求的方法不再类函数中，那么就会报405请求方法不被允许的错误

    # 装饰器装饰类视图方法，方式1
    # path('test8/', check_ip(views.RegisterView.as_view())),

    # 方式2, 不在路由中添加装饰器
    path('test8/', views.RegisterView.as_view()),
]