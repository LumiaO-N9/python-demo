# 集合 也是用{}花括号定义 需要与dict区分
# 集合中的数据唯一
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

print(setA and setB)
print(setA or setB)
print(setA ^ setB)
print(setA - setB)

# set会对里面的元素自动去重
setC = {1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6}
print(setC)
