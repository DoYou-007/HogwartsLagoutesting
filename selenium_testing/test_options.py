'''
1.通过chromeoptions来进行参数设置达到复用浏览器的效果
chrome --remote-debugging-port=9222 --user-data-dir="D:\selenium\AutomationProfile"
https://home.testing-studio.com/t/topic/1402 ：帖子中出问题是因为自己代码写错的原因
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testdemo:
    def setup_method(self, method):
        # 第一种复用书写方式
        # chrome_opts = webdriver.ChromeOptions()
        # chrome_opts.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_opts)

        # 第二种复用书写方式
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)


    # @pytest.mark.skip
    # def teardown(self):
    #     self.driver.quit()

    def test_case(self):
        # self.driver.get("https://home.testing-studio.com/")
        self.driver.find_element_by_css_selector(".d-button-label:nth-child(2)").click()
        # self.driver.find_element_by_xpath('//*[@id="ember40"]/a').click()  # //*[@id="ember40"]/a
        # self.driver.find_element_by_id("su").click()

def test_case1():
    # chrome_opts = webdriver.ChromeOptions()
    # chrome_opts.debugging_address = "127.0.0.1:52"
    # driver = webdriver.Chrome(options=chrome_opts)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # driver.get("https://home.testing-studio.com/")
    driver.find_element_by_id("kw").send_keys('selenium测试')



