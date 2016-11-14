# coding=utf-8

import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.emailCollect import sendReportWithAtt
reload(sys)
sys.setdefaultencoding('utf8')

basedir = os.path.abspath(os.path.dirname(__file__))
tmpEnvFile = basedir + '\.tmp'
home_path = os.environ.get('PY_DEV_HOME')

envpath = {'default': home_path + '\webTest_pro\cfg\init_default.conf',
           'dev': home_path + '\webTest_pro\cfg\init_dev.conf',
           'test': home_path + '\webTest_pro\cfg\init_test.conf',
           'debug': home_path + '\webTest_pro\cfg\init_debug.conf'}

receiver = {'default': 'wangfm@3bu.cn',
            'dev': 'wangfm@3bu.cn',
            'test': 'wangfm@3bu.cn',
            'debug': 'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn>;xiahao@3bu.cn;'

class TestRunner:
    """doc"""
    homePath = os.environ.get("PY_DEV_HOME")
    test_dir = '.'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_sta.py')

    def __init__(self, exectype='default'):

        self.exectype = exectype
        if exectype == 'default':
            with open(tmpEnvFile, 'w+') as f:
                f.write(envpath['default'])
            self.receiver = receiver['default']
            self.test_dir = '.'
        elif exectype == 'dev':
            with open(tmpEnvFile, 'w+') as f:
                f.write(envpath['dev'])
            self.receiver = receiver['dev']
            self.test_dir = '.'
        elif exectype == 'test':
            with open(tmpEnvFile, 'w+') as f:
                f.write(envpath['test'])
            self.receiver = receiver['test']
            self.test_dir = '.'
        elif exectype == 'debug':
            with open(tmpEnvFile, 'w+') as f:
                f.write(envpath['test'])
            self.receiver = receiver['test']
            self.test_dir = '.'
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

    def run(self):
        now = time.strftime("%Y-%m-%d%H%H%S")
        filename = reportPath + now + '_restult.html'
        fp = open(filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
        runner.run(self.receiver)
        fp.close()

if __name__ == '__main__':
    #
    # # print basedir
    # # print tmpEnvFile
    #
    # # with open(tmpEnvFile, 'w+') as f:
    # #     f.write(envpath['test'])
    #
    # with open(tmpEnvFile, 'r+') as f:
    #     pathTmp = f.readlines()
    #
    # print type(pathTmp)
    # print pathTmp
    runner = TestRunner('dev')
    runner.run()
