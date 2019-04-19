from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from DRF import views

urlpatterns = [
    # 使用了restful接口后，定义的路由可以是一样的test1/
    path('test1', views.BooksAPIView.as_view()),
    re_path('test1/(?P<pk>\d+)/$', views.BookAPIView.as_view()),
]

# 使用DRF框架的路由进行路由转发
router = DefaultRouter()
router.register('books', views.BookInfoViewSet)

# 不能直接写在urlpattern中，dajngo不认
# 将路由器中的所以路由信息追到到django的路由列表中
urlpatterns += router.urls
