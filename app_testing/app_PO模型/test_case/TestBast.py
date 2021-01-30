
from page.app import APP

#对启动app进行封装处理后，后续的测试case直接继承后运行即可，还有断言后的处理等都可以用这种方式来进行集中处理
class TestBase:
    app = None
    def setup(self):
        self.app = APP()

