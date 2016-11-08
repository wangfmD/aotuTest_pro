# coding=utf-8
"""
     *.py
     Desc: test _env import
     Maintainer: wangfm
     CreateDate: 2016-11-07 17:32:23
"""
import sys
from _env import addPaths
addPaths('.')
# sys.path.append('G:\\00project\\aotuTest_pro\\webTest_pro\\common')
# sys.path.append('G:\\00project\\aotuTest_pro\\..\\..\\')
# sys.path.append('..')
#  from init import base_url
# from init import base_url

#  currentP = os.path.dirname(__file__)
#  dirs = os.path.join(currentP, '..\..')
#  sys.path.append(dirs)
from init import base_url

if __name__ == '__main__':
    print base_url
    for path in sys.path:
        print path



