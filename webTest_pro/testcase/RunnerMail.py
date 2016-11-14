# _*_ coding: utf-8 _*_
"""
__title__ = ""
__auther__ = "acer"
__mtime__ = "2016/10/26"
"""

import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from _env import addPaths
addPaths('.')
from common.emailCollect import sendReportWithAtt

reload(sys)

sys.setdefaultencoding('utf8')

homePath = os.environ.get("PY_DEV_HOME")

# 设置测试报告路径
if os.name == 'nt':
    reportPath = homePath + '\webTest_pro\\report\\'
else:
    reportPath = homePath + '/webTest_pro/report/'

# 测试报告路径不存在，则创建该路径
if os.path.exists(reportPath) == True:
    print "The report path exist!"
else:
    print "The report path is not exist,create report directory..."
    os.mkdir(reportPath)

# print  reportPath
test_dir = '.'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')

#  receiver = 'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn>;xiahao@3bu.cn;'  # 收件人地址，多人以分号分隔
receiver = 'wangfm@3bu.cn'

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d%H%H%S")
    filename = reportPath + now + '_restult.html'

    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    runner.run(discover)
    fp.close()
    # sendReportWithAtt(filename, receiver)
