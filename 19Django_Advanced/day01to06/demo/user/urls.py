from django.urls import path, re_path

from user import views

urlpatterns = [

    path('test1/', views.test1, name='test1'),
    path('test2/', views.test2),
    re_path('test3/(\d+)/(\d+)', views.test3),
    re_path('test4/(?P<a>\d+)/(?P<b>\d+)', views.test4),
    path('test5/', views.test5),
    path('test6/', views.Test6View.as_view()),

]