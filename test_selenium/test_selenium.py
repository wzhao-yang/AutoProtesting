import pytest
from selenium import webdriver


# 打开chrome浏览器，输入百度网站
class TestHome:
    @pytest.fixture()
    def goto(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_home(self, goto):
        self.driver.get("https://testerhome.com/")
        # self.driver.find_element_by_xpath("xpath=//a[contains(text(),'社团')]")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("社区").click()
        self.driver.find_element_by_xpath("//div[2]/div/a").click()
        print("测试完成")


if __name__ == '__main__':
    pytest.main(['-vs'])
