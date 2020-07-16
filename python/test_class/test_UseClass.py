# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/14 13:19
# @Author   : XFbeibei.
# @File     : test_UseClass.py
# @Software : PyCharm

"""
类的创建：
类变量、类方法
调用类变量及方法
"""


class People():
    name = 'noname'

    def get_name(self):
        return self.name


print(People.name)
a = People()
print(a.name)
print(a.get_name())

a.name = '实例'
print(a.name)
print(People.name)
People.name = '类变量'
print(a.name)
a1 = People()
print(a1.name)
