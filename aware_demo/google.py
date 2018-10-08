#coding:utf-8
from selenium import webdriver
import os
import time
chromedriver="C:\\Users\\edz\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("http://admin.test.initialvc.com/admin/auth/login")
driver.maximize_window()
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[1]/input").send_keys("admin")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/input").send_keys("123456")
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/button").click()
time.sleep(2)
os.environ["webdriver.chrome.driver"] = chromedriver
driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[4]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("/html/body/div/aside/section/ul/li[4]/ul/li[1]/a/span").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='pjax-container']/section[2]/div[2]/div/div/div[1]/div/div[1]/a[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='filter-modal']/div/div/form/div[1]/div/div[3]/div/div/input").send_keys("42")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='filter-modal']/div/div/form/div[2]/button[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='pjax-container']/section[2]/div[2]/div/div/div[1]/span/div[1]/ins").click()
time.sleep(2)
# inputs = driver.find_elements_by_tag_name('input')
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
#         time.sleep(3)
driver.find_element_by_xpath("//*[@id='pjax-container']/section[2]/div[2]/div/div/div[1]/span/div[2]/button").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='pjax-container']/section[2]/div[2]/div/div/div[1]/span/div[2]/ul/li/a").click()
time.sleep(2)
# driver.find_element_by_xpath("//*[@id='audit-pass']").click()

driver.quit()

