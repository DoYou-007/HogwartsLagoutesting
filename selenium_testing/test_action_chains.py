from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class TestAction():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        db = self.driver.find_element(By.XPATH, "/html/body/form/input[2]")
        cl = self.driver.find_element(By.XPATH, "/html/body/form/input[3]")
        right = self.driver.find_element(By.XPATH, "/html/body/form/input[4]")
        acitons = ActionChains(self.driver)
        acitons.double_click(db)
        acitons.click(cl)
        acitons.context_click(right)
        sleep(3)
        acitons.perform()
        sleep(3)

    @pytest.mark.skip
    def test_moveaction(self):
        self.driver.get("https://www.baidu.com/")
        elements_move = self.driver.find_element(By.LINK_TEXT, "设置")
        acitons = ActionChains(self.driver)
        acitons.move_to_element(elements_move)
        sleep(3)
        acitons.perform()
        sleep(3)

    def test_drop_and_drag(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element = self.driver.find_element(By.ID, "dragger")
        move_element = self.driver.find_element(By.XPATH, "/html/body/div[2]")
        acitons = ActionChains(self.driver)
        ##如下有三种方法可以实现
        # acitons.drag_and_drop(drag_element, move_element).perform()
        # acitons.click_and_hold(drag_element).release(move_element).perform()
        acitons.click_and_hold(drag_element).move_to_element(move_element).perform()
        sleep(3)
