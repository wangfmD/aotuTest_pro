# coding=utf-8
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from init import loginInfo
from  baseActionAdd import user_login

reload(sys)
sys.setdefaultencoding("utf-8")


# def add_school_1(driver, **kwargs):
#     print kwargs['schoolName'], kwargs['schoolType'], kwargs['schoolArea']
#     # def add_school(driver, schoolName, schoolType, schoolArea):


def add_schools(driver, **kwargs):
    pass


def modify_classrooms(driver, **kwargs):
    # para:
    '''修改教室信息'''
    print "add info:{0},{1}".format(kwargs['className'], kwargs['classAccNumber'])
    # refresh main page
    driver.refresh()

    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_link_text(u"教室列表").click()
    sleep(1)
    # click add btn
    # driver.find_element_by_css_selector(u"a[title=\"添加教室\"] > span").click()
    # click modify btn
    driver.find_element_by_xpath("//button[@id='addcla']").click()
    sleep(0.5)
    # operation
    driver.find_element_by_xpath("(//div[@id='className']/div/input)[2]").clear()
    driver.find_element_by_xpath("(//div[@id='className']/div/input)[2]").send_keys(kwargs['className'])
    driver.find_element_by_xpath("(//div[@id='classAccNumber']/div/input)[2]").clear()
    driver.find_element_by_xpath("(//div[@id='classAccNumber']/div/input)[2]").send_keys(kwargs['classAccNumber'])
    # click 确定
    driver.find_element_by_xpath("(//button[@id='submit'])[4]").click()
    sleep(1)
    print "add {} success.".format(kwargs['className'])

    # print "add {} failed.".format(kwargs['className'])


