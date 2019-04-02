from django.db import models

# Create your models here.
# 书籍信息模型，因为之前BookManager2版本中已经在数据库中做了迁移，所以本次BookManager3模型没更改，不需要再次迁移；额


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


class PictureInfo(models.Model):
    """图片上传的模型类"""

    # upload_to：表示图片上传到哪儿
    # 这样后台或者用户上传后会创建模型类将图片string地址保存在数据库,重新制作迁移文件
    # ImageField的作用在后台就会显示一个上传图片的按钮
    path = models.ImageField(upload_to='Book/')

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'pictureinfo'


class AreaInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='地区名称') #名称
    parent = models.ForeignKey('self',null=True,blank=True, verbose_name='上级地区', on_delete=models.CASCADE) #关系

    # 元类信息 ：修改表名
    class Meta:
        db_table = 'areainfo'

    def __str__(self):
        return self.name

    def title(self):
        return self.name

    # 指定方法作为列的排序依据
    title.admin_order_field = 'name'
    # 给自己定义的方法指定名称
    title.short_description = '区域'


