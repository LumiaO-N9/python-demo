print("abc")
# pinrt("abc")aa
if 1 == 1:
    print("bcd")
a = "abc"


# 类型转换异常
# b = int(a)

# 除零异常
# print(10 / 0)

# 函数在调用的时候 需要先定义
# func()


def func():
    print("abc")


a = 1
# 类型错误
# b = a + "a"

# 值错误
# float("12a")

# 索引错误
listA = [1, 2, 3, 4, 5]
print(listA[4])
# 索引错误
# listA[5]
# 属性错误
# listA.appendA

# 自己处理异常
# try except


try:
    a = 10
    b = 0
    print("异常发生前")
    # a / b  # 这里会发生异常 后面的代码就不会继续执行了
    # 如果在 except 中捕获了该异常，那么就会直接跳到 异常处理的地方
    print("异常发生后")
    # 如果只写except 则表示捕获所有异常
except (ZeroDivisionError):
    print("除零异常")
# 如果没有异常 则 执行 else中的代码块
else:
    print("没有发生异常")
finally:
    print("不管有没有异常，都会执行")


# 自己定义一个异常
class MyException(Exception):
    # 如果什么都不写，可以使用 pass 做个占位符
    pass


def a(x, y):
    if y == 0:
        # 手动抛出一个异常
        raise MyException("除零错误")
    return x / y


print(a(5, 2))
try:
    a(10, 0)
except (MyException):
    print("捕获到了自己定义的异常")
