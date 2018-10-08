import requests
from lxml import html
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
def spider(sn):
    """ 爬取京东的图书数据 """
    url = 'https://search.jd.com/Search?keyword={0}'.format(sn)
    # 获取HTML文档

    resp = requests.get(url)
    print(resp.encoding)
    resp.encoding = 'utf-8'

    html_doc = resp.text

    # 获取xpath对象
    selector = html.fromstring(html_doc)

    # 找到列表的集合
    ul_list = selector.xpath('//div[@id="J_goodsList"]/ul/li')
    print(len(ul_list))

    # 解析对应的内容，标题，价格，链接
    for li in ul_list:
        # 标题
        title = li.xpath('div/div[@class="p-name"]/a/@title')
        print(title[0])
        # 购买链接
        link = li.xpath('div/div[@class="p-name"]/a/@href')
        print(link[0])

        # 价格
        price = li.xpath('div/div[@class="p-price"]/strong/i/text()')
        print(price[0])

        # 店铺
        store = li.xpath('div//a[@class="curr-shop"]/@title')
        print(store[0])

def get_main():
    url = 'https://api.at.top/v1/index'
    header = {
        'Host': 'api.at.top',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.8.1',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvYXBpLmF0LnRvcFwvdjFcL2FjY291bnRcL3NpZ25pbiIsImlhdCI6MTUzNTYxMTk3NiwiZXhwIjoxNTY3MTQ3OTc2LCJuYmYiOjE1MzU2MTE5NzYsImp0aSI6InpFcHcyWkVrVUlTcHJxZ3YiLCJzdWIiOiIzMyIsInBydiI6ImM4ZWUxZmM4OWU3NzVlYzRjNzM4NjY3ZTViZTE3YTU5MGI2ZDQwZmMifQ.Ezs1NU0qEOLgNVVfDAXA2BvEo5fAwVSqqyAqLMVLDhE',
        'deviceid': 'f4:f5:db:15:ec:1b-f4:f5:db:15:ec:1b',
        'platform': 'android',
        'userid': '33',
        'version': '2.0'
    }
    res=requests.get(url=url,headers=header).json()
    # print(res)
    # res1=json.dumps(res,indent=2,sort_keys=True)
    hot_num=len(res['data']['hot_questions'])
    #热门回答的列表详情
    for i in range(hot_num):
        hot_title=res['data']['hot_questions'][i]['title']
        hot_icon_name = res['data']['hot_questions'][i]['symbol']
        hot_answer_num = res['data']['hot_questions'][i]['answer_num']
        hot_follow_num=res['data']['hot_questions'][i]['follow_num']
        print(hot_title,hot_icon_name,hot_answer_num,hot_follow_num)
    #等待回答的列表详情
    for i in range(hot_num):
        unpopular_title=res['data']['unpopular_questions'][i]['title']
        unpopular_icon_name = res['data']['unpopular_questions'][i]['symbol']
        unpopular_answer_num = res['data']['unpopular_questions'][i]['answer_num']
        unpopular_follow_num=res['data']['unpopular_questions'][i]['follow_num']
        # print(unpopular_title,unpopular_icon_name,unpopular_answer_num,unpopular_follow_num)
if __name__ == '__main__':
    get_main()
    # spider('9787115428028')