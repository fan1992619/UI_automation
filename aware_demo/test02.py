from aware_demo.test01 import TestAction
class TestAction02(TestAction):
    def __init__(self):
        super(TestAction02,self).__init__()
        # self.test=TestAction()
    def copy_test(self):
        self.driver.find_element_by_xpath("//*[@text='项目地图']").click()
        TestAction.click_test(self)
if __name__ == '__main__':
    run_main=TestAction02()
    run_main.copy_test()
