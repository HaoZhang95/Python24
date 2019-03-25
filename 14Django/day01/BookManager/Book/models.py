from django.db import models

# django中内嵌orm，可以用对象的方式操作数据库
# 该类继承的不是python中的object，而是django中的models.Model类，表明是一个数据模型，而不是普通的python类
# model中的不需要定义主键，主键由orm自己维护

"""
    1- 更新完models文件需要做迁移，生成迁移文件，或者是根据models.py生成建表的语句,使用：python manage.py makemigrations
    2- 生成建表语句后，执行: python manage.py migrate来创建表根据上面的生成的建表与 

"""


class BookInfo(models.Model):
    """书籍信息模型类"""

    name = models.CharField(max_length=10)

    def __str__(self):
        """把模型对象以字符串的形式输出，在后台界面中显示"""
        return self.name


class PeopleInfo(models.Model):
    """人物信息类"""

    # 设计姓名字段
    name = models.CharField(max_length=10)
    # 设计性别字段
    gender = models.BooleanField(default=False)
    # 添加外键, django2.0以后，外键添加的需要设置on-delete参数
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    def __str__(self):
        """把模型对象以字符串的形式输出，在后台界面中显示"""
        return self.name

