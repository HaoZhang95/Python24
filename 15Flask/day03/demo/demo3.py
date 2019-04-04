from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 在初始化sqlalchemy对象之前设置app的数据库配置，因为实例对象会读取app中的config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:haozhang@127.0.0.1:3306/test_27'

# 是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 初始化SQLAlchemy对象，配置给app
database = SQLAlchemy(app)


"""
    一个Role对应多个User

"""


# 定义角色模型.继承自SQLAlchemy.model
class Role(database.Model):
    """创建表，设置表结构"""
    __tablename__ = 'roles'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)

    # 通过relationship就能在查询的时候role.users可以点出来了
    # relationship中的backref意思是反向给它前面的User设置一个叫做role的属性，这样就可以user.role获取了
    # 实现了一获多喝多获一
    users = database.relationship('User', backref='role')

    # 显示一个可读字符串
    def __repr__(self):
        return 'Role %d %s' % (self.id, self.name)


class User(database.Model):
    """创建表，设置表结构, 添加外键"""
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)
    role_id = database.Column(database.Integer, database.ForeignKey(Role.id))

    # 显示一个可读字符串
    def __repr__(self):
        return 'User %d %s' % (self.id, self.name)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/demo1')
def demo1():
    # 创建一个表,# create-all会把继承自database.Model的所有类表创造出来
    database.drop_all()
    database.create_all()
    return '创建表成功...'


@app.route('/demo2')
def demo2():
    # insert
    role = Role(name='admin')
    database.session.add(role)
    database.session.commit()

    # update
    # role.name = "laowang"
    # database.session.commit()

    # delete
    # database.session.delete(role)
    # database.session.commit()
    return 'insret成功...'


@app.route('/demo3')
def demo3():

    role1 = Role(name='Role1')
    role2 = Role(name='Role2')

    database.session.add_all([role1, role2])
    database.session.commit()

    user1 = User(name='User1', role_id=1)
    user2 = User(name='User2', role_id=1)
    user3 = User(name='User3', role_id=2)

    database.session.add_all([user1, user2, user3])
    database.session.commit()

    return 'ok...'


@app.route('/demo4')
def demo4():

    # 模型类.query.all()或者get(index)
    user_list = User.query.all()
    user1 = User.query.get(1)

    # 通过user获取其对象外键的Role,一获多
    user1.role()
    return 'user_list= %s, user1= %s' % (user_list, user1)


if __name__ == '__main__':
    app.run()
