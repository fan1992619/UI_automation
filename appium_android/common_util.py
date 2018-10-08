#coding=utf-8
import unicodedata
class CommonUtil:
#判断一个字符串是否包含另一个字符串
#str_one：查找的字符串
#str_two：被查找的字符串
#判断一下，传的值是一个什么类型，如果是unicode类型，那么就转化成字符串，
#语法isinstance(str_one,unicode)
    def is_contain(self,str_one,str_two):
        flag=None
        #如果说是unicode类型，那么就需要转译
        if isinstance(str_one,unicode):
                #不管怎样先转换成encode('unicode-escape')类型，再转换成字符串类型decode('string_escape')
            # print(1,type(str_one))
            str_one=str_one.encode('unicode-escape').decode('string_escape')
        # if isinstance(str_two,unicode):
        #     str_two=str_two.encode('unicode-escape').decode('string_escape')
            # print(1,type(str_one))
        # if str_one is unicode and str_two is unicode:
        #     str_one=str_one.decode('utf-8')
        #     str_two=str_two.decode('utf-8')
        # print(str_one,str_two)
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
if __name__ == '__main__':
    com_util=CommonUtil()
    a="我们"
    print(type(a))
    b="我们"
    print(com_util.is_contain(a,b))

