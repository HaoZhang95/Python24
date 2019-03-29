from django.db import models

# Create your models here.
# 书籍信息模型，因为之前BookManager2版本中已经在数据库中做了迁移，所以本次BookManager3模型没更改，不需要再次迁移；额


class BookInfo(models.Model):
    name = models.CharField(max_length=20)
    pub_date = models.DateField(null=True)
    read_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    # 元类信息 : 修改表名
    class Meta:
        db_table = 'bookinfo'
