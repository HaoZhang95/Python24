from django.contrib import admin
from django.urls import path, re_path, include
from Book import views

urlpatterns = [

    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test21/', views.test21),
    path('test3/', views.test3),
    re_path('page(\d*)/$', views.test4),
    path('test5/', views.test5),
    path('sheng/', views.sheng),
    path('shi/', views.shi),
    path('qu/', views.qu),

]
