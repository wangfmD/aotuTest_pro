# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, add_interactgrps
from model.baseActionDel import del_interactgrp
from  model.baseActionSearch import search_interactgrps
from  model.baseActionModify import update_Interactive

reload(sys)
sys.setdefaultencoding("utf-8")

interactgrps = [{'grpName': 'grp1', 'schoolgrTypeId': u'课程组'},
                {'grpName': 'grp2', 'schoolgrTypeId': u'会议组'},
                {'grpName': 'grp3', 'schoolgrTypeId': u'会议组'}]

interactiveData = [{'grpName': u'互动组','searchName':'grp1'}]


class interactGroup(unittest.TestCase):
    ''''互动组管理'''

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
        print "schoolmanager end!"
        print "=" * 60

    def test_add_interactgrp(self):
        '''添加互动组'''
        print "exec：test_add_interactgrp..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for interactgrp in interactgrps:
            add_interactgrps(driver, **interactgrp)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_interactgrp success."

    def test_bsearch_interactgrp(self):
        '''查询互动组信息'''
        print "exec：test_search_interactgrp"

        driver = self.driver
        user_login(driver, **loginInfo)
        for interactgrp in interactgrps:
            search_interactgrps(driver, **interactgrp)
            self.assertEqual(interactgrp['grpName'],
                             driver.find_element_by_xpath("//table[@id='schooltab']/tbody/tr/td[3]").text)
        print "exec: test_search_interactgrp success."
        sleep(0.5)
		
    def test_bupdate_interactgrp(self):
        '''修改互动组信息'''
        print "exec：test_bupdate_interactgrp"
        driver = self.driver
        user_login(driver, **loginInfo)
        for operater in interactiveData:
            update_Interactive(driver, **operater)
        print "exec: test_bupdate_interactgrp success."
        sleep(0.5)

    def test_del_interactgrp_ok(self):
        '''删除互动组_确定'''
        print "exec：test_del_interactgrp_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for interactgrp in interactgrps:
            del_interactgrp(driver)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_interactgrp_ok success."

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
