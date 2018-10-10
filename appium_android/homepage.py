#coding:utf-8
import datetime
import sys
sys.path.append("D:\PycharmProjects\AWARE")
import os
import requests
import json
# from selenium import webdriver
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver import Remote
import unittest
import time
from common_util import CommonUtil
from desired_capabilities import get_desired_capabilities
# from runmethod import RunMethod
# sys.setdefaultencoding("gbk")
# import codecs
# fr = codecs.open("0.htm","r","gbk")
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
class HomePage(object):
    def __init__(self):
        # self.run_test=RunMethod()
        self.com=CommonUtil()
        desired_caps = get_desired_capabilities()
        #启动aware
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)
        self.home_page=self.driver.find_element_by_xpath("//*[@text='首页']")
        self.follow=self.driver.find_element_by_xpath("//*[@text='关注']")
        self.project_map=self.driver.find_element_by_xpath("//*[@text='项目地图']")
        self.my=self.driver.find_element_by_xpath("//*[@text='我的']")
    # def driver_one(self):
    #     desired_caps = get_desired_capabilities()
    #     # 启动aware
    #     diver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    #     return driver
    #banner
    def test_banner(self):
        for i in range(3):
            self.swipeLeft(1000)
            self.driver.tap([(348,363),(414,429)],900)
            self.back_button()
    #大盘行情
    def big_Quotation(self):
        url='https://api.at.top/v1/globals'
        self.swipeDown(1000)
        res1=requests.get(url).json()
        btc_one=res1['data']['list'][1]['price']
        print(btc_one)
        time.sleep(13)
        self.swipeDown(1000)
        res2 = requests.get(url).json()
        btc_two = res2['data']['list'][1]['price']
        print(btc_two)
        if btc_one != btc_two:
            print ("数字行情更新成功")
        else:
            print ("数字行情更新失败")
        self.driver.quit()
    #热门项目
    def hot_project(self):
        #热门项目定位，数量6个
        hot_e1 = self.driver.find_element_by_id("com.aware:id/home_hot_ll")
        hot_e3 = hot_e1.find_elements_by_class_name("android.widget.RelativeLayout")
        # hot=hot_e3[0].find_elements_by_class_name("android.widget.TextView")[0].text
        if len(hot_e3)==6:
            print("热门项目数量符合预期:{0}".format(len(hot_e3)))
        else:
            print("热门项目数量不符合预期:{0}".format(len(hot_e3)))
            #   get_attribute--获取content - desc属性，这里注意了，如果content - desc属性为空，那么获取的就是text属性，不为空获取的才是content - desc属性,content- desc属性为空, 打印结果：书架
            #   driver.find_element_by_id("com.baidu.yuedu:id/lefttitle").text  获取元素的文本
        for i in range(6):
            #   获取热门项目的标题
            t2 = hot_e3[i].find_elements_by_class_name("android.widget.TextView")[0].text
            # t2=hot.encode('utf-8')
            hot_e3[i].click()
            time.sleep(2)
            #   获取热门项目——详情页的标题
            t1=self.driver.find_element_by_id("com.aware:id/tv_title_title").text
            # t1=t1.encode('utf-8')
            t3='一级市场'
            # print(t1)
            if self.com.is_contain(t1,t3):
                #   获取第一页的数量
                e1=self.driver.find_element_by_id("com.aware:id/project_listview").find_elements_by_id("com.aware:id/project_itme_rl")
                e2=e1[i].find_element_by_id("com.aware:id/project_unissueed_tv").text
                # print(type(e2))
                print(e2)
            elif self.com.is_contain(t1,t2):
                print('第%d次' % i,"首页热门标题:{0}".format(t2), "-->","项目详情页标题符合预期:{0}".format(t1))
                # print('第%d次' % i, res)
            else:
                pass
            self.back_button()
        self.driver.quit()
    #发送get请求
    def request_main(self):
        #首页的接口
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
        return res
    #首页深度回答
    def homepage_deep_answer(self):
        answer_one = self.driver.find_element_by_id("com.aware:id/question_rl")
        answer_two = answer_one.find_elements_by_class_name("android.widget.TextView")
        res = self.request_main()
        deep_num = len(res['data']['deep_answers'])
        if deep_num == 5:
            print("深度回答的数量为{0}个".format(deep_num), "--->符合预期")
        else:
            print("深度回答的数量为{0}个".format(deep_num), "--->不符合预期")
        answer_two[0].click()
        # 深度回答的总的列表
        deep_answer_list = self.driver.find_element_by_id(
            "com.aware:id/home_question_hot_list").find_elements_by_id(
            "com.aware:id/qa_rl")
        # print(len(wait_answer_list))
        self.driver.find_elements_by_id("com.aware:id/post_title_tv")[0].click()
        answer_title = '回答详情'
        deep_click_answer_title = self.driver.find_element_by_id("com.aware:id/tv_title_title").text
        if self.com.is_contain(answer_title, deep_click_answer_title):
            print("深度回答跳转回答详情页--->成功")
            self.back_button()
        else:
            print("深度回答跳转失败")
        deep_down_cell = deep_answer_list[0].find_element_by_id(
            "com.aware:id/post_info_rl").find_elements_by_class_name(
            "android.widget.TextView")
        client_deep_question_title = deep_answer_list[0].find_element_by_id("com.aware:id/post_title_tv").text
        # print(client_question_title)
        # 项目icon，回答个数，关注人数
        client_deep_icon = deep_down_cell[0].text
        # 判断赞同文本和评论文本
        deep_like = '赞同'
        deep_comment = '评论'
        client_deep_answer_like_num = deep_down_cell[1].text
        if self.com.is_contain(deep_like, client_deep_answer_like_num):
            pass
        else:
            print("深度回答文本错误:{0}".format(client_deep_answer_like_num))
        client_deep_comment_num = deep_down_cell[2].text
        if self.com.is_contain(deep_comment, client_deep_comment_num) and self.com.is_contain(deep_like,
                                                                                              client_deep_answer_like_num):
            pass
        else:
            print("深度回答文本错误:{0}".format(client_deep_answer_num))
        print("等待回答的title为:{0}".format(client_deep_question_title),
              "项目icon文本名称为:{0}".format(client_deep_icon),
              "赞同个数为:{0}".format(client_deep_answer_like_num),
              "评论人数:{0}".format(client_deep_comment_num))
    #首页热门问题
    def homepage_hot_question(self):
        answer_one = self.driver.find_element_by_id("com.aware:id/question_rl")
        answer_two = answer_one.find_elements_by_class_name("android.widget.TextView")
        res = self.request_main()
        hot_num = len(res['data']['hot_questions'])
        if hot_num == 10:
            print("热门问题的数量为{0}个".format(hot_num), "--->符合预期")
        else:
            print("热门问题的数量为{0}个".format(hot_num), "--->不符合预期")
        answer_two[1].click()
        self.driver.find_elements_by_id("com.aware:id/post_title_tv")[0].click()
        self.back_button()
        # 热门问题总的列表
        hot_answer_list = self.driver.find_element_by_id("com.aware:id/home_question_hot_list").find_elements_by_id(
            "com.aware:id/qa_rl")
        hot_down_cell = hot_answer_list[0].find_element_by_id("com.aware:id/post_info_rl").find_elements_by_class_name(
            "android.widget.TextView")
        # 获取热门问题第一行的title，项目icon的文本，回答个数，关注人数
        hot_question_title = hot_answer_list[0].find_element_by_id("com.aware:id/post_title_tv").text
        hot_icon = hot_down_cell[0].text
        hot_answer_num = hot_down_cell[1].text
        hot_follow_num = hot_down_cell[2].text
        print("热门问题的title为:{0}".format(hot_question_title),
              "项目icon文本名称为:{0}".format(hot_icon),
              "回答个数为:{0}".format(hot_answer_num),
              "关注人数为:{0}".format(hot_follow_num))
    #首页待会答
    def homepage_wait_answer(self):
        answer_one = self.driver.find_element_by_id("com.aware:id/question_rl")
        answer_two = answer_one.find_elements_by_class_name("android.widget.TextView")
        res = self.request_main()
        wait_num = len(res['data']['unpopular_questions'])
        if wait_num == 10:
            print("等待回答的数量为{0}个".format(wait_num), "--->符合预期")
        else:
            print("等待回答的数量为{0}个".format(wait_num), "--->不符合预期")
        answer_two[2].click()
        self.driver.find_elements_by_id("com.aware:id/post_title_tv")[0].click()
        self.back_button()
        # 等待回答的总的列表
        wait_answer_list = self.driver.find_element_by_id("com.aware:id/home_question_hot_list").find_elements_by_id(
            "com.aware:id/qa_rl")
        # print(len(wait_answer_list))
        wait_down_cell = wait_answer_list[0].find_element_by_id(
            "com.aware:id/post_info_rl").find_elements_by_class_name(
            "android.widget.TextView")
        client_wait_question_title = wait_answer_list[0].find_element_by_id("com.aware:id/post_title_tv").text
        # print(client_question_title)
        # 项目icon，回答个数，关注人数
        client_wait_icon = wait_down_cell[0].text
        client_wait_answer_num = wait_down_cell[1].text
        client_wait_follow_num = wait_down_cell[2].text
        print("等待回答的title为:{0}".format(client_wait_question_title),
              "项目icon文本名称为:{0}".format(client_wait_icon),
              "回答个数为:{0}".format(client_wait_answer_num),
              "关注人数为:{0}".format(client_wait_follow_num))
    #热门问答页面
    def hot_answer(self):
        # 回答的一级定位和属性数量
        self.swipeDown(1000)
        self.swipeUp(1000)
        answer_one = self.driver.find_element_by_id("com.aware:id/question_rl")
        answer_two = answer_one.find_elements_by_class_name("android.widget.TextView")
        # 检查一级定位的文本
        for i in range(len(answer_two)):
            client_answer_text = answer_two[i].text
            print("热门回答的的文本分别为:{0}".format(client_answer_text))
            str_wait_answer = '待回答'
            str_hot_answer = '热门问题'
            str_Deep_answer='深度回答'
            if self.com.is_contain(str_hot_answer, client_answer_text):
                #热门回答
                self.homepage_hot_question()
            elif self.com.is_contain(str_wait_answer, client_answer_text):
                #等待回答
                self.homepage_wait_answer()
            elif self.com.is_contain(str_Deep_answer,client_answer_text) :
                # 深度回答
                self.homepage_deep_answer()
            else:
                # 更多页面
                answer_two[i].click()
                more_text=self.driver.find_element_by_id("com.aware:id/id_stickynavlayout_indicator").find_elements_by_class_name("android.widget.TextView")
                # print(len(more_text))
                more_deep_answer='深度回答'
                more_hot_answer='热门'
                more_wait_answer='待回答'
                for i in range(len(more_text)):
                    if self.com.is_contain(more_deep_answer,more_text[i].text):
                        more_text[i].click()
                        self.swipeDown(1000)
                        self.swipeUp(1000)
                        self.driver.find_elements_by_id("com.aware:id/post_title_tv")[0].click()
                        answer_title = '回答详情'
                        deep_click_answer_title = self.driver.find_element_by_id("com.aware:id/tv_title_title").text
                        if self.com.is_contain(answer_title, deep_click_answer_title):
                            print("更多页面深度回答跳转回答详情页--->成功")
                            self.back_button()
                        else:
                            print("深度回答跳转失败")
                    elif self.com.is_contain(more_hot_answer,more_text[i].text):
                        more_text[i].click()
                        self.swipeDown(1000)
                        self.swipeUp(1000)
                        self.driver.find_elements_by_id("com.aware:id/post_title_tv")[0].click()
                        self.back_button()
                    elif self.com.is_contain(more_wait_answer,more_text[i].text):
                        more_text[i].click()
                        self.swipeDown(1000)
                        self.swipeUp(1000)
                        self.driver.find_elements_by_id("com.aware:id/post_title_tv")[0].click()
                        self.back_button()
                self.driver.find_element_by_id("com.aware:id/qa_post_tv").click()
                question_text = '提问'
                put_question_title=self.driver.find_element_by_id("com.aware:id/tv_title_title").text
                if self.com.is_contain(question_text,put_question_title):
                    print("从更多页面跳转提问页面--->成功")
                    self.back_button()#返回更多页面
                else:
                    print("跳转失败")
                self.back_button()#返回主页面
        self.driver.quit()
    #最热文章
    def hot_articles(self):
        res=self.request_main()
        article_num=res['data']['articles']
        # print(len(article_num))
        if len(article_num)==30:
            print("最热文章的数量为:{0}个".format(len(article_num))+"--->符合预期")
        else:
            print("最热文章数量--->不符和预期")
        for i in range(3):
            self.swipeUp(1000)
        best_hot=self.driver.find_element_by_id("com.aware:id/home_hotarticle_ll")
        best_title=best_hot.find_element_by_class_name("android.widget.TextView").text
        print(best_title)
        #最热文章标题list
        best_article_title_list=self.driver.find_element_by_id("com.aware:id/home_article_list_ll").find_elements_by_id("com.aware:id/article_title_tv")
        # print(len(best_article_title_list))
        #显示icon，作者，阅读数，点赞数并获取文本
        best_down_cell_list=self.driver.find_element_by_id("com.aware:id/article_info_rl").find_elements_by_class_name("android.widget.TextView")
        # print(len(best_down_cell_list))
        article_icon=best_down_cell_list[0].text
        article_reprint=best_down_cell_list[1].text
        article_name=best_down_cell_list[2].text
        article_read_num=best_down_cell_list[3].text
        article_like_num=best_down_cell_list[4].text
        best_article_title = best_article_title_list[0].text
        print("文章的标题为:{0}".format(best_article_title),"项目icon为:{0}".format(article_icon),
              "作者为:"+article_reprint,article_name,"阅读数为:{0}".format(article_read_num),
              "点赞数为:{0}".format(article_like_num))
        #进入文章详情页面
        best_article_title_list[0].click()
        article_detail_onlist=self.driver.find_element_by_id("com.aware:id/article_user_rl").find_elements_by_class_name("android.widget.TextView")
        article_detail_user=article_detail_onlist[0].text
        if self.com.is_contain(article_name,article_detail_user):
            print("文章作者--->符合预期")
        else:
            print("文章作者--->不符合预期")
            #获取当前时间
        today=datetime.date.today()
        article_detail_releasetime=article_detail_onlist[1].text
        if self.com.is_contain(str(today),article_detail_releasetime):
            print("最热文章--->是{0}当天的随机文章--->符合预期".format(article_detail_releasetime))
        else:
            print("最热文章--->不符合预期")
        article_detail_read=article_detail_onlist[2].text
        if self.com.is_contain(article_read_num,article_detail_read):
            print("文章阅读数--->符合预期")
        else:
            print("文章阅读数--->不符合预期")
        article_user_detail_state=article_detail_onlist[3].text
        self.back_button()
        for i in range(3):
            self.swipeUp(1000)
        self.driver.quit()
    #项目地图
    def test_Projectmap(self):
        quotation.click()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@text='一种点对点的电子现金系统']").click()
        time.sleep(1)
    #左上角返回按钮
    def back_button(self):
        # driver.find_element_by_id("com.aware:id/iv_title_left").click()
        # driver.tap([(48, 63), (114, 129)],900)
        #物理键返回
        self.driver.keyevent(4)
        time.sleep(1)
        # self.driver.quit()
    #获取屏幕尺寸大小
    def getSize(self):
        x=self.driver.get_window_size()['width']
        y=self.driver.get_window_size()['height']
        return x,y
    #向上滑动
    def swipeUp(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.75)
        y2=int(l[1]*0.2)
        self.driver.swipe(x1,y1,x1,y2,t)
        # print (x1,y1,y2)
    #向下滑动
    def swipeDown(self,t):
        l=self.getSize()
        x1=int(l[0]*0.5)
        y1=int(l[1]*0.25)
        y2=int(l[1]*0.75)
        self.driver.swipe(x1,y1,x1,y2,t)
    #向左滑动：从右向左滑动
    def swipeLeft(self,t):
        l=self.getSize()
        x1=int(l[0]*0.75)
        x2=int(l[0]*0.05)
        y1=int(l[1]*0.85)
        self.driver.swipe(x1,y1,x2,y1,t)
        # print (x1,x2,y1)
    #向右滑动:从左向右滑动
    def swipeRight(self,t):
        l=self.getSize()
        x1=int(l[0]*0.05)
        x2=int(l[0]*0.75)
        y1=int(l[1]*0.85)
        self.driver.swipe(x1,y1,x2,y1,t)
        # print (x1, x2, y1)
if __name__ == '__main__':
    run=HomePage()
    # run.test_banner()
    # run.test_Quotation()
    # run.hot_project()
    # run.hot_answer()
    # run.request_main()
    run.hot_articles()