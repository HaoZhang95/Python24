from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 在初始化sqlalchemy对象之前设置app的数据库配置，因为实例对象会读取app中的config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:haozhang@127.0.0.1:3306/booktest'

# 是否追踪数据库的修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True

# 初始化SQLAlchemy对象，配置给app
database = SQLAlchemy(app)

# 用于session中的csrf
app.secret_key = 'Hao'

# 不使用模型来创建多对多的中间表, 外键设置为student表中的id
tb_student_course = database.Table.create(
    "student_course",
    database.Column('student_id', database.Integer, database.ForeignKey('students.id')),
    database.Column('course_id', database.Integer, database.ForeignKey('courses.id')),
)


class Student(database.Model):
    __tablename__ = "students"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)

    # 多对多表中需要使用secondary中间表的设置， 多对多表中需要设置lazy(是否加载中间表中的数据)
    # lazy懒加载,返回的不再是具体的数据列表,而是一个叫做Cursor
    # 没有lazy=dynamic的话，那么当student查询出来以后，course也就同时被查询出来，已经有值了
    # 使用dynamic的话，student查询出来后，该courses属性并没有赋值，而只是一个查询对象，避免不必要的查询操作
    courses = database.relationship('Course', secondary=tb_student_course,
                                    # 设置Course.students的动态加载
                                    backref=database.backref('students', lazy='dynamic'),
                                    # 下面的是设置Student.courses的动态加载
                                    lazy='dynamic')


class Course(database.Model):
    __tablename__ = "courses"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)


@app.route('/')
def hello_world():
    database.drop_all()
    database.create_all()

    # 添加测试数据

    stu1 = Student(name='张三')
    stu2 = Student(name='李四')
    stu3 = Student(name='王五')

    cou1 = Course(name='物理')
    cou2 = Course(name='化学')
    cou3 = Course(name='生物')

    # 多对多的中需要设置stu中的courses属性
    stu1.courses = [cou2, cou3]
    stu2.courses = [cou2]
    stu3.courses = [cou1, cou2, cou3]

    database.session.add_all([stu1, stu2, stu2])
    database.session.add_all([cou1, cou2, cou3])

    database.session.commit()

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
