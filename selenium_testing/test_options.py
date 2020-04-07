'''
1.通过chromeoptions来进行参数设置达到复用浏览器的效果
chrome --remote-debugging-port=9222 --user-data-dir="D:\selenium\AutomationProfile"
https://home.testing-studio.com/t/topic/1402
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Testdemo:
    def setup_method(self, method):
        # chrome_opts = webdriver.ChromeOptions()
        # chrome_opts.debugging_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_opts)

        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # chrome_options = Options()
        # chrome_options.add_experimental_option("debuggingAddress", "127.0.0.1:9222")
        # self.driver = webdriver.Chrome(options=chrome_options)

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



