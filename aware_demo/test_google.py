from selenium import webdriver
import time
#加载谷歌驱动
chromedriver ="C:\\Users\\edz\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.baidu.com/")
#窗口最大化
driver.maximize_window()
time.sleep(3)
#在百度搜索框输入
driver.find_element_by_id("haosou-input").send_keys("国庆")
driver.find_element_by_xpath('//*[@id="search-form"]/div/button').click()
time.sleep(5)
#关闭浏览器
driver.quit()
