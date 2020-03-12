# 21.以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有键值对组成的元组
a21 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
b21 = a21.keys()
c21 = a21.values()
print(b21)
print(c21)
d21 = list(zip(b21, c21))
print(d21)

# 22.向字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中追加 ‘David’:19 键值对，更新Cecil的值为17
a22 = dict(Alice=20, Beth=18, Cecil=21)
a22['David'] = 19
a22['Cecil'] = 17
print(a22)

# 23.删除字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中的Beth键后，清空该字典
a23 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
a23.pop('Beth')
print(a23)
a23.clear()
print(a23)

# 24.判断 David 和 Alice 是否在字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中
a24 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
if 'David' in a24.keys():
    print('True')
else:
    print('False')

# 25.遍历字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21}，打印键值对
a25 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
# 遍历字典中的键
for key in a25.keys():
    print(key)
# 遍历字典中的值
for value in a25.values():
    print(value)
# 遍历字典中的元素
for item in a25.items():
    print(item)

# 26.若 a = dict()，令 b = a，执行 b.update({‘x’:1})， a亦被改变。为何？如何避免？
a26 = dict()
b26 = a26
b26.update({'x': 1})
print(b26)
print(a26)
# 避免
c26 = dict()
d26 = c26.copy()
d26.update({'x': 1})
print(d26)
print(c26)

# 27.以列表 [‘A’,‘B’,‘C’,‘D’,‘E’,‘F’,‘G’,‘H’] 中的每一个元素为键，默认值都是0，创建一个字典
# 方法一
a27 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
b27 ={}
for i in range(0, len(a27)):
    b27[a27[i]] = 0
print(b27)
# 方法二
c27 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
d27 = [0]*len(c27)
print(dict(zip(c27, d27)))

# 28.将二维结构 [[‘a’,1],[‘b’,2]] 和 ((‘x’,3),(‘y’,4)) 转成字典
a28 = [['a', 1], ['b', 2]]
b28 = (('x', 3), ('y', 4))
print(dict(a28))
print(dict(b28))

# 29.将元组 (1,2) 和 (3,4) 合并成一个元组
a29 = (1, 2)
b29 = (3, 4)
c29 = a29 + b29
print(c29)

# 30.将空间坐标元组 (1,2,3) 的三个元素解包对应到变量 x,y,z
a30 = (1, 2, 3)
(x, y, z) = a30
print(x)
print(y)
print(z)