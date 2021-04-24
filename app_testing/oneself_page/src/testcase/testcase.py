# coding:utf-8

import unittest
from src.common.browser_engine import BrowserEngine
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# from src.pageobject.searchpage.searchpage import SearchPage
import time


class Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser()
        cls.driver.implicitly_wait(3)
        # cls.searchpage = SearchPage(cls.driver)
        # cls.searchpage.goto_searchpage()

    @classmethod
    def tearDownClass(cls):
        print("准备退出浏览器")
        cls.driver.quit()
        print("退出浏览器成功")

    def test01_searchoname(self):
        # webdriver.ActionChains(self.driver).send_keys(Keys.ENTER).perform()
        print('代码执行完成')
        time.sleep(3)
