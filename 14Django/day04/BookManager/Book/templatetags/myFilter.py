from django.template import Library

# 注册过滤器对象,注册对象必须命名为register
register = Library()


# 使用装饰器，装饰该方法
@register.filter
def mod(num):
    """判断奇数偶数， 返回0/1，非零即一，返回一个boolean"""
    return num % 2


@register.filter
def mod2(num1, num2):
    """对任意num2进行取模"""
    return num1 % num2


