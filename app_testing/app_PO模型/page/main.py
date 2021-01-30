from selenium.webdriver.common.by import By

from .base_page import Base_Page

#定义起始页面的有哪些方法
class Main(Base_Page):

    #起始页面去搜索的方法
    def goto_search(self):
        self.find(By.ID,'home_search').click()
        # self.steps('../page/main.yaml')

    def goto_windows(self):
        self.find(By.ID,'post_status').click()
        self.find(By.ID, 'home_search').click()