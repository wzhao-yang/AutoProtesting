import pytest


# test fixture 的高级用法
@pytest.fixture()
def login():
    """
    使用fixture后，就可以不用setup这种实现方式了，
    可以直接调用fixture
    :return:
    """
    print("需要登录")
    username = "xiaoming"
    yield username
    print("相当于teardown的操作，来激活后面的操作")


class TestDemo:
    # def setup_class(self):
    #     # 第一步，打开浏览器
    #     print("打开浏览器")
    #
    # def teardown_class(self):
    #     # 关闭浏览器
    #     print("关闭浏览器")

    def test_a(self, login):
        """
        第一步，打开浏览器
        第二步，输入网址
        第三步，定位
        第四步，各种操作
        第五步，关闭浏览器
        如果，b,c 都需要重复执行这些，可以用setup抽出公共方法
        :return:
        """
        print(f"test_a===>{login}")

    def test_b(self):
        pass

    def test_c(self, login):
        pass
