listA = [1, 2, 3, 4, 5]
# for 循环
for i in listA:
    print(i)

a = 'abcde'
b = "abcde"
c = "abc'de"
d = 'ab\'c"de'
# 所见即所得
e = r"ab\ncde"
f = "ab\\ncde"
for i in a:
    print(i)
print(e)
print(f)

# enumerate函数 可以给我们的序列加上一个索引
for i, j in enumerate(listA):
    print(i, j, sep="\t")

listB = [1, 2, 3, 4, 9]
listC = [5, 6, 7, 8]
for i in zip(listB, listC):
    print(i)

tupA = (1, 2, 3, 4)
# 如果元组只有1个元素，那么在初始化的时候需要加上一个 ,
tupB = (1,)
for i in tupA:
    print(i)
print(type(tupB))

# 遍历字典
dictA = {"a": 1, "b": 2, "c": 3}
for i in dictA:
    print(i, end=" ")
    print(dictA[i])

for k, v in dictA.items():
    print(k, v)

for k in dictA.keys():
    print(k)

if "d" in dictA:
    print(dictA["d"])

# 从dict里取key的时候，可以使用get函数，指定一个默认值
# 如果没有取到key，则返回默认值
print(dictA.get("d", "null"))

setA = {1, 2, 2, 3, 4, 5}
for i in setA:
    print(i)

# 计算1~100的累加值
# range 函数 给定两个参数
# 返回一个 含头不含尾 范围的 list、
sum = 0
for i in range(0, 101):
    sum += i
print(sum)
