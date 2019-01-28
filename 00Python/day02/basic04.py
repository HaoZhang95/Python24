"""
    if else 语句
"""

flag = True
if flag:
    print("你没有危险物品")
print("if语句结束，缩进代表是不是和if为一体")

my_password = "12345"
if my_password == "12345":
    print("密码正确")
else:
    print("密码错误")

a = 10
b = 20
if a >= b:
    print("a大于等于b")
else:
    print("a不大于等于b")


"""
    逻辑运算符：与或非, and or not
"""
my_name = "admin"
my_passwd = "12345"
if (my_name == "admin") and (my_passwd == "12345"):
    print("登陆成功，用户名和密码都正确")

if (my_name != "admin") or (my_passwd != "12345"):
    print("用户名或者密码错误")

is_man = False
is_woman = not True
if not is_man:
    print("假男人")



