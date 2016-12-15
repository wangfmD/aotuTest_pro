autoTest_pro
=======================

## tags 摘要
**v000.000.001:**
+   基础数据增删改查功能的可用版本。
+   基础功能、课程、排互动课、精品课功能
+   新增调试模式见 config.py接口  debug\test\dev等
+   新增日志功能默认路径 $PY_DEV_HOME\webTest_pro\log目录下
+   新增sql文件执行调用接口，$PY_DEV_HOME\webTest_pro\common\execsql.py
+   优化testcase目录结构，level_A etc.  目录下需要__init__.py文件，否则unittest 加载不到测试用例。
+   优化testcase的文件名称 以test_开头，以便使用nose能够执行。
+   添加生成静态html报告功能，全部报告可以跳转。

**v000.000.002:**
+ 添加文件上传功能。
+ 修改了排课功能。
+ 修改_env为sys.append(os.getenv("PY_DEV_HOME"))

**next tag:**
+ xxx




## Installation Steps

### 1. clone 到本地
* 安装git：\\nas.3bu.cn\software\Git\official 自行选择合适版本安装。
* 下载autoTest_pro
* "win+r cmd" enter
```
D:
mkdir project&cd project
git clone http://git.3bu.cn/wangfm/autoTest_pro
```
* windows中配置环境变量。PY_DEV_HOME：D:\project\autoTest_pro
* 测试环境变量是否配置成功。
* "win+r cmd" enter
```
echo %PY_DEV_HOME%
D:\project\autoTest_pro
```

### 2. 安装依赖包


##### 2.1 系统依赖
* 访问：\\nas.3bu.cn\builds\stable\test\os_img\wfm\pythonPackage
* 安装：python-2.7.11_x64.msi。安装时选择add path in system，默认路径或自行选择python安装路径。
* 安装：MySQL-python-1.2.4b4.win32-py2.7.exe
* 安装：PIL-1.1.7.win32-py2.7.exe
* 安装：pywin32-218.win32-py2.7.exe
* selenium、requests、MySQL-python、nose、python 获取坐标、等
* "win+r cmd" enter
```
pip install selenium
pip install requests
pip install nose
pip install \\nas.3bu.cn\builds\stable\test\os_img\wfm\pythonPackage\SendKeys-0.3-cp27-none-win32.whl
```
* 安装chrome驱动，拷贝chrome驱动到python安装路径下即可。
* "win+r cmd" enter
```
cp \\nas.3bu.cn\builds\stable\test\os_img\wfm\pythonPackage\chromedriver.exe C:\python27
```
* 测试安装结果
* "win+r cmd" enter
```
python
import selenium
import requests
import MySQLdb
```
* python命令下import后没有任何报错，则导入selenium、requests、MySQLdb成功。

*  安装安装mysql：“\\nas.3bu.cn\temp\王发明\mysql”拷贝到本地，并配置mysql\bin到path。
* test mysql
```
mysql --version
```


## 运行
#### 1.1 修改测试环境ip
```
vim $PY_DEV_HOME$\webTest_pro\cfg\init_default.conf
%s/10.1.0.56/xx.xx.xx.xx
```
#### 1.2 执行
```
cd  $PY_DEV_HOME$\webTest_pro\middleClientTest
python Runner.py
```

#### 1.3 执行结果
* $PY_DEV_HOME$\webTest_pro\log
* $PY_DEV_HOME$\webTest_pro\report


##### 2.2 参考
+ [MySQL-python](https://pypi.python.org/pypi/MySQL-python)
+ [requests](http://docs.python-requests.org/zh_CN/latest/)





>test tools
nose install:
 *pip install nose
 *pip install nose-html-reporting
exec nose:
 *>nosetests . --with-html --html-report="./report/"reportname.html"
