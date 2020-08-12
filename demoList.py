# 使用[] 定义一个 List
# 有序，可以重复，每个元素的类型可以不同
list1 = [1, 1, 2, 3, 4, "abc", "efg"]
print(list1)
print(type(list1))
print(type(list1[0]))
print(type(list1[5]))
# 增加一个元素
list1.append("java")
print(list1)
# 删除一个元素
del list1[0]
list1.remove("abc")
list1.pop(0)
print(list1)
# 取出一个元素,使用[索引]
# 索引从 0 开始
print(list1[2])

# 修改一个元素
list1[2] = "scala"
print(list1)

# 切片
# 开始位置:结束位置:步长
# -1 表示 list 最后一个位置
print(list1[0::2])

# list反转
print(list1[::-1])

# 清空list
list1.clear()
print(list1)

listA = [1, 2, 3]
listB = [4, 5, 6]
# 合并两个list
print(listA + listB)
listA.extend(listB)
print(listA)

# 反转
listA.reverse()
print(listA)

# 排序 不指定reverse参数 默认为False 表示 升序排序
listC = [1, 3, 2, 4526, 12341, 342, 55, 88, 333]
listC.sort(reverse=True)
print(listC)

# 检查是否包含某个元素
print(45261 in listC)

# 按照给定的索引位置插入一个元素
listD = [0, 1, 2, 3]
listD.insert(1, "java")
print(listD)

# 查看list长度
print(len(listD))

# 二维列表
listE = [[1, 2, 3], [4, 5, 6]]
print(listE)
print(listE[0][1])
