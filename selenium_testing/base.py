import os

from selenium import webdriver


class Base:
    '''
    selenium多浏览器处理：chrome，Firefox，headless ;
    通过os模块来获取browser是什么浏览器然后打开相应的drvier
    其中一种启动方式：命令行运行  browser = firefox  pytest  文件
    '''
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
