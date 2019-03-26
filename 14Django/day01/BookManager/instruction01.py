# MVT设计模式，model-view-template
# model负责和数据库交互来获取model数据
# view相当于MVC中的Controller负责处理网络请求http response
# template相当于MVC中的View负责封装html，css，js等内置模板引擎

# 具体流程：客户端发出网页请求 --> View接受网络请求 --> 找mdel去数据库找数据 -->找回的model数据返回给view
# --> view可以直接返回无修饰的model原始数据给客户端 --> 或者找template去美化数据，添加css,html等，动态生成一个html文件返回给View
# --> View将动态生成的html返回给客户端， MVT中的View充当中间人，两头链接M和T

# django安装的时候会默认安装在一个公共的路径下，这样开发不同项目的时候，可能会用到不同版本的django，因为安装在公共陆空
# 这样就会版本覆盖，其他项目可能会产生版本不兼容的异常
# 所以安装django的时候会搭建虚拟环境，一个项目对应一个环境

"""
    django的配置，直接使用pycharm专业版，在设置中解释器中使用pip安装django
    1- 安装成功后，整体的使用类似于angular的使用方法，关键字django-admin
    2- cd到对应的目录下，django-admin startproject 项目名称
                _init_.py --> 项目初始化文件，表示该项目可以被当作一个package引入
                settings.py --> 项目的整体配置文件，比如在这里关联Book这个app
                urls.py --> 项目的url配置文件
                wsgi.py --> 项目和WSGI兼容的Web服务器入口

                manage.py --> 项目运行的入口，指定配置文件路径，里面包含main函数


    3- cd到项目名称下面才可以: python manage.py startapp 应用名称 (创建应用，类似于angular中的模块？)
                init.py --> 应用初始化文件，表示该项目可以被当作一个package引入
                admin.py --> 后台的站点管理注册文件
                apps.py --> 当前app的基本信息
                models.py --> 数据模型，里面存放各种bean
                tests.py --> 单元测试
                views.py --> 处理业务逻辑，MVT中的中间人
                migrations --> 模型model迁移的，将model类制作成数据库中的表

    4- 配置刚刚创建的app，在项目的settings.py中的installed_apps中添加当前app，进行组装

"""

"""
    站点管理： 1- settings.py中设置语言和时区
              2- python manage.py createsuperuser 创建管理员
              3- 启动服务,到 http://127.0.0.1:8000/admin进行登陆
              4- 在admin.py中注册自己的数据models用来在后台显示
"""

"""
    ORM: object-relation-mapping 对象关系映射
    优点：面向对象编程，不再是面向数据库写代码
        实现了数据模型和数据库的解耦，不在关注用的是oracle,mysql还是其他数据库
    缺点: object需要花费一点时间转换为sql语句，有性能损失(不过可忽略不计)

"""

