##触屏操作自动化
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction:
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

    def teardown(self):
        self.driver.back()
        self.driver.back()

    #     self.driver.quit()

    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=643, y=2057).wait(2000).move_to(x=643, y=682).wait(2000).release().perform()

    # 第二中方法（较常用）
    def test_touchaction2(self):
        action = TouchAction(self.driver)
        windows_rect = self.driver.get_window_rect()
        width = windows_rect['width']
        height = windows_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).wait(2000).release().perform()

    # 手势操作：TouchAction(driver).press(x=244,y=374).wait(100).move_to(x=711,y=374).wait(100).move_to(x=1198,y=374).wait(100)
    # .move_to(x=1198,y=865).wait(100).move_to(x=1198,y=1323).wait(100).release().preform
    # 解锁手势操作
    def test_touchaction_unlock(self):
        touch = TouchAction(self.driver)
        touch.press(x=244, y=374).wait(100) \
            .move_to(x=711, y=374).wait(100) \
            .move_to(x=1198, y=374).wait(100) \
            .move_to(x=1198, y=865).wait(100) \
            .move_to(x=1198, y=1323).wait(100).release().perform()
