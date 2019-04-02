from django.contrib import admin
from Book import models
# Register your models here.


class BookInfoAdmin(admin.ModelAdmin):
    """站点管理类"""

    # 列表页自定义选项------------------------------------------------

    # 每页显示10条数据
    list_per_page = 10

    # 为底部也添加删除
    actions_on_top = False
    actions_on_bottom = True

    # 显示item的某些字段
    list_display = ['id', 'name', 'pub_date', 'my_field']

    # 右侧的过滤栏, 有些字段不能显示在过滤，报异常
    list_filter = ['name']

    # 增加搜索框，有些字段不能显示在搜索框，报异常
    search_fields = ['name', 'id']

    # 数据编辑页面自定义选项------------------------------------------------

    # 改变字段在编辑页面的顺序
    # fields = ['name', 'pub_date', 'comment_count', 'read_count', 'is_delete']

    # 字段分组：与fields二选一使用
    fieldsets = [
        ('基本', {'fields': ['name', 'pub_date']}),
        ('高级', {'fields': ['comment_count', 'read_count', 'is_delete']}),
    ]

    # admin后台页面的自定义------------------------------------------------
    # 需要手动找到django存放的base_site.html: /home/python/.virtualenvs/py3_django/lib/python3.5/site-packages/django/contrib/admin/templates/admin/base_site.html
    # 然后在template下新建一个admin文件夹，然后编辑这个base_site.html即可


admin.site.register(models.BookInfo, BookInfoAdmin)
admin.site.register(models.PictureInfo)

