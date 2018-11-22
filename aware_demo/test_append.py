import re
# 要求：不要调用str2int,parseInt等转换函数。按位读取字符串里的字符进行处理将字符串转化为整数，
# 不考虑整数溢出问题，给定的输入一定是合法输入不包含非法字符，字符串头尾没有空格，考虑字符串开头可能有正负号
class Test(object):
    def str_to_int(self, str):
        # 使用正则查找字符串中全部符合条件的整数
        res = re.findall(r"^[-+]?\d+",str.strip())
        if res:
            res_str = res[0]  # 符合条件的数字的字符串
            # 判断首位是否带有符号 +
            if res_str[0] == "+":
                res_str2 = res_str[1:]
            else:
                res_str2 = res_str
            # str转int
            res_int = int(res_str2)
            return res_int
        else:
            return 0
    def re_test(self):
        '''*表示匹配前一个字符串0次或者无数次 +表示匹配前一个字符串1次或者多次 .表示任意字符串，？表示0次或者1次 []表示中括号里面任意一个字符串'''
        key=r"lalala<hTml>hello</Html>heiheihei"
        p1=r"<[Hh][Tt][Mm][Ll]>.*</[Hh][Tt][Mm][Ll]>"
        res=re.compile(p1)
        print(re.findall(res,key))
if __name__ == '__main__':
    s = Test()
    s.re_test()
    # res_str = s.str_to_int("666hello pyton")#输出666
    # res_str1 = s.str_to_int("hello pyton12")#输出0
    # res_str2 = s.str_to_int("-66hello python") # 输出-66
    # res_str3 = s.str_to_int("+66hello pyton12")  # 输出66
    # print(res_str,res_str1,res_str2,res_str3)