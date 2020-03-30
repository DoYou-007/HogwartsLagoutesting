from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestFirst:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://testerhome.com/")
        self.driver.implicitly_wait(3)  # 使用隐示等待

    def test_wait(self):
        # sleep(3)    #直接等待
        self.driver.find_element(By.XPATH, '//*[@id="main-nav-menu"]/ul/li[4]/a').click()

        def wait(x):
            return len(
                self.driver.find_elements(By.XPATH, '//*[@id="hot_teams"]/div[1]/strong')) >= 1  # 为什么不可以使用element

        WebDriverWait(self.driver, 10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@title="霍格沃兹测试学院(hogwarts)"]').click()


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
