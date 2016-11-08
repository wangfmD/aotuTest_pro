# coding: utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from model.baseActionAdd import admin_login, add_tenants
from model.baseActionSearch import search_tenant
from model.baseActionModify import update_Tenant
from common.init import execEnv

reload(sys)
sys.setdefaultencoding('utf-8')

tenantAdd = [{'areaid': "//div[@id='treeview']/ul/li[17]",'platmarkName':u'河南教育局','platmarkCode':'001'},
             {'areaid': "//div[@id='treeview']/ul/li[18]",'platmarkName':u'张三教育局','platmarkCode':'002'},
             {'areaid': "//div[@id='treeview']/ul/li[19]",'platmarkName':u'李四教育局','platmarkCode':'003'} ]

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

    def test_bsearch_tenant_exist(self):
        '''查询租户_存在'''
        print "exec: test_search_tenant_exist..."
        driver = self.driver
        condition = {'condition': u'河南'}
        admin_login(driver)
        search_tenant(driver, **condition)
        # print driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td[2]").text
        self.assertEqual(u"河南教育局", driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td[2]").text)
        print "exec: test_search_tenant_exist OK"

    def test_bsearch_tenant_no_existent(self):
        '''查询租户_不存在'''
        print "exec: test_search_tenant_no_existent..."
        driver = self.driver
        condition = {'condition': 'dafa'}
        admin_login(driver)
        search_tenant(driver, **condition)
        # print driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td").text
        self.assertEqual(u"无数据", driver.find_element_by_xpath("//*[@id='tenantmanager']/tbody/tr/td").text)
        print "exec: test_search_tenant_no_existent OK"

    def test_bupdate_Tenant(self):
        '''修改单条租户管理'''
        print "exec: test_update_Tenant..."
        driver = self.driver
        admin_login(driver)
        for itms in tenantData:
            update_Tenant(driver, **itms)
        print "exec: test_bupdate_Tenant OK"

    # def test_del_tenants(self):
    #     '''删除多个租户'''
    #     print "exec: test_del_tenant..."
    #     driver = self.driver
    #     admin_login(driver)
    #     for itms in tenantDel :
    #         del_tenants(driver,**itms)


    def test_del_tenant(self):
        '''主人删除租户'''
        print "exec: test_del_tenant..."
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
        print "exec: test_del_tenant OK"

        # bug 新建立组合要等到一点时间，新组合才能登录系统
        sleep(1)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

if __name__ == '__main__':
    unittest.main()
