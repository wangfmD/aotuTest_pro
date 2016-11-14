UPDATE base_sys_config set CONFIG_VALUE = 'rtmp://10.1.0.56:1935/live/' where CONFIG_KEY = 'live_server_url';
UPDATE base_sys_config set CONFIG_VALUE = 'http://10.1.0.56' where CONFIG_KEY = 'web_server_resource';
UPDATE base_sys_config set CONFIG_VALUE = '10.1.0.56/filesrv' where CONFIG_KEY = 'file_server_url';
UPDATE base_sys_config set CONFIG_VALUE = '10.1.0.56' where CONFIG_KEY = 'mcu_center_host';
UPDATE base_sys_config set CONFIG_VALUE = '10.1.0.56:11194' where CONFIG_KEY = 'file_server_url_visit';
UPDATE base_sys_config set CONFIG_VALUE = '10.1.0.56' where CONFIG_KEY = 'message_center_host';
UPDATE base_sys_config set CONFIG_VALUE = '10.1.0.56' where CONFIG_KEY = 'file_server_ftp_host';
UPDATE base_sys_config set CONFIG_VALUE = 'http://10.1.0.56/middleclient/index.do' where CONFIG_KEY = 'web_server_client';


INSERT INTO `xg_middleware_local` VALUES ('faad4ff5-1bdb-4f3f-8aae-fa2ad04f1d84', 'ec3ae035-8c9f-45fd-956f-772e285a6e21', '10.1.0.56', '80', '/interact', 'administrator', 'xungejiaoyu', '634ed72f-383b-4eae-af85-47bcb039dae2', '0', '0', null, '0', '', '', '', '2016-09-12 18:58:23', '1', '1', null);
INSERT INTO `xg_middleware` VALUES ('ec3ae035-8c9f-45fd-956f-772e285a6e21', '10.1.0.56', '80', null, null, 'administrator', 'xungejiaoyu', '634ed72f-383b-4eae-af85-47bcb039dae2', null, '1', '2016-09-12 18:57:54', '0', '2', '', '', '', '1', '/interact', '');