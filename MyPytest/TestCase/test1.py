import unittest


class TestCase1(unittest.TestCase):
    def setUp(self) -> None:
        print("这是case1的setup")

    def tearDown(self) -> None:
        print("这是case1的teardown")

    def test_func1(self):
        print("这是测试函数1-1")

    def test_func2(self):
        print("这是测试函数1-2")

    def test_func3(self):
        print("这是测试函数1-3")


class TestCase2(unittest.TestCase):
    # 使用setup和teardown可以给每个测试方法加上清理操作
    # def setUp(self) -> None:
    #     print("这是case2的setup")
    # def tearDown(self) -> None:
    #     print("这是case2的teardown")

    # 使用setUpClass/tearDownClass可以给整个测试类加清理操作，注意要加上@classmethod
    @classmethod
    def setUpClass(cls) -> None:
        print("这是Class2的setup")

    @classmethod
    def tearDownClass(cls) -> None:
        print("这是Class2的teardown")

    def test_func1(self):
        print("这是测试函数2-1")

    def test_func2(self):
        print("这是测试函数2-2")

    def test_func3(self):
        print("这是测试函数2-3")
# if __name__ == '__main__':
# 方法一：执行所有的满足UNITTEST要求的测试类中的测试方法
# unittest.main()

# #方法二：把测试方法加入容器中执行
# suite = unittest.TestSuite()
# suite.addTest(TestCase1("test_func1"))
# suite.addTest(TestCase1("test_func3"))
# suite.addTest(TestCase2("test_func1"))
# unittest.TextTestRunner().run(suite)

# #方法三：把测试类加入容器中执行
# suite1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
# suite2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)
# suite = unittest.TestSuite([suite1,suite2])
# unittest.TextTestRunner(verbosity=2).run(suite)

# 方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
