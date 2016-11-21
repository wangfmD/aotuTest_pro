# coding: utf-8
import os
import sys
from time import sleep
from _env import addPaths
addPaths(".")

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import SendKeys
import win32con
import win32api
import common.init as init



from common.init import loginInfo
from model.baseActionAdd import user_login

reload(sys)
sys.setdefaultencoding("utf-8")
'''添加节目数据'''
videoData = [
{
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频mp4)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'001.mp4',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '001.mp4',
    'sleepTime': '45'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频asf)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'002.asf',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '002.asf',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频3gp)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'003.3gp',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '003.3gp',
    'sleepTime': '10'
}, 
{
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频mpg)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'004.mpg',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '004.mpg',
    'sleepTime': '15'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频mov)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'005.mov',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '005.mov',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频wmv)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'006.wm',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '006.wmv',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频flv)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'007.flv',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '007.flv',
    'sleepTime': '45'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名(视频avi)',
    'addFileDesc': u'测试备注信息',
    'videoType': u'视频',
    'fileName': u'008.avi',
    'uploadType': 'video',
    'disk': 'Z:\\testResource\\py',
    'fileNames': '008.avi',
    'sleepTime': '10'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档docx)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'001.docx',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '001.docx',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档pptx)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'002.pptx',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '002.pptx',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档ppt)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'003.ppt',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '003.ppt',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档xlsx)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'004.xlsx',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '004.xlsx',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档doc)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'005.doc',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '005.doc',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档txt)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'006.tx',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '006.txt',
    'sleepTime': '20'
},{
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档txt)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'006zh.tx',
    'uploadType': 'doc',
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '006zh.txt',
    'sleepTime': '20'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名1(文档pdf)',
    'addFileDesc': u'测试备注信息1',
    'videoType': u'文档',
    'fileName': u'007.pdf',
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
    'fileName': u'banner01.png',
    'uploadType': 'pictrue',
    'disk': 'Z:\\testResource\\py\\pic',
    'fileNames': 'banner01.png',
    'sleepTime': '4'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(图片PNG)',
    'addFileDesc': u'测试备注信息2',
    'videoType': u'图片',
    'fileName': u'banner01.jpg',
    'uploadType': 'pictrue',
    'disk': 'Z:\\testResource\\py\\pic',
    'fileNames': 'banner01.jpg',
    'sleepTime': '4'
},{
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(图片PNG)',
    'addFileDesc': u'测试备注信息2',
    'videoType': u'图片',
    'fileName': u'banner03.jpg',
    'uploadType': 'pictrue',
    'disk': 'Z:\\testResource\\py\\pic',
    'fileNames': 'banner03.jpg',
    'sleepTime': '4'
},{
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(水印)',
    'addFileDesc': u'测试备注信息3',
    'videoType': u'水印',
    'fileName': u'文件名3',
    'uploadType': 'watermark',
    'disk': 'Z:\\testResource',
    'fileNames': '002.PNG',
    'sleepTime': '4'
}, {
    'addTypeSelect': u'公共资源库',
    'addFileN': u'测试节目名2(资料)',
    'addFileDesc': u'测试备注信息4',
    'videoType': u'资料',
    'fileName': u'文件名4',
    'uploadType': 'data',
    'disk': 'Z:\\testResource',
    'fileNames': '002.PNG',
    'sleepTime': '4'
}]


