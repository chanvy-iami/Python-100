# 31.返回元组 (‘Alice’,‘Beth’,‘Cecil’) 中 ‘Cecil’ 元素的索引号
a31 = ('Alice', 'Beth', 'Cecil')
print(a31.index('Cecil'))

# 32.返回元组 (2,5,3,2,4) 中元素 2 的个数
a32 = (2, 5, 3, 2, 4)
print(a32.count(2))

# 33.判断 ‘Cecil’ 是否在元组 (‘Alice’,‘Beth’,‘Cecil’) 中
a33 = ('Alice', 'Beth', 'Cecil')
print('Cecil' in a33)

# 34.返回在元组 (2,5,3,7) 索引号为2的位置插入元素 9 之后的新元组
a34 = list((2, 5, 3, 7))
a34.insert(2, 9)
print(tuple(a34))

# 35.创建一个空集合，增加 {‘x’,‘y’,‘z’} 三个元素
a35 = set()
print(type(a35))
a35.update({'x', 'y', 'z'})
print(a35)

# 36.删除集合 {‘x’,‘y’,‘z’} 中的 ‘z’ 元素，增加元素 ‘w’，然后清空整个集合
a36 = {'x', 'y', 'z'}
print(type(a36))
a36.remove('z')
print(a36)
a36.add('w')
print(a36)
a36.clear()
print(a36)

# 37.返回集合 {‘A’,‘D’,‘B’} 中未出现在集合 {‘D’,‘E’,‘C’} 中的元素（差集）
a37 = {'A', 'D', 'B'}
b37 = {'D', 'E', 'C'}
print(a37.difference(b37))

# 38.返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的并集
a38 = {'A', 'D', 'B'}
b38 = {'D', 'E', 'C'}
print(a38.union(b38))

# 39.返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 的交集
a39 = {'A', 'D', 'B'}
b39 = {'D', 'E', 'C'}
print(a39.intersection(b39))

# 40.返回两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 未重复的元素的集合
a40 = {'A', 'D', 'B'}
b40 = {'D', 'E', 'C'}
print(a40 ^ b40)
print(a40.symmetric_difference(b40))