from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    '''
    打开百度网址，输入selenium测试，然后使用touchAction来移动到末尾
    知识点：
    1.top是对某个元素进行点击
    2.scroll_from_element：指定某个起使位置，然后指定滑动的x,y的距离
    3.w3c有个异常需要处理。此处为何pycharm没有报错这个w3c的异常
    '''
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()

    def teardown(self):
            self.driver.quit()

    def test_touchAction(self):
        self.driver.get("https://www.baidu.com/")
        el = self.driver.find_element_by_id("kw")
        el_serach = self.driver.find_element_by_id("su")

        el.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(el_serach)
        action.perform()

        action.scroll_from_element(el,0,10000).perform()
        self.driver.find_element_by_xpath("//*[@id='page']/a[10]").click()
        sleep(2)


