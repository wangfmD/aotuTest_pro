# coding:utf-8
import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

reload(sys)
sys.setdefaultencoding('utf8')

homePath = os.environ.get("PY_DEV_HOME")
reportPath = homePath + '\webTest_pro\\report\\'
# print  reportPath
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d%H%H%S")
    # filename = './report/' + now + '_restult.html'
    filename = reportPath + now + '_restult.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
    # print  reportPath
