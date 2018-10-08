#coding:utf-8
import os
import unittest
from selenium import webdriver
from time import sleep
import time
# import sys
# reload(sys)
# sys.setdefaultencoding("gbk")
# import codecs
# fr = codecs.open("0.htm","r","gbk")
desired_caps = {}
desired_caps['platformVersion'] = '6.0'
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'NNQWDQDMVKYP59JF'
#desired_caps['app'] = True
desired_caps['appPackage'] = 'com.ss.android.ugc.aweme'
desired_caps['appActivity'] = 'com.ss.android.ugc.aweme/.splash.SplashActivity'
# 安装一个中文的输入法
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
#启动aware
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(3)
driver.quit()