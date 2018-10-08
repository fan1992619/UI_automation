#coding:utf-8
import unittest
import json
class TestMethod(unittest.TestCase):
	def setUp(self):
            pass
	def test_01(self):
		url='http://coding.imooc.com/api/cate'
		data = {
			'timestamp':'1507034803124',
			'uid':'5249191',
			'uuid':'5ae7d1a22c82fb89c78f603420870ad7',
			'secrect':'078474b41dd37ddd5efeb04aa591ec12',
			'token':'7d6f14f21ec96d755de41e6c076758dd',
			'cid':'0'
		}
		res=self.run.run_main(url,'POST',data)
		#print res
		print "这是第二个case"
if __name__ == '__main__':
	unittest.main()