import functools


def user_login_data(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper


@user_login_data
def num1():
    print("aaa")


@user_login_data
def num2():
    print("bbb")


if __name__ == '__main__':
    print(num1.__name__)
    print(num2.__name__)
