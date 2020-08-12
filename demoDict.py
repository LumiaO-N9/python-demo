# 字典  使用花括号{}定义，但是花括号中的数据 都是 k:v 格式的
# 可以用于存储 需要快速查找的数据
# 字典是无序的，key值不能重复，key必须为不可变对象
dictA = {1: "a", 2: "b", 3: "c"}
print(type(dictA))
print(dictA)

# key必须为不可变对象，list 是可变对象 不能作为dict的key
# list1 = [1, 2, 3]
# dictB = {list1: "abc"}
# print(dictB)

# 元组是不可变的，所以可以作为dict的key
tup1 = (1, 2, 3)
dictC = {tup1: "abc"}
print(dictC)
