"# aotuTest_pro" 
tag:
    v001.00.00 
    " 基础数据增删改查功能的可用版本。


#test tools
nose install:
 *pip install nose
 *pip install nose-html-reporting
exec nose:
 *>nosetests . --with-html --html-report="./report/"reportname.html"

