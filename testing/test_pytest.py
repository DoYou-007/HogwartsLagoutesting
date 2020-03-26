from python.caic import Caic


class TestCaic:
    def setup(self):
        self.calc = Caic()

    def test_add_1(self):
        # calc = Caic()
        assert self.calc.add(1, 2) == 3  # 整数相加

    def test_add_2(self):
        assert self.calc.add(1.0, 2) == 3.0  # 浮点数相加

    def test_add_3(self):
        assert self.calc.add('1', 2) == 3  # 字符串相加

    def test_add_4(self):
        assert self.calc.add('1', '2') == '13'  # 字符串相加

    def test_add_5(self):
        assert self.calc.add('加法', 2) == '加法2'  # 中文相加

    def test_add_6(self):
        assert self.calc.add('#', 2) == '#2'  # 字符相加

    def test_add_7(self):
        assert self.calc.add(-22, 2) == -20  # 一正一负相加

    def test_div_1(self):
        assert self.calc.div(1, 2) == 0.5

    def test_div_2(self):
        assert self.calc.div(0, 2) == 0  # 分母为零

    def test_div_3(self):
        assert self.calc.div(1, 0) == 0  # 分子为零
