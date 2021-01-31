from selenium.webdriver.common.by import By

from HogwartsLagoutesting.app_testing.test_frame.page.Market_page import MarketPage
from HogwartsLagoutesting.app_testing.test_frame.basepage import BasePage


class MainPage(BasePage):
    def goto_Marketpage(self):
        self.find_and_click((By.ID, "post_status"))
        self.find_and_click((By.XPATH, "//*[@text='行情']"))
        return MarketPage(self.driver)