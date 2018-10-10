#coding:utf-8
import requests
import json
# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
url='https://api.at.top/v1/articles/redirect/40676520884185644'
def send_post(url,data=None):
    res=requests.post(url=url,data=data).text
    return res
if __name__ == '__main__':
    print(send_post(url))


