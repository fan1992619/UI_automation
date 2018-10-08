#coding:utf-8
#字符串没有key
import requests
import time
from appium_android.common_util import CommonUtil
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# header={
#     'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMDA3ODI1OCwiZXhwIjoxNTYxNjE0MjU4LCJuYmYiOjE1MzAwNzgyNTgsImp0aSI6InFSVGo2TmtKS3VmazhWd3oiLCJzdWIiOjMxLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.I0YSOhvOl4MBZuLS52gIe27DlXDCFYpM6M_xFY6lcoA',
#     'Host': 'api.at.top',
#     'Connection': 'Keep-Alive',
#     'Accept-Encoding': 'gzip',
#     'User-Agent': 'okhttp/3.6.0'
# }'
def send_get(url):
    com_util=CommonUtil()
    res=requests.get(url=url).json()
    title1 = res['data']['articles'][0]['title']
    time.sleep(3)
    title2=res['data']['articles'][0]['title']
    # print title
    print(title1,title2)
    if com_util.is_contain(title1,title2):
        print("更新失败")
    else:
        print("更新成功")
if __name__ == '__main__':
    url = 'https://api.at.top/v1/index'
    send_get(url)


