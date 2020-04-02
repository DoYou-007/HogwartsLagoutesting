import json
from typing import List, Dict

from selenium import webdriver


class Testdemo:
    def setup_method(self):
        chrome_opts = webdriver.ChromeOptions()
        chrome_opts.debugging_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.implicitly_wait(3)

    def test_cookie_pass(self):

        ##获取登录状态的cookie信息
        # sleep(15)
        # cookies = self.driver.get_cookies()
        # with open("cookies.txt", "w") as f:
        #     json.dump(cookies, f)
        with open('cookies.txt', 'r') as f:
            cookies: List[Dict] = json.load(f)
        for cookie in cookies:  # 解决expiry无法识别的问题，但是这里没有理解为什么知道处理的是这个字段
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_xpath("//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[3]/div/span[2]").click()
