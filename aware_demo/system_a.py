import system_b
from mock import Mock
def system_b_test():
    mock_result={u'code':1,u'data':[]}
    system_b.send_request=Mock(return_value=mock_result)
    if system_b.visit_ustack()['code'] == 0:
        print("system b正常,测试通过")
    else:
        print("system b异常,测试失败")
system_b_test()