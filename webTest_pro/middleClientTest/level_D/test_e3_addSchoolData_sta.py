# coding=utf-8
import os
import sys
import unittest

from selenium import webdriver

sys.path.append(os.environ.get('PY_DEV_HOME'))

from webTest_pro.common.initData import init
from webTest_pro.common.model.baseActionAdd import user_login, add_schools, \
    add_classrooms, add_terminals, add_integrateds, add_users
from webTest_pro.common.logger import logger, T_INFO

reload(sys)
sys.setdefaultencoding("utf-8")
loginInfo = init.loginInfo
classroom_para = init.classroom_para
db_conf = init.db_conf

users = [{'loginName': 'user', 'trueName': 'teacher'},
         {'loginName': 'user1', 'trueName': 'teacher1'}]

middle_interact_ip = db_conf['hostadd']
child_interact_ip = '10.1.0.45'
middle_interacts = {'host': middle_interact_ip, 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}
child_interacts = {'host': child_interact_ip, 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}

schools = []
school = {}


class generateSystemData(unittest.TestCase):
    ''''学校教室设备基础数据添加'''

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

    def test_agenerateSchoolInfo(self):
        '''生成学校教室设备'''
        print 'exec: test_agenerateSchoolInfo...'
        # 获取学校数据 schools
        print 'exec:'
        schoolTmps = []
        schools = []
        school = {}
        for classroom in classroom_para:
            if classroom['schoolid'] not in schoolTmps:
                schoolTmps.append(classroom['schoolid'])

        for schoolTmp in schoolTmps:
            print schoolTmp
            school = {}
            school.setdefault('schoolName', schoolTmp.decode('utf-8'))
            # school.setdefault('schoolName', schoolTmp)
            school.setdefault('schoolType', u'高中')
            school.setdefault('schoolArea', u'郑州市')
            print school
            schools.append(school)
        # 获取教室数据
        classrooms = []
        classroom = {}
        for classroomTmp in classroom_para:
            classroom = {}
            classroom.setdefault('className', classroomTmp['classname'].decode('utf-8'))
            classroom.setdefault('classAccNumber', classroomTmp['classaccnumber'].decode('utf-8'))
            classroom.setdefault('schoolid', classroomTmp['schoolid'].decode('utf-8'))
            classroom.setdefault('equipmentModel', classroomTmp['equipmentmodel'].decode('utf-8'))
            classroom.setdefault('className', classroomTmp['classname'].decode('utf-8'))
            classroom.setdefault('equipment_name', classroomTmp['equipment_name'].decode('utf-8'))
            classroom.setdefault('ipAddr', classroomTmp['ipaddr'].decode('utf-8'))
            classroom.setdefault('locAddr', classroomTmp['ipaddr'].decode('utf-8'))
            classroom.setdefault('equipmentLogName', 'admin')
            classroom.setdefault('equipmentLogPwd', 'admin')
            classroom.setdefault('equimenttype', classroomTmp['equimenttype'].decode('utf-8'))
            classrooms.append(classroom)
        print classrooms

        driver = self.driver
        user_login(driver, **loginInfo)

        for school in schools:
            # 添加学校
            add_schools(driver, **school)
            for user in users:
                add_users(driver, **user)
            for classroom in classrooms:
                # 添加教室
                if classroom['schoolid'] == school['schoolName']:
                    add_classrooms(driver, **classroom)
                    print classroom['schoolid'], school['schoolName']
                    # 添加设备
                    if classroom['equimenttype'] == '1':
                        add_integrateds(driver, **classroom)
                    else:
                        add_terminals(driver, **classroom)
        print 'exec: test_agenerateSchoolInfo end.'

        # def test_bgenerateTeacherInfo(self):
        #     '''生成教师信息'''
        #     print 'exec: test_generateTeacherInfo...'
        #     driver = self.driver
        #     user_login(driver, **loginInfo)
        #     for user in users:
        #         add_users(driver, **user)
        #
        #     print 'exec: test_generateTeacherInfo end.'


if __name__ == '__main__':
    unittest.main()
