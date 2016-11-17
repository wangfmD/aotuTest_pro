# coding=utf-8
import ConfigParser
# 依赖包
import requests,_env

from _env import addPaths
addPaths(".")

cf = ConfigParser.ConfigParser()
cf.read(_env.Home_Path_TMP+"\\src\\init\\init.conf")

address_http = cf.get("portal", "address_http")
host = cf.get("portal", "host")
address_oauth = cf.get("portal", "address_oauth")
address_api = cf.get("portal", "address_api")
address_api1 = cf.get("portal", "address_api1")
address_guest = cf.get("portal", "address_guest")
address_host = cf.get("portal", "address_host")
address_oauth_api = cf.get("portal", "address_oauth_api")
address_wechat_oauth_api= cf.get("portal", "address_wechat_oauth_api")
address_wechat_api= cf.get("portal", "address_wechat_api")
address_api_v1= cf.get("portal", "address_api_v1.1")
address_guest_api= cf.get("portal", "address_guest_api")
address_guestresapp_api= cf.get("portal", "address_guestresapp_api")
address_guest_api1= cf.get("portal", "address_guest_api1")

user_name = cf.get("user", "user_name")
user_password = cf.get("user", "user_password")
user_platform = cf.get("user", "user_platform")
user_client_id = cf.get("user", "user_client_id")
user_redirect_uri = cf.get("user", "user_redirect_uri")
shiro_sid = cf.get("shiro", "shiro_sid")

if __name__ == "__main__":
    print address_http

def returnValue(self,req):
    print "响应状态码：%s" %(req.status_code)
    print "目标地址的URL：%s" %(req.url)
    print "-" * 80
    
    if req.status_code==200:
        print "返回的text：%s" %(req.text)
        print "返回的json：%s" %(req.json())
    elif req.status_code==201:
         print "（已创建）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==202:
         print "（已接受）服务器已接受了请求，但尚未对其进行处理！".encode("utf-8")
    elif req.status_code==203:
         print "（非授权信息）服务器已成功处理了请求，但返回了可能来自另一来源的信息！".encode("utf-8")
    elif req.status_code==204:
         print "（无内容）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==205:
         print "（重置内容）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==206:
         print "（部分内容）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==302:
         print "（临时移动）    服务器目前正从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。此代码与响应 GET 和 HEAD 请求的 301 代码类似，会自动将请求者转到不同的位置。但由于 Googlebot 会继续抓取原有位置并将其编入索引，因此您不应使用此代码来通知 Googlebot 某个页面或网站已被移动！".encode("utf-8")
    elif req.status_code==403:
         print "（已禁止）服务器拒绝请求。如果在 Googlebot 尝试抓取您网站上的有效网页时显示此状态代码（您可在 Google 网站管理员工具中诊断下的网络抓取页面上看到此状态代码），那么，这可能是您的服务器或主机拒绝 Googlebot 对其进行访问！".encode("utf-8")
    elif req.status_code==500:
         print "（服务器内部错误） 服务器遇到错误，无法完成请求！".encode("utf-8")
    else :
         print "接口不通，请联系管理员！".encode("utf-8")
    self. assertEqual(200, req.status_code)
      
      
def returnValues(req):
    print "响应状态码：%s" %(req.status_code)
    print "目标地址的URL：%s" %(req.url)
    print "-" * 80
    if req.status_code==200:
        print "返回的text：%s" %(req.text)
        print "返回的json：%s" %(req.json())
    elif req.status_code==201:
         print "（已创建）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==202:
         print "（已接受）服务器已接受了请求，但尚未对其进行处理！".encode("utf-8")
    elif req.status_code==203:
         print "（非授权信息）服务器已成功处理了请求，但返回了可能来自另一来源的信息！".encode("utf-8")
    elif req.status_code==204:
         print "（无内容）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==205:
         print "（重置内容）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==206:
         print "（部分内容）请求成功且服务器已创建了新的资源！".encode("utf-8")
    elif req.status_code==302:
         print "（临时移动）    服务器目前正从不同位置的网页响应请求，但请求者应继续使用原有位置来进行以后的请求。此代码与响应 GET 和 HEAD 请求的 301 代码类似，会自动将请求者转到不同的位置。但由于 Googlebot 会继续抓取原有位置并将其编入索引，因此您不应使用此代码来通知 Googlebot 某个页面或网站已被移动！".encode("utf-8")
    elif req.status_code==403:
         print "（已禁止）服务器拒绝请求。如果在 Googlebot 尝试抓取您网站上的有效网页时显示此状态代码（您可在 Google 网站管理员工具中诊断下的网络抓取页面上看到此状态代码），那么，这可能是您的服务器或主机拒绝 Googlebot 对其进行访问！".encode("utf-8")
    else :
         print "接口不通，请联系管理员！".encode("utf-8")
      