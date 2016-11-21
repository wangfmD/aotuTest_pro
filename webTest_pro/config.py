# coding=utf-8

import os
import shutil
import sys
import time
import socket
import unittest
import requests
import json
import common.init as init
from common.generateHtml.HTMLTestRunner import HTMLTestRunner
from common.emailCollect import sendReportWithAtt
from common.generateHtml.file_os import HTMLFileRunner
# from common.generateHtml.file_os import ss
reload(sys)
sys.setdefaultencoding('utf8')

home_path = os.environ.get('PY_DEV_HOME')
basedir = os.path.abspath(os.path.dirname(__file__))
tmpEnvFile = home_path + '\webTest_pro\common\.tmp'

envpath = {
    'dev_wf_56': home_path + '\webTest_pro\cfg\init_dev_56.conf',
    'dev_wf_57': home_path + '\webTest_pro\cfg\init_dev_57.conf',
    'dev_56': home_path + '\webTest_pro\cfg\init_dev_56.conf',
    'dev_57': home_path + '\webTest_pro\cfg\init_dev_57.conf',
    'default': home_path + '\webTest_pro\cfg\init_default.conf',
    'dev': home_path + '\webTest_pro\cfg\init_dev.conf',
    'test': home_path + '\webTest_pro\cfg\init_test.conf',
    'debug': home_path + '\webTest_pro\cfg\init_debug.conf'
}

receiver = {
    'dev_wf_57': 'wuf@3bu.cn',
    'dev_wf_56': 'wuf@3bu.cn',
    'dev_56': 'wangfm@3bu.cn',
    'dev_57': 'wangfm@3bu.cn',
    'default': 'wangfm@3bu.cn',
    'dev': 'wangfm@3bu.cn',
    'test': 'wangfm@3bu.cn',
    'debug':
    'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;\
        tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn>;xiahao@3bu.cn;'
}


class TestRunner:
    """doc"""

    def __init__(self, exectype='default', generateHtmlType="no"):
        self.homePath = os.environ.get("PY_DEV_HOME")
        # test_dir = '.'
        self.tmpEnvFile = self.homePath + '\webTest_pro\common\.tmp'
        self.exectype = exectype
        self.generateHtmlType = generateHtmlType
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
        elif exectype == 'dev_wf_56':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['dev_wf_56'])
            self.receiver = receiver['dev_wf_56']
            self.test_dir = '.'
        elif exectype == 'dev_wf_57':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['dev_wf_57'])
            self.receiver = receiver['dev_wf_57']
            self.test_dir = '.'
        elif exectype == 'dev_57':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['dev_57'])
            self.receiver = receiver['dev_57']
            self.test_dir = '.'
        elif exectype == 'dev_56':
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['dev_56'])
            self.receiver = receiver['dev_56']
            self.test_dir = '.'
        else:
            with open(self.tmpEnvFile, 'w+') as f:
                f.write(envpath['default'])
            self.receiver = receiver['default']
            self.test_dir = '.'
        #
        self.discover = unittest.defaultTestLoader.discover(
            self.test_dir, pattern='*_sta.py')
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
        restult=self.now + '_restult.html'
        self.filename = self.reportPath + restult
        fp = open(self.filename, 'wb')
        runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：', sqlAdd=init.db_conf)
        runner.run(self.discover)
        sendReportWithAtt(self.filename, self.receiver)
        fp.close()
        if self.generateHtmlType=='is':
            folderPath = "Z:\\reports\\"
            hostname = socket.gethostname()
            shutil.copy(self.filename, folderPath+socket.gethostbyname(hostname) + "report\\"+restult)
            HTMLFileRunner(title='测试报告 ', description='用例执行情况：').generatr(folderPath)

if __name__ == '__main__':
    runner = TestRunner('dev_wf_57','is')
    runner.run()
#     print init.db_conf["hostadd"]
