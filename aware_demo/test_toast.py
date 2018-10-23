from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class GetToast:
    def get_desired_capabilities(self):
        desired_caps = {
            'platformName':'Android',
            'platformVersion':'6.0',
            'deviceName':'NNQWDQDMVKYP59JF',
            'appPackage':'com.aware',
            'appActivity':'com.aware.moudle_main.ui.activity.MainActivity',
            'automationName':'uiautomator2',
            'newCommandTimeout':'50',#appium服务器等待appium客户端发送新消息的时间，默认为60s
            'unicodeKeyboard':True,#是否支持Unicode键盘，如果如要输入中文，要设置为True
            'resetKeyboard':True,
            #升级appium大于1.6版本之后，需要设置noReset为true，否则每次都会重新登录
            'noReset':True
        }
        return desired_caps
    def is_toast_exist(self,driver,text,timeout=5,poll_frequency=0.5):
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            # print(toast_loc)
            toast_text=WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            # print(toast_text)
            return True
        except:
            return False
if __name__ == "__main__":
    gettoast=GetToast()
    desired_caps=gettoast.get_desired_capabilities()
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    time.sleep(5)
    # 等主页面activity出现
    # driver.wait_activity(".base.ui.MainActivity", 10)
    driver.find_elements_by_id("com.aware:id/base_id_tab_text")[2].click()
    time.sleep(2)
    driver.find_elements_by_id("com.aware:id/project_itme_rl")[0].click()
    time.sleep(1)
    driver.find_elements_by_id("com.aware:id/article_rl")[0].click()
    time.sleep(1)
    driver.find_element_by_id("com.aware:id/collect_status_iv").click()
    time.sleep(1)
    #判断是否出现toast收藏成功
    print(gettoast.is_toast_exist(driver, '收藏成功'))