from selenium import webdriver
import os
import time
chromedriver="C:\\Users\\edz\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.baidu.com/")
driver.maximize_window()
text_button=driver.find_element_by_id("kw")
text_button.click()#点击事件
text_button.send_keys("shixiufang") #输入内容后+点击