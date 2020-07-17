# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/16 13:20
# @Author   : XFbeibei.
# @File     : os_moudle.py
# @Software : PyCharm

import os

# os.mkdir('OsTest')
print(os.getcwd())  # 获取当前文件目地址
print(os.listdir('../'))  # 获取当前目录有哪些文件
print(os.path.exists('OsTest'))

# if os.path.exists('OsTest'):
#     os.removedirs('OsTest')

if not os.path.exists("b"):
    os.mkdir('b')
if not os.path.exists('b/test.txt'):
    f = open("b/test.txt", 'w')
    f.write('hello os module')
    f.close()
