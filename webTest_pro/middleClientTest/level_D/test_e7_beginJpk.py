# coding=utf-8
"""
     beginJpk.py
     Desc: checkout JPK info
     Maintainer: wangfm
     CreateDate: 2016-11-09 16:30:34
"""
import os
import sys
import unittest
from time import sleep

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import add_excellentClass, user_login
from webTest_pro.common.model.baseLesson import beginJpk
from webTest_pro.common.logger import logger, T_INFO

loginInfo = init.loginInfo

class beginJpkMgr(unittest.TestCase):
    """精品课测试"""

    def setUp(self):
        if init.execEnv['execType'] == 'local':
            T_INFO(logger,"\nlocal exec testcase")
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            T_INFO(logger,"start tenantmanger...")
        else:
            T_INFO(logger,"\nremote exec testcase")
            browser = webdriver.DesiredCapabilities.CHROME
            self.driver = webdriver.Remote(command_executor=init.execEnv['remoteUrl'], desired_capabilities=browser)
            self.driver.implicitly_wait(8)
            self.verificationErrors = []
            self.accept_next_alert = True
            T_INFO(logger,"start tenantmanger...")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        T_INFO(logger,"tenantmanger end!")

    def test_addjpk(self):
        """添加精品课"""
        driver = self.driver
        user_login(driver, **loginInfo)
        add_excellentClass(driver)

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
