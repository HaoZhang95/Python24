from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from Book.models import BookInfo

"""
    视图就是应用app中的views.py中的视图函数，用来处理不同url的请求响应，中间人
    HttpResponse的子类有jsonResponse，HttpResponseRedirct,请求响应可以是:html页面,404错误,重定向,或者纯json    
    
"""


def book_list(request):

    return HttpResponse('ok...')


def test1(request, num1, num2):
    """从url中获取有用的数据"""

    return HttpResponse('ok... num1=%s num2=%s' % (num1, num2))


def test2(request, num2, num1):
    """关键字参数取值, 使用关键字参数的话，urls.py的关键字必须和test2中的形参名字一样，顺序无所谓"""

    return HttpResponse('ok... num1=%s num2=%s' % (num1, num2))


def test3(request):
    """
        httpRequest对象用来获取/home/?a=1&b=2&b=3中的请求报文参数
        request.path --> home/
        request.GET --> queryDict字典可以一键多值，b=2,b=3可以重复的key，获取问号后面的str
                        GET属性和get方法没有任何关系，post方式也是使用GET来获取问号后面的str
        request。POST --> 获取表单数据

    """

    path = request.path
    method = request.method
    query_dict = request.GET

    # http://127.0.0.1:8000/test3/?a=1&b=2&b=3
    # get --> 一键一值
    # getlist(key) --> query_dict=['2', '3']获取一键多值
    return HttpResponse('ok... path=%s method=%s query_dict=%s'
                        % (path, method, query_dict.getlist('b')))


def test4(request):

    return render(request, 'Book/post.html')


def test41(request):
    # POST获取表单信息
    query_dict = request.POST
    name = query_dict.get('username')
    like = query_dict.getlist('like')

    return HttpResponse('ok... name=%s like=%s' % (name, like))


def test5(request):
    # ajax局部刷新
    return render(request, 'Book/ajax.html')


def test51(request):
    # 响应ajax局部刷新，返回一个json

    # 数据库查询
    book_list = BookInfo.objects.all()

    # 不能直接传入一个列表，需要传入一个json格式的列表，或者一个json对象
    # 转成以下的格式
    """
        {  这里或者替换成[]都行
            'book_list': [
                {'name': 'book1'},
                {'name': 'book2'},
            ]
        }
    """
    book_dict_list = []
    for book in book_list:
        book_dict_list.append({'name': book.name})

    json_dict = {'book_list': book_dict_list}

    return JsonResponse(json_dict)


def test6(request):
    # test61/: http://127.0.0.1:8000/test6/test61/
    # /test61/: http://127.0.0.1:8000/test61/ 开头一斜线表示从根路径开始拼接
    return redirect('/test61/')


def test61(request):
    return HttpResponse('登陆成功...')


def test7(request):
    """先判断cookie的读取"""
    request.COOKIES.get('login')
    if 'login' in request.COOKIES:
        pass
    # request.delete_cookie('')

    """cookie的写入"""
    response = HttpResponse('ok...')
    # 一次只能写入一个key-value
    response.set_cookie('login', 'yes')

    return response


def test8(request):
    """默认存储在django_session的表中,暗文的方式存储，并且把这个暗文的key存储到cookie中，所以session是基于cookie的"""
    request.session['login'] = 'yes'

    #  request.session.get('键',默认值)
    #  del request.session['键']
    #  request.session.clear()

    return HttpResponse('ok...')


