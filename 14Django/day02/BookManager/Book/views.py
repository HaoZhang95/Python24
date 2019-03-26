from django.db.models import F, Q, Sum
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Book.models import BookInfo, PeopleInfo, AreaInfo


def book_list(request):

    # 使用默认的管理器对象objects
    # book_list = BookInfo.objects.all()

    # 使用自定义的管理器对象books
    book_list = BookInfo.books.all()

    # ======================================================
    # 限制limit查询
    # book_list = BookInfo.objects.all()[0:2]

    # 条件查询的格式: filter(模型属性名__条件运算符=值)
    # 1.查询id为1的书籍,exact判断相等（可省略）
    book_list = BookInfo.books.filter(id=1)
    book_list = BookInfo.books.filter(pk=1)
    book_list = BookInfo.books.filter(id__exact=1)
    book_list = BookInfo.books.filter(pk__exact=1)
    book_list = BookInfo.books.get(id=1)

    # 2.查询书名包含‘湖’的书籍
    book_list = BookInfo.books.filter(name__contains='湖')

    # 3.查询书名以‘部’结尾的书籍
    book_list = BookInfo.books.filter(name__endswith='部')

    # 4.查询书名不为空的书籍
    book_list = BookInfo.books.filter(name__isnull=False)

    # 5.查询编号为2或4的书籍
    book_list = BookInfo.books.filter(id__in=[2, 4])

    # 6.查询编号大于2的书籍，gt, lt, gte(大等于), lte(小等于)
    book_list = BookInfo.books.filter(id__gt=2)

    # 7.查询id不等于3的书籍
    book_list = BookInfo.books.exclude(id__exact=3)

    # 8.查询1980年发表的书籍
    book_list = BookInfo.books.filter(pub_date__year='1980')

    # 9.查询1990年1月1日后发表的书籍
    book_list = BookInfo.books.filter(pub_date__gt='1990-01-01')

    from datetime import date
    book_list = BookInfo.books.filter(pub_date__gt=date(1990, 1, 1))

    # ======================================================
    # F(Field)对象的查询,进行属性变量之间的比较，并且支持计算
    # 1.查询阅读量大于评论量的书籍
    book_list = BookInfo.books.filter(read_count__gt=F('comment_count'))

    # 2.查询阅读量大于2倍评论量的书籍
    book_list = BookInfo.books.filter(read_count__gt=F('comment_count') * 2)

    # Q对象表示的是或链接，非~Q， 并连接直接逗号
    # 查询阅读量大于20，并且编号小于3的图书
    book_list = BookInfo.books.filter(read_count__gt=20, id__lt=3)
    book_list = BookInfo.books.filter(read_count__gt=20).filter(id__lt=3)

    # Q(模型属性1__条件运算符=值) | Q(模型属性2__条件运算符=值)
    # 1.查询阅读量大于20，或编号小于3的图书
    book_list = BookInfo.books.filter(Q(read_count__gt=20) | Q(id__lt=3))

    # 2.查询编号不等于3的书籍,exclude或者~Q
    book_list = BookInfo.books.filter(~Q(id=3))

    # ======================================================
    # aggregate聚合函数sum,avg,max,min,count --> 字典 {'read_count__sum': 134}
    total_count = BookInfo.books.aggregate(Sum('read_count'))

    # ======================================================
    # 关联查询之基础关联查询, 需要使用get，而不是filter，否则不出现peopleinfo_set外键关联
    # 1.查询编号为1的图书中所有人物信息: 一对多:peopleinfo_set
    book1 = BookInfo.books.get(id__exact=1)
    people_list1 = book1.peopleinfo_set.all()

    # 2.查询编号为1的英雄出自的书籍：多查一: people1.book(直接调用people对应的外键属性book)
    people1 = PeopleInfo.objects.get(id=1)
    book2 = people1.book

    # ======================================================
    # 关联查询之内链接查询(将以上的两步骤使用内链接合成一步)
    # 1.查询书名为"天龙八部"的所有人物信息, 一对多, 内链接需要使用外键book来作为关联
    people_list2 = PeopleInfo.objects.filter(book__name='天龙八部')

    # 2.查询书籍中人物的描述包含"降龙"的书籍，多对一:bookinfo中没有外键链接peopleinfo，
    # 所以使用filter(关联模型类名小写__属性名__运算符=值)
    book_list2 = BookInfo.books.filter(peopleinfo__description__contains='降龙')

    # 使用自定义管理器类的实例方法
    # book1 = BookInfo.books.create_model('zxc')
    # book2 = BookInfo.books.create_model('xyz')
    # book_list = [book1, book2]

    # models.Model中有一个默认的objects管理器对象
    # BookInfo.objects只在查询的时候会出现objects，类型是一个Manager管理器对象

    # BookInfo.save 在ORM中成成insert/update的语句
    # BookInfo.delete 在ORM中成成delete的语句
    # BookInfo.str 对象转换为字符串的方法

    context = {
        'book_list': book_list,
        'total_count': total_count,
        'book2': book2,
        'people_list2': people_list2,
        'book_list2': book_list2,
    }

    # 惰性查询，并不是在book_list = BookInfo.books.all()立即查询
    # 而是在模板中使用到book_list的时候才会真正的在数据库查询
    return render(request, "Book/booklist.html", context)


def area_list(request):

    city_info = AreaInfo.objects.get(name='广州市')
    context = {'city': city_info}

    return render(request, 'Book/arealist.html', context)
