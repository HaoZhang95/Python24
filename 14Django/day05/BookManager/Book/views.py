from django.conf import settings
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from Book.models import PictureInfo, BookInfo, AreaInfo


def test1(request):
    return render(request, 'Book/test1.html')


def test2(request):
    return render(request, 'Book/test2.html')


def test21(request):
    """接收用户上传的图片"""

    # 从请求报文中获取图片的网络数据
    picture = request.FILES.get('pic')
    # 获取图片名字
    name = picture.name
    # 拼接图片保存在服务器路径
    path = '%s/Book/%s' % (settings.MEDIA_ROOT, name)

    # 将图片网络数据写入到path
    with open(path, 'wb') as file:
        # 遍历图片网络数据
        for c in picture.chunks():
            # 写入图片网络数据到本地保存
            file.write(c)

    # 创建模型类将图片路径写入到数据库
    pictureinfo = PictureInfo()
    pictureinfo.path = 'Book/%s' % name
    # save才能写入到数据库
    pictureinfo.save()

    return HttpResponse('OK!')


def test3(request):
    """展示上传的图片"""
    return render(request, 'Book/test3.html')


def test4(request, index):
    """数据获取后的分业操作"""
    bookinfos = BookInfo.objects.all()

    # 对获取到的数据使用分液器进行分页,每页显示2个
    paginator = Paginator(bookinfos, 2)

    if index == "":
        index = '1'

    # 使用分液器的page函数获取第几页的数据，默认1开始
    current_page = paginator.page(int(index))

    context = {
        'current_page': current_page,
    }

    """
        paginator对象： 方法init(列表,int每页显示的条数)
                        方法page(m)：返回Page对象，表示第m页的数据，下标以1开始
                        属性page_range：返回页码列表，从1开始，例如[1, 2, 3, 4]
                        属性count：返回对象总数
                        属性num_pages：返回页面总数
                        
        paginator.page对象：属性number：返回当前是第几页，从1开始
                            属性paginator：当前页对应的Paginator对象
                            方法has_next()：如果有下一页返回True
                            方法has_previous()：如果有上一页返回True
                            属性object_list：返回当前页对象的列表
                            方法len()：返回当前页面对象的个数
        
    """

    return render(request, 'Book/test4.html', context)


def test5(request):
    
    return render(request, 'Book/test5.html')


def sheng(request):
    """获取省级数据，转换为json"""

    # 查询省级数据
    shenglist = AreaInfo.objects.filter(parent__isnull=True)

    # 构造json
    list = []
    for sheng in shenglist:
        list.append([sheng.id, sheng.name])

    sheng_json_list = {
        'shenglist': list
    }

    return JsonResponse(sheng_json_list)


def shi(request):

    # 从请求报文中获取请求参数shengid
    shengid = request.GET.get('shengid')
    # 根据省份id查询市信息
    shilist = AreaInfo.objects.filter(parent=shengid)

    # 构造json {"list":[{"id":*, "name":*}, {"id":*, "name":*}, ...]}
    list = []
    for shi in shilist:
        list.append({"id": shi.id, "name": shi.name})
    shidata = {"list": list}

    return JsonResponse(shidata)


def qu(request):

    # 从请求报文中获取请求参数shiid
    shiid = request.GET.get('shiid')
    # 根据市id查询区信息
    qulist = AreaInfo.objects.filter(parent=shiid)

    # 构造json {"list":[{"id":*, "name":*}, {"id":*, "name":*}, ...]}
    list = []
    for qu in qulist:
        list.append({"id": qu.id, "name": qu.name})
    qudata = {"list": list}

    return JsonResponse(qudata)
