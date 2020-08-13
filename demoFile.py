# 使用open 打开一个文件
f = open("students.txt", encoding="utf-8")

# 直接读所有行
# for i in f.readlines():
#     # strip() 这个函数可以去除 一行数据 两边的 隐藏字符
#     # \n \t 空格
#     print(i.strip())


# 读取一行数据
# print("*" * 100)
# for i in range(100):
#     print(f.readline())

# 读取指定个字符
print(f.read(13))
# 用完记得关闭
f.close()

listA = ["java", "scala", "python", "hadoop"]

# mode : r w x a
# r : 读文件模式 read 默认值
# w : 覆盖写 overwrite
# x : 写模式，写之前会创建一个新的文件，如果文件存在就报错
# a : 追加模式 append
w = open("a.txt", mode="a")
for i in listA:
    w.write(i)
    w.write("\n")

# 使用完文件后 记得 关闭
w.close()

# 如果不想使用close来关闭文件，可以使用下面这种写法
# 代码执行完以后 会自动释放（自动关闭）
with open("b.txt", mode="w") as w:
    for i in listA:
        w.write(i)
        w.write("\n")
