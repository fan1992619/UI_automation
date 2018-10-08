# coding:utf-8
import requests
import json
import time
#解决ssl证书报错导入以下包
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# verify=False  忽略https产生的ssl报错
import random
i = random.randint(1, 10000)
class RunMethod:
    # 定义一个post方法
	def post_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			res = requests.post(url=url,data=data,headers=header,verify=False).json()
			if res['code']==-204:
				print ("文章重复，false")
			elif res['code']!=0:
				res=self.delete_main(url,data,header)
				res=requests.post(url=url,data=data,headers=header,verify=False).json()
		else:
			res = requests.post(url=url,data=data,verify=False).json()
		return res
    #定义一个get方法
	def get_main(self,url,data=None,header=None):
		res = None
		if header !=None:
			# res = requests.get(url=url, data=data, headers=header, verify=False)
			# print('-'*80)
			# print(res)
			# time.sleep(5)
			res = requests.get(url=url,data=data,headers=header,verify=False).json()
		else:
			# res = requests.get(url=url, data=data, verify=False).json()
			# print('-' * 80)
			# print(res.content.decode())
			# time.sleep(5)
			res = requests.get(url=url,data=data,verify=False).json()
		return res
	#定义一个delete方法
	def delete_main(self,url,data=None,header=None):
		res=None
		res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		if res['code']!=0:
			res=self.post_main(url,data,header)
			res=requests.delete(url=url,data=data,headers=header,verify=False).json()
		return res
	def run_main(self,method,url,header=None,data=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		elif method=='delete':
			res=self.delete_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		# return json.dumps(res,ensure_ascii=False)
		return res
if __name__ == '__main__':
    run=RunMethod()
    url = 'https://api.at.top/v1/index'
    header = {
        'Host': 'api.at.top',
        'Accept': '*/*',
        'deviceid': 'bfd01a02cd4f4a97a0b1ceb71cd12402',
        'Connection': 'keep-alive',
        'platform': 'iOS',
        'userid': '33',
        'version': '2.0',
        'Accept-Language': 'zh-Hans-CN;q=1.0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzMzg4NDY0NywiZXhwIjoxNTY1NDIwNjQ3LCJuYmYiOjE1MzM4ODQ2NDcsImp0aSI6ImlGTlJkTTRSVk90S3ZhWTgiLCJzdWIiOjMzLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.uMkAI8VR6lZOCr27znRYLfkZRazvpvxDHjc8wBi1xPw',
        'User-Agent': 'AWARE-iOS/2.0 (top.at.aware; build:001; iOS 11.4.1) Alamofire/4.7.2',
        'Accept-Encoding': 'gzip;q=1.0, compress;q=0.5'
    }
    run.run_main('get',url)

