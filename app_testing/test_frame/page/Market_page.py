from selenium.webdriver.common.by import By

from HogwartsLagoutesting.app_testing.test_frame.basepage import BasePage
from HogwartsLagoutesting.app_testing.test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    def goto_search(self):
        self.find_and_click((By.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]'))
        return SearchPage(self.driver)