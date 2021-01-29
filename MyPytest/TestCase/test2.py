import unittest


class TestCase3(unittest.TestCase):
    def setUp(self) -> None:
        print("这是case3的setup")

    def tearDown(self) -> None:
        print("这是case3的teardown")

    def test_func1(self):
        print("这是测试函数3-1")

    def test_func2(self):
        print("这是测试函数3-2")


class TestCase4(unittest.TestCase):
    # 使用setup和teardown可以给每个测试方法加上清理操作
    # def setUp(self) -> None:
    #     print("这是case2的setup")
    # def tearDown(self) -> None:
    #     print("这是case2的teardown")

    # 使用setUpClass/tearDownClass可以给整个测试类加清理操作，注意要加上@classmethod
    @classmethod
    def setUpClass(cls) -> None:
        print("这是Class4的setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是Class4的teardown")

    def test_func1(self):
        print("这是测试函数4-1")

    def test_func2(self):
        print("这是测试函数4-2")

    def test_func3(self):
        print("这是测试函数4-3")
