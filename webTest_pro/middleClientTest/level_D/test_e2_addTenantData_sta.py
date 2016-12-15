# coding: utf-8
import os
import sys
import unittest

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import admin_login, add_tenants
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

tenantAdd = [{'areaid': "//div[@id='treeview']/ul/li[17]", 'platmarkName': u'河南教育局', 'platmarkCode': '001'}]

tenantData = [{'platmarkName': u'张三教育局11', 'platmarkCode': '002', 'searchName': u'张三教育局'}]

tenantDel = [{'searchName': u'张三教育局11'}, {'searchName': u'李四教育局'}]


class tenantmanger(unittest.TestCase):
    '''租户管理场景'''

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

    def test_add_tenant(self):
        '''添加租户'''
        print "exec: test_add_tenant..."
        driver = self.driver
        admin_login(driver)
        for itme in tenantAdd:
            add_tenants(driver, **itme)
        print "exec: test_add_tenant OK"


if __name__ == '__main__':
    unittest.main()
