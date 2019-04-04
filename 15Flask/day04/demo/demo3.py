from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager

app = Flask(__name__)
# 创建终端命令对象
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:haozhang@127.0.0.1:3306/migratetest'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 使用Migarate把app和db链接起来
Migrate(app, db)

# 将数据库的迁移命令交给manager用来使用命令行的方式启动服务器
# python demo3.py aaa init  必须在项目根文件中执行命令才有效，才会生产migration文件夹
# python demo3.py aaa migrate -m '这是初始化，第一次迁移'  生成迁移文件在migrations/version文件夹
# python demo3.py aaa upgrade 真正的在数据库创建表
manager.add_command('aaa', MigrateCommand)

"""
    数据库迁移:表结构字段的修改， 追踪数据库模式的变化，然后把变动应用到数据库中。
            不再需要手动的删除旧表，导入数据到新表，不能在使用db.createall来创建表了
"""


# 定义模型Role
class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    nick_name = db.Column(db.String(64), unique=True)

    # title的新增字段
    title = db.Column(db.String(64))
    user = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串，
    def __repr__(self):
        return 'Role:'.format(self.name)


# 定义用户
class User(db.Model):
    __talbe__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    # 设置外键
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:'.format(self.username)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # 一定要使用manager.run否则命令行启动无效
    manager.run()
