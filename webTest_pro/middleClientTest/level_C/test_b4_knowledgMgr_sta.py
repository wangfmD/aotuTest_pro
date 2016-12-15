# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_knowledges
from webTest_pro.common.model.baseActionDel import del_knowledge
from webTest_pro.common.model.baseActionSearch import search_knowledge
from webTest_pro.common.model.baseActionModify import update_Knowledge
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo

knowledges = [{'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'小学语文', 'sectionid': u"词", 'knowledgeName': u"双细胞", 'knowledgeCode': u"双细胞1"},
              {'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'小学语文', 'sectionid': u"词", 'knowledgeName': u"多细胞", 'knowledgeCode': u"多细胞1"}]
knowledgeData = [{'knowledgeName': u'梯形的特征modify', 'knowledgeCode': 'SX01', 'searchName': u'比的性质'},
                 {'knowledgeName': u'比的性质', 'knowledgeCode': 'SX01', 'searchName': u'梯形的特征modify'}]


class knowledgemanager(unittest.TestCase):
    ''''知识点管理'''

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

    def test_add_knowledges(self):
        '''添加知识点'''
        print "exec：test_add_knowledges..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for knowledge in knowledges:
            add_knowledges(driver, **knowledge)
            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)
        print "exec：test_add_knowledges success."

    def test_bsearch_knowledge(self):
        '''查询知识点信息'''
        print "exec：test_search_knowledge"

        driver = self.driver
        user_login(driver, **loginInfo)

        for knowledge in knowledges:
            search_knowledge(driver, **knowledge)
            self.assertEqual(knowledge['knowledgeName'],
                             driver.find_element_by_xpath("//table[@id='knowledgetable']/tbody/tr/td[7]").text)
        print "exec: test_search_knowledge success."
        sleep(0.5)

    def test_bupdate_knowledge(self):
        '''修改知识点信息'''
        print "exec：test_bupdate_knowledge"

        driver = self.driver
        user_login(driver, **loginInfo)

        for knowledge in knowledgeData:
            update_Knowledge(driver, **knowledge)
        print "exec: test_bupdate_knowledge success."
        sleep(1)

    def test_del_knowledge_ok(self):
        '''删除知识点_确定'''
        print "exec：test_del_knowledge_ok..."

        driver = self.driver
        user_login(driver, **loginInfo)

        for knowledge in knowledges:
            del_knowledge(driver, **knowledge)
            sleep(1.5)
            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
            sleep(0.5)

        print "exec：test_del_knowledge_ok success."

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
