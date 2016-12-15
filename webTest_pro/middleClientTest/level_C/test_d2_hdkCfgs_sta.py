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
    add_cfg_hdks
from webTest_pro.common.model.baseActionDel import del_cfg_hdks
from webTest_pro.common.model.baseActionSearch import search_cfg_hdks
from webTest_pro.common.model.baseActionModify import update_InteractiveTeaching
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动_课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品_课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会_议480p'}]
speaker_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲_下课_1'}]
listener_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲_下课_1'}]
interactiveTeachingData = [{'name': '720PP', 'searchName': u'互动课模板'},
                           {'name': u'互动课模板', 'searchName': '720PP'}]


class hdkCfgsMgr(unittest.TestCase):
    ''''互动课模板管理'''

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

    def test_add_cfg_hdks(self):
        '''添加互动课模板'''
        print "exec：test_add_cfg_hdks..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for hdk_lesson_cfg in hdk_lesson_cfgs:
            add_cfg_hdks(driver, **hdk_lesson_cfg)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_cfg_hdks success."

    def test_bsearch_cfg_hdks(self):
        '''查询互动课模板信息'''
        print "exec：test_search_cfg_hdks"

        driver = self.driver
        user_login(driver, **loginInfo)

        for hdk_lesson_cfg in hdk_lesson_cfgs:
            search_cfg_hdks(driver, **hdk_lesson_cfg)
            self.assertEqual(hdk_lesson_cfg['name'],
                             driver.find_element_by_xpath("//table[@id='interactteachtable']/tbody/tr/td[3]").text)
        print "exec: test_search_cfg_hdks success."
        sleep(0.5)

    def test_bupdate_cfg_hdks(self):
        '''修改互动课模板信息'''
        print "exec：test_bupdate_cfg_hdks"

        driver = self.driver
        user_login(driver, **loginInfo)

        for hdk_lesson_cfg in interactiveTeachingData:
            update_InteractiveTeaching(driver, **hdk_lesson_cfg)
        print "exec: test_bupdate_cfg_hdks success."
        sleep(0.5)

    def test_del_cfg_hdks(self):
        '''删除互动课模板_确定'''
        print "exec：test_del_cfg_hdks..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for hdk_lesson_cfg in hdk_lesson_cfgs:
            del_cfg_hdks(driver, **hdk_lesson_cfg)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)
        print "exec：test_del_cfg_hdks success."

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
