"""
    如果在类的外面取值和修改私有属性的值，需要自己定义get/set方法
"""

class Person(object):

    def __init__(self):
        self.name = "老王"
        self.__age = 20

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

p = Person()
print(p.name)

p.name = "王五"
print(p.name)

print(p.get_age())
p.set_age(28)
print(p.get_age())

"""
    多态，因为python是弱引用类型，并不关注参数的类型，所以需要自己打出obj.eat()的方法
"""

"""
    1- 实例属性就是对象属性， 和类属性不是一回事
    2- 对象创建的属性叫做实例属性， 类中的属性叫做类属性 
    3- 如果想使用类属性，直接大写Student.num即可, 或者s1.num
    4- 但是修改类属性的值只能通过Student.num
    5- 类方法需要添加修饰器@classmethod, 每个对象都自动拥有的方法，只有一份的属性和方法
"""
class Student(object):

    # 类属性，每个创建的对象都有这个num的属性，不会为类属性单独的开辟多份内存
    # 多个对象共享一份类属性，修改的话，每个对象的num都会更改，全变了
    # 如果想在类的外面修改类私有属性，使用类方法
    num = 0
    __sex = "Male"

    @classmethod
    def get_sex(cls):
        return cls.__sex

    @classmethod
    def set_sex(cls, sex):
        cls.__sex = sex

    def __init__(self, name, age, country = "中国"):
        self.name = name
        self.age = age
        self.country = country

s1 = Student("小明", 22)
s2 = Student("小红", 28)

s1.city = "石家庄"
print(s1.city)          # 实例属性
print(Student.num)      # 类属性
print(s1.num)

Student.num = 200
print(s1.num)
print(s2.num)

print(Student.get_sex())
Student.set_sex("Female")
print(Student.get_sex())

print(s1.get_sex())
s1.set_sex("Male")
print(Student.get_sex())

"""
    静态方法，并没有self或者cls
    类中存在的方法只有三个， 类方法， 对象方法， 静态方法
    1- 如果在类的内部想使用self --> 对象方法
    2- 如果在类的内部想使用cls --> 类方法
    3- 如果在类的内部不使用self和cls --> 静态方法
"""
class Teacher(object):

    __country = "中国"

    def __init__(self):
        self.__age = 10

    # 类方法-用来读写类属性的
    @classmethod
    def get_country(cls):
        return cls.__country

    # 对象方法
    def get_age(self):
        return self.__age

    # 静态方法- Teacher.say_hello()或者t1.say_hello()都可以访问
    @staticmethod
    def say_hello():
        print("Hello Python.")

Teacher.say_hello()
t1 = Teacher
t1.say_hello()
