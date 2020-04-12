from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'ec76ef18'
desired_caps['appPackage'] = 'com.android.setting'
desired_caps['appActivity'] = 'com.android.setting.Setting'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # http://localhost:4723wd/hub 这个用处是什么？
driver.quit()
