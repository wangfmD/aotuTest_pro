# coding=utf-8
import json
import os
import socket
import sys
import time
import unittest
import requests
import shutil
from common.emailCollect import sendReportWithAtt
# from common.generateHtml.file_os import HTMLFileRunner
# from common.generateHtml.HTMLTestRunner import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner

reload(sys)
sys.setdefaultencoding('utf8')

home_path = os.environ.get('PY_DEV_HOME')
tmpEnvFile = home_path + '\webTest_pro\common\.tmp'

envpath = {
    'dev_wf': home_path + '\webTest_pro\cfg\init_wf.conf',
    'default': home_path + '\webTest_pro\cfg\init_default.conf',
    'dev': home_path + '\webTest_pro\cfg\init_dev.conf',
    'test': home_path + '\webTest_pro\cfg\init_test.conf',
    'debug': home_path + '\webTest_pro\cfg\init_debug.conf'
}

receiver = {
    'dev_56': 'wangfm@3bu.cn',
    'default': 'wangfm@3bu.cn',
    'dev': 'wangfm@3bu.cn',
    'test': 'wangfm@3bu.cn',
    'debug':
    'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;\
        tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn;xiahao@3bu.cn;'
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
        # elif exectype == 'dev_wf_56':
        #     with open(self.tmpEnvFile, 'w+') as f:
        #         f.write(envpath['dev_wf_56'])
        #     self.receiver = receiver['dev_wf_56']
        #     self.test_dir = '.'
        # elif exectype == 'dev_wf_57':
        #     with open(self.tmpEnvFile, 'w+') as f:
        #         f.write(envpath['dev_wf_57'])
        #     self.receiver = receiver['dev_wf_57']
        #     self.test_dir = '.'
        # elif exectype == 'dev_57':
        #     with open(self.tmpEnvFile, 'w+') as f:
        #         f.write(envpath['dev_57'])
        #     self.receiver = receiver['dev_57']
        #     self.test_dir = '.'
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
        self.discover = unittest.defaultTestLoader.discover(
            self.test_dir, pattern='*_sta.py')
        # 设置测试报告路径
        if os.name == 'nt':
            self.reportPath = self.homePath + '\webTest_pro\\report\\'
        else:
            self.reportPath = self.homePath + '/webTest_pro/report/'
        # 测试报告路径不存在，则创建该路径
        if os.path.exists(self.reportPath) is True:
            print " Report Path is {path}".format(path=self.reportPath)
        else:
            print "The report path is not exist,create report directory..."
            os.mkdir(self.reportPath)

    def run(self):

        version = ""
        sql_Add = ""
        from webTest_pro.common.initData import init
        try:
            try:
                # 获取init.db_conf[]
                sql_Add = init.db_conf["hostadd"]
                strs = requests.get(
                    "http://" + sql_Add + "/middleclient/version", timeout=5)
                # print sql_Add
                s = json.loads(strs.text)
                version = 'middleclient_' + s['version']
            except AttributeError:
                sql_Add = "init.db_conf Configuration is not read"
                # 获取init.db_conf[]
        except:
            version = "version Timeout!"

        self.now = time.strftime("%Y-%m-%d%H%H%S")
        restult = self.now + '_restult.html'
        self.filename = self.reportPath + restult
        fp = open(self.filename, 'wb')
        # runner = HTMLTestRunner(
        #     stream=fp,
        #     title='测试报告',
        #     description='用例执行情况：',
        #     sqlAdd=sql_Add,
        #     version_add=version)
        runner = HTMLTestRunner(
            stream=fp,
            title='测试报告',
            description='用例执行情况：')
        runner.run(self.discover)
        sendReportWithAtt(self.filename, self.receiver)
        fp.close()

        # if self.generateHtmlType == 'is':
        #     folderPath = "Z:\\reports\\"
        #     if os.path.exists(folderPath):
        #         hostname = socket.gethostname()
        #         mkdirFolder = folderPath + socket.gethostbyname(
        #             hostname) + "report\\"
        #         if not os.path.exists(mkdirFolder):
        #             os.mkdir(mkdirFolder)
        #         shutil.copy(self.filename, mkdirFolder)
        #         HTMLFileRunner(
        #             title='测试报告 ', description='用例执行情况：').generatr(folderPath)
        #     else:
        #         print "没有挂在nas到本地请挂在！"


if __name__ == '__main__':
    runner = TestRunner('dev_wf_57', 'is')
    runner.run()
