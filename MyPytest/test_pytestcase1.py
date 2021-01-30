import pytest


class Test_Case1:
    @pytest.fixture()
    def login(self):
        loginname = "zhourong"
        return loginname;

    def test_a(self, login):
        print(f"aaaaaa   登录名 = {login}")

    def test_b(self):
        print("bbbbbb")


class Test_Case2:
    @pytest.mark.parametrize("a,b", [(1, 2), (2, 3), (4, 4)])
    def test_1(self, a, b):
        print("这是参数化的用例")
        print(f"参数1={a},参数b={b}")

    def test_2(self):
        print("这是2")

    def test3(self):
        print("这是3")


if __name__ == '__main__':
    # pytest.main(["test_pytestcase1.py"])  #可以执行对应文件的全部满足要求的用例
    pytest.main(["test_pytestcase1.py::Test_Case1", "-v"])  # 可以指定部分（类）要执行的用例（类），加上-v可以打印详细的信息
    # pytest -k "test_2" -v ，可以在命令行中选择部分用例来执行，这个针对的是测试用例方法，而不是测试用例类
