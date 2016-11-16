# coding: utf-8
import os
import sys
from time import sleep

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import SendKeys
import win32con
import win32api

from _env import addPaths
addPaths(".")

from common.init import loginInfo
from model.baseActionAdd import user_login

reload(sys)
sys.setdefaultencoding("utf-8")
'''添加节目数据'''
videoData = [{
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频mp4)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '001.mp4',
    'sleepTime': '45'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频asf)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '002.asf',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频3gp)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '003.3gp',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频mpg)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '004.mpg',
    'sleepTime': '15'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频mov)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '005.mov',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频wmv)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '006.wmv',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频flv)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '007.flv',
    'sleepTime': '45'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频avi)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'文件名',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '008.avi',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档docx)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '001.docx',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档pptx)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '002.pptx',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档ppt)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '003.ppt',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档xlsx)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '004.xlsx',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档doc)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '005.doc',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档txt)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '006.txt',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档pdf)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '007.pdf',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档xls)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'文件名1',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '008.xls',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(图片)',
    'addFileDesc': u'测试备注信息2',
    'videoType': u'图片',
    'fileName': u'文件名2',
    'uploadType': 'pictrue',
    'disk': 'Z:\\testResource',
    'fileNames': '002.PNG',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(水印)',
    'addFileDesc': u'测试备注信息3',
    'videoType': u'水印',
    'fileName': u'文件名3',
    'uploadType': 'watermark',
    'disk': 'Z:\\testResource',
    'fileNames': '002.PNG',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(资料)',
    'addFileDesc': u'测试备注信息4',
    'videoType': u'资料',
    'fileName': u'文件名4',
    'uploadType': 'data',
    'disk': 'Z:\\testResource',
    'fileNames': '002.PNG',
    'sleepTime': '20'
}]


