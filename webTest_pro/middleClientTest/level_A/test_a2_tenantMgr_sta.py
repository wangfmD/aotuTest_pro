# coding: utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro .common.model.baseActionAdd import admin_login, add_tenants
from webTest_pro.common.model.baseActionSearch import search_tenant
from webTest_pro.common.model.baseActionModify import update_Tenant
from webTest_pro.common.initData import init
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding('utf-8')

tenantAdd = [{'areaid': "//div[@id='treeview']/ul/li[17]", 'platmarkName': u'河南教育局', 'platmarkCode': '001'},
             {'areaid': "//div[@id='treeview']/ul/li[18]", 'platmarkName': u'张三教育局', 'platmarkCode': '002'},
             {'areaid': "//div[@id='treeview']/ul/li[19]", 'platmarkName': u'李四教育局', 'platmarkCode': '003'}]

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
        T_INFO(logger, "exec: test_add_tenant...")
        driver = self.driver
        admin_login(driver)
        for itme in tenantAdd:
            add_tenants(driver, **itme)
        T_INFO(logger, "exec: test_add_tenant OK")

    def test_bsearch_tenant_exist(self):
        '''查询租户_存在'''
        T_INFO(logger, "exec: test_search_tenant_exist...")
        driver = self.driver
        condition = {'condition': u'河南'}
        admin_login(driver)
        search_tenant(driver, **condition)
        # print driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td[2]").text
        self.assertEqual(u"河南教育局", driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td[2]").text)
        T_INFO(logger,"exec: test_search_tenant_exist OK")

    def test_bsearch_tenant_no_existent(self):
        '''查询租户_不存在'''
        T_INFO(logger,"exec: test_search_tenant_no_existent...")
        driver = self.driver
        condition = {'condition': 'dafa'}
        admin_login(driver)
        search_tenant(driver, **condition)
        # print driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td").text
        self.assertEqual(u"无数据", driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td").text)
        T_INFO(logger,"exec: test_search_tenant_no_existent OK")

    def test_bupdate_Tenant(self):
        '''修改单条租户管理'''
        T_INFO(logger,"exec: test_update_Tenant...")
        driver = self.driver
        admin_login(driver)
        for itms in tenantData:
            update_Tenant(driver, **itms)
        T_INFO(logger,"exec: test_bupdate_Tenant OK")


    def test_del_tenant(self):
        '''主人删除租户'''
        T_INFO(logger, "exec: test_del_tenant...")
        driver = self.driver
        admin_login(driver)
        sleep(0.5)
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"租户管理").click()
        #
        sleep(1)
        driver.find_element_by_xpath("//button[@id='delten']").click()
        verifyText = driver.find_element_by_css_selector(".layui-layer-content").text
        self.assertEqual(u"平台主人无法删除！", verifyText)
        T_INFO(logger,"exec: test_del_tenant OK")
        # bug 新建立租户要等到一点时间，新租户才能登录系统
        sleep(1)


if __name__ == '__main__':
    unittest.main()
