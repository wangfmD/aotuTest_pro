# coding=utf-8
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from init import loginInfo
reload(sys)
sys.setdefaultencoding("utf-8")



def add_tenant(driver):
    '''添加租户'''

    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"租户管理").click()
    sleep(0.5)
    driver.find_element_by_css_selector("i.fa.fa-plus").click()
    sleep(0.5)
    driver.find_element_by_css_selector("#areaId > div.col-sm-9 > input.form-control").click()
    sleep(1)
    driver.find_element_by_xpath("//div[@id='treeview']/ul/li[17]").click()
    sleep(1)
    driver.find_element_by_css_selector("div.modal-content > div.text-center > button.btn.btn-success").click()
    sleep(1)
    driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#platmarkName > div.col-sm-9 > input.form-control").send_keys(u"河南教育局")
    driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").clear()
    driver.find_element_by_css_selector("#platmarkCode > div.col-sm-9 > input.form-control").send_keys("001")
    sleep(1)
    driver.find_element_by_id("submit").click()
    sleep(1)


def add_schools(driver, **kwargs):
    # para:schoolName,schoolType,schoolArea
    '''添加学校'''

    print "添加学校信息：{0}，{1}，{2}".format(kwargs['schoolName'], kwargs['schoolType'], kwargs['schoolArea'])

    try:
        driver.refresh()
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()

        # select area
        # driver.find_element_by_id("choosearea").click()
        # sleep(1)
        # driver.find_element_by_xpath("//div[@id='treeview']/ul/li[2]").click()
        # driver.find_element_by_css_selector("div.col-sm-9.text-center > #submit").click()
        sleep(1)
        # 添加学校btn
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
        # self.assertEqual(u"添加成功！", driver.find_element_by_css_selector(".layui-layer-content").text)
        sleep(2)
        print "添加：%s 成功。" % kwargs['schoolName']
    except Exception as e:
        print e
        print "添加：%s 失败。" % kwargs['schoolName']
    #
    # driver.find_element_by_link_text(u"学校管理").click()
    # driver.find_element_by_css_selector(u"a[title=\"添加教室\"] > span").click()
    # sleep(1)
    # driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").clear()
    # driver.find_element_by_css_selector("#className > div.col-sm-9 > input.form-control").send_keys(classroomname)
    # driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").clear()
    # driver.find_element_by_css_selector("#classAccNumber > div.col-sm-9 > input.form-control").send_keys(classaccnumber)
    # sleep(1)
    # driver.find_element_by_css_selector(
    #     "#classroommodal > div.modal-dialog > div.modal-content > form.form-horizontal > div.modal-body.row > div.form-group > div.col-sm-9 > #submit").click()
    # sleep(2)
    # driver.quit()

classrooms = [{'className': '31className', 'classAccNumber': '1'},
              {'className': '32className', 'classAccNumber': '1'}]


def add_classrooms(driver, **kwargs):
    # para:
    '''添加教室组'''
    print "add info:{0},{1}".format(kwargs['className'], kwargs['classAccNumber'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"系统管理").click()
        driver.find_element_by_link_text(u"学校管理").click()
        sleep(1)
        # click add btn
        driver.find_element_by_css_selector(u"a[title=\"添加教室\"] > span").click()
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
    '''添加一个终端'''
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
        sleep(1)
        print "add {} success.".format(kwargs['equipment_name'])
    except Exception as e:
        print e
        print "add {} failed.".format(kwargs['equipment_name'])

subjectsGroups = [{'groupName': u'计算机', 'groupCode': '001', 'description': u'计算机'},
                  {'groupName': u'计算机1', 'groupCode': '002', 'description': u'计算机'}]


def add_schoolgroups(driver, **kwargs):
    # para:
    '''添加教室组'''
    print "add info:{0},{1}".format(kwargs['groupName'], kwargs['groupCode'], kwargs['description'])
    # refresh main page
    driver.refresh()
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"组管理").click()
    sleep(1)
    # click add btn
    driver.find_element_by_xpath("//a[@id='addscgroup']").click()
    sleep(0.5)
    # operation
    driver.find_element_by_xpath("//*[@id='groupName']/div/input").clear()
    driver.find_element_by_xpath("//*[@id='groupName']/div/input").send_keys(kwargs['groupName'])
    driver.find_element_by_xpath("//*[@id='groupCode']/div/input").clear()
    driver.find_element_by_xpath("//*[@id='groupCode']/div/input").send_keys(kwargs['groupCode'])
    driver.find_element_by_xpath("//*[@id='description']/div/textarea").clear()
    driver.find_element_by_xpath("//*[@id='description']/div/textarea").send_keys(kwargs['description'])
    # click 确定
    driver.find_element_by_xpath("//button[@id='submit']").click()
    sleep(1)
    print "add {} success.".format(kwargs['groupName'])

    # print "add {} failed.".format(kwargs[''])


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

if __name__ == '__main__':
    driver = webdriver.Chrome()
    user_login(driver, **loginInfo)
    sleep(500)

