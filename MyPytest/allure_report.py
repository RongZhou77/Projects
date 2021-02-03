import pytest
import allure


@allure.feature("登录模块")
class TestLogin():
    def test_skip(self):
        print("这是跳过的用例")
        pytest.skip("跳过该用例")

    def test_broken(self):
        raise Exception("捕获异常")

    @allure.story("登录成功")
    def test_success(self):
        print("这是成功的用例")
        assert True

    @allure.story("登录失败")
    def test_failure(self):
        print("这是失败的用例")
        assert False

    @allure.story("用户名缺失")
    def test_login_a(self):
        print("用户名缺失")
        pass

    @allure.story("密码错误")
    def test_login_b(self):
        with allure.step("点击用户名"):
            print("输入用户名：")
        with allure.step("点击密码"):
            print("输入密码：")
        print("点击登录")
        with allure.step("点击登录之后登录失败"):
            assert '1' == 1
            print("登陆失败")
        pass

    @allure.story("登陆失败")
    def test_login_failure(self):
        print("登陆失败")
        pass


if __name__ == '__main__':
    pytest.main()
