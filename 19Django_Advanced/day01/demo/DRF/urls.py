from django.urls import path, re_path

from DRF import views

urlpatterns = [

    # 使用了restful接口后，定义的路由可以是一样的test1/
    path('test1', views.BooksAPIView.as_view()),
    re_path('test1/(?P<pk>\d+)/$', views.BookAPIView.as_view())
]