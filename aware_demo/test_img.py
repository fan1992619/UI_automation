import urllib.request   # 导入urllib2模块

import xlrd
import xlsxwriter
import urllib.request
from openpyxl import load_workbook,Workbook
from openpyxl.drawing.image import Image


def img_test():
    listurl = ['https://contestimg.wish.com/api/webimage/59647c7e7baa287c180fa0e0-3-original.jpg','https://contestimg.wish.com/api/webimage/59647c7e7baa287c180fa0e0-original.jpg',]

    #根据图片链接列表，把图片保存到本地
    i = 0
    for url in listurl:
        f = open(str(i)+'.jpg',"wb")    #打开文件
        req = urllib.request.urlopen(url)
        buf = req.read()              #读出文件
        f.write(buf)                  #写入文件
        i = i + 1
    #将图片一次导入到表格的1，2...行
    data = load_workbook('../appium_android/title.xlsx')
    ws=data.active
    img=Image('../aware_demo/0.jpg')
    ws.add_image(img,'E2')
    data.save('../appium_android/title.xlsx')
if __name__ == '__main__':
    img_test()