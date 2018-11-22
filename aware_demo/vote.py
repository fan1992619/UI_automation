import requests
import json
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def send_get(url,header,data=None):
    res=requests.post(url=url,headers=header,data=data,verify=False)
    # print(res.content)
    # print(res)
    return res.status_code
if __name__ == '__main__':
    for i in range(10):
        header_android={
            'Host': 'www.iterduo.com',
            'Content-Length': '16',
            'Accept': '*/*',
            'Origin': 'http://www.iterduo.com',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044306 Mobile Safari/537.36 MMWEBID/4184 MicroMessenger/6.7.3.1360(0x2607033A) NetType/WIFI Language/zh_CN Process/tools',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://www.iterduo.com/2018FH/award_m/award_bangdan.html?index=8&type=1&from=groupmessage&isappinstalled=0',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,en-US;q=0.8',
            'Cookie': 'XSRF-TOKEN=eyJpdiI6Ik5QS3RxMVhXVklia3VmUkNLQmhYQ2c9PSIsInZhbHVlIjoiRnM2UkVFU0E5VjhZRTJyOEI1ZlM4ZXFkcHd2MEVWMnN6cXo5NWE5RnFBNzd4V1ljN09DV3E1MHBvWW9XbGZPNHBaOUlXYlwvMmFQdjlvMTk1c0VXNUdRPT0iLCJtYWMiOiI4MzI0ZDA3MTVlODYzMjMxN2ExODU2NGJlY2ZkYWI4N2Q5MzNmZDMxNzczNzhmMjhlNDMxNDBiNjUwMjVjZWM4In0%3D; laravel_session=eyJpdiI6IldTcVgyT0lQVlF4U09uRGRLR0drOXc9PSIsInZhbHVlIjoieFwvTmJuN0kwUHdLZHZPSUp0SGp1RUpTVUpKYjFoUkhnUWxsWUNEYytZWDBTZUgzVEN2QXRFVW96VXQwU0xYSExhMXo5anNIQUNONlwvbjVGcG12ODRlZz09IiwibWFjIjoiZWJiZjg0MTVlMWVhNDZkYTEwMDJiZTY4NTQwZjZlZTNhNDUwYmRhMTIyMzg5MzBlN2U2NWNiMDI0OWRlMWQwOCJ9',
            'Connection': 'keep-alive'
        }
        data={
            'candidate_id':241
        }
        url='http://www.iterduo.com/api/vote'
        print(send_get(url,header_android,data))
        time.sleep(2)