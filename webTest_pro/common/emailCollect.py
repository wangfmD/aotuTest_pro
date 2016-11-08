# coding=utf-8

"""
     emailCollect.py
     Desc: used to send test report
     Maintainer: wangfm
     CreateDate: 2016-11-08 16:22:39
"""

import smtplib, os
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendReportWithAtt(attachment, *args):
    """
      Function: sendReportWithAtt
      Desc: used to send test report
      Args:
         - : file
         - : 'xx@xx.com;xx@xx.com'
      Return: None
      Usage: sendReportWithAtt(attachment, receiver)
      Maintainer: wangfm
    """
    f = open(attachment, 'rb')
    sendfile = f.read()
    f.close()
    # set os path
    if os.name == 'nt':
        attName = str(attachment).split('\\')[-1]
    else:
        attName = str(attachment).split('/')[-1]
    # init
    smtpserver = 'smtp.exmail.qq.com'
    sender = 'devops@3bu.cn'  # 发件地址
    # receiver = 'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn>;xiahao@3bu.cn;'  # 收件人地址，多人以分号分隔
    receiver = args[0]
    user = 'devops@3bu.cn'
    password = 'Xungejiaoyu@2015'
    Subject = '自动化测试报告'
    # set mail
    msgRoot = MIMEMultipart('related')
    att = MIMEText(sendfile, 'html', 'utf-8')
    # att['Content-Type'] = 'application/octet-stream'
    # att['Content-Disposition'] = 'attachment; filename = "report.html"'
    msgRoot['Subject'] = Subject
    msgRoot['From'] = sender
    msgRoot['to'] = receiver
    msgRoot.attach(att)
    mime = MIMEBase('application', 'html', filename=attName)
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=attName)
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(sendfile)
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msgRoot.attach(mime)
    # send mail
    smtp = smtplib.SMTP(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(msgRoot['From'], msgRoot['To'].split(';'), msgRoot.as_string())
    smtp.quit()
    print('test report has send out!')


def sendReport(file_new):
    """
      Function: sendReport
      Desc:send mail without attachment
      Args:
      Return:None
      Usage: sendReport(file)
    """
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('自动化测试报告', 'utf-8')
    msg['From'] = 'devops@3bu.cn'  # 发件地址
    msg['To'] = 'liman@3bu.cn;wujp@3bu.cn;fuyj@3bu.cn;lubb@3bu.cn;lukai@3bu.cn;wangfm@3bu.cn;tengfei@3bu.cn;daiyd@3bu.cn;daicj@3bu.cn;wuf@3bu.cn>;xiahao@3bu.cn'  # 收件人地址，多人以分号分隔

    smtp = smtplib.SMTP('smtp.exmail.qq.com')
    smtp.login('devops@3bu.cn', 'Xungejiaoyu@2015')  # 登录邮箱的账户和密码
    smtp.sendmail(msg['From'], msg['To'].split(';'), msg.as_string())

    smtp.quit()
    print('test report has send out!')
