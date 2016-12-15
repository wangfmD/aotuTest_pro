# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_jpk_18
from webTest_pro.common.logger import logger, T_INFO

loginInfo = init.loginInfo

class addJpk(unittest.TestCase):
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

    # def test_del_excellentLesson(self):
    #     '''删除精品课'''
    #     print "exec:excellentLesson..."
    #     driver = self.driver
    #     user_login(driver, **loginInfo)
    #     # del excellentClass
    #     del_excellentClass(driver)
    #     sleep(2)
    #     print "exec:excellentLesson end."

    def test_add_jpk(self):
        '''添加精品课堂'''

        print "exec: generate jplk start..."
        driver = self.driver
        user_login(driver, **loginInfo)

        add_jpk_18(driver)
        sleep(2)
        print "exec: generate jpk end."


if __name__ == '__main__':
    unittest.main()
