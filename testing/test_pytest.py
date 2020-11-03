import pytest

from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add_1(self):
        result = self.calc.add(2, 2)
        print(result)
        assert 4 == result

    def test_div_2(self):
        result = self.calc.div(2, 2)
        print(result)
        assert 1 == result


if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div_2'])
