'''
打开页面；
点击-社团标签；
点击-霍格沃兹学院；
访问页面第一条帖子
'''

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFirst:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_case(self):
        self.driver.get("https://testerhome.com/")
        # self.driver.find_element_by_link_text('社团').click()
        self.driver.find_element(By.LINK_TEXT, "社团")  # 第二种书写方式
        self.driver.find_element_by_link_text('霍格沃兹测试学院').click()
        self.driver.find_element_by_css_selector('.topic-22287 .node').click()
