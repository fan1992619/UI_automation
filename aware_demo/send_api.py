#coding:utf-8
import requests
import json
url='https://sensors.at.top/collect'
# data={
# #     'an': 'aware',
# #     'av': '2.0',
# #     'cid': '203a2ad49c914504bd9a2d475adca4a8',
# #     'ds': 'iOS',
# #     'en': 'question_view',
# #     'ev': {
# #         'question_id': '33964101063420460',
# #         'type': '1'
# #     },
# #     'sgn': 'cb30a21ece65a7cf61924fcb88546008',
# #     't': 'track',
# #     'uid': '33',
# #     'v': '1',
# #     'z': '1176287507',
# # }
data={
	"v": "1",
	"an": "aware",
	"ds": "android",
	"av": "version",
	"t": "track",
	"sgn": "b5d03013db05b1a69f01be8e8ecefda9",
	"cid": "ac:c1:ee:c0:33:34-ac:c1:ee:c0:33:34",
	"uid": "33",
	"en": "question_view",
	"ev": {
		"question_id": "33964101063420460",
		"type": "1"
	},
	"z": "1535093930281"
}
def send_post(url,data):
    res=requests.post(url=url,data=data).text
    return res
if __name__ == '__main__':
    print(send_post(url,data))


