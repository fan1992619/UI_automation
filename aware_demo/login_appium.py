#coding:utf-8
import os
import unittest
from selenium import webdriver
from time import sleep
import time
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
desired_caps = {}
desired_caps['platformVersion'] = '6.0'
desired_caps['platformName'] = 'Android'
#desired_caps['app'] = True
desired_caps['deviceName'] = 'NNQWDQDMVKYP59JF'
desired_caps['appPackage'] = 'com.aware'
desired_caps['appActivity'] = 'com.aware.moudle_main.ui.activity.MainActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#启动aware
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
driver.find_element_by_xpath("//*[@text='项目地图']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='我的']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='登录/注册']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@text='请输入手机号']").send_keys("18210542401")
time.sleep(1)
driver.find_element_by_xpath("//*[@text='获取验证码']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@text='登录']").click()
time.sleep(5)
driver.quit()