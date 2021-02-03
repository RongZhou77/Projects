import pytest


# autouse = Ture  可以让全部方法都使用fixture方法，没特例
# @pytest.fixture(autouse=Ture)
@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    usename = "luna"
    password = "123456789"
    token = "2f34r33f33f3"
    # yield关键字可以激活fixture的teardown功能
    # yield 相当于return，如果需要返回数据可以直接跟在yield后面，也支持元组和字典
    yield [usename, password, token]
    print("注销操作")


# fixture：在测试用例中传入fixture修饰的方法名
def test_case1(login):
    print("测试用例1")
    # 调用yield的返回信息则直接调用对应的方法
    print(f"登录用户信息：{login}")


def test_case2():
    print("测试用例2")


def test_case3(login):
    print("测试用例3")


# fixture：用usefixtures自动调用，把方法名以字符串的形式传入
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例4")
