# coding=utf-8
import requests


def restart_service(host, active_code, service):

    addr_ip = "http://" + host + ":6060"

    pollcode = '/login.do?pollcode='

    activation_Code = active_code
    retartcontainer = '/retartcontainer.do?containername='

    image_Name = service

    req = requests.get(addr_ip + pollcode + activation_Code)

    _cookies = req.cookies

    req1 = requests.get(addr_ip + retartcontainer + image_Name, cookies=_cookies)
    # print "text：%s" % (req1.text)
    # print "json：%s" % (req1.json())

if __name__ == '__main__':
    host = '10.1.0.56'
    active_code = 'P7DW-MGAU-QH7R-8FSK'
    service = 'interact'
    restart_service(host, active_code, service)