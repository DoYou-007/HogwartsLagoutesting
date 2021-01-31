from HogwartsLagoutesting.app_testing.test_frame.app import App


class TestMain:
    #测试创建的方法是否生效
    def test_main(self):
        app = App()
        app.start().goto_main().goto_Marketpage().goto_search().search_alibaba()

    #测试yaml文件支持多个功能操作是否生效
    def test_goto_mine(self):
        app = App()
        app.start().goto_main().goto_mine()