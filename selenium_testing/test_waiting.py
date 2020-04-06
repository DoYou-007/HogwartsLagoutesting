from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestFirst:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(3)  # 使用隐示等待

    def teardown(self):
        sleep(3)
        self.driver.quit()

#第一种：自己编写隐式方法
    def test_wait(self):
        # sleep(3)    #直接等待
        self.driver.find_element(By.XPATH, '//*[@id="main-nav-menu"]/ul/li[4]/a').click()

        def wait(x):  # 必须传入一个参数，供until中的method传入一个方法
            return len(
                self.driver.find_elements(By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')) >= 1  # 为什么不可以使用element

        WebDriverWait(self.driver, 10).until(wait)   #wait函数使用时不能使用()，否则会当作函数使用处理
        self.driver.find_element(By.XPATH, '//*[@title="霍格沃兹测试学院(hogwarts)"]').click()
###elements  和element的区别:elements返回的是一个列表其中包含所有的符合要求的对象；而element返回的是一个符合对象的元素


# 第一种：使用selenium自带方法
    def test_wait1(self):
        # sleep(3)    #直接等待
        self.driver.find_element(By.XPATH, '//*[@id="main-nav-menu"]/ul/li[4]/a').click()

        # selenium还提供了一些内置方法，这样我们可以不用自己单独编写方法
        # expected_conditions.element_to_be_clickable(By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')
        # element_to_be_clickable 等待直到元素可被点击
        # presence_of_element_located 等待元素出现
        # visibility_of_element_located  等待元素可见  等等。。

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')))
        self.driver.find_element(By.XPATH, '//*[@title="霍格沃兹测试学院(hogwarts)"]').click()


# self.driver.find_elements(By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')) >= 1  # 为什么不可以使用element
'''
其中element返回的知识指定的一个节点而elements则是返回的是一个列表
'''

'''
#until函数的相关信息
    def until(self, method, message=''):
        """Calls the method provided with the driver as an argument until the \
        return value is not False."""
        screen = None
        stacktrace = None

        end_time = time.time() + self._timeout
        while True:
            try:
                value = method(self._driver)
                if value:
                    return value
            except self._ignored_exceptions as exc:
                screen = getattr(exc, 'screen', None)
                stacktrace = getattr(exc, 'stacktrace', None)
            time.sleep(self._poll)
            if time.time() > end_time:
                break
        raise TimeoutException(message, screen, stacktrace)
'''
