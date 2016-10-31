# coding=utf-8

import sys
import os
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from time import sleep

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from model.init import execEnv
from model.baseActionAdd import user_login, add_knowledges
from model.baseActionDel import del_knowledge
# from model.baseActionModify import 
from  model.baseActionSearch import search_knowledge
from  model.baseActionModify import update_Knowledge
from model.init import loginInfo

reload(sys)
sys.setdefaultencoding("utf-8")

knowledges = [{'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'语文第一章', 'sectionid': u"第一节", 'knowledgeName': u"双细胞", 'knowledgeCode': u"双细胞1"},
              {'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'语文第一章', 'sectionid': u"第一节", 'knowledgeName': u"多细胞", 'knowledgeCode': u"多细胞1"}]
knowledgeData = [{'knowledgeName': u'梯形的特征modify', 'knowledgeCode': 'SX01', 'searchName': u'梯形的特征'},
                 {'knowledgeName': u'梯形的特征', 'knowledgeCode': 'SX01', 'searchName': u'梯形的特征modify'}]


class knowledgemanager(unittest.TestCase):
    ''''知识点管理'''

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
        print "knowledgemanager end!"
        print "=" * 60

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
        sleep(0.5)

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
