#coding:utf-8
#字符串没有key
#import sys拼接字符串的时候输入中文不会报错
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from appium_android.common_util import CommonUtil
from send_mail_to import  SendEmail
class Send_query:
    def send_get(self,url,header):
        link_first = 'https://mp.weixin.qq.com/s/PghlJYjWJIKDrjV0RWaVxg'
        com_util=CommonUtil()
        sen=SendEmail()
        res=requests.get(url=url,headers=header).json()
        result = res['data']['articles'][4]['link']
        title = res['data']['articles'][4]['title']
        print "第一次更新的结果是:"+title + ":" + result
        if com_util.is_contain(link_first,result):
            print "更新失败,第一条文章数据没有更新"
            sen.send_mail(['498904925@qq.com'],"先知首页更新通知","此次更新失败")
        else:
            print "pass"
            res1 = requests.get(url=url, headers=header).json()
            link_first=res1['data']['articles'][4]['link']
            title1=res1['data']['articles'][4]['title']
            print "第二次更新的结果是:"+title1+":"+link_first
if __name__ == '__main__':
    send=Send_query()
    url = 'https://api.at.top/v1/index'
    url1='https://api.at.top/v1/account/signin'
    header1={
        'authorization': 'Bearer',
        'Content-Type': 'multipart/form-data; boundary=0637d5eb-47b1-4050-a6d5-5e6d023c5ceb',
        'Content-Length': '397',
        'Host': 'api.at.top',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.6.0'
    }
    header = {
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMDA3ODI1OCwiZXhwIjoxNTYxNjE0MjU4LCJuYmYiOjE1MzAwNzgyNTgsImp0aSI6InFSVGo2TmtKS3VmazhWd3oiLCJzdWIiOjMxLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.I0YSOhvOl4MBZuLS52gIe27DlXDCFYpM6M_xFY6lcoA',
        'Host': 'api.at.top',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.6.0'
    }
    print send.send_get(url,header)