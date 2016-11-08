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
    add_cfg_jpks
from model.baseActionDel import del_cfg_jpks
from model.baseActionSearch import search_cfg_jpks
from model.baseActionModify import update_ExcellentClassroom

reload(sys)
sys.setdefaultencoding("utf-8")

hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动_课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品_课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会_议480p'}]
speaker_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲_下课_1'}]
listener_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲_下课_1'}]

excellentClassroomData = [{'name': '720PP','searchName':u'精品_课480p'},
                          {'name': u'720精品_课480p','searchName':'720PP'}]


class jpkCfgsMgr(unittest.TestCase):
    ''''精品课模板管理'''

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
        print "jpkCfgsMgr end!"
        print "=" * 60

    def test_add_cfg_jpks(self):
        '''添加精品课模板'''
        print "exec：test_add_cfg_jpks..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for jp_lesson_cfg in jp_lesson_cfgs:
            add_cfg_jpks(driver, **jp_lesson_cfg)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_cfg_jpks success."

    def test_bsearch_cfg_jpks(self):
        '''查询精品课模板信息'''
        print "exec：test_search_cfg_jpks"

        driver = self.driver
        user_login(driver, **loginInfo)

        for jp_lesson_cfg in jp_lesson_cfgs:
            search_cfg_jpks(driver, **jp_lesson_cfg)
            self.assertEqual(jp_lesson_cfg['name'],
                             driver.find_element_by_xpath("//table[@id='excellentclassroomtable']/tbody/tr/td[3]").text)
        print "exec: test_search_cfg_jpks success."
        sleep(0.5)
	
    def test_bupdate_cfg_jpks(self):
        '''修改精品课模板信息'''
        print "exec：test_bupdate_cfg_jpks"

        driver = self.driver
        user_login(driver, **loginInfo)

        for jp_lesson_cfg in excellentClassroomData:
            update_ExcellentClassroom(driver, **jp_lesson_cfg)
        print "exec: test_bupdate_cfg_jpks success."
        sleep(0.5)

    def test_del_cfg_jpks(self):
        '''删除精品课模板_确定'''
        print "exec：test_del_cfg_jpks..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for jp_lesson_cfg in jp_lesson_cfgs:
            del_cfg_jpks(driver, **jp_lesson_cfg)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_cfg_jpks success."

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
