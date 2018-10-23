import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
import uiautomator2
def get_desired_capabilities():
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