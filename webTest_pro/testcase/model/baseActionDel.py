# coding=utf-8
import sys
from time import sleep

from selenium import webdriver

from _env import addPaths

addPaths('.')
from common.init import loginInfo

reload(sys)
sys.setdefaultencoding("utf-8")



def del_school(driver, **kwargs):
    '''删除学校'''
    print "开始删除一所学校..."

    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()
    sleep(0.5)
    driver.find_element_by_id("condition").click()
    driver.find_element_by_id("condition").send_keys(kwargs['schoolName'])
    driver.find_element_by_id("searchbtn").click()
    sleep(0.5)
    valuesText=driver.find_element_by_css_selector("#schooltab > tbody > tr > td").text
    if valuesText!="无数据" :
        # click del button
        driver.find_element_by_xpath("//button[@id='delsc']").click()
        # click ok button
        driver.find_element_by_css_selector("a.layui-layer-btn0").click()
        sleep(1)
        print "删除一所学校成功。"
    else :
        print "没有找到学校数据。"


def del_classroom(driver):
    print "开始删除一间教室..."
    driver.refresh()
    sleep(0.5)
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"学校管理").click()
    driver.find_element_by_link_text(u"教室列表").click()
    sleep(0.5)
    # click del button
    driver.find_element_by_xpath("//button[@id='delcla']").click()
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    print "删除一间教室成功。"

def del_tenants(driver,**kwargs):
    print "开始删除一个租户..."
    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"租户管理").click()
    driver.find_element_by_xpath("//*[@id='condition']").clear()
    driver.find_element_by_xpath("//*[@id='condition']").send_keys(kwargs['searchName'])
    driver.find_element_by_xpath("//*[@id='searchbtn']").click()

    driver.find_element_by_xpath("//button[@id='delten']").click()
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    print "删除一个租户成功。"


def del_schoolgroup(driver):
    print "开始删除一组科目组..."
    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"组管理").click()
    sleep(0.5)
    # click del button
    driver.find_element_by_xpath("//button[@id='delsg']").click()
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    print "删除一组科目组成功。"


searchsubjectGrps = [{'groupName': u'计算机'},
                     {'groupName': u'计算机1'}]


def del_subjectGrp(driver, **kwargs):
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
    # click del button
    driver.find_element_by_xpath("//button[@id='delsg']").click()
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)

    print "删除一组科目组成功。"
    # print "search {} success.".format(kwargs['groupName'])


def del_user(driver):
    print "开始删除一个用户..."
    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"用户列表").click()
    sleep(0.5)
    # click del button
    driver.find_element_by_xpath("//*[@id='userlists']/tr/td[9]/button[3]").click()
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    print "删除一个用户成功。"


def del_interactgrp(driver):
    # para:grpName,schoolgrTypeId
    print "开始删除一个互动组..."
    # refresh main page
    driver.refresh()
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"互动组管理").click()
    # click del button
    driver.find_element_by_xpath("//button[@id='delsc']").click()
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    print "删除一个互动组成功。"


def del_role(driver):
    '''删除角色'''
    driver.refresh()
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"角色管理").click()
    sleep(0.5)
    # click del button tr[6] 第几个
    driver.find_element_by_xpath("//*[@id='dtrole']/tbody/tr[6]/td[5]/button[3]").click()
    sleep(0.5)
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    print "删除角色成功。"


def del_interactgrp(driver):
    '''删除教室组'''
    # refresh main page
    driver.refresh()
    # goto test page
    driver.find_element_by_link_text(u"系统管理").click()
    driver.find_element_by_link_text(u"互动组管理").click()
    sleep(0.5)
    # click add btn
    driver.find_element_by_xpath("//button[@id='delsc']").click()
    sleep(0.5)
    # click ok button
    driver.find_element_by_css_selector("a.layui-layer-btn0").click()
    sleep(1)
    print "删除教室组成功。"


subjects = [{'subjectName': u'书法', 'description': u'学习中国文化'},
            {'subjectName': u'计算机', 'description': u'计算机基础应用'}]


