# 1.将元组 (1,2,3) 和集合 {4,5,6} 合并成一个列表
a1 = (1, 2, 3)
print(type(a1))
b1 = {4, 5, 6}
print(type(b1))
c1 = list(a1) + list(b1)
print(type(c1))
print(c1)

# 2.在列表 [1,2,3,4,5,6] 首尾分别添加整型元素 7 和 0
a2 = [1, 2, 3, 4, 5, 6]
a2.append(0)             # 在列表末尾添加一个元素,append()
print(a2)
a2.extend([8, 9])        # 在列表末尾添加多个元素,extend([])
print(a2)
a2.insert(0, 7)
print(a2)                # 在列表指定位置添加元素,insert(,)

# 3.反转列表 [0,1,2,3,4,5,6,7]
a3 = [0, 1, 2, 3, 4, 5, 6, 7]
a3.reverse()
print(a3)
print(a3[::-1])

# 4.反转列表 [0,1,2,3,4,5,6,7] 后给出中元素 5 的索引号
a4 = [0, 1, 2, 3, 4, 5, 6, 7]
b4 = a4[::-1]
print(b4)
print(b4.index(5))       # 找出列表元素的索引号index()

# 5.分别统计列表 [True,False,0,1,2] 中 True,False,0,1,2的元素个数，发现了什么
a5 = [True,  False, 0, 1, 2]
print(a5.count(True))
print(a5.count(False))
print(a5.count(0))
print(a5.count(1))       # count()不区分True和1,False和0,但None不等于0
print(a5.count(2))

# 6.从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除元素‘x’
a6 = [True, 1, 0, 'x', None, 'x', False, 2, True]
while 'x' in a6:
    a6.remove('x')
print(a6)

# 7.从列表 [True,1,0,‘x’,None,‘x’,False,2,True] 中删除索引号为4的元素
a7 = [True, 1, 0, 'x', None, 'x', False, 2, True]
del a7[4]
print(a7)

# 8.删除列表中索引号为奇数（或偶数）的元素
a8 = [True, 1, 0, 'x', None, 'x', False, 2, True]
# 方法一
result = []
for i in range(0, len(a8)):
    if i % 2 == 0:               # 通过控制余数来确定是奇数还是偶数
        result.append(a8[i])
print(result)
# 方法二
aa8 = [True, 1, 0, 'x', None, 'x', False, 2, True]
print(aa8[::2])                # 删除奇数
print(aa8[1::2])               # 删除偶数

# 9.清空列表中的所有元素
# 方法一
a9 = [True, 1, 0, 'x', None, 'x', False, 2, True]
a9 = []
print(a9)
# 方法二
aa9 = [True, 1, 0, 'x', None, 'x', False, 2, True]
aa9.clear()
print(aa9)

# 10.对列表 [3,0,8,5,7] 分别做升序和降序排列
a10 = [3, 0, 8, 5, 7]
a10.sort()                # 默认排序为升序
print(a10)
a10.sort(reverse=True)    # 降序排列
print(a10)