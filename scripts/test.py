import allure
import pytest
class Test:

    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.step(title='输出第一个测试用例')
    def test01(self):
        allure.attach('输出','1',allure.attachment_type.PNG)
        print('1')
        assert 1

    def test02(self):
        print('2')
        assert 1

    def test03(self):
        print('3')
        assert 1