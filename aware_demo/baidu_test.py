from selenium import webdriver
import os
import time
chromedriver="C:\\Users\\edz\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://veervr.tv/")
time.sleep(15)
driver.maximize_window()
time.sleep(3)
first=driver.find_elements_by_class_name("navbar")
second=first[0].find_element_by_class_name("ant-menu")
thrid=second.find_elements_by_class_name("ant-menu-item")
thrid[2].click()
time.sleep(3)
driver.quit()
# text_button=driver.find_element_by_id("kw")
# text_button.click()#点击事件
# text_button.send_keys("shixiufang") #输入内容后+点击