def add_UploadVideo(driver, **kwargs):
    print "添加节目信息：{0}，{1}，{2}，{3}，{4}".format(
        kwargs['addTypeSelect'], kwargs['addFileN'], kwargs['addFileDesc'],
        kwargs['videoType'], kwargs['fileName'])

    driver.refresh()
    driver.find_element_by_link_text(u"文件管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"文件目录").click()
    sleep(1)
    driver.find_element_by_xpath("//div/div[2]/button").click()
    sleep(1)
    # 节目类型
    Select(driver.find_element_by_id(
        "addTypeSelect")).select_by_visible_text(kwargs["addTypeSelect"])
    sleep(1)
    # 节目名:
    driver.find_element_by_id("addFileN").clear()
    driver.find_element_by_id("addFileN").send_keys(kwargs["addFileN"])
    # 备注信息:
    driver.find_element_by_id("addFileDesc").clear()
    driver.find_element_by_id("addFileDesc").send_keys(kwargs[
        "addFileDesc"])
    # 确定按钮
    if kwargs["addFileN"] == "测试节目名(视频mp4)":
        driver.find_element_by_id("makeSureProgram").click()
    driver.find_element_by_id("makeSureProgram").click()
    sleep(1)
    # ########################
    Select(driver.find_element_by_id(
        "pTypeSelect")).select_by_visible_text(kwargs["addTypeSelect"])
    sleep(1)
    # 搜索文件名
    driver.find_element_by_id("searchT").clear()
    driver.find_element_by_id("searchT").send_keys(kwargs["addFileN"])
    # 搜索按钮
    driver.find_element_by_xpath("//div/a/i").click()
    # 点击搜索出来的结果
    driver.find_element_by_xpath("//li/span").click()
    # 点击上传文件
    sleep(5)
    driver.find_element_by_xpath(
        "//button[@onclick='upInfoDetail()']").click()
    sleep(1)
    # #文件类型
    Select(driver.find_element_by_xpath(
        "//div[2]/select")).select_by_visible_text(kwargs["videoType"])
    # 文件名
    driver.find_element_by_xpath("//div[2]/input").clear()
    driver.find_element_by_xpath("//div[2]/input").send_keys(kwargs[
        "fileName"])
    # 描述
    driver.find_element_by_xpath("//div[2]/textarea").clear()
    driver.find_element_by_xpath("//div[2]/textarea").send_keys(kwargs[
        "addFileDesc"])
    sleep(2)
    if kwargs["uploadType"] == "video" or kwargs[
            "uploadType"] == "doc" or kwargs["uploadType"] == "data":
        driver.find_element_by_xpath("//a[contains(text(),'选择文件')]").click(
        )
    elif kwargs["uploadType"] == "pictrue" or kwargs[
            "uploadType"] == "watermark":
        driver.find_element_by_id("file").click()
    sleep(2)
    ################################点击文件操作######################################
    # ctrl+L
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(76, 0, 0, 0)  # L键位码是73
    win32api.keybd_event(76, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(kwargs["disk"])  # 输入磁盘
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    sleep(4)
    # ALT+N
    win32api.keybd_event(18, 0, 0, 0)  # ALT键位码是18
    win32api.keybd_event(78, 0, 0, 0)  # N键位码是78
    win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(kwargs["fileNames"])  # 发送文件地址
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    ################################点击文件操作########################################
    sleep(4)
    # m.click(984L, 618L)
    # 如果是图片   就需要点击截取  不是图片不需要
    if kwargs["uploadType"] == "pictrue" or kwargs[
            "uploadType"] == "watermark":
        driver.find_element_by_id("clipBtn").click()
    # 确定按钮

    # 上传文件确定按钮
    driver.find_element_by_id("upDetail").click()
    print kwargs["sleepTime"]
    sleep(float(kwargs["sleepTime"]))



'''添加视频任务'''
videoTaskData = [{
    'taskName': u'测试任务名1',
    'taskRemark': u'测试描述',
    'pTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频)',
    'fileName': u'测试文件名',
    'fileType': u'视频',
    'fileFormat': u'mp4',
    'FileDesc': u'测试描述',
    'clarity': '720p',
    'startTiem': '00:00:01',
    'endTiem': '00:00:30'
}]


def add_videoTask(driver, **kwargs):
    print "添加节目信息：{0}，{1}，{2}，{3}".format(
        kwargs['taskName'], kwargs['taskRemark'], kwargs['pTypeSelect'],
        kwargs['addFileN'])
    try:
        driver.refresh()
        driver.find_element_by_link_text(u"文件管理").click()
        sleep(0.5)
        driver.find_element_by_link_text(u"视频任务").click()
        sleep(2)
        # 任务名
        driver.find_element_by_id("taskName").clear()
        driver.find_element_by_id("taskName").send_keys(kwargs["taskName"])
        # 描述
        driver.find_element_by_id("taskRemark").clear()
        driver.find_element_by_id("taskRemark").send_keys(kwargs["taskRemark"])
        # 节目类型
        Select(driver.find_element_by_id(
            "pTypeSelect")).select_by_visible_text(kwargs["pTypeSelect"])
        # 源文件添加按钮
        driver.find_element_by_xpath("//button[@onclick='addTask();']").click()
        sleep(1)
        # 搜索框
        driver.find_element_by_id("searchT").clear()
        driver.find_element_by_id("searchT").send_keys(kwargs["addFileN"])
        sleep(1)
        # 点击搜索
        driver.find_element_by_xpath(
            "//button[@onclick='querySrcProgram();']").click()
        # 回车键 是13
        # win32api.keybd_event(13,0,0,0)
        # win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
        # 点击左侧的菜单
        driver.find_element_by_xpath("//div[3]/ul/li").click()
        # 展开后选择第一个
        driver.find_element_by_xpath(
            "//div[@id='showTreeList']/table/tbody/tr/td[2]").click()
        # 选择第一个视频
        driver.find_element_by_xpath(
            "//div[@id='detail0']/table/tbody/tr/td[4]").click()
        # 选择视频后，点击确定按钮
        driver.find_element_by_xpath(
            "//div/div[2]/div/div/form/div/div/button").click()

        # 目标文件  添加按钮
        driver.find_element_by_xpath(
            "//button[@onclick='addNewFile(1,1);']").click()
        # 节目选择
        driver.find_element_by_xpath("//div/div/div[2]/div/button").click()
        driver.find_element_by_xpath("//div[2]/div/div/div/input").clear()
        driver.find_element_by_xpath("//div[2]/div/div/div/input").send_keys(
            kwargs["addFileN"])
        driver.find_element_by_xpath("//div/div/ul/li[7]/a/span").click()
        # 文件名
        driver.find_element_by_xpath("//div[3]/input").clear()
        driver.find_element_by_xpath("//div[3]/input").send_keys(kwargs[
            "addFileN"])
        # 文件类型
        Select(driver.find_element_by_xpath(
            "//div[4]/select")).select_by_visible_text(kwargs["fileType"])
        # 文件格式
        Select(
            driver.find_element_by_xpath(
                "//div[@id='addFile1']/div/div[2]/div[2]/select")
        ).select_by_visible_text(kwargs["fileFormat"])
        # 描述
        driver.find_element_by_xpath(
            "//div[@id='addFile1']/div/div[3]/div[2]/textarea").clear()
        driver.find_element_by_xpath(
            "//div[@id='addFile1']/div/div[3]/div[2]/textarea").send_keys(
                kwargs["fileName"])
        # 清晰度
        driver.find_element_by_xpath("//input[@name='" + kwargs["clarity"] +
                                     "']").click()
        # 开始时间
        driver.find_element_by_xpath("//div[2]/div[3]/input").clear()
        driver.find_element_by_xpath("//div[2]/div[3]/input").send_keys(kwargs[
            "startTiem"])
        # 结束时间
        driver.find_element_by_xpath("//div[4]/input").clear()
        driver.find_element_by_xpath("//div[4]/input").send_keys(kwargs[
            "endTiem"])
        # 结束时间
        driver.find_element_by_xpath("//div[3]/div[2]/textarea").clear()
        driver.find_element_by_xpath("//div[3]/div[2]/textarea").send_keys(
            kwargs["FileDesc"])
        # 上传文件按钮
        # driver.find_element_by_xpath("//a[contains(text(),'选择文件')]").click()
        # 确定按钮
        driver.find_element_by_xpath("//div[2]/div/div/button[2]").click()
        # 弹框的确定按钮
        driver.find_element_by_xpath("//a[contains(text(),'确定')]").click()
    except Exception as e:
        print e
    # driver.close()
    # driver.quit()
    # driver = None


'''查询任务列表'''
teskListData = [{'taskName': u'测试任务名1'}]


def select_teskList(driver, **kwargs):
    print "查询任务列表：{0}".format(kwargs['taskName'])
    try:
        count = 0
        while (count < 20):
            results = cycle_teskList(driver, kwargs["taskName"])
            print results
            if results != "完成":
                cycle_teskList(driver, kwargs["taskName"])
            else:
                print u"转码成功！"
                return
            count = count + 1
    except Exception as e:
        print e
    # driver.close()
    # driver.quit()
    # driver = None


def cycle_teskList(driver, taskName):
    driver.refresh()
    sleep(8)
    driver.find_element_by_link_text(u"文件管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"任务列表").click()
    sleep(1)
    # 根据任务名查询
    driver.find_element_by_id("TASK_NAME").clear()
    driver.find_element_by_id("TASK_NAME").send_keys(taskName)
    # 点击搜索
    driver.find_element_by_xpath("//div/div[2]/button").click()
    results = driver.find_element_by_xpath(
        "//tbody[@id='taskView']/tr/td[8]").text
    return results


# 删除文件目录    没做    好多发布的视频删除不了


def delete_UploadVideo(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"文件管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"文件目录").click()
    sleep(1)
    Select(driver.find_element_by_id("pTypeSelect")).select_by_visible_text(
        kwargs["addTypeSelect"])
    # 搜索文件名
    driver.find_element_by_id("searchT").clear()
    driver.find_element_by_id("searchT").send_keys(kwargs["addFileN"])
    # 搜索按钮
    driver.find_element_by_xpath("//div/a/i").click()
    program = driver.find_element_by_id("program").text
    print program


# def user_login(driver, **kwargs):
#     """
#     Func desc
#     Args:
#     -
#     Usage:
#
#     """
#     print "loginfo:\nuser:{0}，platform:{1}".format(kwargs['username'],
#                                                    kwargs['platformname'])
#     # open url
#     driver.get('http://10.1.0.57' + "/middleclient/index.do")
#     driver.maximize_window()
#     driver.refresh()
#     # select platform and login
#     Select(driver.find_element_by_id("platform")).select_by_visible_text(
#         kwargs['platformname'])
#     driver.find_element_by_id('s_username').clear()
#     driver.find_element_by_id('s_username').send_keys(kwargs['username'])
#     driver.find_element_by_id('s_password').clear()
#     driver.find_element_by_id('s_password').send_keys('111111')
#     # click login btn
#     driver.find_element_by_name('submit').click()
#     sleep(0.5)


if __name__ == "__main__":
    driver = webdriver.Chrome()
    user_login(driver, **loginInfo)
    for i in range(1, 100):
        for itme in videoData:
            add_UploadVideo(driver, **itme)
        for itme in videoTaskData:
            add_videoTask(driver, **itme)
        for itme in teskListData:
            select_teskList(driver, **itme)
        driver.close()
        driver.quit()
        driver = None
    # dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
    # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    #
    # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
    # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
