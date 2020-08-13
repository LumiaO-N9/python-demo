# 每次只能导入 某个 packages的一个模块
# 如果一个 packages 下有很多模块 需要 单独导入
# from package2 import test2 as t
# import package2.test2 as t
# from package2.test3 import *

# 每个模块里的所有函数 可以使用 * 一次性导入
import site
import sys

from mulu import mulu

mulu.mulu("abcdef")

from package2.test3 import fun3
from package2.test3 import fun4
from package2.test3 import fun5
from package2.test3 import *

# 导入的时候 也可以 重新取个别名

from package2.test3 import fun3 as f3

f3("abc")
# 如果代码没有写在main方法中，当被其他模块引用的时候，会被执行
print("hello World1!")

a = 2


def squar(x):
    return x ** 2


# sys.modules 可以查看 当前文件 引入了 哪些模块
print(sys.modules)

# 查看python程序运行时的环境变量
# 使用pip 安装的packages
# 会默认 保存在 python 安装目录下的 lib/site-packages/
print(sys.path)

print(site.getsitepackages())

# python里面的main方法
if __name__ == '__main__':
    print("hello World2!")
