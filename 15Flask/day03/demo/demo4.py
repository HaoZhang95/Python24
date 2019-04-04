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


class Role(database.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义列对象
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)
    us = database.relationship('User', backref='role')

    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s'% self.name


class User(database.Model):
    __tablename__ = 'users'
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True, index=True)
    email = database.Column(database.String(64),unique=True)
    password = database.Column(database.String(64))
    role_id = database.Column(database.Integer, database.ForeignKey('roles.id'))

    def __repr__(self):
        return 'User:%s'%self.name


@app.route('/')
def hello_world():

    # database.drop_all()
    # database.create_all()
    #
    # ro1 = Role(name='admin')
    # database.session.add(ro1)
    # database.session.commit()
    # #再次插入一条数据
    # ro2 = Role(name='user')
    # database.session.add(ro2)
    # database.session.commit()
    #
    # us1 = User(name='wang',email='wang@163.com',password='123456',role_id=ro1.id)
    # us2 = User(name='zhang',email='zhang@189.com',password='201512',role_id=ro2.id)
    # us3 = User(name='chen',email='chen@126.com',password='987654',role_id=ro2.id)
    # us4 = User(name='zhou',email='zhou@163.com',password='456789',role_id=ro1.id)
    # us5 = User(name='tang',email='tang@itheima.com',password='158104',role_id=ro2.id)
    # us6 = User(name='wu',email='wu@gmail.com',password='5623514',role_id=ro2.id)
    # us7 = User(name='qian',email='qian@gmail.com',password='1543567',role_id=ro1.id)
    # us8 = User(name='liu',email='liu@itheima.com',password='867322',role_id=ro1.id)
    # us9 = User(name='li',email='li@163.com',password='4526342',role_id=ro2.id)
    # us10 = User(name='sun',email='sun@163.com',password='235523',role_id=ro2.id)
    # database.session.add_all([us1,us2,us3,us4,us5,us6,us7,us8,us9,us10])
    # database.session.commit()

    print("ahhahaha")
    print("ahhahaha")
    print("ahhahaha")
    print("ahhahaha")
    print("ahhahaha")
    print("ahhahaha")
    print("ahhahaha")
    print("ahhahaha")
    return 'Hello World!'


"""
查询所有用户数据
    User.query.all()
查询有多少个用户
    User.query.count()
查询第1个用户
    User.query.first()
查询id为4的用户[3种方式]
    User.query.get(4)
    User.query.filter(User.id==4).first()
    User.query.filter_by(id=4).first()
    
查询名字结尾字符为g的所有数据[开始/包含]
    User.query.filter(User.name.endwith('g')).all()
    User.query.filter(User.name.contains('g')).all()
查询名字不等于wang的所有数据[2种方式]
    User.query.filter(User.name!='wang').all()
    User.query.filter(not_(User.name=='wang')).all()
查询名字和邮箱都以 li 开头的所有数据[2种方式]
    User.query.filter(User.name.startwith('li'), User.email.startwith('li')).all()
    User.query.filter(and_(User.name.startwith('li'), User.email.startwith('li'))).all()

查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
    User.query.filter(or_(User.password=='123456', User.email.endwith('itheima.com'))).all()
查询id为 [1, 3, 5, 7, 9] 的用户列表
    User.query.filter(User.id.in_([1, 3, 5, 7, 9])).all()

查询name为liu的角色数据
    User.query.filter(User.name=='liu').role
查询所有用户数据，并以邮箱排序
    User.query.order_by(User.email.asc()).all()
    User.query.order_by(User.email.desc()).all()
每页3个，查询第2页的数据
    paginate = User.query.paginate(2, 3)
    paginate.items --> [第二页的列表]
    paginate.page  --> 当前页数
    paginate.pages --> 总页数
"""


if __name__ == '__main__':
    app.run()
