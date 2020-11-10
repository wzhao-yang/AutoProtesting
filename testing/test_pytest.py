import pytest
import yaml
from python.calc import Calc


# 获取测试步骤liebiao，add ，add1
def steps():
    with open("../datas/steps.yml") as f:
        return yaml.safe_load(f)


class TestParametrize:
    def setup(self):
        self.calc = Calc()
        # self.yaml_lode = yaml_load_data()

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open('../datas/add.yml')))
    def test_parametrize_1(self, a, b, expect):
        print('\n测试函数1测试数据为:{}+{}={}'.format(a, b, expect))
        result = self.calc.add(a, b)
        assert result == expect

    # 按测试步骤执行
    @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open('../datas/add.yml')))
    def test_steps_1(self, a, b, expect):
        steps1 = steps()
        for step in steps1:
            print(f"step ====> {step}")
            if 'add' == step:
                result = self.calc.add(a, b)
            elif 'add1' == step:
                result = self.calc.add1(a, b)
            print('\n测试函数1测试数据为:{}+{}={}'.format(a, b, expect))
            assert result == expect

    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize('a, b, expect', yaml.safe_load(open('../datas/add.yml')))
    # def test_parametrize_2(self, a, b, expect):
    #     print('\n测试函数2数据为:{}/{}={}'.format(a, b, expect))
    #     result = self.calc.div(a, b)
    #     assert result == expect

    @pytest.mark.run(order=1)  # mark.run(order=1)进行排序，同时有可以使用pytest.mark.run.first
    @pytest.mark.parametrize('a', yaml.safe_load(open('../datas/add.yml')))
    def test_01(self, a):
        return a


if __name__ == '__main__':
    pytest.main(['-vs'])
    # pytest.main(['—alluredir ./report/allure_raw'])
    # pytest.main(['allure serve report/allure_raw'])
    # pytest.main(['--junit-xml=./result'])
    # pytest.main(['--collect-only'])  # collect只是收集case用例，但是不运行
    # pytest.main(['-v', '-m', 'div'])
    # pytest.main(['-v', '-k', '_2'])  # 选取_2得case
    # pytest.main(['-v', '-s', 'test_pytest.py::TestParametrize'])
    # pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div_2'])
    # pytest —alluredir ./report/allure_raw
    # allure serve report/allure_raw
    # allure generate ./report
