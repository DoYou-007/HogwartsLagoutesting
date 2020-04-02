'''
1.通过chromeoptions来进行参数设置达到复用浏览器的效果
'''
import json
from time import sleep
from typing import List, Dict

import pytest
from selenium import webdriver


class Testdemo:
    def setup(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugging_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_opts)

    @pytest.mark.skip
    def teardown(self):
        self.driver.quit()

    # def test_case(self):
    #     self.driver.get("https://home.testing-studio.com/")
    #     self.driver.find_element_by_xpath('//*[@id="ember40"]/a').click()   #//*[@id="ember40"]/a
