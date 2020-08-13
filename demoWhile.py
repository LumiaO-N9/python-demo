# 使用while循环 计算 1~100的累加值
i = 0
sum = 0
while i <= 100:
    sum += i
    # i = i + 1
    i += 1
print(sum)

listA = [1, 2, 3, 4, 5]
listB = []
for i in listA:
    listB.append(i ** 2)
print(listB)

# 列表推导式
listC = [i ** 2 for i in listA]
print(listC)

# 9 9 乘法表
# 使用两个for循环
for i in range(1, 10):
    for j in range(1, (11 - i)):
        print(i, "*", j, "=", i * j, " ", end="")
    print()

# 使用列表推导式


print("\n".join(['\t'.join(['{}*{}={}'.format(j, i, i * j) for j in range(1, 1 + i)]) for i in range(1, 10)]))

listD = ["1", "2", "3", "4", "5"]
print(listD)
print("|".join(listD))
i = 10
j = 5
p = i * j

# i*j = p
# 10*5 = 50
print(str(i) + "*" + str(j) + "=" + str(p))
strFormat = "{}*{}={}"
print(strFormat.format(i, j, p))

print("\n".join(["\t".join(["{}*{}={}".format(j, i, i * j) for j in range(1, 1 + i)]) for i in range(1, 10)]))

print("\n".join(["\t".join(["{}*{}={}".format(j, i, i * j) for j in range(1, 1 + i)]) for i in range(1, 10)]))
