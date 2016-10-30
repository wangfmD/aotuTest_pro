#!/usr/bin/env python
# encoding: utf-8

import os
print os.getcwd()
paths = os.listdir('G:\\04py\\aotuTest_pro\\webTest_pro\\testcase')
for path in paths:
    print path

def test_dd():
    print 'dddo'
