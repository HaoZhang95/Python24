import unittest

from demo.demo5 import app


class DatabaseTestCase(unittest.TestCase):

    """
        测试数据库的添加i和删除，需要设置一个单独的数据库，不能使用真实的数据库
    """

    def setUp(self):
        """单元测试开始之前执行的操作"""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@localhost/test0'
        self.app = app
        db.create_all()


    def tearDown(self):
        """单元测试结束后执行的操作"""

        # db.session类似于数据库的连接
        db.session.remove()
        db.drop_all()

    def test_append_data(self):
        """"""
        au = Author(name='itcast')
        bk = Book(info='python')
        db.session.add_all([au, bk])
        db.session.commit()
        author = Author.query.filter_by(name='itcast').first()
        book = Book.query.filter_by(info='python').first()
        #断言数据存在
        self.assertIsNotNone(author)
        self.assertIsNotNone(book)