integrateds = [{'classroom': '32className', 'equipment_name': '81lb', 'ipAddr': '10.1.0.81', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'},
               {'classroom': '31className', 'equipment_name': '82lb', 'ipAddr': '10.1.0.82', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'}]

terminals = [
    {'equipmentModel': u'Group系列', 'classroom': '32className', 'equipment_name': '81lb', 'ipAddr': '10.1.0.81', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'},
    {'equipmentModel': u'Group系列', 'classroom': '31className', 'equipment_name': '82lb', 'ipAddr': '10.1.0.82', 'locAddr': '10.1.0.81', 'equipmentLogName': 'admin', 'equipmentLogPwd': 'admin'}]

modifysubjectsGroup = [{'groupName': u'计算机modif', 'groupCode': '0101', 'description': u'计算机modif','searchName':u'计算机'}]
def update_subjectGrp(driver, **kwargs):
    '''修改组管理'''
    print "update info:{0},{1},{2}".format(kwargs['groupName'], kwargs['groupCode'], kwargs['description'])
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"组管理").click()
    sleep(1)
    # operation
    driver.find_element_by_xpath("//input[@id='condition']").clear()
    driver.find_element_by_xpath("//input[@id='condition']").send_keys(kwargs['searchName'])
    sleep(0.5)

    # click 确定
    driver.find_element_by_xpath("//button[@id='searchbtn']").click()
    # click add btn
    driver.find_element_by_xpath("//button[@id='insertsg']").click()
    sleep(1)
    driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(kwargs['groupName'])
    driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys(kwargs['groupCode'])
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[2]").clear()
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[2]").send_keys(kwargs['description'])
    sleep(0.5)
    # click 确定
    driver.find_element_by_xpath("(//button[@id='submit'])[2]").click()
    sleep(1)



def modify_terminals(driver, **kwargs):
    # para:
    '''添加一体机'''
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


def test_modify_terminal(driver):
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_link_text(u"教室列表").click()
    sleep(1)
    driver.find_element_by_link_text("32className").click()
    sleep(1)
    driver.find_element_by_xpath(u"//a[contains(text(),'设备管理')]").click()
    # click modify button

    driver.find_element_by_xpath("//td[10]/button[2]").click()
    # driver.find_element_by_xpath("(//input[@name='isIngkup'])[2]").click()
    sleep(1)
    # driver.find_element_by_xpath("(//input[@name='isIngkup'])[2]").click()
    driver.find_element_by_xpath("(//input[@type='text'])[37]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[37]").send_keys(u"10.1.0.81终端mod")
    driver.find_element_by_xpath("(//input[@type='text'])[38]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[38]").send_keys("10.1.0.1")
    driver.find_element_by_xpath("(//input[@type='text'])[39]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[39]").send_keys("10.1.0.1")
    driver.find_element_by_xpath("(//input[@type='text'])[40]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[40]").send_keys("admin1")
    driver.find_element_by_xpath("(//input[@type='text'])[41]").clear()
    driver.find_element_by_xpath("(//input[@type='text'])[41]").send_keys("admin1")
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").clear()
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").send_keys("11")
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").clear()
    driver.find_element_by_xpath("(//div[@id='description']/div/textarea)[7]").send_keys("11bz")
    # click OK button
    driver.find_element_by_xpath("(//button[@id='submit'])[7]").click()


def add_integrateds(driver, **kwargs):
    # para:
    '''添加一体机'''
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
        "div#Integrated.modal.fade.ui-draggable.in"
        sleep(1)
        print "add {} success.".format(kwargs['equipment_name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipment_name'])


def search_school(driver):
    '''删除学校'''
    pass


def add_users(driver, **kwargs):
    # pra: loginName, trueName
    '''添加用户'''
    print "添加用户的信息：{0},{1}".format(kwargs['loginName'], kwargs['trueName'])
    try:
        # driver.find_element_by_css_selector("#div_menu > ul.nav.nav-list > li > a.dropdown-toggle > span.menu-text").click()
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"用户列表").click()
        driver.find_element_by_id("adduserlist").click()
        sleep(1)
        driver.find_element_by_name("loginName").clear()
        driver.find_element_by_name("loginName").send_keys(kwargs['loginName'])
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("111111")
        driver.find_element_by_name("passwords").clear()
        driver.find_element_by_name("passwords").send_keys("111111")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("13700010001")
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("user@3bu.cn")
        driver.find_element_by_name("trueName").clear()
        driver.find_element_by_name("trueName").send_keys(kwargs['trueName'])
        driver.find_element_by_id("determine").click()
        sleep(1)
        print "添加用户{0}成功。".format(kwargs['trueName'])
    except Exception as e:
        print "添加用户{0}失败。".format(kwargs['trueName'])
        print e


def add_roles(driver, **kwargs):
    # para: driver,roleName, roleCode, description
    '''添加角色'''
    print "添加的角色信息：{0},{1},{2}".format(kwargs['roleName'], kwargs['roleCode'], kwargs['description'])
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
        print "添加角色{}成功。".format(kwargs['roleName'])
    except Exception as e:
        print e
        print "添加角色{}失败。".format(kwargs['roleName'])


interactgrps = [{'grpName': 'grp1', 'schoolgrTypeId': u'课程组'},
                {'grpName': 'grp2', 'schoolgrTypeId': u'会议组'},
                {'grpName': 'grp3', 'schoolgrTypeId': u'会议组'}]


def add_interactgrps(driver, **kwargs):
    # para:grpName,schoolgrTypeId
    '''添加教室组'''
    print "add info:{0},{1}".format(kwargs['grpName'], kwargs['schoolgrTypeId'])

    try:
        # refresh main page
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"互动组管理").click()
        sleep(0.5)

        # click add btn
        driver.find_element_by_xpath("//button[@id='addSchool']").click()
        sleep(0.5)
        # //*[@id='schoolName']/div/input
        # operation
        driver.find_element_by_xpath("//div[@id='schoolName']/div/input").clear()
        driver.find_element_by_xpath("//div[@id='schoolName']/div/input").send_keys(kwargs['grpName'])
        Select(driver.find_element_by_xpath("//div[@id='schoolTypeId']/div/select")).select_by_visible_text(kwargs['schoolgrTypeId'])
        # //*[@id='schoolTypeId']/div/select
        # click 确定
        driver.find_element_by_xpath("//button[@id='submit']").click()
        # driver.find_element_by_xpath("//*[@id='submit']").click()
        sleep(1)
        print "add {} success.".format(kwargs['grpName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['grpName'])


subjects = [{'subjectName': u'书法', 'description': u'学习中国文化'},
            {'subjectName': u'计算机', 'description': u'计算机基础应用'}]


def add_subjects(driver, **kwargs):
    # para:
    '''添加科目'''
    print "add info:{0},{1}".format(kwargs['subjectName'], kwargs['description'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"科目管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addsubject']").click()
        # //*[@id='addsubject']
        sleep(0.5)

        # operation
        driver.find_element_by_xpath("//input[@id='subjectName']").clear()
        driver.find_element_by_xpath("//input[@id='subjectName']").send_keys(kwargs['subjectName'])
        driver.find_element_by_xpath("//*[@id='description']").clear()
        driver.find_element_by_xpath("//*[@id='description']").send_keys(kwargs["description"])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertsubject']").click()
        sleep(1)
        print "add {} success.".format(kwargs['subjectName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['subjectName'])


chapters = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章a', 'chapterCode': u'助记码1'},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章b', 'chapterCode': u'助记码1'}]


def add_chapters(driver, **kwargs):
    # para:
    '''添加章'''
    print "add info:{0},{1},{2},{3}".format(kwargs['gradeid'], kwargs['subjectid'], kwargs['chapterName'], kwargs['chapterCode'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"章管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addchapter']").click()
        sleep(0.5)

        # operation
        Select(driver.find_element_by_xpath("//select[@id='gradeid']")).select_by_visible_text(kwargs['gradeid'])
        Select(driver.find_element_by_xpath("//select[@id='subjectid']")).select_by_visible_text(kwargs['subjectid'])
        driver.find_element_by_xpath("//input[@id='chapterName']").clear()
        driver.find_element_by_xpath("//input[@id='chapterName']").send_keys(kwargs['chapterName'])
        driver.find_element_by_xpath("//input[@id='chapterCode']").clear()
        driver.find_element_by_xpath("//input[@id='chapterCode']").send_keys(kwargs['chapterCode'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertchapter']").click()
        sleep(1)
        print "add {} success.".format(kwargs['chapterName'])

    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['chapterName'])


sections = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': "zmc11", 'sectionName': u"第一节", 'sectionCode': u"第一节zjm"},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': "zmc11", 'sectionName': u"第二节", 'sectionCode': u"第二节zjm"}]


def add_sections(driver, **kwargs):
    # para:
    '''添加节'''
    print "add info:{0},{1},{2},{3},{4}".format(kwargs['gradeid'], kwargs['subjectid'], kwargs['chapterid'], kwargs['sectionName'], kwargs['sectionCode'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"节管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addsection']/i").click()
        sleep(0.5)

        # operation
        Select(driver.find_element_by_xpath("//select[@id='gradeid']")).select_by_visible_text(u"二年级")
        Select(driver.find_element_by_xpath("//select[@id='subjectid']")).select_by_visible_text(u"数学")
        Select(driver.find_element_by_xpath("//select[@id='chapterid']")).select_by_visible_text("zmc11")
        driver.find_element_by_xpath("//input[@id='sectionName']").clear()
        driver.find_element_by_xpath("//input[@id='sectionName']").send_keys(u"jmc的")
        driver.find_element_by_xpath("//input[@id='sectionCode']").clear()
        driver.find_element_by_xpath("//input[@id='sectionCode']").send_keys(u"jmc的")
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertsection']").click()
        sleep(1)
        print "add {} success.".format(kwargs['sectionName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['sectionName'])


knowledges = [{'gradeid': u'六年级/小学', 'subjectid': u'自然科学', 'chapterid': u'第二章', 'sectionid': u"第二节", 'knowledgeName': u"双细胞", 'knowledgeCode': u"双细胞1"},
              {'gradeid': u'六年级/小学', 'subjectid': u'自然科学', 'chapterid': u'第二章', 'sectionid': u"第二节", 'knowledgeName': u"多细胞", 'knowledgeCode': u"多细胞1"}]


def add_knowledges(driver, **kwargs):
    # para:
    '''添加知识点'''
    print "add info:{0},{1}".format(kwargs['knowledgeName'], kwargs['subjectid'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"知识点管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//a[@id='addknowledge']").click()
        sleep(0.5)

        # operation
        Select(driver.find_element_by_xpath("//select[@id='gradeid']")).select_by_visible_text(kwargs['gradeid'])
        Select(driver.find_element_by_xpath("//select[@id='subjectid']")).select_by_visible_text(kwargs['subjectid'])
        Select(driver.find_element_by_xpath("//select[@id='chapterid']")).select_by_visible_text(kwargs['chapterid'])
        Select(driver.find_element_by_xpath("//select[@id='sectionid']")).select_by_visible_text(kwargs['sectionid'])
        driver.find_element_by_xpath("//input[@id='knowledgeName']").clear()
        driver.find_element_by_xpath("//input[@id='knowledgeName']").send_keys(kwargs['knowledgeName'])
        driver.find_element_by_xpath("//input[@id='knowledgeCode']").clear()
        driver.find_element_by_xpath("//input[@id='knowledgeCode']").send_keys(kwargs['knowledgeCode'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertknowledge']").click()
        sleep(1)
        print "add {} success.".format(kwargs['knowledgeName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['knowledgeName'])


centerequipments = [{'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.85', 'mcu_port': '80', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'},
                    {'equipmentName': '95mcu', 'equipIpAddr': '10.1.0.95', 'mcu_port': '10000', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'}]


def add_mcus(driver, **kwargs):
    # para:equipmentName，equipIpAddr，mcu_port，mcuLoginName，mcuPasswd
    '''添加mcu'''
    print "add info:{0},{1},{2},{3}".format(kwargs['equipmentName'], kwargs['equipIpAddr'], kwargs['mcuLoginName'], kwargs['mcuPasswd'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)

        # click add btn
        sleep(1)
        driver.find_element_by_css_selector("i.fa.fa-plus").click()
        sleep(1)
        driver.find_element_by_id("mcuAreaName").click()
        sleep(0.5)

        # operation
        driver.find_element_by_css_selector("li.list-group-item.node-treeview").click()
        sleep(1)
        driver.find_element_by_id("equipmentName").clear()
        driver.find_element_by_id("equipmentName").send_keys(kwargs['equipmentName'])
        driver.find_element_by_id("equipIpAddr").clear()
        driver.find_element_by_id("equipIpAddr").send_keys(kwargs['equipIpAddr'])
        driver.find_element_by_id("mcu_port").clear()
        driver.find_element_by_id("mcu_port").send_keys(kwargs['mcu_port'])
        driver.find_element_by_id("mcuLoginName").clear()
        driver.find_element_by_id("mcuLoginName").send_keys(kwargs['mcuLoginName'])
        driver.find_element_by_id("mcuPasswd").clear()
        driver.find_element_by_id("mcuPasswd").send_keys(kwargs['mcuPasswd'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='submit']").click()
        sleep(1)
        print "add {} success.".format(kwargs['equipmentName'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipmentName'])


interacts = [{'host': '10.1.0.2', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'},
             {'host': '10.1.0.3', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}]


def add_interacts(driver, **kwargs):
    # para:host,port,username,password
    '''添加消息中间件'''
    print "add info:{0},{1},{2},{3}".format(kwargs['host'], kwargs['port'], kwargs['username'], kwargs['password'])
    # refresh main page
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)
        driver.find_element_by_id("xiaoximiddleware").click()
        sleep(2)
        driver.find_element_by_css_selector("#addmiddleware > i.fa.fa-plus").click()
        sleep(1)
        driver.find_element_by_id("host").clear()
        driver.find_element_by_id("host").send_keys(kwargs['host'])
        driver.find_element_by_id("port").clear()
        driver.find_element_by_id("port").send_keys(kwargs['port'])
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(kwargs['username'])
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(kwargs['password'])
        sleep(1)
        driver.find_element_by_id("insertmiddleware").click()
        sleep(1)

        print "add {} success.".format(kwargs['host'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['host'])


hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会议480p'}]
speaker_cls_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲下课_1'}]
listener_cls_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲下课_1'}]


def add_cfg_listener_cls_lessons(driver, **kwargs):
    # para:name
    '''添加听讲下课模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_link_text(u"听课下课").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addlisteningclass']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[7]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[7]").send_keys(kwargs['name'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertlectureclass']").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_speaker_cls_lessons(driver, **kwargs):
    # para:name
    '''添加主讲下课模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_link_text(u"主讲下课").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addlectureclass']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[7]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[7]").send_keys(kwargs['name'])
        # click 确定
        driver.find_element_by_id("insertlectureclass").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_conferences(driver, **kwargs):
    # para:name
    '''添加会议模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'视频会议')])[2]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addvideoconference']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[5]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[5]").send_keys(kwargs['name'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertvideoconference']").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_jpks(driver, **kwargs):
    # para:name
    '''添加精品课模板'''
    print "add info:{0}".format(kwargs['name'])
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"模板管理").click()
        driver.find_element_by_xpath(u"(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        # click add btn
        driver.find_element_by_xpath("//a[@id='addexcellentclass']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("(//input[@id='name'])[3]").clear()
        driver.find_element_by_xpath("(//input[@id='name'])[3]").send_keys(kwargs['name'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertexcellentclass']").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['name'])


def add_cfg_hdks(driver, **kwargs):
    # para:name
    '''添加互动模板'''
    print "add info:{0}".format(kwargs['name'])
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
        # click add btn
        driver.find_element_by_xpath("//a[@id='addinteractteach']/i").click()
        sleep(0.5)
        # operation
        driver.find_element_by_xpath("//input[@id='name']").clear()
        driver.find_element_by_xpath("//input[@id='name']").send_keys(kwargs['name'])
        # click 确定
        driver.find_element_by_xpath("//button[@id='insertinteractteach']").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except NoSuchElementException as e:
        print e
        print "add {} failed.".format(kwargs['name'])


emails = [{'smtp': 'smtp.162.com', 'fromName': 'haosea@qq.com', 'password': '111111'},
          {'smtp': 'smtp.163.com', 'fromName': 'haosea1@qq.com', 'password': '111111'}]


def add_emails(driver, **kwargs):
    # para:
    '''添加邮箱服务'''
    print "add info:{0},{1},{2}".format(kwargs['smtp'], kwargs['fromName'], kwargs['password'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"邮箱服务管理").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//button[@id='add_email_setting']").click()
        sleep(0.5)

        # operation
        driver.find_element_by_xpath("//input[@id='smtp']").clear()
        driver.find_element_by_xpath("//input[@id='smtp']").send_keys(kwargs['smtp'])
        driver.find_element_by_xpath("//input[@id='fromName']").clear()
        driver.find_element_by_xpath("//input[@id='fromName']").send_keys(kwargs['fromName'])
        driver.find_element_by_xpath("// input[@id='password']").clear()
        driver.find_element_by_xpath("//input[@id='password']").send_keys(kwargs['password'])
        driver.find_element_by_xpath("//input[@id='status0']").click()
        # click 确定
        driver.find_element_by_xpath("//button[@id='determine']").click()
        sleep(1)
        print "add {} success.".format(kwargs['smtp'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['smtp'])


def add_tmp(driver, **kwargs):
    # para:
    '''添加教室组'''
    print "add info:{0},{1}".format(kwargs[''], kwargs[''])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"").click()
        sleep(1)

        # click add btn
        driver.find_element_by_xpath("//button[@id='addSchool']").click()
        sleep(0.5)

        # operation
        driver.find_element_by_xpath("").clear()
        driver.find_element_by_xpath("").send_keys(kwargs[''])
        driver.find_element_by_xpath("").clear()
        driver.find_element_by_xpath("").send_keys("")
        Select(driver.find_element_by_xpath("//div[@id='schoolTypeId']/div/select")).select_by_visible_text(u"课程组")
        # ...
        # ...
        # ...
        # click 确定
        driver.find_element_by_xpath("//button[@id='submit']").click()
        sleep(1)
        print "add {} success.".format(kwargs[''])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs[''])



'''修改单条用户数据'''
usersData = [{'mobiles': '18551184502', 'emails': '9930356@qq.com','trueName':u'张三','searchName':u''}]
def update_User(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改用户'''

    print "修改用户信息：{0}，{1}，{2}".format(kwargs['mobiles'], kwargs['emails'], kwargs['trueName'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"用户列表").click()
        sleep(2)
        driver.find_element_by_xpath("//input[@id='keyname']").clear()
        driver.find_element_by_xpath("//input[@id='keyname']").send_keys(kwargs['searchName'])
        # click search btn
        driver.find_element_by_xpath("//button[@id='userLike']").click()
        sleep(1)
        driver.find_element_by_xpath("//tbody[@id='userlists']/tr/td[9]/button[2]").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id='modals']/div/div/form/div/div/div[2]/div[6]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='modals']/div/div/form/div/div/div[2]/div[6]/div/input").send_keys(kwargs['mobiles'])
        driver.find_element_by_xpath("//*[@id='modals']/div/div/form/div/div/div[2]/div[7]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='modals']/div/div/form/div/div/div[2]/div[7]/div/input").send_keys(kwargs['emails'])
        driver.find_element_by_xpath("//*[@id='modals']/div/div/form/div/div/div[2]/div[8]/div/input").clear()
        driver.find_element_by_xpath("//*[@id='modals']/div/div/form/div/div/div[2]/div[8]/div/input").send_keys(kwargs['trueName'])
        driver.find_element_by_id("determines").click()
        print "update_User {} success.".format(kwargs['trueName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['trueName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条租户管理'''
tenantData = [{'platmarkName': u'河南教育局','platmarkCode':'001','searchName':u''}]
def update_Tenant(driver, **kwargs):
    '''修改租户管理'''
    print "修改租户管理信息：{0},{1}".format(kwargs['platmarkName'],kwargs['platmarkCode'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"租户管理").click()
        sleep(1)
        driver.find_element_by_xpath("//*[@id='condition']").clear()
        driver.find_element_by_xpath("//*[@id='condition']").send_keys(kwargs['searchName'])
        driver.find_element_by_xpath("//*[@id='searchbtn']").click()
        sleep(0.5)
        driver.find_element_by_id("insertten").click()
        sleep(2)
        driver.find_element_by_xpath("(//input[@type='text'])[10]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[10]").send_keys(kwargs['platmarkName'])
        driver.find_element_by_xpath("(//input[@type='text'])[11]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[11]").send_keys(kwargs['platmarkCode'])

        driver.find_element_by_css_selector("#tenantupdate #formrole #submit").click()

        print "update_Tenant {} success.".format(kwargs['platmarkName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['platmarkName']
    driver.close()
    driver.quit()
    driver = None


'''修改单条学校数据'''
schoolData = [{'schoolName': u'河南一中'}]
def update_School(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改学校'''
    print "修改学校信息：{0}".format(kwargs['schoolName'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"学校管理").click()
        sleep(2)
        driver.find_element_by_id("condition").click()
        driver.find_element_by_id("condition").send_keys(kwargs['searchName'])
        driver.find_element_by_id("searchbtn").click()
        sleep(0.5)
        valuesText=driver.find_element_by_css_selector("#schooltab > tbody > tr > td").text
        if valuesText!="无数据" :
            driver.find_element_by_xpath("//*[@id='addsc']").click()
            sleep(2)
            driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
            driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(kwargs['schoolName'])
            driver.find_element_by_xpath("(//button[@id='submit'])[2]").click()
            print "update_School {} success.".format(kwargs['schoolName'])
        else :
            print "没有找到学校数据。"

    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['schoolName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条学校设备'''
schoolManagementData = [{'name': u'设备1号','ipAddr':u'10.1.0.57','locAddr':u'10.1.0.57','equipmentLogName':u'hnsadmin','equipmentLogPwd':u'111111','description':u'测试数据'}]
def update_DeviceManagement(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改单条学校设备'''
    print "修改单条学校设备：{0},{1},{2},{3},{4},{5}".format(kwargs['name'],kwargs['ipAddr'],kwargs['locAddr'],kwargs['equipmentLogName'],kwargs['equipmentLogPwd'],kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"学校管理").click()
        sleep(0.5)
        driver.find_element_by_xpath("//a[contains(text(),'教室列表')]").click()
        sleep(2)
        driver.find_element_by_css_selector("#classtab tr > td:nth-child(3) a").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'设备管理')]").click()
        sleep(1)
        driver.find_element_by_css_selector("#schoolequipmenttab tr:nth-child(2) button:eq(1)").click()
        sleep(1)
        driver.find_element_by_css_selector("#Integratedupdate #name div>input").clear()
        driver.find_element_by_css_selector("#Integratedupdate #name div>input").send_keys(kwargs['name'])
        driver.find_element_by_css_selector("#Integratedupdate #ipAddr div>input").clear()
        driver.find_element_by_css_selector("#Integratedupdate #ipAddr div>input").send_keys(kwargs['ipAddr'])
        driver.find_element_by_css_selector("#Integratedupdate #locAddr div>input").clear()
        driver.find_element_by_css_selector("#Integratedupdate #locAddr div>input").send_keys(kwargs['locAddr'])
        driver.find_element_by_css_selector("#Integratedupdate #equipmentLogName div>input").clear()
        driver.find_element_by_css_selector("#Integratedupdate #equipmentLogName div>input").send_keys(kwargs['equipmentLogName'])
        driver.find_element_by_css_selector("#Integratedupdate #equipmentLogPwd div>input").clear()
        driver.find_element_by_css_selector("#Integratedupdate #equipmentLogPwd div>input").send_keys(kwargs['equipmentLogPwd'])
        driver.find_element_by_css_selector("#Integratedupdate #description div>textarea").clear()
        driver.find_element_by_css_selector("#Integratedupdate #description div>textarea").send_keys(kwargs['description'])
        sleep(1)
        driver.find_element_by_css_selector("#Integratedupdate #submit").click()
        sleep(2)
        print "update_DeviceManagement  SUCCESS{0}".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    driver.close()
    driver.quit()
    driver = None


'''修改单条组管理数据'''
GroupData = [{'groupName': u'奥数组','groupCode':'001','description':u'说明测试数据'}]
def update_GroupManagement(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改学校'''
    print "修改学校信息：{0}{1}{2}".format(kwargs['groupName'],kwargs['groupCode'],kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"组管理").click()
        sleep(1)
        driver.find_element_by_css_selector("#SchoolGroupmodaltab #insertsg").click()
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate #formrole #groupName input.form-control").clear()
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate #formrole #groupName input.form-control").send_keys(kwargs['groupName'])
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate #formrole #groupCode input.form-control").clear()
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate #formrole #groupCode input.form-control").send_keys(kwargs['groupCode'])
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > #description > div.col-sm-9 > textarea.form-control").clear()
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > #description > div.col-sm-9 > textarea.form-control").send_keys(kwargs['description'])
        # click 确定
        driver.find_element_by_css_selector("#SchoolGroupmodalupdate #submit").click()
        sleep(1)
        print "add {} success.".format(kwargs['groupName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['groupName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条角色管理数据'''
roleData = [{'roleName': u'奥数组','roleCode':'001','description':u'说明测试数据','searchName':''}]
def update_roleManagement(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改角色'''
    print "修改角色信息：{0},{1},{2}".format(kwargs['roleName'], kwargs['roleCode'], kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"角色管理").click()
        sleep(1)

        driver.find_element_by_id("searchrole").clear()
        driver.find_element_by_id("searchrole").send_keys(kwargs['searchName'])
        # click search btn
        driver.find_element_by_id("search").click()
        sleep(1)

        driver.find_element_by_xpath("//table[@id='dtrole']/tbody/tr/td[5]/button[2]").click()
        driver.find_element_by_css_selector("#roleupdate #roleNames").clear()
        driver.find_element_by_css_selector("#roleupdate #roleNames").send_keys(kwargs['roleName'])
        driver.find_element_by_css_selector("#roleupdate #roleCodes").clear()
        driver.find_element_by_css_selector("#roleupdate #roleCodes").send_keys(kwargs['roleCode'])
        driver.find_element_by_css_selector("#roleupdate #descriptions").clear()
        driver.find_element_by_css_selector("#roleupdate #descriptions").send_keys(kwargs['description'])
        # click 确定
        driver.find_element_by_css_selector("#roleupdate #updaterole").click()
        sleep(1)
        print "add {} success.".format(kwargs['roleName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['roleName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条互动组管理数据'''
interactiveData = [{'grpName': u'互动组','searchName':''}]
def update_Interactive(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改互动组管理'''
    print "修改互动组管理信息：{0}".format(kwargs['grpName'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"互动组管理").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='condition']").clear()
        driver.find_element_by_xpath("//input[@id='condition']").send_keys(kwargs['searchName'])
        sleep(0.5)

        # click 确定
        driver.find_element_by_xpath("//button[@id='searchbtn']").click()

        driver.find_element_by_css_selector("#schooltab #addsc").click()
        driver.find_element_by_css_selector("#schoolmodalupdate #schoolName input").clear()
        driver.find_element_by_css_selector("#schoolmodalupdate #schoolName input").send_keys(kwargs['grpName'])
        # click 确定
        driver.find_element_by_css_selector("#schoolmodalupdate #submit").click()
        sleep(1)
        print "add {} success.".format(kwargs['grpName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['grpName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条科目管理数据'''
subjectsData = [{'subjectName': u'测试科目名称','description':'描述说明','searchName':''}]
def update_Subjects(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改互动组管理'''
    print "修改互动组管理信息：{0}{1}".format(kwargs['subjectName'],kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"基础数据").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"科目管理").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='searchsubject']").clear()
        driver.find_element_by_xpath("//input[@id='searchsubject']").send_keys(kwargs['searchName'])
        driver.find_element_by_xpath("//button[@id='search']").click()

        driver.find_element_by_id("subjects").click()
        driver.find_element_by_css_selector("#subjectupdate #subjectName").clear()
        driver.find_element_by_css_selector("#subjectupdate #subjectName").send_keys(kwargs['subjectName'])
        driver.find_element_by_css_selector("#subjectupdate #description").clear()
        driver.find_element_by_css_selector("#subjectupdate #description").send_keys(kwargs['description'])
        # click 确定
        driver.find_element_by_css_selector("#subjectupdate #updatesubject").click()
        sleep(1)
        print "add {} success.".format(kwargs['subjectName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['subjectName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条章管理数据'''
chapterData = [{'chapterName': u'数学第一章测试','chapterCode':'SX01','searchName':''}]
def update_Chapter(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改章管理'''
    print "修改章管理信息：{0}{1}".format(kwargs['chapterName'],kwargs['chapterCode'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"基础数据").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"章管理").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='searchchapter']").clear()
        driver.find_element_by_xpath("//input[@id='searchchapter']").send_keys(kwargs['searchName'])
        #click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        driver.find_element_by_id("chapters").click()
        sleep(1)
        driver.find_element_by_css_selector("#chapterupdate #formrole #chapterName").clear()
        driver.find_element_by_css_selector("#chapterupdate #formrole #chapterName").send_keys(kwargs['chapterName'])
        driver.find_element_by_css_selector("#chapterupdate #formrole #chapterCode").clear()
        driver.find_element_by_css_selector("#chapterupdate #formrole #chapterCode").send_keys(kwargs['chapterCode'])
        # click 确定
        driver.find_element_by_id("updatechapter").click()
        sleep(2)
        print "add {} success.".format(kwargs['chapterName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['chapterName']
    # driver.close()
    # driver.quit()
    # driver = None


'''修改单条节管理数据'''
sectionData = [{'sectionName': u'第一节测试','sectionCode':'SX01','searchName':u''}]
def update_Section(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改节管理'''
    print "修改节管理信息：{0}{1}".format(kwargs['sectionName'],kwargs['sectionCode'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"基础数据").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"节管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchsection']").clear()
        driver.find_element_by_xpath("//input[@id='searchsection']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        driver.find_element_by_id("sections").click()
        sleep(1)
        driver.find_element_by_css_selector("#sectionupdate #formrole #sectionName").clear()
        driver.find_element_by_css_selector("#sectionupdate #formrole #sectionName").send_keys(kwargs['sectionName'])
        driver.find_element_by_css_selector("#sectionupdate #formrole #sectionCode").clear()
        driver.find_element_by_css_selector("#sectionupdate #formrole #sectionCode").send_keys(kwargs['sectionCode'])
        # click 确定
        driver.find_element_by_id("updatesection").click()
        sleep(1)
        print "add {} success.".format(kwargs['sectionName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['sectionName']
    driver.close()
    driver.quit()
    driver = None


'''修改单条知识点管理数据'''
knowledgeData = [{'knowledgeName': u'小猫钓鱼测试','knowledgeCode':'SX01','searchName':u''}]
def update_Knowledge(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改知识点管理'''
    print "修改知识点管理信息：{0}{1}".format(kwargs['knowledgeName'],kwargs['knowledgeCode'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"基础数据").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"知识点管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchknowledge']").clear()
        driver.find_element_by_xpath("//input[@id='searchknowledge']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(0.5)

        driver.find_element_by_id("knowledges").click()
        sleep(1)
        driver.find_element_by_css_selector("#knowledgeupdate #formrole #knowledgeName").clear()
        driver.find_element_by_css_selector("#knowledgeupdate #formrole #knowledgeName").send_keys(kwargs['knowledgeName'])
        driver.find_element_by_css_selector("#knowledgeupdate #formrole #knowledgeCode").clear()
        driver.find_element_by_css_selector("#knowledgeupdate #formrole #knowledgeCode").send_keys(kwargs['knowledgeCode'])
        # click 确定
        driver.find_element_by_id("updateknowledge").click()
        sleep(1)
        print "add {} success.".format(kwargs['knowledgeName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['knowledgeName']
    driver.close()
    driver.quit()
    driver = None


'''修改单条中心设备数据'''
equipmentData = [{'equipmentName': u'测试设备','equipIpAddr':'10.1.0.19','mcu_port':'80','mcuLoginName':'zhangsan','mcuPasswd':'111111','softAgentIp':'10.1.4.33','softAgentPort':'80','bandWidth':'1000','searchName':u''}]
def update_Equipment(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改中心设备'''
    print "修改中心设备信息：{0},{1},{2},{3},{4},{5},{6},{7}".format(kwargs['equipmentName'],kwargs['equipIpAddr'],kwargs['mcu_port'],kwargs['mcuLoginName'],kwargs['mcuPasswd'],kwargs['softAgentIp'],kwargs['softAgentPort'],kwargs['bandWidth'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='mcuNmCondition']").clear()
        driver.find_element_by_xpath("//input[@id='mcuNmCondition']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='btnMcuNm']").click()
        sleep(0.5)
        driver.find_element_by_css_selector("button.btn.grey").click()
        sleep(1)
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #equipmentModel #equipmentName").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #equipmentModel #equipmentName").send_keys(kwargs['equipmentName'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #equipIpAddr").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #equipIpAddr").send_keys(kwargs['equipIpAddr'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #mcu_port").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #mcu_port").send_keys(kwargs['mcu_port'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #mcuLoginName").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #mcuLoginName").send_keys(kwargs['mcuLoginName'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #equipmentName").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #equipmentName").send_keys(kwargs['equipmentName'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #mcuPasswd").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #mcuPasswd").send_keys(kwargs['mcuPasswd'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #softAgentIp").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #softAgentIp").send_keys(kwargs['softAgentIp'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #softAgentPort").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #softAgentPort").send_keys(kwargs['softAgentPort'])

        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #bandWidth").clear()
        driver.find_element_by_css_selector("#mcuequipmentupdate #formrole #bandWidth").send_keys(kwargs['bandWidth'])

        # click 确定
        driver.find_element_by_id("submit").click()
        sleep(1)
        print "add {} success.".format(kwargs['equipmentName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['equipmentName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条中心设备消息中间件数据'''
middlewareData = [{'host': u'1.1.0.1','port':'80','username':'zhangsan','password':'111111','servicepath':'/interact','description':u'测试说明','searchName':u''}]
def update_Middleware(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改中心设备消息中间件'''
    print "修改中心设备消息中间件信息：{0},{1},{2},{3},{4},{5}".format(kwargs['host'],kwargs['port'],kwargs['username'],kwargs['password'],kwargs['servicepath'],kwargs['description'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"设备管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)
        driver.find_element_by_id("xiaoximiddleware").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='selectmiddleware']").clear()
        driver.find_element_by_xpath("//input[@id='selectmiddleware']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='btnmiddleware']").click()
        sleep(0.5)
        driver.find_element_by_id("middlewrupd").click()
        sleep(1)
        driver.find_element_by_css_selector("#middlewareupdate > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > div > div.form-group > #host").clear()
        driver.find_element_by_css_selector("#middlewareupdate > div.modal-dialog > div.modal-content > #formrole > div.modal-body.row > div > div.form-group > #host").send_keys(kwargs['host'])

        driver.find_element_by_css_selector("#middlewareupdate #formrole #port").clear()
        driver.find_element_by_css_selector("#middlewareupdate #formrole #port").send_keys(kwargs['port'])

        driver.find_element_by_css_selector("#middlewareupdate #formrole #username").clear()
        driver.find_element_by_css_selector("#middlewareupdate #formrole #username").send_keys(kwargs['username'])

        driver.find_element_by_css_selector("#middlewareupdate #formrole #password").clear()
        driver.find_element_by_css_selector("#middlewareupdate #formrole #password").send_keys(kwargs['password'])

        driver.find_element_by_css_selector("#middlewareupdate #formrole #servicepath").clear()
        driver.find_element_by_css_selector("#middlewareupdate #formrole #servicepath").send_keys(kwargs['servicepath'])

        driver.find_element_by_css_selector("#middlewareupdate #formrole #description").clear()
        driver.find_element_by_css_selector("#middlewareupdate #formrole #description").send_keys(kwargs['description'])

        # click 确定
        driver.find_element_by_id("updateMiddleWare").click()
        sleep(1)
        print "add {} success.".format(kwargs['host'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['host']
    driver.close()
    driver.quit()
    driver = None


'''修改单条模板管理互动教学数据'''
interactiveTeachingData = [{'name': u'720PP','searchName':u''}]
def update_InteractiveTeaching(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改模板管理互动教学'''
    print "修改中心设备信息：{0}".format(kwargs['name'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"模板管理").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchinteractteach']").clear()
        driver.find_element_by_xpath("//input[@id='searchinteractteach']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        driver.find_element_by_id("updinterteach").click()
        sleep(1)
        driver.find_element_by_css_selector("#interactteachupdate #formrole #name").clear()
        driver.find_element_by_css_selector("#interactteachupdate #formrole #name").send_keys(kwargs['name'])

        # click 确定
        driver.find_element_by_id("updateinteractteach").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    driver.close()
    driver.quit()
    driver = None

'''修改单条模板管理精品课堂数据'''
excellentClassroomData = [{'name': u'720PP','searchName':u''}]
def update_ExcellentClassroom(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改模板管理精品课堂'''
    print "修改中心设备精品课堂信息：{0}".format(kwargs['name'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"模板管理").click()
        sleep(1)
        driver.find_element_by_xpath("(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchexcellentclassroom']").clear()
        driver.find_element_by_xpath("//input[@id='searchexcellentclassroom']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='searchs']").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@id='updinterteach'])[3]").click()
        sleep(0.5)
        driver.find_element_by_css_selector("#excellentclassupdate #formrole #name").clear()
        driver.find_element_by_css_selector("#excellentclassupdate #formrole #name").send_keys(kwargs['name'])

        # click 确定
        driver.find_element_by_id("updateexcellentclass").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    driver.close()
    driver.quit()
    driver = None


'''修改单条模板管理精品课堂数据'''
excellentClassroomData = [{'name': u'720PP','searchName':u'互动课模板'}]
def update_ExcellentClassroom(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改模板管理精品课堂'''
    print "修改中心设备精品课堂信息：{0}".format(kwargs['name'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"模板管理").click()
        sleep(1)
        driver.find_element_by_xpath("(//a[contains(text(),'精品课堂')])[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='searchexcellentclassroom']").clear()
        driver.find_element_by_xpath("//input[@id='searchexcellentclassroom']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='searchs']").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@id='updinterteach'])[2]").click()
        sleep(0.5)
        driver.find_element_by_css_selector("#excellentclassupdate #formrole #name").clear()
        driver.find_element_by_css_selector("#excellentclassupdate #formrole #name").send_keys(kwargs['name'])

        # click 确定
        driver.find_element_by_id("updateexcellentclass").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    driver.close()
    driver.quit()
    driver = None

'''修改单条模板管理视频会议数据'''
VideoConferencingData = [{'name': u'720PP','searchName':u'会议'}]
def update_VideoConferencing(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改模板管理视频会议'''
    print "修改中心设备视频会议信息：{0}".format(kwargs['name'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"模板管理").click()
        sleep(1)
        driver.find_element_by_xpath("(//a[contains(text(),'视频会议')])[2]").click()
        sleep(1)
        driver.find_element_by_xpath("//input[@id='searchvideoconference']").clear()
        driver.find_element_by_xpath("//input[@id='searchvideoconference']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='searched']").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@id='updinterteach'])[3]").click()
        sleep(0.5)
        driver.find_element_by_css_selector("#videoconferenceupdate #formrole #name").clear()
        driver.find_element_by_css_selector("#videoconferenceupdate #formrole #name").send_keys(kwargs['name'])

        # click 确定
        driver.find_element_by_id("updatevideoconference").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    # driver.close()
    # driver.quit()
    # driver = None

'''修改单条模板管理主讲下课数据'''
theClassData = [{'name': u'下课模板测试数据','searchName':u''}]
def update_TheClass(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改模板管理主讲下课'''
    print "修改主讲下课信息：{0}".format(kwargs['name'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"模板管理").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'主讲下课')]").click()
        sleep(1)

        # input search tontent
        driver.find_element_by_xpath("//input[@id='searchlectureclass']").clear()
        driver.find_element_by_xpath("//input[@id='searchlectureclass']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search_lec']").click()
        sleep(0.5)
        driver.find_element_by_xpath("//table[@id='lectureclasstable']/tbody/tr/td[4]/button[2]").click()
        driver.find_element_by_css_selector("#lectureclassupdate #formrole #name").clear()
        driver.find_element_by_css_selector("#lectureclassupdate #formrole #name").send_keys(kwargs['name'])

        # click 确定
        driver.find_element_by_id("updatelectureclass").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    driver.close()
    driver.quit()
    driver = None

'''修改单条模板管理主讲听课下课'''
classOverData = [{'name': u'下课模板测试数据','searchName':''}]
def update_ClassOver(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改模板管理听课下课'''
    print "修改听课下课信息：{0}".format(kwargs['name'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"模板管理").click()
        sleep(1)
        driver.find_element_by_xpath("//a[contains(text(),'听课下课')]").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchlisteningclass']").clear()
        driver.find_element_by_xpath("//input[@id='searchlisteningclass']").send_keys(kwargs['searchName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search_lic']").click()
        sleep(0.5)
        driver.find_element_by_xpath("(//button[@id='updinterteach'])[5]").click()
        sleep(1)
        driver.find_element_by_css_selector("#lectureclassupdate #formrole #basicfact #name").clear()
        driver.find_element_by_css_selector("#lectureclassupdate #formrole #basicfact #name").send_keys(kwargs['name'])

        # click 确定
        driver.find_element_by_id("updatelectureclass").click()
        sleep(1)
        print "add {} success.".format(kwargs['name'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['name']
    driver.close()
    driver.quit()
    driver = None

'''修改单条邮箱服务管理'''
smtpData = [{'smtp': u'smtp.163.com','fromName':'519484955@qq.com','password':'111111'}]
def update_Smtp(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改邮箱服务管理'''
    print "修改邮箱服务管理：{0},{1},{2}".format(kwargs['password'],kwargs['fromName'],kwargs['password'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"配置管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"邮箱服务管理").click()
        sleep(1)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(1)
        driver.find_element_by_css_selector("#modal #smtp").clear()
        driver.find_element_by_css_selector("#modal #smtp").send_keys(kwargs['smtp'])

        driver.find_element_by_css_selector("#modal #fromName").clear()
        driver.find_element_by_css_selector("#modal #fromName").send_keys(kwargs['fromName'])

        driver.find_element_by_css_selector("#modal #password").clear()
        driver.find_element_by_css_selector("#modal #password").send_keys(kwargs['password'])

        # click 确定
        driver.find_element_by_id("determine").click()
        sleep(1)
        print "add {} success.".format(kwargs['smtp'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['smtp']
    driver.close()
    driver.quit()
    driver = None

'''修改单条互动教学'''
lessonData = [{'lessonName': u'测试课表','searchName':u''}]
def update_Lesson(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改互动教学'''
    print "修改互动教学：{0}".format(kwargs['lessonName'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"课堂管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"互动教学").click()
        sleep(1)

        sleep(0.5)
        driver.find_element_by_xpath("//td[7]/button").click()
        sleep(1)
        driver.find_element_by_id("lessonName").clear()
        driver.find_element_by_id("lessonName").send_keys(kwargs['lessonName'])

        # click 确定
        driver.find_element_by_id("saveButtonByAll").click()
        sleep(1)
        print "add {} success.".format(kwargs['lessonName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['lessonName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条精品课堂'''
goodsClassData = [{'lessonName': u'测试课表'}]
def update_GoodsClass(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改精品课堂'''
    print "修改精品课堂：{0}".format(kwargs['lessonName'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"课堂管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"精品课堂").click()
        sleep(1)
        driver.find_element_by_id("modify_inter_button").click()
        sleep(1)
        driver.find_element_by_id("lessonName").clear()
        driver.find_element_by_id("lessonName").send_keys(kwargs['lessonName'])

        # click 确定
        driver.find_element_by_id("saveButtonByAll").click()
        sleep(1)
        print "add {} success.".format(kwargs['lessonName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['lessonName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条视频会议'''
videoConferenceData = [{'meetingName': u'会议名称测试','confName':u'会议别名测试','meeting_password':'111111'}]
def update_VideoConference(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改视频会议'''
    print "修改视频会议：{0}".format(kwargs['meetingName'],kwargs['confName'],kwargs['meeting_password'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"课堂管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"视频会议").click()
        sleep(1)
        driver.find_element_by_id("modify_inter_button").click()
        sleep(1)
        driver.find_element_by_id("meetingName").clear()
        driver.find_element_by_id("meetingName").send_keys(kwargs['meetingName'])

        driver.find_element_by_id("confName").clear()
        driver.find_element_by_id("confName").send_keys(kwargs['confName'])

        driver.find_element_by_id("meeting_password").clear()
        driver.find_element_by_id("meeting_password").send_keys(kwargs['meeting_password'])

        # click 确定
        driver.find_element_by_id("save_click").click()
        sleep(1)
        print "add {} success.".format(kwargs['meetingName'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['meetingName']
    driver.close()
    driver.quit()
    driver = None

'''修改单条视频管理'''
videoManagementData = [{'title': u'测试标题','remark':u'描述测试'}]
def update_VideoManagement(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改视频管理'''
    print "修改视频管理：{0}{1}".format(kwargs['title'],kwargs['remark'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"内容管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"视频管理").click()
        sleep(1)
        driver.find_element_by_xpath("//td[11]/button").click()
        sleep(1)
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(kwargs['title'])

        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(kwargs['remark'])

        # click 确定
        driver.find_element_by_id("modeeditsure").click()
        sleep(1)
        print "add {} success.".format(kwargs['title'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['title']
    driver.close()
    driver.quit()
    driver = None

'''修改单条文档管理'''
documentManagementData = [{'title': u'测试标题','remark':u'描述测试'}]
def update_DocumentManagement(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改文档管理'''
    print "修改文档管理：{0}{1}".format(kwargs['title'],kwargs['remark'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"内容管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"文档管理").click()
        sleep(1)
        driver.find_element_by_xpath("//td[9]/button").click()
        sleep(1)
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(kwargs['title'])

        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(kwargs['remark'])

        # click 确定
        driver.find_element_by_id("modeeditsure").click()
        sleep(1)
        print "add {} success.".format(kwargs['title'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['title']
    driver.close()
    driver.quit()
    driver = None

'''修改单条微课管理'''
smallClassManagemenData = [{'title': u'测试标题','remark':u'描述测试'}]
def update_SmallClassManagement(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''修改微课管理'''
    print "修改微课管理：{0}{1}".format(kwargs['title'],kwargs['remark'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"内容管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"微课管理").click()
        sleep(1)
        driver.find_element_by_xpath("//td[10]/button").click()
        sleep(1)
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(kwargs['title'])

        driver.find_element_by_id("remark").clear()
        driver.find_element_by_id("remark").send_keys(kwargs['remark'])

        # click 确定
        driver.find_element_by_id("modeeditsure").click()
        sleep(1)
        print "add {} success.".format(kwargs['title'])
    except Exception as e:
        print e
        print "修改：%s 失败。" % kwargs['title']
    driver.close()
    driver.quit()
    driver = None


if __name__ == "__main__":
    # chrome_driver = os.path.abspath(r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
    # os.environ["webdriver.chrome.driver"] = chrome_driver
    driver = webdriver.Chrome()
    user_login(driver,**loginInfo)
#     for itms in usersdata:
#         update_User(driver,**itms)
    for itms in modifysubjectsGroup:
        update_subjectGrp(driver,**itms)
#     for itms in schoolManagementData:
#         update_DeviceManagement(driver,**itms)
#     for itms in schoolSchoolClassroomData:
#         update_SchoolClassroom(driver,**itms)
#     for itms in GroupData:
#         update_GroupManagement(driver,**itms)
#     for itms in GroupData:
#         update_GroupManagement(driver,**itms)
#     for itms in subjectsData:
#         update_Subjects(driver,**itms)
#     for itms in chapterData:
#         update_Chapter(driver,**itms)
#     for itms in sectionData:
#         update_Section(driver,**itms)
#     for itms in knowledgeData:
#         update_Knowledge(driver,**itms)
#     for itms in equipmentData:
#         update_Equipment(driver,**itms)
#     for itms in interactiveTeachingData:
#         update_InteractiveTeaching(driver,**itms)
#     for itms in middlewareData:
#         update_Middleware(driver,**itms)
#     for itms in excellentClassroomData:
#         update_ExcellentClassroom(driver,**itms)
#     for itms in VideoConferencingData:
#         update_VideoConferencing(driver,**itms)
#     for itms in theClassData:
#         update_TheClass(driver,**itms)
#     for itms in classOverData:
#         update_ClassOver(driver,**itms)
#     for itms in smtpData:
#         update_Smtp(driver,**itms)
#     for itms in lessonData:
#         update_Lesson(driver,**itms)
#     for itms in goodsClassData:
#         update_GoodsClass(driver,**itms)
#     for itms in videoConferenceData:
#         update_VideoConference(driver,**itms)

