import os

from selenium import webdriver

chrome_driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
chrome_drvier_new_file = os.path.join(chrome_driver_path,'driver/chromedriver')
print(chrome_drvier_new_file)
# driver = webdriver.Firefox(chrome_driver_path)
driver = webdriver.Chrome(chrome_drvier_new_file)
driver.get('https://www.baidu.com')

# from selenium import webdriver  # 先安装selenium模块，再导入模块
# import time  # 导入time模块
#
# url = "https://mail.163.com/"  # 163邮箱的网址
# browser = webdriver.Chrome()  # 打开网址程序，Chrome 是 WebDriver 的子类，是 WebDriver 类的一种
# browser.get(url)  # 浏览器打开https://mail.163.com/网址
#
# pw_login = browser.find_element_by_id("switchAccountLogin")
# pw_login.click()  # 找到密码登陆的界面，click()鼠标左键点击页面元素
#
# time.sleep(2)  # 停留2秒
#
# iframe1 = browser.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]")  # 单引号和双引号分别开，要一单一双才行
# browser.switch_to.frame(iframe1)
#
# email = browser.find_element_by_name("email")
# email.clear()  # 清除已有的账号信息
# email.send_keys("********")  # 输入自己的账号
#
# time.sleep(2)  # 停留2秒
#
# password = browser.find_element_by_name("password")
# password.send_keys("*****")  # 输入自己的密码
#
# time.sleep(2)  # 停留2秒
#
# button = browser.find_element_by_id("dologin")  # 登陆
# button.click()  # click()鼠标左键点击页面元素

