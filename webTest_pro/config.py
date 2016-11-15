# coding=utf-8

import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from common.emailCollect import sendReportWithAtt
reload(sys)
sys.setdefaultencoding('utf8')

home_path = os.environ.get('PY_DEV_HOME')
basedir = os.path.abspath(os.path.dirname(__file__))
tmpEnvFile = home_path + '\webTest_pro\common\.tmp'

envpath = {'default': home_path + '\webTest_pro\cfg\init_default.conf',
           'dev': home_path + '\webTest_pro\cfg\init_dev.conf',
           'test': home_path + '\webTest_pro\cfg\init_test.conf',
           'debug': home_path + '\webTest_pro\cfg\init_debug.conf'}

receiver = {'default': 'wangfm@3bu.cn',
            'dev': 'wangfm@3bu.cn',
            'test': 'wangfm@3bu.cn',
            'debug': 'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn>;xiahao@3bu.cn;'}


class TestRunner:
    """doc"""

    def __init__(self, exectype='default'):
        self.homePath = os.environ.get("PY_DEV_HOME")
        # test_dir = '.'
        self.tmpEnvFile = self.homePath + '\webTest_pro\common\.tmp'
        self.exectype = exectype
        if exectype == 'default':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['default'])
            self.receiver = receiver['default']
            self.test_dir = '.'
        elif exectype == 'dev':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['dev'])
            self.receiver = receiver['dev']
            self.test_dir = '.'
        elif exectype == 'test':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['test'])
            self.receiver = receiver['test']
            self.test_dir = '.'
        elif exectype == 'debug':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['test'])
            self.receiver = receiver['test']
            self.test_dir = '.'
        else:
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['default'])
            self.receiver = receiver['default']
            self.test_dir = '.'
        #
        self.discover = unittest.defaultTestLoader.discover(self.test_dir, pattern='*_sta.py')
        # 设置测试报告路径
        if os.name == 'nt':
            self.reportPath = self.homePath + '\webTest_pro\\report\\'
        else:
            self.reportPath = self.homePath + '/webTest_pro/report/'
        # 测试报告路径不存在，则创建该路径
        if os.path.exists(self.reportPath) == True:
            print "The report path exist!"
        else:
            print "The report path is not exist,create report directory..."
            os.mkdir(self.reportPath)

    def run(self):
        self.now = time.strftime("%Y-%m-%d%H%H%S")
        self.filename = self.reportPath + self.now + '_restult.html'
        fp = open(self.filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
        runner.run(self.discover)
        sendReportWithAtt(self.filename, self.receiver)
        fp.close()

if __name__ == '__main__':
    runner = TestRunner('dev')
    runner.run()
