#coding=utf8
"""
     _env.py
     Desc: Be used import diffent directory`s package
     Maintainer: wangfm
     CreateDate: 2016-11-07 17:05:50
"""

__all__ = []

import os
import sys

libs_path =  ["\..\\..\\",
              "\..\\",
              "\..",
              "\..\\..\\..\\"]


Home_Path_TMP = os.environ.get('PY_DEV_HOME')
Home_Path = Home_Path_TMP
#  if Home_Path_TMP is None:
    #  print('ERROR: PY_DEV_HOME not found!')
    #  raise NameError
#  else:
    #  Home_Path = Home_Path_TMP

def addPaths(top_dir = None):
    if top_dir is None or top_dir == '':
        top_dir = Home_Path
    for _path in libs_path:
        sys.path.append(top_dir+_path)

if __name__ == '__main__':
    addPaths()
    for path in sys.path:
        print path
