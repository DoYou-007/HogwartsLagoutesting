from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Basepage:
    # driver需要指定一个类型
    def __init__(self, driver: WebDriver = None):
        # 让python编译器知道有个实例变量
        self.driver = None
        if driver is None:
            # 复用已有的浏览器
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
        else:
            self.driver = driver

    def find(self, by, lactory):
        return self.driver.find_element(by, lactory)
