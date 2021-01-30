import pytest
import yaml

from page.app import APP
from test_case.TestBast import TestBase


class TestMain(TestBase):
    #测试main方法
    def test_main(self):
        # app = APP()
        # app.start_app().main().goto_search()
        # app.stop_app()

        #对app启动处理后的调用
        self.app.start_app().main().goto_search()

    #测试数据参数化：使用pytest框架
    @pytest.mark.parametrize('value1,value2',yaml.safe_load(open('./test_main.yaml')))
    def test_parameter(self,value1,value2):
        print(value1)
        print(value2)

    #测试弹窗处理逻辑
    def test_goto_windows(self):
        # app = APP()
        # app.start_app().main().goto_windows()

        # 对app启动处理后的调用
        self.app.start_app().main().goto_windows()
        
    