def add_UploadVideo(driver, **kwargs):
    print "添加节目信息：{0}，{1}，{2}，{3}，{4}".format(
        kwargs['addTypeSelect'], kwargs['addFileN'], kwargs['addFileDesc'],
        kwargs['videoType'], kwargs['fileName'])

    driver.refresh()
    driver.find_element_by_link_text(u"文件管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"任务列表").click()
    sleep(1)
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
    sleep(3)
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
    #文件上传方法
    file_upload(kwargs["disk"],kwargs["fileNames"])
    sleep(4)
    # m.click(984L, 618L)
    # 如果是图片   就需要点击截取  不是图片不需要
    if kwargs["uploadType"] == "pictrue" or kwargs[
            "uploadType"] == "watermark":
        driver.find_element_by_id("clipBtn").click()
    # 确定按钮
  
#    上传文件确定按钮
    driver.find_element_by_id("upDetail").click()
    sleep(float(kwargs["sleepTime"]))
     
    Select(driver.find_element_by_id(
        "pTypeSelect")).select_by_visible_text(kwargs["addTypeSelect"])
    sleep(1)
    # 搜索文件名
    driver.find_element_by_id("searchT").clear()
    driver.find_element_by_id("searchT").send_keys(kwargs["addFileN"])
    # 搜索按钮
    driver.find_element_by_xpath("//div/a/i").click()
    program = driver.find_element_by_id("program").text
    if program != "无数据" :
        # 点击搜索出来的结果
        driver.find_element_by_xpath("//li/span").click()
        
        driver.find_element_by_id("fileName").clear()
        driver.find_element_by_id("fileName").send_keys(kwargs["fileName"])
        
        driver.find_element_by_xpath("//div[2]/div/button").click()
        
        fileList = driver.find_element_by_css_selector("#fileList div").text
        if fileList!="此节目下未有文件明细信息！" :
            print kwargs['fileName']+"节目添加成功"
        else :
             print kwargs['fileName']+"节目添加失败"
    else :
        print kwargs['addFileN']+"新建节目失败"

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


'''添加流媒体地址管理'''
streamingData = [{'addName': u'19流媒体地址',"ipAdd":init.db_conf["hostadd"],"serverIps":init.streaming_media["serverIps"],"addType":u"内网"}]
def add_Streaming(driver, **kwargs):
    driver.refresh()
    driver.find_element_by_link_text(u"文件管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"流媒体地址管理").click()
    sleep(1)
    mbs_addlist = driver.find_element_by_css_selector("#mbs_addlist").text
    
    if mbs_addlist=="":
        #添加按钮
        driver.find_element_by_id("add_mbsadd_setting").click()
        sleep(1)
        driver.find_element_by_id("addName").clear()
        driver.find_element_by_id("addName").send_keys(kwargs["addName"])
        
        driver.find_element_by_id("ipAdd").clear()
        driver.find_element_by_id("ipAdd").send_keys(kwargs["ipAdd"])
         
        driver.find_element_by_id("serverIps").clear()
        driver.find_element_by_id("serverIps").send_keys(kwargs["serverIps"])
        Select(driver.find_element_by_id("addType")).select_by_visible_text(kwargs["addType"])
        
        driver.find_element_by_id("btnSaveMbsAdd").click()
        print "流媒体地址已经添加"
    else :
        print "流媒体地址已经存在"
        

'''添加节目数据'''
contntVideoData = [
{
    'disk': 'Z:\\testResource\\py',
    'fileNames': '001.mp4',
    'fileName': '001mp4',
    'sleepTime': '45',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '002.asf',
    'fileName': '002asf',
    'sleepTime': '20',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '003.3gp',
    'fileName': '0033gp',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, 
{
    'disk': 'Z:\\testResource\\py',
    'fileNames': '004.mpg',
    'fileName': '004mpg',
    'sleepTime': '15',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '005.mov',
    'fileName': '005mov',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '006.wmv',
    'fileName': '006wmv',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '007.flv',
    'fileName': '007flv',
    'sleepTime': '45',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '008.avi',
    'fileName': '008avi',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'视频管理'
}, 
{
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '001.docx',
    'fileName': '001docx',
    'sleepTime': '4',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '002.pptx',
    'fileName': '002pptx',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '003.ppt',
    'fileName': '003ppt',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '004.xlsx',
    'fileName': '004xlsx',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '005.doc',
    'fileName': '005doc',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '006.txt',
    'fileName': '006txt',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
},{
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '006zh.txt',
    'fileName': '006zhtxt',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '007.pdf',
    'fileName': '007pdf',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
}, {
    'disk': 'Z:\\testResource\\py\\wd',
    'fileNames': '008.xls',
    'fileName': '008xls',
    'sleepTime': '6',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'文档管理'
},
{
    'disk': 'Z:\\testResource\\py',
    'fileNames': '001.mp4',
    'fileName': '001mp4',
    'sleepTime': '45',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '002.asf',
    'fileName': '002asf',
    'sleepTime': '20',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '003.3gp',
    'fileName': '0033gp',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, 
{
    'disk': 'Z:\\testResource\\py',
    'fileNames': '004.mpg',
    'fileName': '004mpg',
    'sleepTime': '15',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '005.mov',
    'fileName': '005mov',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '006.wmv',
    'fileName': '006wmv',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '007.flv',
    'fileName': '007flv',
    'sleepTime': '45',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, {
    'disk': 'Z:\\testResource\\py',
    'fileNames': '008.avi',
    'fileName': '008avi',
    'sleepTime': '10',
    'gradetype':'小学',
    'gradename':'一年级',
    'subjectname':'音乐',
    'Schapter':'音乐第一章',
    'Ssection':'',
    'sknow':'',
    'remark':'测试描述',
    'type_click':'微课管理'
}, 
]

def add_ContntVideo(driver, **kwargs):
    print "添加节目信息：{0}，{1}，{2}，{3}，{4}".format(
        kwargs['disk'], kwargs['fileNames'], kwargs['sleepTime'],
        kwargs['gradetype'], kwargs['remark'])
    driver.refresh()
    driver.find_element_by_link_text(u"文件管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(u"任务列表").click()
    sleep(1)
    driver.find_element_by_link_text(u"内容管理").click()
    sleep(0.5)
    driver.find_element_by_link_text(kwargs["type_click"]).click()
    sleep(1)
    # 点击上传按钮
    driver.find_element_by_id("upRes").click()
    sleep(1)
    #  点击请选择..
    driver.find_element_by_id("swfu-placeholder").click()
    sleep(1)
    #文件上传方法
    file_upload(kwargs["disk"],kwargs["fileNames"])
    sleep(4)
    Select(driver.find_element_by_id("gradetype")).select_by_visible_text(
        kwargs["gradetype"])
    Select(driver.find_element_by_id("gradename")).select_by_visible_text(
        kwargs["gradename"])
    Select(driver.find_element_by_id("subjectname")).select_by_visible_text(
        kwargs["subjectname"])
    Select(driver.find_element_by_id("Schapter")).select_by_visible_text(
        kwargs["Schapter"])
#     Select(driver.find_element_by_id("Ssection")).select_by_visible_text(
#         kwargs["Ssection"])
#     Select(driver.find_element_by_id("sknow")).select_by_visible_text(
#         kwargs["sknow"])
    sleep(1)
    driver.find_element_by_id("title").clear()
    driver.find_element_by_id("title").send_keys(kwargs["fileName"])
    #确定按钮
    driver.find_element_by_css_selector(".submitFile").click()
    sleep(float(kwargs["sleepTime"]))
    driver.find_element_by_id("bysearchtext").clear()
    driver.find_element_by_id("bysearchtext").send_keys(kwargs["fileName"])
    driver.find_element_by_id("search_btn").click()
    sleep(2)
    videolist = driver.find_element_by_id("videolist").text
    print videolist
    if videolist !="":
        print kwargs["fileNames"]+"上传"+kwargs["type_click"]+"成功"
    else :
        print kwargs["fileNames"]+"上传"+kwargs["type_click"]+"失败"
        
    sleep(6)
#文件上传方法
def file_upload(disk,fileNames):
    sleep(1)
    ################################点击文件操作######################################
    #shift+alt
#     win32api.keybd_event(16, 0, 0, 0)  # shift
#     win32api.keybd_event(18, 0, 0, 0)  # L键位码是73
#     win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
#     win32api.keybd_event(16,0,win32con.KEYEVENTF_KEYUP,0)
#     sleep(2)
    # ctrl+L
    win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
    win32api.keybd_event(76, 0, 0, 0)  # L键位码是73
    win32api.keybd_event(76, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(disk)  # 输入磁盘
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    sleep(4)
    # ALT+N
    win32api.keybd_event(18, 0, 0, 0)  # ALT键位码是18
    win32api.keybd_event(78, 0, 0, 0)  # N键位码是78
    win32api.keybd_event(78, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
    SendKeys.SendKeys(fileNames)  # 发送文件地址
    SendKeys.SendKeys('{ENTER}')  # 发送回车键
    ################################点击文件操作########################################

if __name__ == "__main__":
    driver = webdriver.Chrome()
    user_login(driver,**loginInfo)
#     for itme in contntVideoData:
#         add_ContntVideo(driver, **itme)
#     for itme in videoData:
#         add_UploadVideo(driver, **itme)
#     for itme in streamingData:
#         add_Streaming(driver, **itme)
#     for i in range(1, 100):
#         for itme in videoData:
#             add_UploadVideo(driver, **itme)
#         for itme in videoTaskData:
#             add_videoTask(driver, **itme)
#         for itme in teskListData:
#             select_teskList(driver, **itme)
#         driver.close()
#         driver.quit()
#         driver = None
    # dialog = win32gui.FindWindow('#32770', u'文件上传')  # 对话框
    # ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    # ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    # Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    # button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button
    #
    # win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'd:\\baidu.py')  # 往输入框输入绝对地址
    # win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
