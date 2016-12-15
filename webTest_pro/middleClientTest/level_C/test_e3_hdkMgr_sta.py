# coding=utf-8
import os
import sys
import unittest
from time import sleep

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionDel import del_hdk
from webTest_pro.common.model.baseActionAdd import user_login, add_hdk_18
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo


class interActiveTeachingMgr(unittest.TestCase):
    ''''课程管理'''

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

    def test_add_hdk(self):
        '''添加互动课'''
        print "exec：test_add_hdk..."

        driver = self.driver
        user_login(driver, **loginInfo)
        add_hdk_18(driver)
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
