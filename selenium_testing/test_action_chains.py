from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


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

    def test_keys(self):
        '''
        访问网址：http://sahitest.com/demo/label.htm
        定位输入框e1，e2；然后输入username tom;删除一个m；最后将e1中的内容复制到e2中
        知识点：
        1.运用到的是selenium中的ActionChains的api；
        2.send_keys来传入keys中的内容
        3.keys:ctrl+点击进入查看详细内容
        4.pause为暂停时间
        5.ele2.send_keys(Keys.CONTROL,'v')  这是control的用法
        '''

        self.driver.get("http://sahitest.com/demo/label.htm")
        ele1 = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele1.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        ele1.send_keys(Keys.CONTROL, 'a')
        sleep(1)
        ele1.send_keys(Keys.CONTROL, 'c')
        sleep(1)
        ele2 = self.driver.find_element_by_xpath("/html/body/label[2]/table/tbody/tr/td[2]/input")
        ele2.send_keys(Keys.CONTROL, 'v')
        sleep(1)
