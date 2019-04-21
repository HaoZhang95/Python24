from django import forms
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from django.urls import reverse
from django.views import View

from user.models import BookInfo


def test1(request):
    return HttpResponse('OK...')


def test2(request):
    return render(request, 'test2.html')


def test3(request, a, b):
    return HttpResponse("%s ---> %s" % (a, b))


def test4(request, a, b):
    return HttpResponse("%s ---> %s" % (a, b))


def test5(request):

    # 反向解析，可以用来模板中指定路由 {% url 'user:test1' %}
    # 或者在函数中使用reverse函数获取请求该视图函数的url地址
    str = reverse('user:test1')
    return HttpResponse("OK... %s" % str)


class BookInfoForm(forms.Form):
    title = forms.CharField(label='图书名称', required=True, max_length=20)
    pub_date = forms.DateField(label='发布日期', required=True)


# form的另一种方式，继承自forms.modelform
# class BookInfoForm2(forms.ModelForm):
#
#     # 使用元信息来整合数据模型
#     class Meta:
#         model = BookInfo
#         # 这样就不需要使用上面的forms.Charfiled来一一制定input了
#         # 具体的input中的name或者约束条件会根据数据模型中title字段的label, required,verbose_name等进行显示
#         fields = ('title', 'pub_date')


class Test6View(View):

    def get(self, request):
        form = BookInfoForm()
        return render(request, 'test6.html', {'form': form})

    def post(self, request):
        # 表单的获取是通过request.POST的方式获取表单信息的，所以需要将它传递给自定义的form当作参数
        form = BookInfoForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("ok...")
        else:
            return render(request, 'test6.html', {'form': form})

