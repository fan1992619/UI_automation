import os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
def get_desired_capabilities():
    desired_caps = {
        'platformName':'Android',
        'platformVersion':'6.0',
        'deviceName':'NNQWDQDMVKYP59JF',
        'appPackage':'com.aware',
        'appActivity':'com.aware.moudle_main.ui.activity.MainActivity',
        'automationName':'Uiautomator2',
        'unicodeKeyboard':True,
        'resetKeyboard':True
    }
    return desired_caps