from selenium.webdriver.common.by import By

from HogwartsLagoutesting.app_testing.test_frame.basepage import BasePage
from HogwartsLagoutesting.app_testing.test_frame.page.search_page import SearchPage


class MarketPage(BasePage):
    #在行情页面进入搜索页面
    def goto_search(self):
        # 注意使用绝对路径
        self.get_steps("../page/market_page.yaml",'goto_search')

        # self.find_and_click((By.XPATH,'//*[@resource-id="com.xueqiu.android:id/action_search"]'))
        return SearchPage(self.driver)