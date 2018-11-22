import json
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
        # if isinstance(str_one,unicode):
        #         #不管怎样先转换成encode('unicode-escape')类型，再转换成字符串类型decode('string_escape')
        #     str_one=str_one.decode('ucicode_escape')
        if str_one in str_two:
            flag=True
        else:
            flag=False
        return flag
if __name__ == '__main__':
    com_util=CommonUtil()
    str_one={'code':0}
    str_one=json.dumps(str_one)
    print(type(str_one))
    print(str_one)
    str_two={"code": 0, "data": {"ios_public_hide": 0, "invite_reward_intro": "\u9080\u8bf7\u597d\u53cb\u4e00\u8d77\u53ef\u83b7\u597d\u53cb20%\u6536\u76ca"}}
    str_two=json.dumps(str_two)
    print(type(str_two))
    print(str_two)
    print(com_util.is_contain(str_one,str_two))

