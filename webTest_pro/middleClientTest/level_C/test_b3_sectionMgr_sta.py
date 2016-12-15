# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_sections
from webTest_pro.common.model.baseActionDel import del_section
from webTest_pro.common.model.baseActionSearch import search_section
from webTest_pro.common.model.baseActionModify import update_Section
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

sections = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': u"数学第二章", 'sectionName': u"sx第一节", 'sectionCode': u"第一节zjm"},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': u"数学第二章", 'sectionName': u"sx第二节", 'sectionCode': u"第二节zjm"}]
sectionData = [{'sectionName': u'平行线test', 'sectionCode': 'SX01', 'searchName': u'平行线'}]


class sectionmanager(unittest.TestCase):
    ''''节管理'''

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

    def test_add_sections(self):
        '''添加节'''
        print "exec：test_add_sections..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for section in sections:
            add_sections(driver, **section)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_sections success."

    def test_bsearch_section(self):
        '''查询节信息'''
        print "exec：test_search_section"

        driver = self.driver
        user_login(driver, **loginInfo)

        for section in sections:
            search_section(driver, **section)
            self.assertEqual(section['sectionName'],
                             driver.find_element_by_xpath("//table[@id='sectiontable']/tbody/tr/td[6]").text)
        print "exec: test_search_section success."
        sleep(0.5)

    def test_bupdate_section(self):
        '''查询节信息'''
        print "exec：test_search_section"

        driver = self.driver
        user_login(driver, **loginInfo)

        for section in sectionData:
            update_Section(driver, **section)
        print "exec: test_search_section success."
        sleep(0.5)

    def test_del_section_ok(self):
        '''删除节_确定'''
        print "exec：test_del_section_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for section in sections:
            del_section(driver, **section)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)

        print "exec：test_del_section_ok success."

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
