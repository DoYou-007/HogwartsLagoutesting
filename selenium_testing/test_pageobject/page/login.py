from selenium.webdriver.common.by import By
from selenium_testing.test_pageobject.page.base_page import BasePage
from selenium_testing.test_pageobject.page.register import Register


class Login(BasePage):
    '''登录界面相关操作及跳转到注册页面'''

    def scan(self):
        #扫码登录跳过
        pass

    def goto_register(self):
        self.find(By.XPATH, "//*[@id='wework_admin.loginpage_wx_$']/main/div[2]/a").click()
        return Register(self._driver)
