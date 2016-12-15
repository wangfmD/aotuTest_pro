# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_chapters
from webTest_pro.common.model.baseActionDel import del_chapter
from webTest_pro.common.model.baseActionSearch import search_chapter
from webTest_pro.common.model.baseActionModify import update_Chapter
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

subjects = [{'subjectName': u'书法', 'description': u'学习中国文化'},
            {'subjectName': u'计算机', 'description': u'计算机基础应用'}]
chapters = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章a', 'chapterCode': u'助记码1'},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章b', 'chapterCode': u'助记码1'}]
chapterData = [{'chapterName': u'语文第一章modify', 'chapterCode': 'SX01', 'searchName': u'语文第一章'}]


class chaptermanager(unittest.TestCase):
    ''''章管理'''

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

    def test_add_chapters(self):
        '''添加章'''
        print "exec：test_add_chapters..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for chapter in chapters:
            add_chapters(driver, **chapter)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_chapters success."

    def test_bsearch_chapter(self):
        '''查询章信息'''
        print "exec：test_search_chapter"

        driver = self.driver
        user_login(driver, **loginInfo)

        for chapter in chapters:
            search_chapter(driver, **chapter)
            self.assertEqual(chapter['chapterName'],
                             driver.find_element_by_xpath("//table[@id='chaptertable']/tbody/tr/td[5]").text)
        print "exec: test_search_chapter success."
        sleep(0.5)

    def test_bupdate_chapter(self):
        '''修改章信息'''
        print "exec：test_bupdate_chapter"

        driver = self.driver
        user_login(driver, **loginInfo)

        for chapter in chapterData:
            update_Chapter(driver, **chapter)
        print "exec: test_bupdate_chapter success."
        sleep(0.5)

    def test_del_chapter_ok(self):
        '''删除章_确定'''
        print "exec：test_del_chapter_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for chapter in chapters:
            del_chapter(driver, **chapter)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)

        print "exec：test_del_chapter_ok success."

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
