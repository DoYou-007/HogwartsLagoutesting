from selenium_testing.test1_PO.page.home_page import Homepage


class Testaddmember:
    def setup(self):
        self.homepage = Homepage()

    def test_add_member(self):
        assert self.homepage.goto_addmember().addmember()
