#!/usr/bin/python2.7
# coding=utf8

__all__ = []

import os
import sys

libs_path = ["../../../",
             "../../",
             "../"]

Home_Path = os.environ.get('PY_DEV_HOME')
print '-' * 20
print os.environ.get('PY_DEV_HOME')

# for i in os.environ.keys():
#     print i
# if Home_Path is None:
# Home_Path = '.'

for _path in libs_path:
    sys.path.append(Home_Path + '/' + _path)


def addPaths(top_dir=None):
    if top_dir is None or top_dir == '':
        top_dir = Home_Path
    for _path in libs_path:
        sys.path.append(top_dir + '/' + _path)
