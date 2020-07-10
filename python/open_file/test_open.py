f = open('D:\pycharmfile\HogwartsLagoutesting\python\open_file\\txtfile', 'r')
# print(f.readlines())  #readlines 和 read两个只能使用一个
print('------------------')
print(f.readline(), end='')
print(f.readline())
print(f.readline())
print(f.readable())
f.close()

with open('D:\pycharmfile\HogwartsLagoutesting\python\open_file\\txtfile', 'r+') as f:
    f.write('我是新加入的1号')
    f.write('我是新加入的2号')

##还有待补充其他文件操作形式
