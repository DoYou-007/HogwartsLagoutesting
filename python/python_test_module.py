import sys
import numpy

print('调用了内置模块sys:查看当前路径')
for i in sys.argv:
    print(i)

a = numpy.arange(15).reshape(3, 5)  # 生成一个三行五列 矩阵数组
print(a)
