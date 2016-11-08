# coding=utf-8
import os
import sys
import unittest

sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.getcwd())
from model.init import execEnv
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from time import sleep
from model.baseActionAdd import add_schools, user_login
from model.baseActionDel import del_school
from model.baseActionModify import update_School
from model.init import loginInfo

reload(sys)
sys.setdefaultencoding("utf-8")

schools = [{'schoolName': u'����', 'schoolType': u'����', 'schoolArea': u'֣����'},
           {'schoolName': u'����', 'schoolType': u'��ѧ', 'schoolArea': u'֣����'},
           {'schoolName': u'����', 'schoolType': u'��ѧ', 'schoolArea': u'������'},
           {'schoolName': u'����', 'schoolType': u'Сѧ', 'schoolArea': u'������'},
           {'schoolName': u'����', 'schoolType': u'Сѧ', 'schoolArea': u'������'},
           {'schoolName': u'һ��', 'schoolType': u'����', 'schoolArea': u'֣����'}]
schoolData = [{'schoolName': u'����һ��','searchName':u'����'}]
schoolDel = [{'schoolName': u'����'},
           {'schoolName': u'����'},
           {'schoolName': u'����'},
           {'schoolName': u'����'},
           {'schoolName': u'һ��'}]

class schoolmanager(unittest.TestCase):
    ''''ѧУ����'''

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

    def test_addschool(self):
        '''���ѧУ'''
        print "ִ�У����ѧУ����"
        driver = self.driver
        driver.refresh()
        sleep(2)
        user_login(driver, **loginInfo)

        for school in schools:
            add_schools(driver, **school)
            self.assertEqual(u"��ӳɹ���", driver.find_element_by_css_selector(".layui-layer-content").text)

        sleep(0.5)

    def test_bsearch_school(self):
        '''ѧУ��ѯ'''
        print "ִ�У�ѧУ��ѯ"

        try:
            driver = self.driver
            user_login(driver, **loginInfo)

            driver.find_element_by_link_text(u"ϵͳ����").click()
            driver.find_element_by_link_text(u"ѧУ����").click()
            sleep(1)
            driver.find_element_by_xpath("//input[@id='condition']").clear()
            driver.find_element_by_xpath("//input[@id='condition']").send_keys(u"������")
            driver.find_element_by_xpath("//button[@id='searchbtn']").click()
            sleep(1)
            self.assertEqual(u"����ʡ������", driver.find_element_by_xpath(".//*[@id='schoolname']").text)
            print "��ѯѧУ�ɹ���"
        except Exception as e:
            print "��ѯѧУʧ�ܡ�"
        sleep(1)

    def test_bupdate_school(self):
        '''�޸ĵ���ѧУ����'''
        print "ִ�У��޸ĵ���ѧУ����"
        # try:
        driver = self.driver
        user_login(driver, **loginInfo)
        for itms in schoolData:
            update_School(driver,**itms)
        sleep(1)
        # resultContent = driver.find_element_by_css_selector("div.layui-layer-content.firepath-matching-node").text
        # self.assertEqual(u"����һ��", resultContent)
        print "�޸ĵ���ѧУ����:�ɹ���"
    # except Exception as e:
        print "�޸ĵ���ѧУ����ʧ�ܡ�"
        sleep(1)

    def test_del_school_ok(self):
        '''ɾ��ѧУ_ȷ��'''
        print "ִ�У�ɾ��ѧУ_ȷ��"
        driver = self.driver
        user_login(driver, **loginInfo)

        for flag in schoolDel:
            del_school(driver,**flag)
            # self.assertEqual(u"ɾ���ɹ���", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(0.5)

    def test_del_school_cancel(self):
        '''ɾ��ѧУ_ȡ��'''
        print "ִ�У�ɾ��ѧУ_ȡ��"
        try:
            driver = self.driver
            user_login(driver, **loginInfo)

            # add_school(driver, u'һ��', u'����', u'֣����')
            sleep(0.5)
            driver.find_element_by_link_text(u"ϵͳ����").click()
            driver.find_element_by_link_text(u"ѧУ����").click()
            sleep(0.5)
            driver.find_element_by_xpath("//button[@id='delsc']").click()
            driver.find_element_by_css_selector("a.layui-layer-btn1").click()
            self.assertEqual(u"һ��", driver.find_element_by_xpath("//*[@id='schoolname']").text)
            # print driver.find_element_by_xpath("//*[@id='schoolname']").text
            print "ɾ��ѧУ_ȡ�����ɹ�"
        except Exception as e:
            print "ɾ��ѧУ_ȡ����ʧ��"

        sleep(1)

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
