from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

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


def test3(request):

    """测试转义，防止js代码注入,默认就自动开启转移"""

    # 直接httpResponse('<h1></h1>')的形式不会被转移，django识别出这是硬解码，无危险
    # 下面的通过上下文的形式传入html会被检测到危险，才会被转移
    context = {'text': '<h1>我是最大的标题标签</h1>'}

    return render(request, 'Book/test3.html', context)


def test4(request):
    """防止CSRF需要在返回页面之前向客户端写入一个CSRF cookie防止页面被修改之前，在html中的form表单中嵌入{% csrf_token %}"""

    return render(request, 'Book/test4.html')


def test41(request):
    """直接相应表单POST回送请求的话，会直接forbidden： CSRF cookie not set."""
    # 表单默认是GET，会返回405 POST方法找不到错误
    name = request.POST.get['uname']
    money = request.POST.get['money']

    return HttpResponse("%s --> %s" % (name, money))
#
# from pil.image import Image
# from pil.imagedraw import ImageDraw
# from pil.imagefont import ImageFont
# from django.utils.six import BytesIO
#
# # 生成验证码
#
#
# def verify_code(request):
#     # 引入随机函数模块
#     import random
#     # 定义变量，用于画面的背景色、宽、高
#     bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
#     width = 100
#     height = 25
#     # 创建画面对象
#     im = Image.new('RGB', (width, height), bgcolor)
#     # 创建画笔对象
#     draw = ImageDraw.Draw(im)
#     # 调用画笔的point()函数绘制噪点
#     for i in range(0, 100):
#         xy = (random.randrange(0, width), random.randrange(0, height))
#         fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
#         draw.point(xy, fill=fill)
#     # 定义验证码的备选值
#     str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
#     # 随机选取4个值作为验证码
#     rand_str = ''
#     for i in range(0, 4):
#         rand_str += str1[random.randrange(0, len(str1))]
#     # 构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
#     font = ImageFont.truetype('AdobeArabic-Regular.otf', 23)
#     # 构造字体颜色
#     fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
#     # 绘制4个字
#     draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
#     draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
#     draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
#     draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
#     # 释放画笔
#     del draw
#     # 存入session，用于做进一步验证
#     request.session['verifycode'] = rand_str
#     # 内存文件操作
#     buf = BytesIO()
#     # 将图片保存在内存中，文件类型为png
#     im.save(buf, 'png')
#     # 将内存中的图片数据返回给客户端，MIME类型为图片png
#     return HttpResponse(buf.getvalue(), 'image/png')


def test5(request):
    return render(request, 'Book/test5.html')


def test52(request):
    # 接受客户端传递的验证码
    client_code = request.POST.get('yzm')
    # 服务器生成的验证码
    server_code = request.session['verifycode']
    # 对比
    if client_code == server_code:
        return HttpResponse('验证码OK！')
    else:
        return HttpResponse('验证码错误')


def test6(request):
    return render(request, 'Book/test6.html')


def test61(request):
    return HttpResponse('来自test6中的链接跳转成功...')


def test7(request):
    """html模板和重定向中经常使用的反向解析, 如果一个路由改变了地址，那么重定向的地址不需要改变"""
    # return redirect('/test61/')
    return redirect(reverse('book:test61'))


def test8(request, num1, num2):

    return HttpResponse('来自test8中的链接跳转成功...')


def test9(request):

    return redirect(reverse('book:test9', args=(11, 22)))


def test91(request, num1, num2):
    return HttpResponse('91成功...')


def test10(request, num1, num2):
    return HttpResponse('10成功...')


def test11(request):

    return redirect(reverse('book:test11', kwargs={
        'num1': 11,
        'num2': 22,
    }))


def test111(request, num1, num2):

    return HttpResponse('11重定向成功...')
