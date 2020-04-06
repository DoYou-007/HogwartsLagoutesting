from selenium.webdriver.common.by import By

from selenium_testing.test_pageobject.page.base_page import BasePage
from selenium_testing.test_pageobject.page.login import Login
from selenium_testing.test_pageobject.page.register import Register


class Main(BasePage):
    '''
    企业微信的主页面：提供两个方法
    1.登录的方法
    2.前往注册的方法
    '''
    _base_url = "https://work.weixin.qq.com/"

    def goto_register(self):
        self.find(By.XPATH, "//*[@id='tmp']/div[1]/a[2]").click()
        return Register(self._driver)

    def goto_login(self):
        self.find(By.XPATH, "//*[@id='indexTop']/div[2]/aside/a[1]").click()
        return Login(self._driver)
