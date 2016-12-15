# coding:utf-8

# 依赖包
import requests
import json
import os
import time
home_path = os.environ.get('PY_DEV_HOME')

def getSqlPath(sql_Add = None):
    # sql的版本
    dbversion = ""
    if sql_Add != None :
        ########################获取版本号###########################
        
        try:
            try:
                ########################获取init.db_conf[]###########################
                strs=requests.get(sql_Add+"/middlecenter/version", timeout=5)
                s=json.loads(strs.text)
                dbversion=s['dbversion'][:-2]
            except AttributeError:
                sql_Add = "init.db_conf Configuration is not read"
                 ########################获取init.db_conf[]###########################
        except :
            dbversion = "dbversion,Timeout!"
            ########################获取版本号###########################
    sqlFilePath = ""
    currentFile = ""
    base_dir="X:\\"
    if dbversion != "dbversion,Timeout!" or  dbversion !="":
        if os.path.exists(base_dir):
            l=os.listdir(base_dir)
            l.sort(reverse=True)
            for i in l:
                fileVersion = base_dir+i+'\VERSION'
                if os.path.exists(fileVersion) :
                    f = open(fileVersion, 'r')
                    version = f.read().replace('\t','').replace('\n','').replace(' ','')
                    if dbversion == version:
                        sqlFilePath =base_dir + i
                        break
                    
        dataTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "INSERT INTO `middle_db_version` VALUES ('1', '%s', '', '%s');" %(dbversion, dataTime)
        os.system("copy /y "+sqlFilePath+"\\middle.sql "+home_path + "\\webTest_pro\\data\\sqllib\\")
#     else :
        sqlFile = home_path + '\webTest_pro\data\sqllib\\'
    return sqlFile,sql

# def middle_db_version(Sqlpath):
#     try:
        #获取文件最后一行  拿到id的值  start
#         os.chdir(Sqlpath)
#         files = open('middle_db_version.sql', 'r')
#         i = -1                                    
#         while True:
#             i = i - 1                           
#             files.seek(i, 2)                     
#             if files.read(1) == '\n':          
#                  break   
#         str = files.readline().strip()
#         digital_id = str[str.index("(")+2:str.index("',")]
#         digital_version = str[str.index(", '")+3:str.index("'',")-3]
        
        #获取文件最后一行  拿到id的值  end
        
        
        #开始插入sql数据  start
#         u = open('middle_db_version.sql', 'a')
        
#         f = open(getSqlPath()[0]+'VERSION', 'r')
#         version = f.read().replace('\t','').replace('\n','').replace(' ','')
        #判断nas上面取的地址  是否和我本地version 版本号一样   如果不一样   进行添加操作   如果一样  不做任何添加操作
#         if digital_version !=  version :
            #获取当前时间
#             dataTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#             sql = "INSERT INTO `middle_db_version` VALUES ('%s', '%s', '', '%s');" %(int(digital_id)+1, version, dataTime)
#             u.write("\n" + sql)
            #开始插入sql数据  end
        
#         #关闭流  start
#         if f or u or files:
#             files.close()
#             u.close()
#             f.close()
        #关闭流 end
#     except IOError :
#         print ' No such file or directory'
    

if __name__ == "__main__":
    print getSqlPath("http://10.1.0.56")