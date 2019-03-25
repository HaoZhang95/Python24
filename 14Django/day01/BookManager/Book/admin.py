from django.contrib import admin
from Book.models import BookInfo
from Book.models import PeopleInfo

# Register your models here.
# 在后台数据显示界面显示的数据models在这里注册


class PeopleInfoAdmin(admin.ModelAdmin):
    """自定义模型类的站点管理类，继承父类admin.ModelAdmin，默认的话直接显示模型类的tostring方法"""

    # 设置模型需要显示的字段
    list_display = ['id', 'name', 'gender', 'book']


class BookInfoAdmin(admin.ModelAdmin):
    """自定义模型类的站点管理类"""

    list_display = ['id', 'name']


admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(PeopleInfo, PeopleInfoAdmin)
