# 11.将列表 [3,0,8,5,7] 中大于 5 元素置为1，其余元素置为0
a11 = [3, 0, 8, 5, 7]
for i in range(0, len(a11)):
    if a11[i] > 5:
        a11[i] = 1
    else:
        a11[i] = 0
print(a11)

# 12.遍历列表 [‘x’,‘y’,‘z’]，打印每一个元素及其对应的索引号
a12 = ['x', 'y', 'z']
for i in range(0, len(a12)):
    print(a12[i], i)

# 13.将列表 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 拆分为奇数组和偶数组两个列表
a13 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result1 = []         # 奇数组
result2 = []         # 偶数组
for i in range(0, len(a13)):
    if a13[i] % 2 == 1:
        result1.append(a13[i])
    else:
        result2.append(a13[i])
print(result1)
print(result2)

# 14.分别根据每一行的首元素和尾元素大小对二维列表 [[6, 5], [3, 7], [2, 8]] 排序
a14 = [[6, 5], [3, 7], [2, 8]]
print(a14)
b14 = sorted(a14, key=lambda x: x[0])
print(b14)
c14 = sorted(a14, key=lambda x: x[-1], reverse=True)
print(c14)


# 15.从列表 [1,4,7,2,5,8] 索引为3的位置开始，依次插入列表 [‘x’,‘y’,‘z’] 的所有元素
# 方法一
a15 = [1, 4, 7, 2, 5, 8]
b15 = ['x', 'y', 'z']
j = 3
for i in range(0, len(b15)):
    a15.insert(j, b15[i])
    j = j + 1
print(a15)
# 方法二
aa15 = [1, 4, 7, 2, 5, 8]       # 方法二错误
bb15 = ['x', 'y', 'z']
aa15.insert(3, bb15)
print(aa15)
# 方法三
aaa15 = [1, 4, 7, 2, 5, 8]
bbb15 = ['x', 'y', 'z']
aaa15[3:3] = bbb15
print(aaa15)

# 16.快速生成由 [5,50) 区间内的整数组成的列表
# 方法一
a16 = []
for i in range(5, 50):
    a16.append(i)
print(a16)
# 方法二
print(list(range(5, 50)))

# 17.若 a = [1,2,3]，令 b = a，执行 b[0] = 9， a[0]亦被改变。为何？如何避免
a17 = [1, 2, 3]
b17 = a17
b17[0] = 9
print(b17)
print(a17)
# 避免
c17 =[1, 2, 3]
d17 = c17.copy()
d17[0] = 9
print(d17)
print(c17)

# 18.将列表 [‘x’,‘y’,‘z’] 和 [1,2,3] 转成 [(‘x’,1),(‘y’,2),(‘z’,3)] 的形式
a18 = ['x', 'y', 'z']
b18 = [1, 2, 3]
c18 = list(zip(a18, b18))
print(c18)

# 19.以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的键
a19 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print(a19.keys())
b19 = list(a19.keys())
print(b19)

# 20.以列表形式返回字典 {‘Alice’: 20, ‘Beth’: 18, ‘Cecil’: 21} 中所有的值
a20 = {'Alice': 20, 'Beth': 18, 'Cecil': 21}
print(a20.values())
b20 = list(a20.values())
print(b20)