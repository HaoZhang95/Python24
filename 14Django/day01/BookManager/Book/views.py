from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# views视图就是一个python函数，用来处理网络请求，承上启下的中间人
# views中需要首先在urls中设置路由
from Book.models import BookInfo, PeopleInfo


def test(request):
    """
        第一个参数必须是httprequest类型的对象，包含了所有请求信息
        并且返回值是一个httpresponse的对象，包含给请求者的相应信息,或者交给render其返回值就是一个response对象
    """

    # return HttpResponse('Hello World...')

    # context是一个字典，用于封装数据库查询后的结果
    context = {
        'key': "这是数据库查询的数据..."
    }

    response = render(request, 'Book/test.html', context=context)
    return response


def book_list(request):
    """提供书籍列表页面的"""

    # 查询所有的书籍信息 --> 列表
    book_list = BookInfo.objects.all()

    context = {
        'book_list': book_list
    }

    return render(request, 'Book/booklist.html', context)


def people_list(request, book_id):
    """
        路由正则匹配的时候，会自动把正则中的括号参数和视图函数的参数一一对应， r'booklist/(\d+)
        正则中的第一个括号的值传递给book_id提供书籍列表页面的
    """

    # 查询所有的书籍信息 --> 列表
    book = BookInfo.objects.get(id = book_id)

    # 因为是1对多的关系，可以直接获取多的那一方的集合
    people_list = book.peopleinfo_set.all()

    context = {
        'people_list': people_list
    }

    return render(request, 'Book/peoplelist.html', context)

