import json
from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from rest_framework.viewsets import ModelViewSet

from DRF.serializers import BookInfoSerializer
from user.models import BookInfo


class BooksAPIView(View):
    """查询所有的图书，添加图书"""

    # GET /books/
    def get(self, request):

        queryset = BookInfo.objects.all()
        book_list = []
        for book in queryset:
            book_list.append({
                'id': book.id,
                'name': book.name,
                'pub_date': book.pub_date,
                'read_count': book.read_count,
                'comment_count': book.comment_count,
                # 'image': book.image.url if book.image else ''
            })

        # 返回一个列表，列表中包含多个字典
        # python是支持[{},{},{}]但是django认为这样是不安全的，会进行检验是不是都是键值对，报错，关闭检验即可
        # 不设置safe=false的话，JSONREsponse只会接受传统的json格式
        return JsonResponse(book_list, safe=False)

    # POST /books/
    def post(self, request):

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略

        book = BookInfo.objects.create(
            btitle=book_dict.get('btitle'),
            # strftime 从time类型转换为str类型
            # strptime 从str类型转换为time类型
            bpub_date=datetime.strptime(book_dict.get('pub_date'), '%Y-%m-%d').date()
        )

        # 数据库create成功之后，根据restful规范需要返回这个新对象的json信息
        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        }, status=201)


# BookAPIView是单数形式，所以没有POST，post存在于BOOKSAPIVIEW因为post不需要pk
class BookAPIView(View):
    def get(self, request, pk):
        """
        获取单个图书信息
        路由： GET  /books/<pk>/
        url中则需要设置books/(?P<pk>d+)/
        """

        # 主要注意的是django总get一个不存在的数据则会报错并不是返回一个none
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
            'id': book.id,
            'name': book.name,
            'pub_date': book.pub_date,
            'read_count': book.read_count,
            'comment_count': book.comment_count,
        })

    def put(self, request, pk):
        """
        修改图书信息
        路由： PUT  /books/<pk>
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        book_dict = json.loads(json_str)

        # 此处详细的校验参数省略

        book.btitle = book_dict.get('btitle')
        book.bpub_date = book_dict.get('bpub_date')
        book.save()

        return JsonResponse({
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
            'image': book.image.url if book.image else ''
        })

    def delete(self, request, pk):
        """
        删除图书
        路由： DELETE /books/<pk>/
        """
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()

        return HttpResponse(status=204)


class BookInfoViewSet(ModelViewSet):
    """
        DRF框架中使用自定义的序列化器，继承自不再是View，而是框架中的ModelViewSet
        下面的两行代码就相当于
    """
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer
