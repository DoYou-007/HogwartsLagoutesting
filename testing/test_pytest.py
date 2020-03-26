from python.caic import Caic


class TestCaic:
    def setup(self):
        self.calc = Caic()

    def test_add(self):
        # calc = Caic()
        assert self.calc.add(1, 2) == 3

    def test_div(self):
        # calc = Caic()
        assert self.calc.div(1, 2) == 0.5
