from HogwartsLagoutesting.app_testing.test_frame.app import App


class TestMain:
    def test_main(self):
        app = App()
        app.start().goto_main().goto_Marketpage().goto_search()