import unittest

from MyPytest.util.HTMLTestRunner_PY3 import HTMLTestRunner

if __name__ == '__main__':
    # 方法四：匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    # test_dir:定义被测试脚本的路径;pattern:脚本名称匹配规则
    # test_dir = "./TestCase"
    # discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    # unittest.TextTestRunner(verbosity=2).run(discover)

    # 使用HTMLTestRunner发送测试报告
    test_dir = "./TestCase"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

    report_title = "周蓉的测试用例执行报告"
    desc = "用于周蓉的第一个测试框架的测试用例执行的测试报告"
    report_file = "./report/result.html"

    with open(report_file, "wb") as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(discover)
