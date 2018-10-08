from selenium import webdriver
import time
chromedriver ="C:\\Users\\edz\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.360.cn/")
driver.maximize_window()
time.sleep(3)
driver.find_element_by_id("haosou-input").send_keys("国庆")
driver.find_element_by_xpath('//*[@id="search-form"]/div/button').click()
time.sleep(5)
driver.quit()
