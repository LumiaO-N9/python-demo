# 如果代码没有写在main方法中，当被其他模块引用的时候，会被执行
print("hello World1!")
# python里面的main方法
if __name__ == '__main__':
    print("hello World2!")