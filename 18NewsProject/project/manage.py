from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
# info包中的init文件在这里使用的时候被初始化
from info import create_app, db

# 类似于工厂方法来创建返回一个app
app = create_app('development')
# 配置脚本启动app
manager = Manager(app)

# 使用migrate扩展将数据库和app关联
Migrate(app, db)
# 把数据库的迁移命令添加在manager中
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
