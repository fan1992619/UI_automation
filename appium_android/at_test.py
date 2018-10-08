#coding:utf-8
import unittest
from desired_capabilities import get_desired_capabilities
import time
from selenium import webdriver
from appium import webdriver
class AtTests(unittest.TestCase):
    def setUp(self):
        desired_caps=get_desired_capabilities()
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()
    def test_homepage_01(self):
        print(测试成功)
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumTests)
    unittest.run(suite)