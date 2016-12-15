import os
import sys
import unittest


try:
    sys.path.append(os.environ.get('PY_DEV_HOME'))
    from webTest_pro.common.mysqlKit import sqlOperating
    from webTest_pro.common.logger import logger,T_INFO
    from webTest_pro.common.initData import init

except ImportError as e:
    print e

host = init.db_conf['host']
active_code, service = init.active_code, 'interact'
streaming_media = init.streaming_media
hostadd = init.db_conf['hostadd']
mediaAddr = streaming_media['serverIps']

# set log info
# LOG_INIT(logFile)
# logger = LOG_MODULE_DEFINE('Platform')
# SET_LOG_LEVEL(logger, 'info')

sqlpara = [{'col_name': 'live_server_url', 'col_value': 'rtmp://' + hostadd + ':1935/live/'},
           {'col_name': 'web_server_resource', 'col_value': 'http://' + hostadd},
           {'col_name': 'file_server_url', 'col_value': mediaAddr + '/filesrv'},
           {'col_name': 'mcu_center_host', 'col_value': hostadd},
           {'col_name': 'file_server_url_visit', 'col_value': mediaAddr + ':11194'},
           {'col_name': 'message_center_host', 'col_value': hostadd},
           {'col_name': 'file_server_ftp_host', 'col_value': mediaAddr},
           {'col_name': 'web_server_client', 'col_value': 'http://' + hostadd + '/middleclient/index.do'},
           {'col_name': 'centerfile_host', 'col_value': hostadd}
           ]


class dbMgr(unittest.TestCase):
    def test_updateDB(self):
        T_INFO( logger, 'start case dbMgr')
        for s in sqlpara:
            conn = sqlOperating(init.db_conf['host'],
                                init.db_conf['user'],
                                init.db_conf['passwd'],
                                init.db_conf['db'])
            # c = sqlOperating()
            # print s['col_name'], s['col_value']
            conn.updaeDb("UPDATE base_sys_config set CONFIG_VALUE = '%s' where CONFIG_KEY = '%s'" % (s['col_value'], s['col_name']))
        T_INFO(logger, 'exec: test_updateDB end.')


if __name__ == '__main__':
    unittest.main()
