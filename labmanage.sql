-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2015-05-16 22:17:30
-- 服务器版本: 5.5.41-0ubuntu0.14.04.1
-- PHP 版本: 5.5.9-1ubuntu4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `labmanage`
--

-- --------------------------------------------------------

--
-- 表的结构 `administer`
--

CREATE TABLE IF NOT EXISTS `administer` (
  `uid` char(20) NOT NULL,
  `lcid` char(20) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `admin_lc` (`lcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `administer`
--

INSERT INTO `administer` (`uid`, `lcid`) VALUES
('244', '1'),
('7', '1'),
('245', '2'),
('246', '2'),
('247', '2'),
('8', '2'),
('248', '4'),
('249', '4');

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=19 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `circle_open_lab_detail`
--

CREATE TABLE IF NOT EXISTS `circle_open_lab_detail` (
  `coldid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `olid` char(40) NOT NULL,
  `lid` char(20) NOT NULL,
  `weekday` int(10) unsigned NOT NULL,
  `begin_time` int(10) unsigned NOT NULL,
  `end_time` int(10) unsigned NOT NULL,
  `number` int(10) unsigned NOT NULL DEFAULT '0',
  PRIMARY KEY (`coldid`),
  KEY `cold_l` (`lid`),
  KEY `cold_ol` (`olid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=39 ;

--
-- 转存表中的数据 `circle_open_lab_detail`
--

INSERT INTO `circle_open_lab_detail` (`coldid`, `olid`, `lid`, `weekday`, `begin_time`, `end_time`, `number`) VALUES
(13, '42015 02 27 10 49 39', '1', 0, 8, 13, 0),
(14, '42015 02 27 10 49 39', '2', 0, 8, 13, 0),
(27, '42015 02 27 14 12 12', '1', 0, 8, 10, 4),
(28, '42015 02 27 14 12 12', '2', 0, 8, 10, 0),
(29, '52015 02 28 07 39 18', '1', 1, 8, 15, 6),
(30, '52015 02 28 07 39 18', '2', 1, 8, 15, 0),
(31, '42015 03 11 15 03 45', '3', 0, 8, 10, 0),
(32, '42015 03 11 15 03 47', '3', 0, 8, 10, 0),
(33, '42015 03 11 15 03 49', '3', 0, 8, 10, 0),
(34, '42015 03 11 15 03 57', '3', 0, 8, 10, 0),
(35, '42015 03 11 15 47 22', '4', 0, 8, 10, 0),
(36, '42015 03 11 15 47 24', '4', 0, 8, 10, 0),
(37, '42015 03 11 15 47 26', '4', 0, 8, 10, 0),
(38, '42015 03 11 15 47 28', '4', 0, 8, 10, 0);

-- --------------------------------------------------------

--
-- 表的结构 `circle_order`
--

CREATE TABLE IF NOT EXISTS `circle_order` (
  `corder_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` char(20) NOT NULL,
  `coldid` int(10) unsigned NOT NULL,
  `state` char(20) NOT NULL DEFAULT '未审核',
  `seat_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`corder_id`),
  KEY `circle_order_user` (`uid`),
  KEY `co_ol` (`coldid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;

--
-- 转存表中的数据 `circle_order`
--

INSERT INTO `circle_order` (`corder_id`, `uid`, `coldid`, `state`, `seat_id`) VALUES
(2, '2', 27, '通过', NULL),
(3, '1', 27, '拒绝', NULL),
(4, '2', 29, '通过', NULL),
(5, '3', 29, '通过', NULL),
(6, '100', 27, '通过', 4),
(7, '102', 27, '未审核', NULL);

-- --------------------------------------------------------

--
-- 表的结构 `department`
--

CREATE TABLE IF NOT EXISTS `department` (
  `did` char(20) NOT NULL,
  `dname` char(40) NOT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `department`
--

INSERT INTO `department` (`did`, `dname`) VALUES
('1', '软件学院'),
('2', '物理系'),
('3', '电子系'),
('4', 'A院');

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6gi2xognuuln7sv3er85thvp0wmwc9v4', 'ZTUzMDdmYzJiM2IwMWE0MjQ2YjFhZDQzM2RlNmM2NDYxNmQxZGQ4MDp7Im15X3VzZXIiOnsicGVybV9saXN0IjpbeyJ1cmwiOiIvY2hlY2tfb3Blbl9sYWIiLCJwbmFtZSI6Ilx1NWJhMVx1NjgzOFx1NWYwMFx1NjUzZVx1OGJhMVx1NTIxMiJ9LHsidXJsIjoiL2FkZF91c2VyIiwicG5hbWUiOiJcdTZkZmJcdTUyYTBcdTc1MjhcdTYyMzcifSx7InVybCI6Ii9sb2dvdXQiLCJwbmFtZSI6Ilx1OTAwMFx1NTFmYSJ9XSwidW5hbWUiOiJBZG1pbjEiLCJ1aWQiOiI3In19', '2015-03-02 14:51:45'),
('ee479cbwro8zf1bujvukg5puu3sgorv9', 'MTM1ZDRjMTMyMTU5MTZiMWZiMzUzZjMxNTNjM2MxMWE5MGY3NmNkZTp7InBlcm1fbGlzdCI6W3sidXJsIjoib3JkZXIiLCJwbmFtZSI6Ilx1OTg4NFx1N2VhNlx1NWI5ZVx1OWE4Y1x1NWJhNCJ9XSwidW5hbWUiOiJcdTU0MzRcdTc5M2NcdTg1MWEiLCJteV91c2VyIjp7InBlcm1fbGlzdCI6W3sidXJsIjoiL29wZW5fbGFiIiwicG5hbWUiOiJcdTVmMDBcdTY1M2VcdTViOWVcdTlhOGNcdTViYTQifSx7InVybCI6Ii9jaGVja19vcmRlciIsInBuYW1lIjoiXHU1YmExXHU2ODM4XHU1YjY2XHU3NTFmXHU5ODg0XHU3ZWE2In0seyJ1cmwiOiIvbXlfb3Blbl9sYWIiLCJwbmFtZSI6Ilx1NjIxMVx1NzY4NFx1NWYwMFx1NjUzZVx1OGJhMVx1NTIxMiJ9LHsidXJsIjoiL2xvZ291dCIsInBuYW1lIjoiXHU5MDAwXHU1MWZhIn1dLCJ1bmFtZSI6IldvbGYiLCJwYXNzd29yZCI6IjExMjIzMzQ0IiwidWlkIjoiNCIsImlkZW50aXR5IjpbIlx1NjU1OVx1NWUwOCJdfSwidWlkIjoiMSJ9', '2015-03-27 14:26:49'),
('ifpaw0x1tpiteyejesgaftt0omqy4ulq', 'OTZmY2IwMDNkZDVlZTdhMjEwNzNhMzY4ZGI1MmNiMjZjODZmZjBmODp7Im15X3VzZXIiOnsicGVybV9saXN0IjpbeyJ1cmwiOiIvb3Blbl9sYWIiLCJwbmFtZSI6Ilx1NWYwMFx1NjUzZVx1NWI5ZVx1OWE4Y1x1NWJhNCJ9LHsidXJsIjoiL2NoZWNrX29yZGVyIiwicG5hbWUiOiJcdTViYTFcdTY4MzhcdTViNjZcdTc1MWZcdTk4ODRcdTdlYTYifSx7InVybCI6Ii9teV9vcGVuX2xhYiIsInBuYW1lIjoiXHU2MjExXHU3Njg0XHU1ZjAwXHU2NTNlXHU4YmExXHU1MjEyIn0seyJ1cmwiOiIvbG9nb3V0IiwicG5hbWUiOiJcdTkwMDBcdTUxZmEifV0sInVuYW1lIjoiV29sZjIiLCJ1aWQiOiI1In19', '2015-02-10 12:19:09'),
('shuo83nbn57trubeiwwn3pc3w95kih74', 'ZGM1MzcxZmZjNDc0MTg2NjlhODEyZTNkYWUyNzM0YTJlOTM1OTVmMTp7Im15X3VzZXIiOnsicGVybV9saXN0IjpbeyJ1cmwiOiIvb3Blbl9sYWIiLCJwbmFtZSI6Ilx1NWYwMFx1NjUzZVx1OGJhMVx1NTIxMiJ9LHsidXJsIjoiL2FkZF9zdHVkZW50X3RlYWNoZXIiLCJwbmFtZSI6Ilx1NmRmYlx1NTJhMFx1NzUyOFx1NjIzNyJ9LHsidXJsIjoiL3N0dV9hcHBfY2hlY2siLCJwbmFtZSI6Ilx1NWJhMVx1NjgzOFx1NWI2Nlx1NzUxZlx1OTg4NFx1N2VhNiJ9LHsidXJsIjoiL2xvZ291dCIsInBuYW1lIjoiXHU5MDAwXHU1MWZhIn1dLCJ1bmFtZSI6IkFkbWluMiIsInBhc3N3b3JkIjoiMTEyMjMzNDQiLCJ1aWQiOiI4IiwiaWRlbnRpdHkiOlsiXHU1YjllXHU5YThjXHU1YmE0XHU3YmExXHU3NDA2XHU1NDU4Il19fQ==', '2015-05-28 12:20:20');

-- --------------------------------------------------------

--
-- 表的结构 `identity`
--

CREATE TABLE IF NOT EXISTS `identity` (
  `gid` char(20) NOT NULL,
  `gname` char(40) NOT NULL,
  PRIMARY KEY (`gid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `identity`
--

INSERT INTO `identity` (`gid`, `gname`) VALUES
('1', 'student'),
('2', 'teacher'),
('3', 'administer');

-- --------------------------------------------------------

--
-- 表的结构 `lab`
--

CREATE TABLE IF NOT EXISTS `lab` (
  `lid` char(20) NOT NULL,
  `lname` char(40) NOT NULL,
  `lcid` char(20) NOT NULL,
  `number` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`lid`),
  KEY `lab_lc` (`lcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `lab`
--

INSERT INTO `lab` (`lid`, `lname`, `lcid`, `number`) VALUES
('1', 'A实验室', '1', 10),
('10', 'I实验室', '5', 20),
('11', 'Dlab', '6', 20),
('12', 'Elab', '6', 30),
('2', 'B实验室', '1', 20),
('3', 'C实验室', '2', 30),
('4', 'D实验室', '2', 20),
('8', 'LL实验室', '1', 20),
('9', 'H实验室', '4', 10);

-- --------------------------------------------------------

--
-- 表的结构 `lab_center`
--

CREATE TABLE IF NOT EXISTS `lab_center` (
  `lcid` char(20) NOT NULL,
  `lcname` char(40) NOT NULL,
  PRIMARY KEY (`lcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `lab_center`
--

INSERT INTO `lab_center` (`lcid`, `lcname`) VALUES
('1', 'A中心'),
('2', 'B中心'),
('4', 'LL中心'),
('5', 'LL中心2'),
('6', '实验中心1'),
('7', '实验中心2'),
('8', '实验中心３');

-- --------------------------------------------------------

--
-- 表的结构 `open_lab`
--

CREATE TABLE IF NOT EXISTS `open_lab` (
  `olid` char(40) NOT NULL DEFAULT '',
  `lcid` char(20) DEFAULT NULL,
  `uid` char(20) NOT NULL,
  `begin_date_time` datetime NOT NULL,
  `end_date_time` datetime NOT NULL,
  `status` char(20) NOT NULL DEFAULT '未审核',
  `olname` char(60) NOT NULL,
  `type` char(30) NOT NULL,
  PRIMARY KEY (`olid`),
  KEY `open_lab_user` (`uid`),
  KEY `open_lab_lc` (`lcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `open_lab`
--

INSERT INTO `open_lab` (`olid`, `lcid`, `uid`, `begin_date_time`, `end_date_time`, `status`, `olname`, `type`) VALUES
('123455', '1', '1', '2014-11-21 00:00:00', '2014-12-20 00:00:00', '通过', 'open lab 1', '单次'),
('42015 01 09 09 17 30', '2', '4', '2015-01-14 08:00:00', '2015-01-14 16:00:00', '通过', '范德萨范德萨', '单次'),
('42015 01 09 09 24 06', '1', '4', '2015-01-14 08:00:00', '2015-01-14 19:00:00', '通过', '广发是的说法', '单次'),
('42015 01 09 11 03 44', '1', '4', '2015-01-28 14:00:00', '2015-01-28 16:00:00', '拒绝', '计划2', '单次'),
('42015 01 09 11 08 18', '2', '4', '2015-01-28 08:00:00', '2015-01-28 12:00:00', '通过', '计划3', '单次'),
('42015 02 05 11 49 02', '2', '4', '2015-02-05 14:00:00', '2015-02-05 17:00:00', '通过', 'MM开放计划', '单次'),
('42015 02 18 01 27 44', '1', '4', '2015-02-19 08:00:00', '2015-02-19 10:00:00', '未审核', 'test jihua', '单次'),
('42015 02 26 11 43 21', '1', '4', '2015-02-27 08:00:00', '2015-02-27 11:00:00', '未审核', 'test one time', '单次'),
('42015 02 27 10 49 39', '1', '4', '2015-02-23 00:00:00', '2015-03-09 00:00:00', '未审核', 'c test', '循环'),
('42015 02 27 14 12 12', '1', '4', '2015-02-23 00:00:00', '2015-03-09 00:00:00', '通过', 'c test 2', '循环'),
('42015 02 28 07 17 06', '1', '4', '2015-03-01 08:00:00', '2015-03-01 13:00:00', '通过', 'one test1', '单次'),
('42015 02 28 10 34 30', '1', '4', '2015-02-28 08:00:00', '2015-02-28 22:00:00', '通过', 'test get', '单次'),
('42015 03 03 09 31 06', '1', '4', '2015-03-05 08:00:00', '2015-03-05 11:00:00', '通过', 'one time test1', '单次'),
('42015 03 11 15 03 45', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '通过', '冲突测试１', '循环'),
('42015 03 11 15 03 47', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '拒绝', '冲突测试１', '循环'),
('42015 03 11 15 03 49', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '拒绝', '冲突测试１', '循环'),
('42015 03 11 15 03 57', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '拒绝', '冲突测试１', '循环'),
('42015 03 11 15 47 22', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '未审核', '冲突测试２', '循环'),
('42015 03 11 15 47 24', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '未审核', '冲突测试２', '循环'),
('42015 03 11 15 47 26', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '未审核', '冲突测试２', '循环'),
('42015 03 11 15 47 28', '2', '4', '2015-03-09 00:00:00', '2015-04-01 00:00:00', '未审核', '冲突测试２', '循环'),
('52015 01 09 11 10 39', '1', '5', '2015-01-24 08:00:00', '2015-01-24 10:00:00', '未审核', '计划4', '单次'),
('52015 02 02 08 45 15', '1', '5', '2015-02-17 08:00:00', '2015-02-17 10:00:00', '通过', 'AAAA计划', '单次'),
('52015 02 28 07 39 18', '1', '5', '2015-02-23 00:00:00', '2015-03-09 00:00:00', '通过', 'c test2', '循环');

-- --------------------------------------------------------

--
-- 表的结构 `open_lab_detail`
--

CREATE TABLE IF NOT EXISTS `open_lab_detail` (
  `oldid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `olid` char(40) DEFAULT NULL,
  `lid` char(20) NOT NULL,
  `begin_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `number` int(10) unsigned NOT NULL DEFAULT '0',
  `coldid` int(11) unsigned DEFAULT NULL,
  PRIMARY KEY (`oldid`),
  KEY `old_l` (`lid`),
  KEY `old_ol` (`olid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=68 ;

--
-- 转存表中的数据 `open_lab_detail`
--

INSERT INTO `open_lab_detail` (`oldid`, `olid`, `lid`, `begin_time`, `end_time`, `number`, `coldid`) VALUES
(1, '123455', '1', '2014-11-24 10:00:00', '2014-11-24 12:00:00', 0, NULL),
(2, '123455', '2', '2014-11-27 10:00:00', '2014-11-24 12:00:00', 0, NULL),
(6, '42015 01 09 09 17 30', '3', '2015-01-14 08:00:00', '2015-01-14 14:00:00', 0, NULL),
(7, '42015 01 09 09 17 30', '3', '2015-01-14 10:00:00', '2015-01-14 16:00:00', 0, NULL),
(8, '42015 01 09 09 24 06', '1', '2015-01-14 08:00:00', '2015-01-14 17:00:00', 0, NULL),
(9, '42015 01 09 09 24 06', '1', '2015-01-14 14:00:00', '2015-01-14 19:00:00', 0, NULL),
(10, '42015 01 09 11 03 44', '1', '2015-01-28 14:00:00', '2015-01-28 16:00:00', 0, NULL),
(11, '42015 01 09 11 03 44', '2', '2015-01-28 14:00:00', '2015-01-28 16:00:00', 0, NULL),
(12, '42015 01 09 11 08 18', '3', '2015-01-28 08:00:00', '2015-01-28 12:00:00', 0, NULL),
(13, '42015 01 09 11 08 18', '4', '2015-01-28 08:00:00', '2015-01-28 12:00:00', 0, NULL),
(14, '52015 01 09 11 10 39', '1', '2015-01-24 08:00:00', '2015-01-24 10:00:00', 0, NULL),
(15, '52015 01 09 11 10 39', '2', '2015-01-24 08:00:00', '2015-01-24 10:00:00', 0, NULL),
(16, '52015 02 02 08 45 15', '1', '2015-02-17 08:00:00', '2015-02-17 10:00:00', 1, NULL),
(17, '52015 02 02 08 45 15', '2', '2015-02-17 08:00:00', '2015-02-17 10:00:00', 0, NULL),
(18, '42015 02 05 11 49 02', '3', '2015-02-05 14:00:00', '2015-02-05 17:00:00', 1, NULL),
(19, '42015 02 18 01 27 44', '1', '2015-02-19 08:00:00', '2015-02-19 10:00:00', 0, NULL),
(20, '42015 02 18 01 27 44', '2', '2015-02-19 08:00:00', '2015-02-19 10:00:00', 0, NULL),
(21, '42015 02 26 11 43 21', '2', '2015-02-27 08:00:00', '2015-02-27 11:00:00', 0, NULL),
(22, '42015 02 27 14 12 12', '1', '2015-02-23 08:00:00', '2015-02-23 10:00:00', 4, 27),
(23, '42015 02 27 14 12 12', '1', '2015-03-02 08:00:00', '2015-03-02 10:00:00', 4, 27),
(24, '42015 02 27 14 12 12', '2', '2015-02-23 08:00:00', '2015-02-23 10:00:00', 0, 28),
(25, '42015 02 27 14 12 12', '2', '2015-03-02 08:00:00', '2015-03-02 10:00:00', 0, 28),
(26, '42015 02 28 07 17 06', '1', '2015-03-01 08:00:00', '2015-03-01 13:00:00', 3, NULL),
(27, '42015 02 28 07 17 06', '2', '2015-03-01 08:00:00', '2015-03-01 13:00:00', 0, NULL),
(28, '52015 02 28 07 39 18', '1', '2015-02-24 08:00:00', '2015-02-24 15:00:00', 6, 29),
(29, '52015 02 28 07 39 18', '1', '2015-03-03 08:00:00', '2015-03-03 15:00:00', 6, 29),
(30, '52015 02 28 07 39 18', '2', '2015-02-24 08:00:00', '2015-02-24 15:00:00', 0, 30),
(31, '52015 02 28 07 39 18', '2', '2015-03-03 08:00:00', '2015-03-03 15:00:00', 0, 30),
(33, '42015 02 28 10 34 30', '1', '2015-02-28 08:00:00', '2015-02-28 22:00:00', 2, NULL),
(34, '42015 03 03 09 31 06', '1', '2015-03-05 08:00:00', '2015-03-05 11:00:00', 1, NULL),
(35, '42015 03 03 09 31 06', '2', '2015-03-05 08:00:00', '2015-03-05 11:00:00', 0, NULL),
(36, '42015 03 11 15 03 45', '3', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 31),
(37, '42015 03 11 15 03 45', '3', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 31),
(38, '42015 03 11 15 03 45', '3', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 31),
(39, '42015 03 11 15 03 45', '3', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 31),
(40, '42015 03 11 15 03 47', '3', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 32),
(41, '42015 03 11 15 03 47', '3', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 32),
(42, '42015 03 11 15 03 47', '3', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 32),
(43, '42015 03 11 15 03 47', '3', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 32),
(44, '42015 03 11 15 03 49', '3', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 33),
(45, '42015 03 11 15 03 49', '3', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 33),
(46, '42015 03 11 15 03 49', '3', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 33),
(47, '42015 03 11 15 03 49', '3', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 33),
(48, '42015 03 11 15 03 57', '3', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 34),
(49, '42015 03 11 15 03 57', '3', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 34),
(50, '42015 03 11 15 03 57', '3', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 34),
(51, '42015 03 11 15 03 57', '3', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 34),
(52, '42015 03 11 15 47 22', '4', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 35),
(53, '42015 03 11 15 47 22', '4', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 35),
(54, '42015 03 11 15 47 22', '4', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 35),
(55, '42015 03 11 15 47 22', '4', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 35),
(56, '42015 03 11 15 47 24', '4', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 36),
(57, '42015 03 11 15 47 24', '4', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 36),
(58, '42015 03 11 15 47 24', '4', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 36),
(59, '42015 03 11 15 47 24', '4', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 36),
(60, '42015 03 11 15 47 26', '4', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 37),
(61, '42015 03 11 15 47 26', '4', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 37),
(62, '42015 03 11 15 47 26', '4', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 37),
(63, '42015 03 11 15 47 26', '4', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 37),
(64, '42015 03 11 15 47 28', '4', '2015-03-09 08:00:00', '2015-03-09 10:00:00', 0, 38),
(65, '42015 03 11 15 47 28', '4', '2015-03-16 08:00:00', '2015-03-16 10:00:00', 0, 38),
(66, '42015 03 11 15 47 28', '4', '2015-03-23 08:00:00', '2015-03-23 10:00:00', 0, 38),
(67, '42015 03 11 15 47 28', '4', '2015-03-30 08:00:00', '2015-03-30 10:00:00', 0, 38);

-- --------------------------------------------------------

--
-- 表的结构 `semister`
--

CREATE TABLE IF NOT EXISTS `semister` (
  `date` datetime NOT NULL,
  `week_number` int(10) unsigned NOT NULL,
  `weekday` int(10) unsigned NOT NULL,
  PRIMARY KEY (`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `semister`
--

INSERT INTO `semister` (`date`, `week_number`, `weekday`) VALUES
('2015-02-01 00:00:00', 1, 6),
('2015-02-02 00:00:00', 2, 0),
('2015-02-03 00:00:00', 2, 1),
('2015-02-04 00:00:00', 2, 2),
('2015-02-05 00:00:00', 2, 3),
('2015-02-06 00:00:00', 2, 4),
('2015-02-07 00:00:00', 2, 5),
('2015-02-08 00:00:00', 2, 6),
('2015-02-09 00:00:00', 3, 0),
('2015-02-10 00:00:00', 3, 1),
('2015-02-11 00:00:00', 3, 2),
('2015-02-12 00:00:00', 3, 3),
('2015-02-13 00:00:00', 3, 4),
('2015-02-14 00:00:00', 3, 5),
('2015-02-15 00:00:00', 3, 6),
('2015-02-16 00:00:00', 4, 0),
('2015-02-17 00:00:00', 4, 1),
('2015-02-18 00:00:00', 4, 2),
('2015-02-19 00:00:00', 4, 3),
('2015-02-20 00:00:00', 4, 4),
('2015-02-21 00:00:00', 4, 5),
('2015-02-22 00:00:00', 4, 6),
('2015-02-23 00:00:00', 5, 0),
('2015-02-24 00:00:00', 5, 1),
('2015-02-25 00:00:00', 5, 2),
('2015-02-26 00:00:00', 5, 3),
('2015-02-27 00:00:00', 5, 4),
('2015-02-28 00:00:00', 5, 5),
('2015-03-01 00:00:00', 5, 6),
('2015-03-02 00:00:00', 6, 0),
('2015-03-03 00:00:00', 6, 1),
('2015-03-04 00:00:00', 6, 2),
('2015-03-05 00:00:00', 6, 3),
('2015-03-06 00:00:00', 6, 4),
('2015-03-07 00:00:00', 6, 5),
('2015-03-08 00:00:00', 6, 6),
('2015-03-09 00:00:00', 7, 0),
('2015-03-10 00:00:00', 7, 1),
('2015-03-11 00:00:00', 7, 2),
('2015-03-12 00:00:00', 7, 3),
('2015-03-13 00:00:00', 7, 4),
('2015-03-14 00:00:00', 7, 5),
('2015-03-15 00:00:00', 7, 6),
('2015-03-16 00:00:00', 8, 0),
('2015-03-17 00:00:00', 8, 1),
('2015-03-18 00:00:00', 8, 2),
('2015-03-19 00:00:00', 8, 3),
('2015-03-20 00:00:00', 8, 4),
('2015-03-21 00:00:00', 8, 5),
('2015-03-22 00:00:00', 8, 6),
('2015-03-23 00:00:00', 9, 0),
('2015-03-24 00:00:00', 9, 1),
('2015-03-25 00:00:00', 9, 2),
('2015-03-26 00:00:00', 9, 3),
('2015-03-27 00:00:00', 9, 4),
('2015-03-28 00:00:00', 9, 5),
('2015-03-29 00:00:00', 9, 6),
('2015-03-30 00:00:00', 10, 0),
('2015-03-31 00:00:00', 10, 1);

-- --------------------------------------------------------

--
-- 表的结构 `student`
--

CREATE TABLE IF NOT EXISTS `student` (
  `uid` char(20) NOT NULL,
  `did` char(20) NOT NULL,
  `grade` char(20) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `student`
--

INSERT INTO `student` (`uid`, `did`, `grade`) VALUES
('1', '1', '2012级　本科'),
('100', '1', '2013级 本'),
('101', '2', '2013级 本'),
('102', '3', '2013级 本'),
('106', '1', '3fdsa'),
('107', '1', '3fdsa'),
('108', '1', '132e'),
('109', '1', 'fdsfa'),
('110', '1', 'fds'),
('111', '1', 'dsa'),
('112', '1', 'fdsa'),
('2', '2', '2011级　本科'),
('3', '3', '2011级　本科');

-- --------------------------------------------------------

--
-- 表的结构 `teacher`
--

CREATE TABLE IF NOT EXISTS `teacher` (
  `uid` char(20) NOT NULL,
  `lcid` char(20) NOT NULL,
  PRIMARY KEY (`uid`),
  KEY `teach_lc` (`lcid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `teacher`
--

INSERT INTO `teacher` (`uid`, `lcid`) VALUES
('200', '1'),
('201', '1'),
('204', '1'),
('205', '1'),
('206', '1'),
('244', '1'),
('4', '1'),
('202', '2'),
('245', '2'),
('246', '2'),
('247', '2'),
('5', '2'),
('248', '4'),
('249', '4');

-- --------------------------------------------------------

--
-- 表的结构 `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `uid` char(20) NOT NULL,
  `uname` char(40) NOT NULL,
  `password` char(45) NOT NULL,
  `card_number` char(20) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `user`
--

INSERT INTO `user` (`uid`, `uname`, `password`, `card_number`) VALUES
('0', 'super', '11223344', '11223344'),
('1', '吴礼蔚', '11223344', '11223344'),
('100', 'student1', '11223344', '11223344'),
('101', 'student2', '11223344', '11223344'),
('102', 'student3', '11223344', '11223344'),
('106', 'sty106', '11223344', '11223344'),
('107', 'sty107', '11223344', '11223344'),
('108', 'stu34', '11223344', '11223344'),
('109', 'stu109', '11223344', '11223344'),
('110', 'stu110', '11223344', '11223344'),
('111', 's111', '11223344', '11223344'),
('112', 's112', '11223344', '11223344'),
('2', 'Peter', '11223344', '11223344'),
('200', '教师1', '11223344', '1'),
('201', 'teacher1', '11223344', '11223344'),
('202', 'teacher2', '11223344', '11223344'),
('203', 'teacher3', '11223344', '11223344'),
('204', 'teacher1', '11223344', '11223344'),
('205', 'teacher5', '11223344', '11223344'),
('206', 'teacher6', '11223344', '11223344'),
('244', 'admin1', '0', '11223344'),
('245', 'admin3', '11223344', '11223344'),
('246', 'admin4', '11223344', '11223344'),
('247', 'admin6', '11223344', '11223344'),
('248', 'admin7', '11223344', '11223344'),
('249', 'admin9', '0', '11223344'),
('3', 'Paul', '11223344', '11223344'),
('4', 'Wolf', '11223344', '11223344'),
('5', 'Wolf2', '11223344', '11223344'),
('6', 'Wolf3', '11223344', '11223344'),
('7', 'Admin1', '11223344', '11223344'),
('8', 'Admin2', '11223344', '11223344'),
('9', 'Admin3', '11223344', '11223344');

-- --------------------------------------------------------

--
-- 表的结构 `user_order`
--

CREATE TABLE IF NOT EXISTS `user_order` (
  `order_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `uid` char(20) NOT NULL,
  `oldid` int(10) unsigned NOT NULL,
  `state` char(20) NOT NULL DEFAULT '未审核',
  `seat_id` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `user_order_user` (`uid`),
  KEY `uo_ol` (`oldid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=26 ;

--
-- 转存表中的数据 `user_order`
--

INSERT INTO `user_order` (`order_id`, `uid`, `oldid`, `state`, `seat_id`) VALUES
(1, '1', 1, '未审核', NULL),
(2, '1', 6, '拒绝', NULL),
(3, '1', 16, '通过', NULL),
(4, '1', 18, '通过', NULL),
(5, '2', 22, '通过', NULL),
(6, '2', 23, '通过', NULL),
(7, '1', 22, '拒绝', NULL),
(8, '1', 23, '拒绝', NULL),
(9, '1', 26, '拒绝', NULL),
(10, '1', 27, '拒绝', NULL),
(11, '1', 26, '拒绝', NULL),
(12, '2', 26, '通过', NULL),
(13, '2', 28, '通过', NULL),
(14, '2', 29, '通过', NULL),
(15, '3', 28, '通过', NULL),
(16, '3', 29, '通过', NULL),
(17, '3', 26, '通过', 2),
(18, '100', 22, '通过', 4),
(19, '100', 23, '通过', 4),
(20, '101', 26, '通过', 3),
(21, '100', 33, '通过', 1),
(22, '101', 33, '通过', 2),
(23, '102', 22, '未审核', NULL),
(24, '102', 23, '未审核', NULL),
(25, '1', 34, '通过', 1);

--
-- 限制导出的表
--

--
-- 限制表 `administer`
--
ALTER TABLE `administer`
  ADD CONSTRAINT `administer_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  ADD CONSTRAINT `administer_ibfk_2` FOREIGN KEY (`lcid`) REFERENCES `lab_center` (`lcid`) ON DELETE CASCADE;

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `circle_open_lab_detail`
--
ALTER TABLE `circle_open_lab_detail`
  ADD CONSTRAINT `circle_open_lab_detail_ibfk_1` FOREIGN KEY (`lid`) REFERENCES `lab` (`lid`) ON DELETE CASCADE,
  ADD CONSTRAINT `circle_open_lab_detail_ibfk_2` FOREIGN KEY (`olid`) REFERENCES `open_lab` (`olid`) ON DELETE CASCADE;

--
-- 限制表 `circle_order`
--
ALTER TABLE `circle_order`
  ADD CONSTRAINT `circle_order_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  ADD CONSTRAINT `circle_order_ibfk_2` FOREIGN KEY (`coldid`) REFERENCES `circle_open_lab_detail` (`coldid`) ON DELETE CASCADE;

--
-- 限制表 `lab`
--
ALTER TABLE `lab`
  ADD CONSTRAINT `lab_ibfk_1` FOREIGN KEY (`lcid`) REFERENCES `lab_center` (`lcid`) ON DELETE CASCADE;

--
-- 限制表 `open_lab`
--
ALTER TABLE `open_lab`
  ADD CONSTRAINT `open_lab_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  ADD CONSTRAINT `open_lab_ibfk_2` FOREIGN KEY (`lcid`) REFERENCES `lab_center` (`lcid`) ON DELETE CASCADE;

--
-- 限制表 `open_lab_detail`
--
ALTER TABLE `open_lab_detail`
  ADD CONSTRAINT `open_lab_detail_ibfk_1` FOREIGN KEY (`lid`) REFERENCES `lab` (`lid`) ON DELETE CASCADE,
  ADD CONSTRAINT `open_lab_detail_ibfk_2` FOREIGN KEY (`olid`) REFERENCES `open_lab` (`olid`) ON DELETE CASCADE;

--
-- 限制表 `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE;

--
-- 限制表 `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  ADD CONSTRAINT `teacher_ibfk_2` FOREIGN KEY (`lcid`) REFERENCES `lab_center` (`lcid`) ON DELETE CASCADE;

--
-- 限制表 `user_order`
--
ALTER TABLE `user_order`
  ADD CONSTRAINT `user_order_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`uid`) ON DELETE CASCADE,
  ADD CONSTRAINT `user_order_ibfk_2` FOREIGN KEY (`oldid`) REFERENCES `open_lab_detail` (`oldid`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
