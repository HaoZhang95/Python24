from django.http import HttpResponse
from django.shortcuts import render
from Book.models import BookInfo

# Create your views here


def test1(request):

    booklist = BookInfo.objects.all();

    context = {
        'name': '你的名字 :)',
        'booklist': booklist,
    }

    """
        自定义的filter必须位于某一个应用下的templatetags包的下面
    """
    return render(request, 'Book/test1.html', context)


def test2(request):

    context = {
        'name': '你的名字',
    }

    return render(request, 'Book/test2.html', context)
