from django.apps import AppConfig


class UserConfig(AppConfig):

    # apps.py包含的是该应用的配置信息

    # 表示记载的应用是user应用
    name = 'user'

    # verbose_name用来给人看的可读的name，显示在页面上的文字，比如后台admin管理中进行显示
    verbose_name = "用户中心"
