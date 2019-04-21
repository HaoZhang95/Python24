from django.db import models

# Create your models here.
class BookInfo(models.Model):

    # verbose_name用来在站点管理显示自定义的文字
    name = models.CharField(max_length=20, verbose_name='书名')
    pub_date = models.DateField(null=True, verbose_name='发布日期')
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    def my_field(self):
        return "自定义field"

    # 为自定义的栏添加动作，否则不能点击，制定其排序规则和name字段一样
    my_field.admin_order_field = 'name'

    def __str__(self):
        return self.name

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'bookinfo'


class PeopleInfo(models.Model):

    # BookInfo模型类继承models.Model，其父类中有一个objects属性，调用返回的是一个管理器新建的对象，调用对象的方法
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    description = models.CharField(max_length=20)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = "peopleinfo"
