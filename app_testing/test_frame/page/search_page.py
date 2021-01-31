from selenium.webdriver.common.by import By

from HogwartsLagoutesting.app_testing.test_frame.basepage import BasePage

class SearchPage(BasePage):
    #搜索alibaba并点击第二栏内容
    def search_alibaba(self):
        #注意使用绝对路径
        self.get_steps("../page/search_page.yaml",'search_alibaba')

        # self.send((By.ID,'search_input_text'),'alibaba')
        # self.find_and_click((By.XPATH,'//*[@resource-id="com.xueqiu.android:id/listview"]/android.widget.RelativeLayout[2]'))