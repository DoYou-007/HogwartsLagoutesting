from selenium.webdriver.common.by import By

from HogwartsLagoutesting.app_testing.test_frame.page.Market_page import MarketPage
from HogwartsLagoutesting.app_testing.test_frame.basepage import BasePage


class MainPage(BasePage):
    #进入到行情页面
    def goto_Marketpage(self):
        # 注意使用绝对路径
        self.get_steps("../page/main_page.yaml",'goto_Marketpage')

        # self.find_and_click((By.ID, "post_status"))
        # self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)

    #进入我的页面
    def goto_mine(self):
        self.get_steps("../page/main_page.yaml", 'goto_mine')

        # self.find_and_click((By.XPATH, "//*[@text='我的']"))