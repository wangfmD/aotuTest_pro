# _*_ coding: utf-8 _*_
"""
__title__ = ""
__auther__ = "acer"
__mtime__ = "2016/10/31"
"""
import os

# print os.getcwd().split("webTest_pro")[0].rstrip('\\')
# print os.getenv("PY_DEV_HOME").rstrip('\\')

execPath = os.getcwd().split("webTest_pro")[0]

if os.getenv("PY_DEV_HOME") != None:
    if os.getenv("PY_DEV_HOME").rstrip('\\') == execPath.rstrip('\\') \
            or os.getenv("PY_DEV_HOME").rstrip('/') == execPath.rstrip('/'):
        print "env:PY_DEV_HOME = exec path"
    else:
         os.environ["execPath"] = execPath

print os.getenv("execPath")