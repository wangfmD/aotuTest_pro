# coding=utf-8
"""
     beginJpk.py
     Desc: checkout JPK info
     Maintainer: wangfm
     CreateDate: 2016-11-09 16:30:34
"""
import unittest, sys
from time import sleep
from selenium import webdriver
from model.baseLesson import beginJpk, user_login

from _env import addPaths

addPaths('.')
from common.mysqlKit import sqlOperating, sqlpara
from common.init import db_conf, loginInfo, execEnv


class beginJpkMgr(unittest.TestCase):
    """精品课测试"""

    def setUp(self):
        if execEnv['execType'] == 'local':
            print "\n", "=" * 20, "local exec testcase", "=" * 19
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."
        else:
            print "\n", "=" * 20, "remote exec testcase", "=" * 18
            browser = webdriver.DesiredCapabilities.CHROME
            self.driver = webdriver.Remote(command_executor=execEnv['remoteUrl'], desired_capabilities=browser)
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            print "start tenantmanger..."

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        print "generateSystemData end!"
        print "=" * 60

    def test_beginJpk(self):
        """精品课检验"""
        driver = webdriver.Chrome()
        user_login(driver, **loginInfo)
        beginJpk(driver, 'jpk')
        sleep(20)

if __name__ == '__main__':
    unittest.main()
    #  for path in sys.path:
        #  print path
