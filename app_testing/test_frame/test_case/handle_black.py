import yaml
from selenium.webdriver.common.by import By

#装饰find方法之去除弹窗操作
def handle_black(fun):
    def black(*args,**kwargs):
        #拿取到shelf的值
        first = args[0]
        #读取到yaml文件中的黑名单元素
        with open('./black_list.yaml','r',encoding='utf-8') as f:
            black_list = yaml.safe_load(f)
        #进行异常捕获
        try:
            return fun(*args,**kwargs)
        except Exception as e:
            #遍历循环黑名单中的内容
            for black in black_list:
                elements = first.driver.find_elements(*black)
                #当找到元素的值时进行点击操作
                if len(elements) > 0:
                    elements[0].click()
                #再次查找
                return fun(*args,**kwargs)
            raise e
    return black