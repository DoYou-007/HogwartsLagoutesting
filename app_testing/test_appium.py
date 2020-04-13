from time import sleep

import pytest
from appium import webdriver


# "noReset": True,  :为了不然每次的activity都重启一遍，在已有的activity上运行
# "unicodeKeyBoard": 'true', ：替换为中文的输入方式
# "resetKeyBoard": "true" ：重置输入法
class Testfind:
    # 初始化用例，设置capbility参数，设置隐式等待时间
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'ec76ef18'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        desired_caps["noReset"] = 'true'
        desired_caps["dontStopAppOnReset"] = 'true'
        desired_caps["skipDeviceInitialization"] = 'true'
        # desired_caps["unicodeKeyBoard"] = 'true'
        # desired_caps["resetKeyBoard"] = 'true'
        desired_caps["unicodeKeyboard"] = True
        desired_caps["resetKeyboard"] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()

    # 测试搜索点击case:通过id,xpath定位
    def testsearch(self):
        el1 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("alibaba")
        # el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
        # el3.click()
        self.driver.find_element_by_xpath("//*[@resource-id = 'com.xueqiu.android:id/name' and @text = '阿里巴巴']").click()

    def testsearch2(self):
        '''
        1.打开 雪球app
        2.点击搜索输入框
        3.向搜索框框中输入“阿里巴巴”
        4.在搜索结果页选择“阿里巴巴”，然后进行点击
        5.获取这只上 阿里巴巴的股价，并判断这只股价的价格>200
        '''
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        sleep(5)
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element_by_xpath("//*[@resource-id = 'com.xueqiu.android:id/name' and @text = '阿里巴巴']").click()
        current_price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert current_price > 200


if __name__ == "__main__":
    pytest.main()
