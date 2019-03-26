from django.db import models


# Create your models here.


class BookInfoManager(models.Manager):
    """自定义管理器类。集成models.Maneger，重写方法"""

    def get_queryset(self):
        """对读取父类super原始结果集进行二次的筛选"""
        return super(BookInfoManager, self).get_queryset().filter(is_delete=False)

    # 自定义管理器类给**模型类**的实例方法

    @staticmethod
    def create_model(name):
        book = BookInfo(
            name=name,
            read_count=0,
            comment_count=0
        )

        return book


class BookInfo(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # name = models.CharField(max_length=20, null=True, blank=True, unique=True)

    # 元选项：用来修改默认的表信息Book_bookinfo
    class Meta:
        db_table = 'bookinfo'

    # models.Model中有一个默认的objects管理器对象
    # BookInfo.objects只在查询的时候会出现objects，类型是一个Manager管理器对象
    # 自定义的管理器对象，默认的objects则会失效

    # books = models.Manager()

    # 自定义管理器类，上面的是使用默认的管理器类来获取管理器对象的，继承model.Manager类
    # 使用场景: 1-查询显示没被删除的帖子，默认objects.all()返回所有，不然的话需要查询一次，filter一次，比较麻烦
    #          2-新增管理类对象方法，除了all(), filter(),order_by(),exclude()不包含...

    books = BookInfoManager()


class PeopleInfo(models.Model):

    # BookInfo模型类继承models.Model，其父类中有一个objects属性，调用返回的是一个管理器新建的对象，调用对象的方法
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    description = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "peopleinfo"


# 地区列表信息,自关联的表结构(多个一对多的表相结合)： id, name, parent 省去了多张表的创建
# 多对一，拿到外键parent获得的就是省会 --> city.parent.name
# 一对多，使用模型名字的小写 --> ity.areainfo_set.all
class AreaInfo(models.Model):
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # 元类信息 ：修改表名
    class Meta:
        db_table = 'areainfo'
