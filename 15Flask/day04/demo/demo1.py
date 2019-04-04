from flask import Flask, render_template, flash, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired

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


class Author(database.Model):

    __tablename__ = "authors"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)

    # 定义属性，以便可以访问多的一方的数据
    books = database.relationship('Book', backref='author')


class Book(database.Model):

    __tablename__ = "books"
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(64), unique=True)
    author_id = database.Column(database.Integer, database.ForeignKey(Author.id))


class AddBookForm(FlaskForm):
    author = StringField(label='作者', validators=[InputRequired('请输入作者')])
    book = StringField(label='书名', validators=[InputRequired('请输入书名')])
    submit = SubmitField('添加')


@app.route('/', methods=['POST', 'GET'])
def index():

    # database.drop_all()
    # database.create_all()
    #
    # #生成数据
    # au1 = Author(name='老王')
    # au2 = Author(name='老尹')
    # au3 = Author(name='老刘')
    # # 把数据提交给用户会话
    # database.session.add_all([au1, au2, au3])
    # # 提交会话
    # database.session.commit()
    # bk1 = Book(name='老王回忆录', author_id=au1.id)
    # bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    # bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    # bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    # bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # # 把数据提交给用户会话
    # database.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # # 提交会话
    # database.session.commit()

    # 创建表单对象
    book_form = AddBookForm()

    if request.method == 'POST':
        if book_form.validate_on_submit():
            # 取出数据
            author_name = request.form.get('author')
            book_name = book_form.book.data

            author = Author.query.filter(Author.name == author_name).first()
            # 查询输入的作者是否存在
            if not author:
                try:
                    # 不存在的话在author数据库中添加
                    author = Author(name=author_name)
                    database.session.add(author)
                    database.session.commit()

                    # 把书籍保存在数据库
                    book = Book(name=book_name, author_id=author.id)
                    database.session.add(book)
                    database.session.commit()
                except Exception as e:
                    database.session.rollback()
                    print(e)
                    flash("数据添加错误 %s" % e)

            else:
                # 作者存在的话，直接保存书籍数据到数据库
                # book = Book.query.filter(Book.name == book_name).first()

                # 列表推导式获取所有该作者下的书，不能直接author.books因为返回的是[book对象，而不是书名的list]
                book_names = [book.name for book in author.books]
                if book_name in book_names:
                    flash('该作者已存在相同的书名')
                else:
                    try:
                        book = Book(name=book_name, author_id=author.id)
                        database.session.add(book)
                        database.session.commit()
                    except Exception as e:
                        # 添加失败的话进行回退
                        database.session.rollback()
                        print(e)
                        flash('书籍添加错误 %s' % e)
        else:
            flash("参数错误")

    # 查询数据,进行每次的数据刷新
    authors = Author.query.all()
    books = Book.query.all()

    # 数据传入到模板
    return render_template('BookDemo.html', authors=authors, books=books, book_form=book_form)


@app.route('/delete_book/<book_id>')
def delete_book(book_id):

    try:
        book = Book.query.get(book_id)
    except Exception as e:
        return '查询错误 %s' % e

    if not book:
        return '书籍不存在'

    try:
        database.session.delete(book)
        database.session.commit()
    except Exception as e:
        database.session.rollback()
        return '书籍删除错误 %s' % e

    return redirect(url_for('index'))


@app.route('/delete_author/<author_id>')
def delete_author(author_id):

    try:
        author = Author.query.get(author_id)
    except Exception as e:
        return '查询错误 %s' % e

    if not author:
        return '作者不存在'

    try:
        # 删除author之前,先删除book多的那一方，因为有外键
        Book.query.filter(Book.author_id == author_id).delete()
        # 再删除指定作者
        database.session.delete(author)
        database.session.commit()
    except Exception as e:
        database.session.rollback()
        return '作者删除错误 %s' % e

    # 重定向首页进行刷新
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
