#coding:utf-8
import os
import unittest
from selenium import webdriver
from time import sleep
import time
#解决不能输入中文的问题
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
desired_caps = {}
desired_caps['platformVersion'] = '6.0'
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'NNQWDQDMVKYP59JF'
desired_caps['appPackage'] = 'com.aware'
desired_caps['appActivity'] = 'com.aware.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#启动aware
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(5)
driver.find_element_by_name("关注度TOP").click()
#my_home = driver.find_element_by_xpath("//*[@class='android.widget.FrameLayout'][5]").click()
time.sleep(3)
driver.quit()