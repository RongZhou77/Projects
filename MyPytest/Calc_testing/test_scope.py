import pytest


# 用fixture完成参数化
@pytest.fixture(params=[1, 2, 3])
def login1(request):
    data = request.param
    print("获取测试数据")
    return data


class Test_DB_demo1():
    def test_a(self, connectDB):
        print("-----测试用例a-----")

    def test_b(self, login1):
        print("-----测试用例b-----")
        print(login1)


class Test_DB_demo2():
    def test_c(self, login1):
        print("-----测试用例c-----")
        print(login1)

    def test_d(self, connectDB):
        print("-----测试用例d-----")
