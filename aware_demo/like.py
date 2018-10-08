#coding:utf-8
import requests
import json
import datetime
url='https://api.at.top/v1/articles/25707426170808868/like'
header={
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMDA3ODI1OCwiZXhwIjoxNTYxNjE0MjU4LCJuYmYiOjE1MzAwNzgyNTgsImp0aSI6InFSVGo2TmtKS3VmazhWd3oiLCJzdWIiOjMxLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.I0YSOhvOl4MBZuLS52gIe27DlXDCFYpM6M_xFY6lcoA',
    'Host': 'api.at.top',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.6.0'
}
def time():
    today=datetime.date.today()
    print(today)
    return today
def send_get(url,header):
    res=requests.get(url=url,headers=header).json()
    return res
if __name__ == '__main__':
    time()

