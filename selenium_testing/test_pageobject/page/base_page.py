from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    '''
    定义初始化url：_base_url = "" 当不是为空时重新打开url
    针对driver也进行复用判断，避免后续操作时重新打开窗口
    '''
    _base_url = ""

    def __init__(self, driver: WebDriver = None):
        self._driver = ""
        if driver is None:
            self._driver = webdriver.Chrome()
        else:
            self._driver = driver
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, by, locator):
        return self._driver.find_element(by, locator)
