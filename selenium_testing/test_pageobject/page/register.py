from selenium.webdriver.common.by import By

from selenium_testing.test_pageobject.page.base_page import BasePage


class Register(BasePage):
    '''注册界面相关操作操作'''

    def register(self):
        self.find(By.ID, "corp_name").send_keys("hellp")
        self.find(By.ID, "manager_name").send_keys("nihaoya")
        return True
