from django.contrib import admin
from django.urls import path, re_path, include
from Book import views

urlpatterns = [
    path('test1/', views.test1),
    path('test2/', views.test2),
]
