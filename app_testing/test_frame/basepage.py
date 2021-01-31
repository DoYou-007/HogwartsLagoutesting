"""
__author__ = 'jaxon'
__time__ = '2021/1/16 下午9:06'
__desc__ = ''
"""
#
from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from HogwartsLagoutesting.app_testing.test_frame.test_case.handle_black import handle_black


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    #增加装饰器防止冗余
    @handle_black
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        self.find(locator).click()

    def send(self,locator,values):
        self.find(locator).send_keys(values)
        sleep(2)

    def scroll_find_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        self.find_and_click(element)

    def find_and_get_text(self, locator):
        return self.find(locator).text

    #添加配置驱动方法
    def get_steps(self,path,pages):
        #读取yaml中的测试步骤
        with open(path, 'r' , encoding='utf-8') as f:
            data = yaml.load(f)
        #获取不同操作的测试步骤
        steps = data[pages]
        #可能存在多个步骤，一一进行操作
        for step in steps:
            action = step['action']
            #执行查找元素并点击
            if 'find_and_click' == action:
                self.find_and_click(step['locator'])
            #执行输入文本操作
            elif 'send' == action:
                self.send(step['locator'],step['send_values'])


