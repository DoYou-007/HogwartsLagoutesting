'''
数据结构：list 、tuple、dict、set
'''
a = []
print(a, type(a))
a.append(23)
print(a)
b = (2, 'ih', 0, 'sha')
a.extend(b)  # 添加可遍历元素
print(a)
b = [2, 4, 1, 45, 64, 3, 45, 7, 56, 9]
c = ['ni', 'ha', 'lj', 'ie', 'vb']
# print(b.sort())
# print(b)
# print(c.sort())
print(c)
b.reverse()
print(b)

a = [i for i in range(20) if i % 2 == 0]
b = [i * j for i in (1, 10) for j in range(10)]
list_squre = []
for i in range(1, 10):
    for j in range(10):
        list_squre.append(i * j)
print(list_squre)
print(a)
print(b)

a = (10, 23, 'e', 90)
print(type(a))
print(a.count(10))
print(a.index(23))
b = (10, 23, 'e', 90, [20, 34])
b[4][0] = 'jp'
print(b)

set_l1 = set()
print(type(set_l1))
