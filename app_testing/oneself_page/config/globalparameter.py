# coding:utf-8
import time, os

'''
配置全局参数
'''

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# project_path1=os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]),'.'))
print (project_path)
# print (project_path1)

# 配置文件存放路径
# config_file_path = project_path + '/config.ini/config.ini'
# config_file_path = project_path + '\\config\\config.ini'
config_file_path = os.path.join(project_path,'config/config.ini')
print(config_file_path)
# 浏览器驱动存放路径
# chrome_driver_path = project_path + '\\driver\\chromedriver'
ie_driver_path = project_path + '\\driver\\IEDriverServer'
chrome_drvier_new_file = os.path.join(project_path,'driver/chromedriver')

# execl测试数据文档存放路径
test_data_path = project_path + "\\data\\testData.xlsx"

# 日志文件存储路径
log_path = project_path + "\\log\\mylog.log"
print("日志路径:" + log_path)
# 测试报告存储路径，并以当前时间作为报告名称前缀
report_path = project_path + "/report/"
# report_path = os.path.join(project_path,'report')
report_name = report_path + time.strftime('%Y%m%d%H%S', time.localtime())
# 异常截图存储路径,并以当前时间作为图片名称前缀
img_path = project_path + "\\error_img\\" + time.strftime('%Y%m%d%H%S', time.localtime())

# 测试用例代码存放路径（用于构建suite，注意该文件夹下的文件都应该以test开头命名）
# test_case_path = project_path + "\\src\\testcase"
test_case_path = os.path.join(project_path,'src/testcase')

# login_username="-------------"
# login_password="-------------"


# if __name__=='__main__':
# test1 = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
