# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv
from model.baseActionAdd import user_login, add_subjects
from model.baseActionDel import del_subject
from  model.baseActionSearch import search_subject
from  model.baseActionModify import update_Subjects

reload(sys)
sys.setdefaultencoding("utf-8")

subjects = [{'subjectName': u'书法', 'description': u'学习中国文化'},
            {'subjectName': u'计算机', 'description': u'计算机基础应用'}]
subjectsData = [{'subjectName': u'测试科目名称','description':u'描述说明','searchName':u'书法'},
                {'subjectName': u'书法', 'description': u'描述说明', 'searchName': u'测试科目名称'}]


class subjectmanager(unittest.TestCase):
    ''''科目互动管理'''

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

    def test_add_subjects(self):
        '''添加科目'''
        print "exec：test_add_subjects..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for subject in subjects:
            add_subjects(driver, **subject)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_subjects success."

    def test_bsearch_subjects(self):
        '''查询科目信息'''
        print "exec：test_bsearch_subjects"

        driver = self.driver
        user_login(driver, **loginInfo)

        for subject in subjects:
            search_subject(driver, **subject)
            self.assertEqual(subject['subjectName'],
                             driver.find_element_by_xpath("//table[@id='subjecttable']/tbody/tr/td[2]").text)
        print "exec: test_bsearch_subjects success."
        sleep(0.5)
		
    def test_bupdate_subjects(self):
        '''修改科目信息'''
        print "exec：test_bupdate_subjects"

        driver = self.driver
        user_login(driver, **loginInfo)

        for subject in subjectsData:
            update_Subjects(driver, **subject)
        print "exec: test_bupdate_subjects success."
        sleep(0.5)


    def test_del_subjects_ok(self):
        '''删除科目_确定'''
        print "exec：test_del_subjects_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for subject in subjects:
            del_subject(driver, **subject)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)

        print "exec：test_del_subjects_ok success."

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
