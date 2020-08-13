class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def point(self):
        print(self.name, self.age)


# python中继承 不需要使用extends关键字
# 直接将需要继承的父类 放入 括号中
class Student(Person):
    # 初始化方法，创建对象时会默认调用此方法
    # 通常 会在 __init__ 函数 里 做一些初始化操作
    # 比如 ： 建立数据库连接
    def __init__(self, id, name, age):
        # python 成员变量
        # 赋值即定义
        # 注意需使用父类的初始化函数时
        # 需要 super() :注意要加上括号
        super().__init__(name, age)
        self.id = id
        # self.__attr = "成员变量" # “私有属性”

    # 定义一个类的方法：成员方法
    # 只能同过对象调用
    # 如果 父类中有同名的函数 那么 在子类 可以继承过来
    # 当然 也可以重写该函数
    def point(self):
        print(self.id, self.name, self.age)


# 创建一个对象
s1 = Student("123456", "张三", "18")
print(s1.name)
print(s1.age)
# 虽然通过 对象名.xxxx 不能 直接 获取 私有属性
# 但可以通过下面这种方式拿到
# print(s1._Student__id)

s1.point()
