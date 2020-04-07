from selenium.webdriver.common.by import By

from selenium_testing.test1_PO.page.basepage import Basepage


class Addmember(Basepage):
    def addmember(self):
        # 填入姓名，账号，手机号码等
        self.find(By.ID, 'username').send_keys("hellll")
        self.find(By.ID, 'memberAdd_acctid').send_keys("jykl")
        self.find(By.ID, 'memberAdd_phone').send_keys("11111111111")
        # 点击保存键
        self.find(By.XPATH,
                  "// *[ @ id = 'js_contacts181'] / div / div[2] / div / div[4] / div / form / div[3] / a[2]").click()
