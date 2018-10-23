import time
import sys
sys.path.append("D:\PycharmProjects\AWARE")
from appium import webdriver
from appium_android.homepage import HomePage
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from appium_android.testmethod import TestMethod
from appium_android.common_util import CommonUtil
from appium_android.send_articles import SendArticles
class Search(TestMethod):
    def __init__(self):
        super(Search,self).__init__()
        self.com=CommonUtil()
        self.get_article=SendArticles()
    def search_test(self):
        home_search_box=self.driver.find_element_by_id("com.aware:id/home_vpsearch_ll").find_element_by_class_name("android.widget.TextView")
        if self.com.is_contain("项目/币种",home_search_box.text):
            print("搜索框的文本为[{0}]--->符合预期".format(home_search_box.text))
        else:
            print("搜索文本框--->不符合预期")
        home_search_box.click()
        # 获取当前页面的所有元素
        source = self.driver.page_source
        # print(source)
        search_text = self.driver.find_element_by_id("com.aware:id/search_search_tv").text
        if self.com.is_contain("搜索",search_text):
            print("跳转搜索页面--->成功")
        else:
            print("跳转失败")
        c = "com.aware:id/search_history_rl"
        flag = self.is_element("id", c)
        search_list=["at", "五条", "btc", "eth", "cmt", "/n","\n", "草莓糖", " yierkahdfkjksadfkjsdjflskjfla k j", "null",
                     "/n", "ht","$8*","这是一个搜索的case，", "usdt", "XMR", "AI欧塔", "习近平", "阿斯蒂芬好看就", "adfjka", "b", "c"]
        search_list_nums=len(search_list)
        search_box_id="com.aware:id/search_input_et"
        # 判断这个页面有没有这个元素
        if flag:
            print(flag)
            # print(search_history_num)
            #清空搜索历史
            self.driver.find_element_by_id("com.aware:id/search_delete").click()
            for i in range(search_list_nums):
                # 随机取list里面的元素
                search_list_ran = random.choice(search_list)
                self.driver.find_element_by_id("com.aware:id/search_input_et").send_keys(search_list_ran)
                self.driver.find_element_by_id("com.aware:id/search_search_tv").click()
                #清空文本框
                search_content=self.find_ele(search_box_id)
                self.clean_text(search_content)
                time.sleep(1)
                search_history = self.driver.find_element_by_id(
                    "com.aware:id/search_history_rl").find_elements_by_class_name("android.widget.TextView")
                search_history_num = len(search_history)
                # print("第%d次搜索的文本为:{0}".format(search_history[i].text) % i+1)
                if i==20:
                    for j in range(search_history_num):
                        print(search_history[j].text)
                    break
            self.driver.quit()
        else:
            print(flag)
            hot_search_list=self.driver.find_element_by_id("com.aware:id/search_flow_hot").find_elements_by_id("com.aware:id/tag_tv")
            hot_search_list[0].click()
            search_content=self.find_ele(search_box_id)
            self.clean_text(search_content)
            self.search_back()
            hot_search_list[1].click()
            time.sleep(1)
            self.driver.quit()


    def follow_tab(self):
        if self.flag:
            self.driver.find_elements_by_id("com.aware:id/base_id_tab_img")[1].click()
            follow_project = self.driver.find_element_by_id("com.aware:id/project_listview").find_elements_by_id("com.aware:id/project_itme_rl")
            print(len(follow_project))
            if len(follow_project) < 1:
                null_text=self.driver.find_element_by_id("com.aware:id/project_listview").find_element_by_class_name("android.widget.TextView").text
                # print(null_text)
                if self.com.is_contain("没有更多内容了",null_text):
                    print("关注tab没有关注的项目")
                    self.driver.find_elements_by_id("com.aware:id/base_id_tab_text")[3].click()
            else:
                HomePage.swipeDown(self,1000)
        else:
            self.login_text()
        # toast_id = ("xpath", "//*[contains(@text='登录成功')]")
        # toast_login_test=WebDriverWait(self.driver,5,0.01).until(EC.presence_of_element_located(toast_id))
        # toast_login_test = WebDriverWait(self.driver, 1, 0.5).until(
        #     expected_conditions.presence_of_element_located(toast_id))
        # print(toast_login_test.text)
    #
    # def always_allow(self,num=2):
    #     # 处理获取手机权限的弹框,该方法暂时不能通用，后期继续调试
    #     for i in range(num):
    #         loc = ("id","com.aware:id/dialog_double_bottom_id_right")
    #         try:
    #             e1=WebDriverWait(self.driver,1,0.5).until(expected_conditions.presence_of_element_located(loc))
    #             e1.click()
    #         except:
    #             pass
    # 转载文章
    def send_article_question(self):
        TestMethod.is_boxframe(self)
        self.driver.find_elements_by_id("com.aware:id/base_id_tab_text")[3].click()
        time.sleep(2)
        TestMethod.login_text(self)
        self.driver.find_element_by_id("com.aware:id/main_iv_post").click()
        photos=self.driver.find_elements_by_class_name("android.widget.TextView")
        for i in range(len(photos)):
            send_text=photos[i].text
            if self.com.is_contain("转载文章",send_text):
                photos[i].click()
                title=self.driver.find_element_by_id("com.aware:id/tv_title_title").text
                print("转载文章页面的标题是:{0}".format(title),"--->符合预期")
                #所属项目-->文章分类-->文章链接-->url
                #随机选择项目类型
                self.driver.find_element_by_id("com.aware:id/publish_project_name").click()
                project_list=self.driver.find_elements_by_id("com.aware:id/project_rl")
                random_project=random.choice(project_list)
                random_project.click()
                #随机选择文章类型
                article_class=self.driver.find_element_by_id("com.aware:id/flowlayout").find_elements_by_class_name("android.widget.RelativeLayout")
                random_articles_class=random.choice(article_class)
                random_articles_class.click()
                #随机选择文章的url
                url_num = random.randint(2, 20)
                url=self.get_article.open_url(url_num)
                # print(url)
                self.driver.find_element_by_id("com.aware:id/publish_project_link").send_keys(url)
                time.sleep(2)
                self.driver.find_element_by_id("com.aware:id/publish_project_title").click()
                self.driver.find_element_by_id("com.aware:id/iv_title_right").click()
                # self.driver.quit()
            elif self.com.is_contain("提问",send_text):
                photos[i].click()

            else:
                continue
if __name__ == '__main__':
    sear = Search()
    # sear.search_test()
    # sear.my_homepage()
    # sear.follow_tab()
    sear.send_article_question()