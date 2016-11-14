-- 删除文件管理 图片任务 文档任务
UPDATE auth_module SET STATUS=3 WHERE module_name IN ('图片任务','文档任务');

-- 更新配置文件 截图用宽高参数
UPDATE base_sys_config SET CONFIG_VALUE='377,215,377*215' WHERE id='df99d32e-8619-478e-8e10-98f6631e4200';

-- 删除 广告管理
UPDATE auth_module SET STATUS=3 WHERE module_name='广告管理';

-- middlecenter_file工程更新的表字段
alter table f_task modify column CONTENT text;
alter table f_intf_log modify column REQ_MSG text;
ALTER TABLE f_program ADD PLAT_MARK varchar(36);

-- 修改默认选中的栏目
UPDATE zy_template SET is_default=1 WHERE tid IN (
'18f66273-f662-4344-94fb-fe90e006a485',
'37232a1e-af8a-4c03-816b-8d2c644281f7',
'57fca910-d2cb-462d-82c3-b5a1e46fbae7',
'87d93c57-a133-4406-b7d0-d3dc5c8e7524',
'a3315a2c-b52c-491d-ae75-99e0ece03924',
'f814e41e-8e71-4e87-95f3-f81aa5e8c458'
);

UPDATE zy_template SET is_default=0 WHERE tid NOT IN (
'18f66273-f662-4344-94fb-fe90e006a485',
'37232a1e-af8a-4c03-816b-8d2c644281f7',
'57fca910-d2cb-462d-82c3-b5a1e46fbae7',
'87d93c57-a133-4406-b7d0-d3dc5c8e7524',
'a3315a2c-b52c-491d-ae75-99e0ece03924',
'f814e41e-8e71-4e87-95f3-f81aa5e8c458'
);