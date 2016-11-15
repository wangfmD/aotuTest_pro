tag:
    v001.00.00
    基础数据增删改查功能的可用版本。

    v001.00.10
    基础功能、课程、排互动课、精品课功能
    新增调试模式见 config.py接口  debug\test\dev等
    新增日志功能默认路径 $PY_DEV_HOME\webTest_pro\log目录下
    新增sql文件执行调用接口，$PY_DEV_HOME\webTest_pro\common\execsql.py
    优化testcase目录结构，level_A etc.  目录下需要__init__.py文件，否则unittest 加载不到测试用例。
    优化testcase的文件名称 以test_开头，以便使用nose能够执行。

#test tools
nose install:
 *pip install nose
 *pip install nose-html-reporting
exec nose:
 *>nosetests . --with-html --html-report="./report/"reportname.html"

