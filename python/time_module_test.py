# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/16 13:37
# @File     : time_module_test.py

import time

print(time.asctime())  # 国外时间格式
print(time.time())  # 时间戳
print(time.localtime())  # 时间戳转换成元组
print(time.strftime("%Y-%M-%d %H-%M-%S", time.localtime()))  # 转换为指定格式
