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


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
