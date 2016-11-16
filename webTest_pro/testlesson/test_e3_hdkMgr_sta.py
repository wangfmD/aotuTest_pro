# coding=utf-8
import sys
import unittest
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from _env import addPaths
from model.baseActionDel import del_hdk

addPaths('.')
from common.init import execEnv, loginInfo
from model.baseActionAdd import user_login, add_hdk

reload(sys)
sys.setdefaultencoding("utf-8")



class interActiveTeachingMgr(unittest.TestCase):
    ''''课程管理'''

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
        print "interActiveTeachingMgr end!"
        print "=" * 60

    def test_add_hdk(self):
        '''添加互动课'''
        print "exec：test_add_hdk..."

        driver = self.driver
        user_login(driver, **loginInfo)
        add_hdk(driver)
        sleep(2)
        # self.assertEqual(u"保存成功", driver.find_element_by_xpath("//*[@id='layui-layer10']/div").text)


        sleep(0.5)

        print "exec：test_add_hdk success."


    def test_del_hdk(self):
        '''删除互动课'''
        print "exec：test_del_hdk..."
        driver = self.driver
        user_login(driver, **loginInfo)
        del_hdk(driver)
        sleep(2)
        print "exec：test_del_hdk successed."


if __name__ == '__main__':
    main = unittest.main()
