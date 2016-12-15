# coding=utf-8
import sys
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import sys, os
sys.path.append(os.environ.get('PY_DEV_HOME'))



reload(sys)
sys.setdefaultencoding("utf-8")

conditions = [{'condition': u"河南"}, {'condition': u"1河南"}]


def search_tenant(driver, **kwargs):
    '''查询租户'''
    driver.refresh()
    sleep(0.5)
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"租户管理").click()
    sleep(0.5)
    driver.find_element_by_xpath("//*[@id='condition']").clear()
    driver.find_element_by_xpath("//*[@id='condition']").send_keys(kwargs['condition'])
    driver.find_element_by_xpath("//*[@id='searchbtn']").click()
    sleep(0.5)

schools = [{'schoolName': u'二中', 'schoolType': u'高中', 'schoolArea': u'郑州市'},
           {'schoolName': u'三中', 'schoolType': u'中学', 'schoolArea': u'郑州市'},
           {'schoolName': u'四中', 'schoolType': u'中学', 'schoolArea': u'开封市'},
           {'schoolName': u'五中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'六中', 'schoolType': u'小学', 'schoolArea': u'开封市'},
           {'schoolName': u'一中', 'schoolType': u'高中', 'schoolArea': u'郑州市'}]


def add_schools(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''查询学校'''

    print "查询学校信息：{0}，{1}，{2}".format(kwargs['schoolName'], kwargs['schoolType'], kwargs['schoolArea'])

    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()

    # select area
    # driver.find_element_by_id("choosearea").click()
    # sleep(1)
    # driver.find_element_by_xpath("//div[@id='treeview']/ul/li[2]").click()
    # driver.find_element_by_css_selector("div.col-sm-9.text-center > #submit").click()
    sleep(1)
    # 查询学校btn
    driver.find_element_by_xpath("//*[@id='addSchool']").click()
    sleep(1)
    # 输入学校
    driver.find_element_by_xpath("//*[@id='schoolName']/div/input").clear()
    driver.find_element_by_xpath("//*[@id='schoolName']/div/input").send_keys(kwargs['schoolName'])
    # 选择学校类型
    Select(driver.find_element_by_css_selector("select.form-control")).select_by_visible_text(kwargs['schoolType'])
    # 学校选择区域
    Select(driver.find_element_by_xpath("//div[@id='areaSelect']/select[2]")).select_by_visible_text(kwargs['schoolArea'])
    # //div[@id='schoolTypeId']/div/select
    # click确定
    driver.find_element_by_xpath("//button[@id='submit']").click()
    # self.assertEqual(u"查询成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
    sleep(2)
    print "查询：%s 成功。" % kwargs['schoolName']

    # print "查询：%s 失败。" % kwargs['schoolName']

classrooms = [{'className': '31className', 'classAccNumber': '1'},
              {'className': '32className', 'classAccNumber': '1'}]


def add_classrooms(driver, **kwargs):
    # para:
    '''查询教室组'''
    print "add info:{0},{1}".format(kwargs['className'], kwargs['classAccNumber'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()
        sleep(1)
        # click add btn
        driver.find_element_by_css_selector(u"a[title=\"查询教室\"] > span").click()
        sleep(0.5)
        # operation
        driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").send_keys(kwargs['className'])
        driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").send_keys(kwargs['classAccNumber'])
        # click 确定
        driver.find_element_by_xpath("(//button[@id='submit'])[3]").click()

        sleep(1)
        print "add {} success.".format(kwargs['className'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['className'])

integrateds = [{'classroom': '32className', 'equipment_name': '81lb', 'ipAddr': '10.1.0.81', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'},
               {'classroom': '31className', 'equipment_name': '82lb', 'ipAddr': '10.1.0.82', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'}]

terminals = [{'equipmentModel': u'Group系列', 'classroom': '32className', 'equipment_name': '81lb', 'ipAddr': '10.1.0.81', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'},
             {'equipmentModel': u'Group系列', 'classroom': '31className', 'equipment_name': '82lb', 'ipAddr': '10.1.0.82', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'}]


def add_terminals(driver, **kwargs):
    # para:
    '''查询一个终端'''
    print "add info:{0},{1}".format(kwargs['equipment_name'], kwargs['classroom'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()
        driver.find_element_by_link_text(u"教室列表").click()
        sleep(1)
        driver.find_element_by_link_text(kwargs['classroom']).click()
        sleep(1)
        driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_id("addterminal").click()
        sleep(1)
        # operation
        driver.find_element_by_css_selector(
            "div.modal-body > div > #name > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #name > div.col-sm-9 > input.form-control").send_keys(kwargs['equipment_name'])
        Select(driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentModel > div.col-sm-9 > select")).select_by_visible_text(kwargs['equipmentModel'])
        driver.find_element_by_css_selector(
            "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys(kwargs['ipAddr'])
        driver.find_element_by_css_selector(
            "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #locAddr > div.col-sm-9 > input.form-control").send_keys(kwargs['locAddr'])
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys(kwargs['equipmentLogName'])
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys(kwargs['equipmentLogPwd'])
        # click OK
        driver.find_element_by_css_selector(
            "#terminal > div.modal-dialog > div.modal-content > #formrole > div.modal-body > div.text-center > #submit").click()
        sleep(1)
        print "add {} success.".format(kwargs['equipment_name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipment_name'])


def add_integrateds(driver, **kwargs):
    # para:
    '''查询一体机'''
    print "add info:{0},{1}".format(kwargs['equipment_name'], kwargs['classroom'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()
        driver.find_element_by_link_text(u"教室列表").click()
        sleep(1)
        driver.find_element_by_link_text(kwargs['classroom']).click()
        sleep(1)
        driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_id("addIntegrated").click()
        sleep(0.5)
        # operation
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #name > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #name > div.col-sm-9 > input.form-control").send_keys(kwargs['equipment_name'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #ipAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #ipAddr > div.col-sm-9 > input.form-control").send_keys(kwargs['ipAddr'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #locAddr > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #locAddr > div.col-sm-9 > input.form-control").send_keys(kwargs['locAddr'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogName > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogName > div.col-sm-9 > input.form-control").send_keys(kwargs['equipmentLogName'])
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").clear()
        driver.find_element_by_css_selector(
            "div.modal-body.row > div > #equipmentLogPwd > div.col-sm-9 > input.form-control").send_keys(kwargs['equipmentLogPwd'])
        # click 确定
        driver.find_element_by_css_selector(
            "#Integrated > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > div.text-center > #submit").click()
        sleep(1)
        print "add {} success.".format(kwargs['equipment_name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipment_name'])

subjectsGroups = [{'groupName': u'计算机', 'groupCode': '001', 'description': u'计算机'},
                  {'groupName': u'计算机1', 'groupCode': '002', 'description': u'计算机'}]

searchSubjectGrps = [{'groupName': u'计算机'},
                    {'groupName': u'计算机1'}]

operaters = [{'user': 'hnsadmin'}]


def search_systemLog(driver, **kwargs):
    #para:  管理员。 查询系统日志
    print "search info:{0}".format(kwargs['user'])
    # refresh main page
    driver.refresh()
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"系统日志").click()
    sleep(1)
    # operation
    driver.find_element_by_xpath("//input[@id='logsUser']").clear()
    driver.find_element_by_xpath("//input[@id='logsUser']").send_keys(kwargs['user'])
    sleep(0.5)

    # click 确定
    driver.find_element_by_xpath("//button[@id='select']").click()
    sleep(1)
    print "search {} success.".format(kwargs['user'])



def search_subjectGrp(driver, **kwargs):
    # para:
    '''search 教室组'''
    print "search info:{0}".format(kwargs['groupName'])
    # refresh main page
    driver.refresh()
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"组管理").click()
    sleep(1)
    # operation
    driver.find_element_by_xpath("//input[@id='condition']").clear()
    driver.find_element_by_xpath("//input[@id='condition']").send_keys(kwargs['groupName'])
    sleep(0.5)

    # click 确定
    driver.find_element_by_xpath("//button[@id='searchbtn']").click()
    sleep(1)
    print "search {} success.".format(kwargs['groupName'])

users = [{'loginName': 'user', 'trueName': 'teacher'},
         {'loginName': 'user1', 'trueName': 'teacher1'},
         {'loginName': 'user2', 'trueName': 'teacher2'},
         {'loginName': 'user3', 'trueName': 'teacher3'},
         {'loginName': 'user4', 'trueName': 'teacher4'}]


def search_user(driver, **kwargs):
    # pra: loginName, trueName
    '''查询用户'''
    print "查询用户的信息：{0},{1}".format(kwargs['loginName'], kwargs['trueName'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"用户列表").click()
        sleep(1)
        # input search text
        driver.find_element_by_xpath("//input[@id='keyname']").clear()
        driver.find_element_by_xpath("//input[@id='keyname']").send_keys(kwargs['trueName'])
        # click search btn
        driver.find_element_by_xpath("//button[@id='userLike']").click()
        sleep(1)
        print "查询用户{0}成功。".format(kwargs['trueName'])
    except Exception as e:
        print "查询用户{0}失败。".format(kwargs['trueName'])
        print e


def add_roles(driver, **kwargs):
    # para: driver,roleName, roleCode, description
    '''查询角色'''
    print "查询的角色信息：{0},{1},{2}".format(kwargs['roleName'], kwargs['roleCode'], kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"角色管理").click()
        sleep(0.5)

        # click addrole button
        driver.find_element_by_xpath("//a[@id='addrole']").click()
        sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='roleName']").clear()
        driver.find_element_by_xpath(".//*[@id='roleName']").send_keys(kwargs['roleName'])
        driver.find_element_by_xpath(".//*[@id='roleCode']").clear()
        driver.find_element_by_xpath(".//*[@id='roleCode']").send_keys(kwargs['roleCode'])
        driver.find_element_by_xpath(".//*[@id='description']").clear()
        driver.find_element_by_xpath(".//*[@id='description']").send_keys(kwargs['description'])
        driver.find_element_by_xpath(".//*[@id='insertrole']").click()
        sleep(1)
        print "查询角色{}成功。".format(kwargs['roleName'])
    except Exception as e:
        print e
        print "查询角色{}失败。".format(kwargs['roleName'])

interactgrps = [{'grpName': 'grp1', 'schoolgrTypeId': u'课程组'},
                {'grpName': 'grp2', 'schoolgrTypeId': u'会议组'},
                {'grpName': 'grp3', 'schoolgrTypeId': u'会议组'}]


def search_interactgrps(driver, **kwargs):
    # para:grpName,schoolgrTypeId
    '''查询教室组'''
    print "search info:{0}".format(kwargs['grpName'])

    try:
        # refresh main page
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"互动组管理").click()
        sleep(0.5)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='condition']").clear()
        driver.find_element_by_xpath("//input[@id='condition']").send_keys(kwargs['grpName'])
        sleep(0.5)
        # click search btn
        driver.find_element_by_xpath("//button[@id='searchbtn']").click()
        sleep(1)
        print "search {} success.".format(kwargs['grpName'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['grpName'])

subjects = [{'subjectName': u'书法', 'description': u'学习中国文化'},
            {'subjectName': u'计算机', 'description': u'计算机基础应用'}]


def search_subject(driver, **kwargs):
    # para:
    '''查询科目'''
    print "add info:{0}".format(kwargs['subjectName'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"科目管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchsubject']").clear()
        driver.find_element_by_xpath("//input[@id='searchsubject']").send_keys(kwargs['subjectName'])
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        print "add {} end.".format(kwargs['subjectName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['subjectName'])

chapters = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章a', 'chapterCode': u'助记码1'},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章b', 'chapterCode': u'助记码1'}]


chapters = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章a', 'chapterCode': u'助记码1'},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章b', 'chapterCode': u'助记码1'}]

def search_chapter(driver, **kwargs):
    # para:
    '''查询章'''
    print "search info:{0},{1}".format(kwargs['subjectid'], kwargs['chapterName'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"章管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchchapter']").clear()
        driver.find_element_by_xpath("//input[@id='searchchapter']").send_keys(kwargs['chapterName'])
        #click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        print "search info:{0},{1} end".format(kwargs['subjectid'], kwargs['chapterName'])

    except Exception as e:
        print e
        print "search {0},{1} failed.".format(kwargs['subjectid'], kwargs['chapterName'])



sections = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': u"数学第二章", 'sectionName': u"sx第一节", 'sectionCode': u"第一节zjm"},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': u"数学第二章", 'sectionName': u"sx第二节", 'sectionCode': u"第二节zjm"}]


def search_section(driver, **kwargs):
    # para:
    '''查询节信息'''

    print "search info:{0},{1},{2},{3},{4}".format(kwargs['gradeid'], kwargs['subjectid'], kwargs['chapterid'], kwargs['sectionName'], kwargs['sectionCode'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"节管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchsection']").clear()
        driver.find_element_by_xpath("//input[@id='searchsection']").send_keys(kwargs['sectionName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        sleep(0.5)
        print "search {} end.".format(kwargs['sectionName'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['sectionName'])


knowledges = [{'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'语文第一章', 'sectionid': u"第一节", 'knowledgeName': u"双细胞", 'knowledgeCode': u"双细胞1"},
              {'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'语文第一章', 'sectionid': u"第一节", 'knowledgeName': u"多细胞", 'knowledgeCode': u"多细胞1"}]


def search_knowledge(driver, **kwargs):
    # para:
    '''查询知识点'''
    print "search info:{0},{1}".format(kwargs['knowledgeName'], kwargs['subjectid'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"知识点管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchknowledge']").clear()
        driver.find_element_by_xpath("//input[@id='searchknowledge']").send_keys(kwargs['knowledgeName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['knowledgeName'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['knowledgeName'])

MCUequipments = [{'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.85', 'mcu_port': '80', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'},
                 {'equipmentName': '95mcu', 'equipIpAddr': '10.1.0.95', 'mcu_port': '10000', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'}]


def search_MCUequipment(driver, **kwargs):
    # para:equipmentName，equipIpAddr，mcu_port，mcuLoginName，mcuPasswd
    '''查查mcu'''
    print "search info:{0},{1},{2},{3}".format(kwargs['equipmentName'], kwargs['equipIpAddr'], kwargs['mcuLoginName'], kwargs['mcuPasswd'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='mcuNmCondition']").clear()
        driver.find_element_by_xpath("//input[@id='mcuNmCondition']").send_keys(kwargs['equipmentName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='btnMcuNm']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['equipmentName'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['equipmentName'])


interacts = [{'host': '10.1.0.2', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'},
             {'host': '10.1.0.3', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}]


def search_interact(driver, **kwargs):
    # para:host,port,username,password
    '''添加消息中间件'''
    print "search info:{0},{1},{2},{3}".format(kwargs['host'], kwargs['port'], kwargs['username'], kwargs['password'])
    # refresh main page
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)
        driver.find_element_by_id("xiaoximiddleware").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='selectmiddleware']").clear()
        driver.find_element_by_xpath("//input[@id='selectmiddleware']").send_keys(kwargs['host'])
        # click search button
        driver.find_element_by_xpath("//button[@id='btnmiddleware']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['host'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['host'])

hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会议480p'}]
speaker_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲下课_1'}]
listener_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲下课_1'}]

def search_cfg_hdks(driver, **kwargs):
    # para:name
    '''查询互动教学模板'''
    print "search info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        driver.find_element_by_xpath(u"(//a[contains(text(),'互动教学')])[2]").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchinteractteach']").clear()
        driver.find_element_by_xpath("//input[@id='searchinteractteach']").send_keys(kwargs['name'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['name'])


def search_cfg_jpks(driver, **kwargs):
    # para:name
    '''查询精品课堂模板'''
    print "search info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchexcellentclassroom']").clear()
        driver.find_element_by_xpath("//input[@id='searchexcellentclassroom']").send_keys(kwargs['name'])
        # click search button
        driver.find_element_by_xpath("//button[@id='searchs']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['name'])



def search_cfg_conferences(driver, **kwargs):
    # para:name
    '''查询视频会议模板'''
    print "search info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'视频会议')])[2]").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchvideoconference']").clear()
        driver.find_element_by_xpath("//input[@id='searchvideoconference']").send_keys(kwargs['name'])
        # click search button
        driver.find_element_by_xpath("//button[@id='searched']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['name'])


def search_cfg_listener_lessons(driver, **kwargs):
    # para:name
    '''查询听课下课模板'''
    print "search info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_link_text(u"听课下课").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchlisteningclass']").clear()
        driver.find_element_by_xpath("//input[@id='searchlisteningclass']").send_keys(kwargs['name'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search_lic']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['name'])


def search_cfg_speaker_lessons(driver, **kwargs):
    # para:name
    '''查询主讲下课模板'''
    print "search info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_link_text(u"主讲下课").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchlectureclass']").clear()
        driver.find_element_by_xpath("//input[@id='searchlectureclass']").send_keys(kwargs['name'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search_lec']").click()
        sleep(0.5)
        print "search {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "search {} failed.".format(kwargs['name'])


emails = [{'smtp': 'smtp.162.com', 'fromName': 'haosea@qq.com', 'password': '111111'},
          {'smtp': 'smtp.163.com', 'fromName': 'haosea1@qq.com', 'password': '111111'}]


def search_emails(driver, **kwargs):
    # 系统暂无email 查询功能
    '''查询邮箱服务'''
    pass

def search_announcement(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"公告管理").click()
    sleep(0.5)
    driver.find_element_by_id("noticeTitle").send_keys(kwargs["add_title"])
    driver.find_element_by_xpath("//div/div[2]/div/div/div/button").click()
    sleep(0.5)
    tbody = driver.find_element_by_css_selector(".table tbody tr").text
    if tbody !="":
        print kwargs["add_title"]+"添加成功"
    else:
        print kwargs["add_title"]+"添加失败"

def search_column(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"栏目管理").click()
    sleep(0.5)
    driver.find_element_by_id("navigationName").send_keys(kwargs["navigationName_add"])
    driver.find_element_by_id("searchBtn").click()
    sleep(0.5)
    datalists = driver.find_element_by_id("datalists").text
    if datalists != "":
        print kwargs["navigationName_add"]+"查询成功"
    else:
        print kwargs["navigationName_add"]+"查询失败"
        
def search_model(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"模板管理").click()
    sleep(0.5)
    driver.find_element_by_id("keyname").send_keys(kwargs["addname"])
    driver.find_element_by_id("selectTemplate").click()
    sleep(0.5)
    dataList = driver.find_element_by_id("dataList").text
    if dataList != "":
        print kwargs["addname"]+"查询成功"
    else:
        print kwargs["addname"]+"查询失败"

def search_live(driver, **kwargs):
    '''删除直播管理'''
    driver.refresh()
    driver.find_element_by_link_text(u"网站管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"直播管理").click()
    sleep(0.5)
    driver.find_element_by_xpath("//div[@id='main-container']/div/div[2]/div/div[2]/div/button[3]").click()
    
    driver.find_element_by_id("pdb_school_name_like").send_keys(kwargs["pd_schoolName"])
    driver.find_element_by_xpath("//div/div[2]/button").click()
    sleep(0.5)
    dataList = driver.find_element_by_id("privateDb_list").text
    if dataList != "":
        print kwargs["pd_schoolName"]+"查询成功"
    else:
        print kwargs["pd_schoolName"]+"查询失败"

if __name__ == '__main__':
    pass
