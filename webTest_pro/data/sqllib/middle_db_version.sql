/*
Navicat MySQL Data Transfer

Source Server         : 10.1.0.56
Source Server Version : 50619
Source Host           : 10.1.0.56:13306
Source Database       : middle

Target Server Type    : MYSQL
Target Server Version : 50619
File Encoding         : 65001

Date: 2016-11-21 15:09:24
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `middle_db_version`
-- ----------------------------
DROP TABLE IF EXISTS `middle_db_version`;
CREATE TABLE `middle_db_version` (
  `ID` int(8) NOT NULL AUTO_INCREMENT COMMENT '当前版本',
  `CUR_VER` varchar(255) DEFAULT NULL COMMENT '当前版本',
  `PRE_VER` varchar(255) DEFAULT NULL COMMENT '前一个版本',
  `CREATE_TIME` datetime DEFAULT NULL COMMENT '更新或者创建时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 COMMENT='数据库版本表';

-- ----------------------------
-- Records of middle_db_version
-- ----------------------------