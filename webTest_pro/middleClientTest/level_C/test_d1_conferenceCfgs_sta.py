# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, \
    add_cfg_conferences
from webTest_pro.common.model.baseActionDel import del_cfg_conferences
from webTest_pro.common.model.baseActionSearch import search_cfg_conferences
from webTest_pro.common.model.baseActionModify import update_VideoConferencing
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动_课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品_课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会_议480p'}]
speaker_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲_下课_1'}]
listener_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲_下课_1'}]

VideoConferencingData = [{'name': '720PP', 'searchName': u'会议'},
                         {'name': u'会议', 'searchName': '720PP'}]


class conferenceCfgsMgr(unittest.TestCase):
    ''''会议模板管理'''

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


    def test_add_cfg_conferences(self):
        '''添加会议模板'''
        print "exec：test_add_cfg_conferences..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for conference_cfg in conference_cfgs:
            add_cfg_conferences(driver, **conference_cfg)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_cfg_conferences success."

    def test_bsearch_cfg_conferences(self):
        '''查询会议模板信息'''
        print "exec：test_search_cfg_conferences"

        driver = self.driver
        user_login(driver, **loginInfo)

        for conference_cfg in conference_cfgs:
            search_cfg_conferences(driver, **conference_cfg)
            self.assertEqual(conference_cfg['name'],
                             driver.find_element_by_xpath("//table[@id='videoconferencetable']/tbody/tr/td[3]").text)
        print "exec: test_search_cfg_conferences success."
        sleep(0.5)

    def test_bupdate_cfg_confrences(self):
        '''修改会议模板信息'''
        print "exec：test_bupdate_cfg_confrences"

        driver = self.driver
        user_login(driver, **loginInfo)

        for conference_cfg in VideoConferencingData:
            update_VideoConferencing(driver, **conference_cfg)
        print "exec: test_bupdate_cfg_confrences success."
        sleep(0.5)

    def test_del_cfg_conferences(self):
        '''删除会议模板_确定'''
        print "exec：test_del_cfg_conferences..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for conference_cfg in conference_cfgs:
            del_cfg_conferences(driver, **conference_cfg)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_cfg_conferences success."

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
