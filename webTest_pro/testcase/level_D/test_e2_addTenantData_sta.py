# coding: utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver

from _env import addPaths

addPaths('.')
from model.baseActionAdd import admin_login, add_tenants
from common.init import execEnv

reload(sys)
sys.setdefaultencoding('utf-8')

tenantAdd = [{'areaid': "//div[@id='treeview']/ul/li[17]",'platmarkName':u'河南教育局','platmarkCode':'001'}]

tenantData = [{'platmarkName': u'张三教育局11','platmarkCode':'002','searchName':u'张三教育局'}]

tenantDel = [{'searchName':u'张三教育局11'},{'searchName':u'李四教育局'}]


class tenantmanger(unittest.TestCase):
    '''租户管理场景'''

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
        print "tenantmanger end!"
        print "=" * 60

    def test_add_tenant(self):
        '''添加租户'''
        print "exec: test_add_tenant..."
        driver = self.driver
        admin_login(driver)
        for itme in tenantAdd:
            add_tenants(driver,**itme)
        print "exec: test_add_tenant OK"

if __name__ == '__main__':
    unittest.main()