def del_subject(driver, **kwargs):
    # para:
    '''删除科目'''
    print "delete info:{0}".format(kwargs['subjectName'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"科目管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchsubject']").clear()
        driver.find_element_by_xpath("//input[@id='searchsubject']").send_keys(kwargs['subjectName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        # click del button
        driver.find_element_by_xpath("//button[@id='subjected']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        print "delete {} end.".format(kwargs['subjectName'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['subjectName'])


chapters = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章a', 'chapterCode': u'助记码1'},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterName': u'第一章b', 'chapterCode': u'助记码1'}]


def del_chapter(driver, **kwargs):
    # para:
    '''删除章'''
    print "delete info:{0},{1}".format(kwargs['subjectid'], kwargs['chapterName'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"基础数据").click()
        driver.find_element_by_link_text(u"章管理").click()
        sleep(1)

        driver.find_element_by_xpath("//input[@id='searchchapter']").clear()
        driver.find_element_by_xpath("//input[@id='searchchapter']").send_keys(kwargs['chapterName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='search']").click()
        sleep(1)
        # click del button
        driver.find_element_by_xpath("//button[@id='chaptered']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        print "delete info:{0},{1} end".format(kwargs['subjectid'], kwargs['chapterName'])

    except Exception as e:
        print e
        print "delete {0},{1} failed.".format(kwargs['subjectid'], kwargs['chapterName'])


sections = [{'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': u"数学第二章", 'sectionName': u"sx第一节", 'sectionCode': u"第一节zjm"},
            {'gradeid': u"二年级", 'subjectid': u"数学", 'chapterid': u"数学第二章", 'sectionName': u"sx第二节", 'sectionCode': u"第二节zjm"}]


def del_section(driver, **kwargs):
    # para:
    '''添加节'''
    print "delete info:{0},{1},{2},{3},{4}".format(kwargs['gradeid'], kwargs['subjectid'], kwargs['chapterid'], kwargs['sectionName'], kwargs['sectionCode'])
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
        # click del button
        driver.find_element_by_xpath("//button[@id='sectioned']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['sectionName'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['sectionName'])

knowledges = [{'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'语文第一章', 'sectionid': u"第一节", 'knowledgeName': u"双细胞", 'knowledgeCode': u"双细胞1"},
              {'gradeid': u'一年级/小学', 'subjectid': u'语文', 'chapterid': u'语文第一章', 'sectionid': u"第一节", 'knowledgeName': u"多细胞", 'knowledgeCode': u"多细胞1"}]

def del_knowledge(driver, **kwargs): # para:
    '''删除知识点'''
    print "delete info:{0},{1}".format(kwargs['knowledgeName'], kwargs['subjectid'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("//button[@id='knowledged']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['knowledgeName'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['knowledgeName'])


MCUequipments = [{'equipmentName': '85mcu', 'equipIpAddr': '10.1.0.85', 'mcu_port': '80', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'},
                 {'equipmentName': '95mcu', 'equipIpAddr': '10.1.0.95', 'mcu_port': '10000', 'mcuLoginName': 'POLYCOM', 'mcuPasswd': 'POLYCOM'}]


def del_MCUequipment(driver, **kwargs):
    # para:equipmentName，equipIpAddr，mcu_port，mcuLoginName，mcuPasswd
    '''添加mcu'''
    print "delete info:{0},{1},{2},{3}".format(kwargs['equipmentName'], kwargs['equipIpAddr'], kwargs['mcuLoginName'], kwargs['mcuPasswd'])
    # refresh main page
    try:
        driver.refresh()

        # goto test page
        driver.find_element_by_link_text(u"设备管理").click()
        driver.find_element_by_link_text(u"中心设备").click()
        sleep(1)
        # input search tontent
        driver.find_element_by_xpath("//input[@id='mcuNmCondition']").clear()
        driver.find_element_by_xpath("//input[@id='mcuNmCondition']").send_keys(kwargs['equipmentName'])
        # click search button
        driver.find_element_by_xpath("//button[@id='btnMcuNm']").click()
        sleep(1)
        # click del button
        driver.find_element_by_xpath("//button[@id='current']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['equipmentName'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['equipmentName'])

interacts = [{'host': '10.1.0.2', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'},
             {'host': '10.1.0.3', 'port': '80', 'username': 'administrator', 'password': 'xungejiaoyu'}]


def del_interact(driver, **kwargs):
    # para:host,port,username,password
    '''添加消息中间件'''
    print "delete info:{0},{1},{2},{3}".format(kwargs['host'], kwargs['port'], kwargs['username'], kwargs['password'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("//button[@id='middlewrdel']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['host'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['host'])

hdk_lesson_cfgs = [{'name': u'互动课模板'}, {'name': u'互动课模板480p'}]
jp_lesson_cfgs = [{'name': u'精品课'}, {'name': u'精品课480p'}]
conference_cfgs = [{'name': u'会议'}, {'name': u'会议480p'}]
speaker_lesson_cfgs = [{'name': u'主讲下课'}, {'name': u'主讲下课_1'}]
listener_lesson_cfgs = [{'name': u'听讲下课'}, {'name': u'听讲下课_1'}]

def del_cfg_hdks(driver, **kwargs):
    # para:name
    '''删除互动教学模板'''
    print "delete info:{0}".format(kwargs['name'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("//button[@id='delinterteach']").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['name'])


def del_cfg_jpks(driver, **kwargs):
    # para:name
    '''删除精品课堂模板'''
    print "delete info:{0}".format(kwargs['name'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("(//button[@id='delinterteach'])[2]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['name'])



def del_cfg_conferences(driver, **kwargs):
    # para:name
    '''删除视频会议模板'''
    print "delete info:{0}".format(kwargs['name'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("(//button[@id='delinterteach'])[3]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['name'])


def del_cfg_listener_lessons(driver, **kwargs):
    # para:name
    '''删除听课下课模板'''
    print "delete info:{0}".format(kwargs['name'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("(//button[@id='delinterteach'])[5]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['name'])


def del_cfg_speaker_lessons(driver, **kwargs):
    # para:name
    '''删除主讲下课模板'''
    print "delete info:{0}".format(kwargs['name'])
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
        sleep(1)
        # click del button
        driver.find_element_by_xpath("(//button[@id='delinterteach'])[4]").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"确定").click()
        sleep(0.5)
        print "delete {} end.".format(kwargs['name'])
    except Exception as e:
        print e
        print "delete {} failed.".format(kwargs['name'])


emails = [{'smtp': 'smtp.162.com', 'fromName': 'haosea@qq.com', 'password': '111111'},
          {'smtp': 'smtp.163.com', 'fromName': 'haosea1@qq.com', 'password': '111111'}]


def del_email(driver):
    # para:
    '''删除邮箱服务'''
    # refresh main page
    try:
        driver.refresh()
        # goto test page
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"邮箱服务管理").click()
        sleep(1)

        # click del btn
        driver.find_element_by_xpath("//button[@id='current']").click()
        sleep(1)
        # click Ok btn
        driver.find_element_by_link_text(u"确定").click()
        sleep(1)
        print " delete email end."
    except Exception as e:
        print e
        print "delete email failed."


def del_excellentClass(driver):
    """
      Func desc
      Args:
      Usage:
    """
    print "删除精品课。"
    try:
        driver.refresh()
        # goto target page
        driver.find_element_by_link_text(u"课堂管理").click()
        driver.find_element_by_link_text(u"精品课堂").click()
        sleep(1)
        # select del target
        driver.find_element_by_xpath("//button[@id='delete_intr_button']").click()
        # driver.find_element_by_xpath("//button[@id='delete_intr_button']").click()
        sleep(2)
        # click Ok btn
        driver.find_element_by_link_text(u"确定").click()
        # driver.find_element_by_link_text(u"取消").click()
        # sleep(2)
        print "删除精品课成功。"
    except Exception as e:
        print "删除精品课失败！"

def del_hdk(driver):
    '''删除互动课'''
    driver.refresh()
    driver.find_element_by_link_text(u"课堂管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"互动教学").click()
    sleep(0.5)
    driver.find_element_by_xpath("//button[@id='delete_intr_button']").click()
    sleep(1)
    driver.find_element_by_link_text(u"确定").click()
    sleep(2)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    user_login(driver, **loginInfo)
    del_excellentClass(driver)
