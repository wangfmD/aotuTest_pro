autoTest_pro
=======================

## tags Info
**v000.000.001:**
+   基础数据增删改查功能的可用版本。
+   基础功能、课程、排互动课、精品课功能
+   新增调试模式见 config.py接口  debug\test\dev等
+   新增日志功能默认路径 $PY_DEV_HOME\webTest_pro\log目录下
+   新增sql文件执行调用接口，$PY_DEV_HOME\webTest_pro\common\execsql.py
+   优化testcase目录结构，level_A etc.  目录下需要__init__.py文件，否则unittest 加载不到测试用例。
+   优化testcase的文件名称 以test_开头，以便使用nose能够执行。
+   添加生成静态html报告功能，全部报告可以跳转。



## Installation steps

### 1. clone 到本地

```
git clone http://git.3bu.cn/wangfm/autoTest_pro
```


### 2. 安装依赖包


##### 2.1 系统依赖
selenium、requests、MySQL-python、nose、python 获取坐标、等
```
pip install selenium
pip install requests
pip install nose
```
##### 2.2 参考
+ [MySQL-python](https://pypi.python.org/pypi/MySQL-python)
+ [requests](http://docs.python-requests.org/zh_CN/latest/)






>test tools
nose install:
 *pip install nose
 *pip install nose-html-reporting
exec nose:
 *>nosetests . --with-html --html-report="./report/"reportname.html"
