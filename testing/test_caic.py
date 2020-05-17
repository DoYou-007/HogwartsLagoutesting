# 对caic文件进行编写测试用例：使用的是unittests
import sys
import unittest

import pytest

sys.path.append('..')
print(sys.path)
from python.caic import Caic


class TestCaic(unittest.TestCase):
    def setUp(self) -> None:
        self.calc = Caic()

    def test_add_1(self):
        # self.calc = Caic()  每次类方法都需要进行初始化操作，使用setup方法代替
        self.assertEqual(3, self.calc.add(1, 2))

    def test_add_2(self):
        # self.calc = Caic()
        self.assertEqual(0.03, self.calc.add(0.01, 0.02))


if __name__ == "__main__":
    unittest.main()
