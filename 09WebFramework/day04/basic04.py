"""
    ORM是django的核心思想, object-related-mapping对象-关系-映射

    ORM核心就是操作数据库的时候不再直接操作sql语句，而是操作对象
    定义一个类，类中有uid,username等类属型，sql语句insert修改的时候直接插入这个User对象
"""


# ORM映射实现原理，通过type修改类对象信息
# 定义这个元类metaclass
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):

        # name --> User
        # bases --> object
        # attrs --> {
        #       "uid" :('uid', "int unsigned"),
        #       "name": ('username', "varchar(30)"),
        #       "email": ('email', "varchar(30)"),
        #       "password": ('password', "varchar(30)"),
        #       "__init__":  xxx,
        #       "save":  xxx2,
        #     }

        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是元组类型
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)    # 等于del attrs[k]

        # 将之前的uid/name/email/password以及对应的对象引用、类名字
        # attrs = {
            # "__init__": xxxx,
            # "save": xxxx2,
            # "__mappings__": {
            #     "uid": ('uid', "int unsigned"),
            #     "name": ('username', "varchar(30)"),
            #     ""email: ('email', "varchar(30)"),
            #     "password": ('password', "varchar(30)")
            # },
            # "__table__": "User"
        # }
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMetaclass):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")
    # 当指定元类之后，以上的类属性将不在类中，而是在__mappings__属性指定的字典中存储
    # 以上User类中有
    # __mappings__ = {
    #     "uid": ('uid', "int unsigned")
    #     "name": ('username', "varchar(30)")
    #     "email": ('email', "varchar(30)")
    #     "password": ('password', "varchar(30)")
    # }
    # __table__ = "User"

    # 参数名是kwargs，不是**kwargs，**只是告诉解释器将传来的参数变为字典
    # for循环遍历__new__返回的attrs字典，实现实例对象的属性和方法赋值
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []     # ["uid", "username"...]
        args = []       #[12345, "laowang"...]

        # 创建的实例对象中没有__mapping__，去类对象中找
        # k --> uid,  v --> 12345
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = list()

        for temp in args:
            if isinstance(temp, int):
                # 判断如果是数字类型
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                # 判断如果是字符串类型
                args_temp.append("""'%s'""" % temp)

        # sql = 'insert into %s (%s) values (%s);' \
        #       % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))

        # 使用",".join为每一个字段后都插入逗号分隔
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))

        print('SQL: %s' % sql)


# 抽取为基类，再创建User2这个类，就直接让其继承Model类
class Model(object, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = list()
        for temp in args:
            # 判断入如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)


class User2(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


def test01():
    u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')
    # print(u.__dict__)
    u.save()


def test02():

    list = ['12356', "laowang", "email"]
    print(",".join(list))


def main():
    # test01()
    test02()


if __name__ == '__main__':
    main()

