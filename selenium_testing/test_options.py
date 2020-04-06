'''
1.通过chromeoptions来进行参数设置达到复用浏览器的效果
'''

import pytest
from selenium import webdriver


class Testdemo:
    def setup_method(self,method):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugging_address = "127.0.0.1:1222"
        self.driver = webdriver.Chrome(options=chrome_opts)

    @pytest.mark.skip
    def teardown(self):
        self.driver.quit()

    def test_case(self):
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_css_selector(".d-button-label:nth-child(2)").click()
        # self.driver.find_element_by_xpath('//*[@id="ember40"]/a').click()  # //*[@id="ember40"]/a

# def test_case1():
#     chrome_opts = webdriver.ChromeOptions()
#     chrome_opts.debugging_address = "127.0.0.1:1222"
#     driver = webdriver.Chrome(options=chrome_opts)
#     driver.get("https://home.testing-studio.com/")
#     driver.find_element_by_css_selector(".d-button-label:nth-child(2)").click()

