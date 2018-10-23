from appium_android.desired_capabilities import get_desired_capabilities
from appium import webdriver
class TestAction(object):
    def __init__(self):
        desired=get_desired_capabilities()
        self.driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired)
    def click_test(self):
        self.home_page=self.driver.find_element_by_xpath("//*[@text='首页']")
        self.home_page.click()
        self.follow=self.driver.find_element_by_xpath("//*[@text='关注']")
        self.follow.click()
        self.project_map=self.driver.find_element_by_xpath("//*[@text='项目地图']")
        self.project_map.click()
        self.my=self.driver.find_element_by_xpath("//*[@text='我的']")
        self.my.click()
if __name__ == '__main__':
    run=TestAction()
    run.click_test()