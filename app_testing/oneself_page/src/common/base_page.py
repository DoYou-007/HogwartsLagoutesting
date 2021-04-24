# coding:utf-8

import time
from src.common.log import log
from selenium.webdriver.support.select import Select
from config.globalparameter import project_path, img_path
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep
import re


class BasePage(object):
    """"
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """


    def __init__(self, driver):
        self.driver = driver
        self.mylog = log()


    # quit browser and end testing
    def quit_browse(self):
        self.driver.quit()


    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        self.mylog.info("Click forward on current page.")


    # 浏览器后退操作
    def back(self):
        self.driver.back()
        self.mylog.info("Click back on current page.")


    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        self.mylog.info("wait for %d seconds." % seconds)


    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            self.mylog.info("Closing and quit the browser.")

        except NameError as e:
            self.mylog.error("Failed to quit the browser with %s" % e)


    # 截图,保存图片
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path + img_name + '.png')

        except:
            self.mylog.error(u'截图失败：' + img_name)


    # 切换到新窗口
    def Current_handel(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)


    # 重写find_element方法，增加定位元素的健壮性
    def find_element(self, *selector):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
            print("self.driver.find_element(*selector)", self.driver.find_element(*selector))
            return self.driver.find_element(*selector)
        except:
            self.mylog.error(u'找不到元素:' + str(selector))


    # 输入，重新send_keys,，先清除后输入
    def type(self, selector, text):
        try:
        # selector = getattr(self, "_%s" % selector)
            el = self.find_element(*selector)
            el.clear()
            el.send_keys(text)
        except NameError as e:
            self.mylog.error("Failed to type in input box with %s" % e)


    def click(self, selector):
        try:
            el = self.find_element(*selector)
            el.click()
            sleep(3)
        except NameError as e:
            self.mylog.error("Failed to click the element with %s" % e)


    # 通过value获取下拉菜单元素并点击
    def select_element_text(self, selector, text):
        try:
            el = self.find_element(*selector)
            Select(el).select_by_visible_text(text)
        except:
            self.mylog.error(u'找不到元素:' + str(selector))


    # 通过index获取下拉菜单元素并点击
    def select_element_index(self, selector, index):
        try:
            el = self.find_element(*selector)
            Select(el).select_by_index(index)
        except:
            self.mylog.error(u'找不到元素:' + str(selector))


    # 获取元素的属性值
    def get_Attribute(self, selector, value):
        el = self.driver.find_element(selector).get_attribute(value)
        return el


    # 获取元素的文本的值
    def get_text(self, selector):
        el = self.find_element(*selector).text
        return el


    # 校验按钮是否为选中状态
    def is_selected(self, selector):
        el = self.find_element(*selector)
        if el.is_selected():
            print(el + "被选中")
        else:
            print("请重新选中")


    # 获取网页标题
    def get_page_title(self):
        # logger.info("Current page title is %s" % self.driver.title)
        return self.driver.title


    # 获取单个表单元素
    def click_table_element(self, selector, text1, index, p_index, a_index):
        el = self.find_element(*selector)
        table_tr_list = el.find_elements_by_tag_name("tr")
        flag = 0
        breakflag = False
        # 循环table中tr的值
        for tr in table_tr_list:
            # 切换tr中的text再循环
            for i in (tr.text).split(" "):
            # 如果i的值=testStop中传入的值
            # print("111111")
            # print("i的值", i)
                if breakflag:
                    break
                if i == text1:
                    # 去查找当前值的td所在的位置
                    ul = table_tr_list[flag].find_elements_by_tag_name("td")[index]
                    # 查找td下p的元素
                    ee = ul.find_elements_by_tag_name("p")
                    if len(ee) == 0:
                        # 邱菊华新增这一行，兼容电桩类型页面的元素
                        tt = ul.find_elements_by_tag_name("div")
                        # 循环td下的p元素
                        n = 0
                        for j in ee or tt:
                            if breakflag:
                                break
                        # 查看p下面的a元素
                            n = n + 1
                            if n == p_index:
                                tt = j.find_elements_by_tag_name("a")
                                flagss = 0
                                # 循环a元素，循环一次后flagss+1，
                                for o in tt:
                                    flagss = flagss + 1
                                    # 如flagss==2，即第二个a元素
                                    if flagss == a_index:
                                    # 点击o元素，即删除按钮
                                        time.sleep(1)
                                    # o.click()
                                    return o
                            breakflag = True
                            break
            flag = flag + 1


    def cc(self, selector, text):
        el = self.find_element(selector)
        try:
            el.send_keys(text)
        except NameError as e:
            self.mylog.error("Failed to type in input box with %s" % e)


    # 重写find_elements方法，增加定位元素的健壮性
    def find_elements(self, *selector):
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(selector))
            return self.driver.find_elements(*selector)
        except:
            self.mylog.error(u'找不到元素:' + str(selector))


    # 批量操作 针对表格 可以传入多个参数（这里采用可变参数来进行判断）
    def table_element(self, selector, *text):
        # 先获取页面元素，这里是table
        print("selector的值", selector)
        el = self.find_element(*selector)
        # 查看table下的tr
        table_tr_list = el.find_elements_by_tag_name("tr")
        flag = 0
        flags = []
        breakflag = False
        # 循环table中所有的tr
        for tr in table_tr_list:
            # 循环一个tr，flag+1
            if breakflag:
                break
            flag = flag + 1
            # 循环每一行并切割取值
            for i in tr.text.split(" "):
                if breakflag:
                    break
                try:
                    # 如果i 在text里面
                    if len(text) == 0:
                        print("请输入要删除的值")
                    elif len(text) == 1:
                        value = "".join(tuple(text))
                        if i == value:
                            flags.append(flag)
                            breakflag = True
                            break
                        else:
                            if i in text:
                                # print(flag)
                                # 把当前的flag即行数传到flags中
                                flags.append(flag)
                except Exception as e:
                    print("未找到相应的结果")
                    # 返回flags 供后面的函数调用
        return flags


    def ul_li(self, selector):
        el = self.find_element(*selector)
        return el.find_elements_by_xpath('li')


    def getdigital(self, oristring):
        return re.sub("\D", "", oristring)


    # 批量传入元素类型（1：文本框输入 2：下拉框选择 3：时间控件）、元素、值
    def add(self, elements):
        pass
        for i in elements:
            if i[0] == 1:
                self.type(i[1], i[2])
            if i[0] == 2:
                self.select_element_index(i[1], i[2])


    def clear(self, selector):
        el = self.find_element(*selector)
        el.clear()


    def get_value(self, selector):
        """获取元素的value属性"""
        return self.driver.find_element(*selector).get_attribute("value")
