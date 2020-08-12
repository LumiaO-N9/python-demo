a = "abc"
A = "bcd"
print(a)
print(A)

# 1b = "x" 变量的命名只能以下划线或字母开头，不能以数字开头
# 只能包含 字母 数字 _  大小写敏感
# 不能使用关键字 class

_b = "x"
print(_b)

# 查看python中的关键字
import keyword

print(keyword.kwlist)
# type()函数可以查看变量的类型
print(type(a))
a = 1
# 动态类型，声明变量的时候，不需要指定类型，
# 程序会自动根据我们所赋的值去判断变量是什么类型
print(type(a))

# 常量
# Java中的常量是不可改变的
# Python中常量用全大写的变量名表示
# 但这只是业界约定，可以修改，但最好不要
# 实际上python中是没有常量的
PI = 3.1415926535

c: int = 1
c = "abc"
print(c)

# 这是一条注释 单行注释
"""
多行注释
这也是一个注释
注释
。。。
"""

'''
这同样也是一个注释
。。
。。
。
'''

print("打印函数")

x = "你好"
y = "中国"
# *args "*" 号表示可变参数，可以传入任意个参数
print(x, y, x, y)

# 参数
# *args 可变参数
# sep=' ', end='\n'
# sep : 输出的分割符
# end ：指定输出最后的字符
print(x, y, sep="|")
print("hello ", end="")
print("world ")

print(1 + 1)

print(type(1))
print(type(1.1))
print(True)
print(False)
print(type(True))
print(type(None))

p = "abcdefg"
print(p)
for i in p:
    print(i)

# & and 都表示 与 运算
print(True & False)
print(True and False)
# | or 都表示  或 运算
print(True | False)
print(True or False)
# 取反
print(not True)

a = 10
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
# 向下取整，直接把小数位舍弃，取整数位
print(a // b)
# ** 表示乘方
print(a ** b)
# python 中没有 a++ / a-- / ++a / --a
# 可以使用 a+=1 a=a+1


# 数据类型转换
# int() float() str() bool()
a = 1
b = "123"
a = int(b)
print(a)
print(type(a))

a = 1
b = "123"
b = str(a)
print(b)
print(type(b))

# 在使用bool()进行类型转换的时候，只能把 int 类型的 0 转成 False
# 其他的都为True
print(bool(1))  # True
print(bool(0))  # False
print(bool("0"))  # True
print(bool("False"))  # True

a = "123"
print(isinstance(a, int))
print(isinstance(a, str))
