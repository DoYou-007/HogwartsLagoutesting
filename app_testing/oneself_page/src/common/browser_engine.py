# -*- coding:utf-8 -*-
import configparser
import os.path
import time

from selenium import webdriver
from config.globalparameter import img_path, chrome_drvier_new_file, ie_driver_path, project_path, config_file_path


class BrowserEngine(object):
    def __init__(self, driver:webdriver=None):
        self.driver = driver

    # read the browser type from config.ini file, return the driver
    def open_browser(self):
        config = configparser.ConfigParser()
        print("配置文件的目录",config_file_path)
        config.read(config_file_path, encoding='UTF-8')
        print('config_data的数据:',config.sections())

        # config.ini.read(config_file_path)#这是原来的
        browser = config.get("browserType", "browserName")

        # logger.info("You had select %s browser." % browser)
        url = config.get("testServer", "URL")
        print(url)

        if browser == "Firefox":
            self.driver = webdriver.Firefox()
        # logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            self.driver = webdriver.Chrome(chrome_drvier_new_file)
        # logger.info("Starting Chrome browser.")
        elif browser == "IE":
            self.driver = webdriver.Ie(ie_driver_path)
        # logger.info("Starting IE browser.")
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver


    def quit_browser(self):
        # logger.info("Now, Close and quit the browser.")
        self.driver.quit()

# one = BrowserEngine()
# one.open_browser()
# time.sleep(2)
# print("准备关闭浏览器")
# one.quit_browser()