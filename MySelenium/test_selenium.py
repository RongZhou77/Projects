# 第一个selenium用例
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_horgworz():
    def setup(self):
        self.driver = webdriver.Firefox()
        url = "https://www.baidu.com/"
        self.driver.get(url)
        # 窗口最大话
        self.driver.maximize_window()
        # 隐式等待5秒
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_horgworz(self):
        # 通过xpath定位百度输入框，并且输入“霍格沃兹测试学院”
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("霍格沃兹测试学院")
        # 通过ID定位百度一下按钮，并点击
        self.driver.find_element(By.ID, 'su').click()
        time.sleep(2)
        # 通过xpath定位百度首页，并点击
        self.driver.find_element(By.XPATH, '//*[@id="u"]/a[1]').click()
        # 通过css选择器定位到hao123并点击
        self.driver.find_element(By.CSS_SELECTOR, '#s-top-left a:nth-child(2)').click()
        time.sleep(5)
