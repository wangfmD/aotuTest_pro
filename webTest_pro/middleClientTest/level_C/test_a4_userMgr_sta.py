# coding=utf-8import osimport sysimport unittestfrom time import sleepfrom selenium import webdriverfrom selenium.common.exceptions import NoAlertPresentException, NoSuchElementExceptionsys.path.append(os.environ.get('PY_DEV_HOME'))from webTest_pro.common.initData import initfrom webTest_pro.common.model.baseActionAdd import user_login, add_usersfrom webTest_pro.common.model.baseActionDel import del_userfrom webTest_pro.common.model.baseActionSearch import search_userfrom webTest_pro.common.model.baseActionModify import update_Userfrom webTest_pro.common.logger import logger, T_INFOreload(sys)sys.setdefaultencoding("utf-8")loginInfo = init.loginInfousers = [{'loginName': 'auser', 'trueName': 'ateacher'},         {'loginName': 'buser1', 'trueName': 'bteacher1'},         {'loginName': 'cuser2', 'trueName': 'cteacher2'},         {'loginName': 'duser3', 'trueName': 'dteacher3'},         {'loginName': 'euser4', 'trueName': 'eteacher4'}]usersData = [{'mobiles': '18551184502', 'emails': '9930356@qq.com', 'trueName': u'张三', 'searchName': u'cteacher2'}]class userlist(unittest.TestCase):    ''''用户管理'''    def setUp(self):        if init.execEnv['execType'] == 'local':            T_INFO(logger,"\nlocal exec testcase")            self.driver = webdriver.Chrome()            self.driver.implicitly_wait(8)            self.verificationErrors = []            self.accept_next_alert = True            T_INFO(logger,"start tenantmanger...")        else:            T_INFO(logger,"\nremote exec testcase")            browser = webdriver.DesiredCapabilities.CHROME            self.driver = webdriver.Remote(command_executor=init.execEnv['remoteUrl'], desired_capabilities=browser)            self.driver.implicitly_wait(8)            self.verificationErrors = []            self.accept_next_alert = True            T_INFO(logger,"start tenantmanger...")    def tearDown(self):        self.driver.quit()        self.assertEqual([], self.verificationErrors)        T_INFO(logger,"tenantmanger end!")    def test_add_user(self):        '''添加用户'''        print "exec：test_add_user..."        driver = self.driver        user_login(driver, **loginInfo)        for user in users:            add_users(driver, **user)            self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)        sleep(0.5)        print "exec：test_add_user success."    def test_bsearch_user(self):        '''查询用户信息'''        print "exec：test_search_user"        driver = self.driver        user_login(driver, **loginInfo)        for user in users:            search_user(driver, **user)            self.assertEqual(user['loginName'],                             driver.find_element_by_xpath("//tbody[@id='userlists']/tr/td[3]").text)        print "exec: test_search_user success."        sleep(0.5)    def test_bupdate_user(self):        '''修改用户信息'''        print "exec：test_search_user"        driver = self.driver        user_login(driver, **loginInfo)        for itms in usersData:            update_User(driver, **itms)        print "exec: test_bupdate_user success."        sleep(0.5)    def test_del_user_ok(self):        '''删除用户_确定'''        print "exec：test_del_user_ok..."        driver = self.driver        user_login(driver, **loginInfo)        for user in users:            del_user(driver)            self.assertEqual(u"删除成功！", driver.find_element_by_css_selector(".layui-layer-content").text)            sleep(0.5)        print "exec：test_del_user_ok success."    def is_element_present(self, how, what):        try:            self.driver.find_element(by=how, value=what)        except NoSuchElementException as e:            return False        return True    def is_alert_present(self):        try:            self.driver.switch_to_alert()        except NoAlertPresentException as e:            return False        return True    def close_alert_and_get_its_text(self):        try:            alert = self.driver.switch_to_alert()            alert_text = alert.text            if self.accept_next_alert:                alert.accept()            else:                alert.dismiss()            return alert_text        finally:            self.accept_next_alert = Trueif __name__ == '__main__':    unittest.main()