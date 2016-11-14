# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, \
    add_cfg_speaker_lessons
from model.baseActionDel import del_cfg_speaker_lessons
from model.baseActionSearch import search_cfg_speaker_lessons
from model.baseActionModify import update_TheClass

reload(sys)
sys.setdefaultencoding("utf-8")

speaker_lesson_cfgs = [{'name': u'a主讲下课'}, {'name': u'主讲_下课_1'}]
theClassData = [{'name': u'下课模板测试数据', 'searchName': u'a主讲下课'},
                {'name': u'a主讲下课', 'searchName': u'下课模板测试数据'}]


class speackCfgsMgr(unittest.TestCase):
    ''''主讲模板管理'''

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
        print "speackCfgsMgr end!"
        print "=" * 60

    def test_add_cfg_speaker_lessons(self):
        '''添加主讲下课模板'''
        print "exec：test_add_cfg_speaker_lessons..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for speaker_lesson_cfg in speaker_lesson_cfgs:
            add_cfg_speaker_lessons(driver, **speaker_lesson_cfg)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_cfg_speaker_lessons success."

    def test_bsearch_cfg_speaker_lessons(self):
        '''查询主讲下课模板信息'''
        print "exec：test_search_cfg_speaker_lessons"

        driver = self.driver
        user_login(driver, **loginInfo)

        for speaker_lesson_cfg in speaker_lesson_cfgs:
            search_cfg_speaker_lessons(driver, **speaker_lesson_cfg)
            self.assertEqual(speaker_lesson_cfg['name'],
                             driver.find_element_by_xpath("//table[@id='lectureclasstable']/tbody/tr/td[3]").text)
        print "exec: test_search_cfg_speaker_lessons success."
        sleep(0.5)

    def test_bupdate_cfg_speaker_lessons(self):
        '''修改主讲下课模板信息'''
        print "exec：test_bupdate_cfg_speaker_lessons"
        #
        driver = self.driver
        user_login(driver, **loginInfo)

        for speaker_lesson_cfg in theClassData:
            update_TheClass(driver, **speaker_lesson_cfg)
        print "exec: test_bupdate_cfg_speaker_lessons success."
        sleep(0.5)

    def test_del_cfg_speaker_lessons(self):
        '''删除主讲下课模板_确定'''
        print "exec：test_del_cfg_speaker_lessons..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for speaker_lesson_cfg in speaker_lesson_cfgs:
            del_cfg_speaker_lessons(driver, **speaker_lesson_cfg)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_cfg_speaker_lessons success."

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
