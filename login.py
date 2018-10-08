#coding:utf-8
#字符串没有key
#import sys拼接字符串的时候输入中文不会报错
import requests
import sys
class Send_query:
    def send_post(self,url,data,header):
        res=requests.post(url=url,data=data,headers=header).json()
        return res
if __name__ == '__main__':
    send=Send_query()
    url='http://api.test.initialvc.com/v1/account/signin'
    header={
        'Host': 'api.test.initialvc.com',
        'Content-Type': 'application/json',
        'deviceid': '88540e12fd4944598903d3cd8844f1ba',
        'Accept': '*/*',
        'User-Agent': 'AWARE-iOS/1.0 (top.at.awareDebug; build:1; iOS 11.1.2) Alamofire/4.7.2',
        'Accept-Language': 'zh-Hans-CN;q=1.0',
        'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5',
        'Content-Length': '45',
        'Connection': 'keep-alive'
    }
    data={
        'phone':'18782610762',
        'verifycode':'111111'
    }
    print (send.send_post(url,data,header))