# 41.判断两个集合 {‘A’,‘D’,‘B’} 和 {‘D’,‘E’,‘C’} 是否有重复元素
a41 = {'A', 'D', 'B'}
b41 = {'D', 'E', 'C'}
# 方法一
if a41 & b41:
    print('True')
else:
    print('False')
# 方法二
print(a41.isdisjoint(b41))        # 有重复元素，返回False,无返回True

# 42.判断集合 {‘A’,‘C’} 是否是集合 {‘D’,‘C’,‘E’,‘A’} 的子集
a42 = {'A', 'C'}
b42 = {'D', 'C', 'E', 'A'}
print(a42.issubset(b42))

# 43.去除数组 [1,2,5,2,3,4,5,‘x’,4,‘x’] 中的重复元素
a43 = [1, 2, 5, 2, 3, 4, 5, 'x', 4, 'x']
b43 = set(a43)
print(list(b43))

# 44.返回字符串 ‘abCdEfg’ 的全部大写、全部小写和大下写互换形式
a44 = 'abCdEfg'
print(a44.upper())
print(a44.lower())
print(a44.swapcase())

# 45.判断字符串 ‘abCdEfg’ 是否首字母大写，字母是否全部小写，字母是否全部大写
a45 = 'abCdEfg'
print(a45.istitle())
print(a45.isupper())
print(a45.islower())

# 46.返回字符串 ‘this is python’ 首字母大写以及字符串内每个单词首字母大写形式
a46 = 'this is python'
print(a46.capitalize())
print(a46.title())

# 47.判断字符串 ‘this is python’ 是否以 ‘this’ 开头，又是否以 ‘python’ 结尾
a47 = 'this is python'
print(a47.startswith('this'))
print(a47.endswith('python'))

# 48.返回字符串 ‘this is python’ 中 ‘is’ 的出现次数
a48 = 'this is python'
print(a48.count('is'))

# 49.返回字符串 ‘this is python’ 中 ‘is’ 首次出现和最后一次出现的位置
a49 = 'this is python'
print(a49.find('is'))
print(a49.rfind('is'))

# 50.将字符串 ‘this is python’ 切片成3个单词
a50 = 'this is python'
b50 = a50.split(' ')
print(b50)
for i in b50:
    print(i)