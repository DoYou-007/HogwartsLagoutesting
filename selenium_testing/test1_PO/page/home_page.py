from selenium.webdriver.common.by import By

from selenium_testing.test1_PO.page.add_member import Addmember
from selenium_testing.test1_PO.page.basepage import Basepage


class Homepage(Basepage):
    def goto_addmember(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.find(By.XPATH, "//*[@id='_hmt_click']/div[1]/div[4]/div[2]/a[1]/div/span[2]").click()
        return Addmember(self.driver)

    def goto_address(self):
        pass

    def goto_memeber(self):
        pass
