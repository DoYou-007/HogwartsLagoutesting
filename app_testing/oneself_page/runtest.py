# conding :utf-8

import unittest
import time
from config.globalparameter import test_case_path, report_name
from src.common import send_email
from src.common.HTMLTestReport import HTMLTestRunner

"""构建测试套件，并执行测试"""

# 构建测试集，包含src/testsuite目录下的所有以test开头的.py文件
print(test_case_path)
suite = unittest.defaultTestLoader.discover(start_dir=test_case_path, pattern='test*.py')

if __name__ == '__main__':
    print("日志保存路径",report_name)
    report = report_name + "Report.html"
    print("日志文件名称",report)
    fb = open(report, 'wb')
    runner = HTMLTestRunner(stream=fb, title=u'测试平台搭建', description=u'测试Team')
    runner.run(suite)
    fb.close()
    email = send_email.send_email()
    email.sendReport()