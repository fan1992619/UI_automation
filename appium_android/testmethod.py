import time
import requests
import json
import sys
sys.path.append("D:\PycharmProjects\AWARE")
from appium import webdriver
# from common_util import CommonUtil
from appium_android.desired_capabilities import get_desired_capabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestMethod(object):
    def __init__(self):
        desired_caps = get_desired_capabilities()
        # 启动aware
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(6)
    #发送get请求
    def request_main(self):
        #首页的接口
        url = 'https://api.at.top/v1/index'
        header = {
            'Host': 'api.at.top',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.8.1',
            'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzNTYxMTk3NiwiZXhwIjoxNTY3MTQ3OTc2LCJuYmYiOjE1MzU2MTE5NzYsImp0aSI6InpFcHcyWkVrVUlTcHJxZ3YiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.Ezs1NU0qEOLgNVVfDAXA2BvEo5fAwVSqqyAqLMVLDhE',
            'deviceid': 'f4:f5:db:15:ec:1b-f4:f5:db:15:ec:1b',
            'platform': 'android',
            'userid': '33',
            'version': '2.0'
        }
        res=requests.get(url=url,headers=header,verify=False).json()
        return res
    #物理键返回
    def back_button(self):
        self.driver.keyevent(4)
        time.sleep(1)
    #搜索页面的返回键
    def search_back(self):
        self.driver.find_element_by_id("com.aware:id/search_back_iv").click()
        time.sleep(1)
    #有title的返回按钮
    def title_back(self):
        self.driver.find_element_by_id("com.aware:id/iv_title_left").click()
        time.sleep(1)
    # 获取屏幕尺寸大小
    def getSize(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return x, y

    # 向上滑动
    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.2)
        self.driver.swipe(x1, y1, x1, y2, t)
        # print (x1,y1,y2)

    # 向下滑动
    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2, t)

    # 向左滑动：从右向左滑动
    def swipeLeft(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        x2 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.85)
        self.driver.swipe(x1, y1, x2, y1, t)
        # print (x1,x2,y1)

    # 向右滑动:从左向右滑动
    def swipeRight(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        x2 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.85)
        self.driver.swipe(x1, y1, x2, y1, t)
        # print (x1, x2, y1)
    # 判断页面中的元素是否存在
    def is_element(self, identifyBy, c):
        try:
            flag_element = None
            if identifyBy == "id":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag_element = True
        except (NoSuchElementException):
            flag_element = False
        finally:
            return flag_element
    #判断页面中的元素是否存在方法二
    def source_element(self,c):
        try:
            #flag_source一定要放在里层先定义，不然会报错“local variable 'flag_source' referenced before assignment”,因为后面的判断接收不到该判断
            flag_source=None
            source=self.driver.page_source
            if c in source:
                flag_source = True
        except(NoSuchElementException):
            flag_source=False
        finally:
            return flag_source
    #搜索按钮页面返回键
    def search_back(self):
        self.driver.find_element_by_id("com.aware:id/search_back_iv").click()
        time.sleep(1)
        self.driver.find_element_by_id("com.aware:id/home_vpsearch_ll").click()
    def clean_text(self,text):
        # 清空文本框的方法
        # 123代表光标移动到最末尾
        self.driver.keyevent(123)
        for i in range(0, len(text)):
            self.driver.keyevent(67)
    def find_ele(self, id):
        ''' 获取到要删除的文本框内容 '''
        find_ele = self.driver.find_element_by_id(id)
        find_ele.click()
        return find_ele.text
    # def Delete(self):
    #     '''删除文本框内容'''
    #     get_text = self.find_ele(id)
    #     self.clean_text(get_text)
    def login_text(self):
        #未登录进行登录
        allow_button="android:id/button2"
        alert_button=self.is_element("id",allow_button)
        if alert_button:
            self.driver.find_element_by_id(allow_button).click()
            time.sleep(3)
            self.driver.find_elements_by_id("com.aware:id/base_id_tab_text")[3].click()
            time.sleep(2)
            name_element="com.aware:id/login_btn"
            flag_articel=self.is_element("id",name_element)
            if flag_articel:
                self.driver.find_element_by_id("com.aware:id/login_phone_input_et").send_keys("18782610762")
                self.driver.find_element_by_id("com.aware:id/login_code_input_et").send_keys("111111")
                self.driver.find_element_by_id("com.aware:id/login_btn").click()
            else:
                pass
        else:
            pass
    #判断是否有复制的弹框,，如果有弹框就点击取消
    def is_boxframe(self):
        c="com.aware:id/dialog_double_bottom_id_left"
        if self.source_element(c):
            self.driver.find_element_by_id(c).click()
        else:
            self.swipeDown(1000)
    #获取toast方法
    def find_toast(self, driver, text, timeout=5, poll_frequency=0.5):
        '''使用uiantomator2获取
        描述：获取Toast的文本信息
        参数：text需要检查的提示信息  time检查总时间  poll_frequency检查时间间隔
        返回值：返回与之匹配到的toast信息
        异常描述：none
        注意下述代码段：" + "'" + text + "'" + "
        使用appium1.6.2以上获取APP中的toast'
        因为当前方法编辑器识别为：//*[contains(@text, 'toast测试')]，我们需要让传入的参数带引号才能被识别，所以才有上述不好看的一段代码
        '''
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            # print(toast_loc)
            toast_text = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
            # print(toast_text)
            return True
        except:
            return False
    #测试能不能获取toast，项目详情页面文章收藏
    def test_toast(self):
        self.login_text()
        self.driver.find_elements_by_id("com.aware:id/base_id_tab_text")[2].click()
        time.sleep(2)
        self.driver.find_elements_by_id("com.aware:id/project_itme_rl")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_id("com.aware:id/article_rl")[0].click()
        time.sleep(1)
        self.driver.find_element_by_id("com.aware:id/collect_status_iv").click()
        time.sleep(1)
        # toast_log=self.driver.page_source
        # print(toast_log)
        res=self.find_toast(self.driver,'收藏成功')
        print(res)
if __name__ == '__main__':
    at=TestMethod()
    # at.login_text()
    # print(at.find_toast("登录成功"))
    at.test_toast()