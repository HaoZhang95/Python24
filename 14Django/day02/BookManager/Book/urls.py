
from django.urls import path
from Book import views

urlpatterns = [
    path('booklist/', views.book_list),
    path('arealist/', views.area_list),
]
