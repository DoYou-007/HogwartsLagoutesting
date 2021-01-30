import yaml
from appium import webdriver
from .base_page import Base_Page
from .main import Main

#定义app相关操作
class APP(Base_Page):
    # com.android.browser/.BrowserActivity
    # com.xueqiu.android com.xueqiu.android.view.WelcomeActivityAlias
    _package = 'com.xueqiu.android'
    _activity = '.view.WelcomeActivityAlias'

    #启动app的一些操作
    def start_app(self):
        if self._drviver is None:
            caps = dict()
            caps['platformName'] = 'Android'
            # caps['platformVersion'] = '10'
            caps['deviceName'] = 'emulator-5554'
            caps['appPackage'] = self._package
            caps['appActivity'] = self._activity
            caps["noReset"] = 'true'
            #公共部分的数据驱动调用
            caps['udid'] = yaml.safe_load(open('../page/configgration.yaml'))['caps']['udid']
            self._drviver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            # print('caps中udid的值：',caps['udid'])

        else:
            self._drviver.start_activity(self._package,self._activity)

        self._drviver.implicitly_wait(5)
        return self

    #停止app
    def stop_app(self):
        self._drviver.close_app()

    #定义进入起始页
    def main(self):
        return Main(self._drviver)