from django.urls import path

from reqresp import views

urlpatterns = [
    path('test1/', views.test1),
    path('test2/', views.test2),
    path('test3/', views.test3),
]