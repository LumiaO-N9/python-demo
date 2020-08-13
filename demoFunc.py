# 使用def定义一个函数
def point(s):
    print(s)


# 调用一个函数
# python 也是一门面向函数的变成语言
# 不需要依赖于 类 或者 对象
# 可以直接调用
point("helloWorld")


# 计算阶乘
# 5! = 5*4*3*2*1
# 使用递归函数来实现
# 如果能用循环，尽量避免使用递归
def a(x):
    # 需要给定结束条件
    if x == 1:
        return 1
    # 自己调用自己
    return x * a(x - 1)


print(a(5))


# 计算一个数的平方
def squar(x):
    return x ** 2


print(squar(10))

# 使用lambda关键字 定义一个lambda表达式
# 以冒号 分成 左右两部分，左边代表 输入的参数
# 右边表示 函数体 同样也表示 返回值
func1 = lambda x: x ** 2
print(func1(10))

func2 = lambda x, y: x * y
print(func2)
print(func2(10, 20))


def b(x):
    if x < 0:
        return -x
    return x


listA = [1, -2, 3, -4, 5]
listA.sort(key=lambda x: b(x))
print(listA)
