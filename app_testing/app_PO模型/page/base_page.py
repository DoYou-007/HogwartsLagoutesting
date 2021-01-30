import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Base_Page:

    #定义driver并进行初始化
    _drviver : WebDriver
    _blck_list = [(By.ID,'iv_close')]
    def __init__(self,driver: WebDriver=None):
        self._drviver = driver

    #封装find的公共方法，使用调用更加简单
    #增加弹窗处理逻辑
    def find(self,locator,value):
        try:
            element = self._drviver.find_element(locator,value)
            return element
        except:
            for black in self._blck_list:
                elements = self._drviver.find_elements(*black)
                print(elements)
                if len(elements) > 0:
                    elements[0].click()
                    break
            return self.find(locator,value)
        
    


    #封装自己click方法
    def click(self,locator,value):
        self.find(locator,value).click()

    # 封装自己send_key方法
    def send_key(self,locator,value,send_value):
        self.find(locator,value).send_keys(send_value)

    #配置驱动：对yaml文件中的步骤一一解析
    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
            element = None
            for step in steps:
                if 'by' in step.keys():
                    element = self.find(step['by'],step['locator'])
                if 'action' in step.keys():
                    action = step['action']
                    if 'click' == action:
                        element.click()