from selenium import webdriver


class TestFrom:
    '''
    打开testerhome的网址，进行登录操作；输入用户名，密码，点击“记住”标签，点击登录，提交表单
    知识点：
    1.form表单获取相关元素等没有任何变化只是在点击登录的情况下才会返回一个登录的链接
    2.get_attaribute():根据需要元素的值来返回内容如：id值等
    '''

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_css_selector(".d-button-label:nth-child(2)").click()

        name_ele = self.driver.find_element_by_id("login-account-name")
        name_ele.send_keys("1782343025@qq.com")
        print(name_ele.get_attribute("value"))

        pwd_ele = self.driver.find_element_by_id("login-account-password")
        pwd_ele.send_keys("ying775825")
        print(pwd_ele.get_attribute("value"))

        login_ele= self.driver.find_element_by_id("login-button")
        login_ele.click()


