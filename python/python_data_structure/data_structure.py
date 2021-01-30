"""
命名规则：
1.以字母、数字、下划线组合而成，不能够以数字开头或者特殊字符
2.变量的大小写是敏感的
3.不能与特殊关键字或者系统保留字（如函数、模块等）冲突
"""

int_a = 2
float_a = 0.2
complex_a = 0.2j
print(type(int_a),type(float_a),type(complex_a))

#字符串
a = 'aaaaa'
b = 'bbbbb'
print('转译符号演示：好的\t换行')
print(r'忽略转译符号演示：好的\t换行')
print("连接符号演示：",a + b)
print(f"引用演示：a.format{b}")

#列表
a= [1,2,3,4,5,6,7,8,9]
#索引
print(a[4])
#切片
print(a[2:7:2])
