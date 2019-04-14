from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# info包中的init文件在这里使用的时候被初始化
# python manage.py db migrate -m 'initial'的时候会发生 No changes in schema detected.
# 因为运行manage.py时候没有识别models类，这里导入逸轩进行避免
from info import create_app, db, models

# 类似于工厂方法来创建返回一个app
from info.models import User

app = create_app('development')

# 配置脚本启动app
manager = Manager(app)

# 使用migrate扩展将数据库和app关联
Migrate(app, db)
# 把数据库的迁移命令添加在manager中, python manage.py db init中会用到
manager.add_command('db', MigrateCommand)


@manager.option('-n', '-name', dest='name')
@manager.option('-p', '-password', dest='password')
def createsuperuser(name, password):
    """使用manager装饰器使这个函数可以以命令行的形式执行, dest的参数名必须和函数的形式参数名一致"""

    if not all([name, password]):
        print("参数不足")

    user = User()
    user.nick_name = name
    user.mobile = name
    user.password = password
    user.is_admin = True

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)

    print("添加成功")


if __name__ == '__main__':
    manager.run()
