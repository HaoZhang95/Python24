# 公用的自定义工具类
import functools

from flask import session, current_app, g

from info.models import User


def do_index_class(index):
    """返回指定索引对应的类名"""
    if index == 0:
        return 'first'
    elif index == 1:
        return 'second'
    elif index == 2:
        return 'third'

    return ""


def user_login_data(func):
    """
        因为多处页面需要检测当前用户是否登陆，多疑抽取出来，可以使用一个独立的方法，或者使用装饰器模式
        需要重写wrapper这个函数并且直接返回该wrapper，当被修饰的函数执行的时候，编译遇到装饰器就执行wrapper里面的
        wrapper方法，在这里执行重复的代码，并且把结果赋值给应用级别的全局变量，然后返回一个执行函数
        这样就能确保在执行函数之前就把值赋好。
    :param func: 被装饰的函数
    :return:
    """

    # 使用@functools.wraps(func)去装饰内层函数，用来保持当前装饰器装饰的函数的__name__的值不变
    # 否则的话，被装饰函数的__name__就会变为return的wrapper名字，如果在同意模块下views中有多个函数使用了同一个装饰器
    # 那么系统就会报错，因为名字都叫做该模块下的wrapper，比如news.wrapper，这样url_map中就会出现重复，所以报错
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get('user_id', None)
        user = None
        if user_id:
            try:
                user = User.query.get(user_id)
            except Exception as e:
                current_app.logger.error(e)
        # 把查询出来的数据赋值给g变量
        g.user = user

        return func(*args, **kwargs)

    return wrapper


def query_user_data():
    user_id = session.get('user_id', None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    return user
