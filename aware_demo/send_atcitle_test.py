#coding:utf-8
import requests
import json
str_187_dev='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkuZGV2LmluaXRpYWx2Yy5jb21cL3YxXC9hY2NvdW50XC9zaWduaW4iLCJpYXQiOjE1MzQ1NjQyNzgsImV4cCI6MTU2NjEwMDI3OCwibmJmIjoxNTM0NTY0Mjc4LCJqdGkiOiJ5QW9SMmtqenJtMmRub0xaIiwic3ViIjoiMzMiLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.av6edKU_nNtzYcgsOqMwa6irnP04odVfnsetbE_G7tg'
str_182_dev='Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkuZGV2LmluaXRpYWx2Yy5jb21cL3YxXC9hY2NvdW50XC9zaWduaW4iLCJpYXQiOjE1MzQ1NzcyMDksImV4cCI6MTU2NjExMzIwOSwibmJmIjoxNTM0NTc3MjA5LCJqdGkiOiIyWGJIN0g0QzJjVEtYOHAxIiwic3ViIjoiMzEiLCJwcnYiOiJjOGVlMWZjODllNzc1ZWM0YzczODY2N2U1YmUxN2E1OTBiNmQ0MGZjIn0.X3BQUpXCtk4F2VpYWB6LiSAxC7tyECbigVDId8ulqpw'
url_arcitle='http://api.dev.initialvc.com/v1/projects/22/articles'
header={
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '346',
    'Host': 'api.dev.initialvc.com',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.8.1',
    'Authorization': str_182_dev,
    'deviceid': '8c:25:05:96:75:5b-8c:25:05:96:75:5b',
    'platform': 'android',
    'userid': '33',
    'version': '1.2.1',
    'Connection': 'keep-alive'
}
url_answer='http://api.dev.initialvc.com/v1/question/15345730068361/answer'
def send_articel(url,data,header):
    res=requests.post(url=url,data=data,headers=header).json()
    return res
def answer_test(url,data,header):
    res=requests.post(url=url,data=data,headers=header).json()
    return res
if __name__ == '__main__':
    for i in range(16):
        data_arcitle = {
            'link': 'https://www.jinse.com/bitcoin/229469{0}.html'.format(i),
            'title': 'first{0}artic'.format(i),
            'type': '1'
        }
        res=send_articel(url_arcitle,data_arcitle,header)
        print('第%d次' % i, res)
        # data_answer={
        #     'content':'来测试一下回答的的激励算发有么有生效，有没有到20个字'.format(i)
        # }
        # res=answer_test(url_answer,data_answer,header)
        # print('第%d次' % i, res)
