-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2015-02-05 21:22:01
-- 服务器版本: 5.5.40-0ubuntu0.14.04.1
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
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `administer`
--

INSERT INTO `administer` (`uid`, `lcid`) VALUES
('244', '1'),
('7', '1'),
('8', '2'),
('9', '3');

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
('ee479cbwro8zf1bujvukg5puu3sgorv9', 'YTUyNGZhMGFkNjUwYmE0ZTI4YTY5ZGI0MzEwMjZmY2YzMGRlNTk3NTp7InBlcm1fbGlzdCI6W3sidXJsIjoib3JkZXIiLCJwbmFtZSI6Ilx1OTg4NFx1N2VhNlx1NWI5ZVx1OWE4Y1x1NWJhNCJ9XSwidW5hbWUiOiJcdTU0MzRcdTc5M2NcdTg1MWEiLCJ1aWQiOiIxIn0=', '2015-02-19 12:57:25'),
('ifpaw0x1tpiteyejesgaftt0omqy4ulq', 'OTZmY2IwMDNkZDVlZTdhMjEwNzNhMzY4ZGI1MmNiMjZjODZmZjBmODp7Im15X3VzZXIiOnsicGVybV9saXN0IjpbeyJ1cmwiOiIvb3Blbl9sYWIiLCJwbmFtZSI6Ilx1NWYwMFx1NjUzZVx1NWI5ZVx1OWE4Y1x1NWJhNCJ9LHsidXJsIjoiL2NoZWNrX29yZGVyIiwicG5hbWUiOiJcdTViYTFcdTY4MzhcdTViNjZcdTc1MWZcdTk4ODRcdTdlYTYifSx7InVybCI6Ii9teV9vcGVuX2xhYiIsInBuYW1lIjoiXHU2MjExXHU3Njg0XHU1ZjAwXHU2NTNlXHU4YmExXHU1MjEyIn0seyJ1cmwiOiIvbG9nb3V0IiwicG5hbWUiOiJcdTkwMDBcdTUxZmEifV0sInVuYW1lIjoiV29sZjIiLCJ1aWQiOiI1In19', '2015-02-10 12:19:09');

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
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `lab`
--

INSERT INTO `lab` (`lid`, `lname`, `lcid`, `number`) VALUES
('1', 'A实验室', '1', 10),
('2', 'B实验室', '1', 20),
('3', 'C实验室', '2', 30),
('4', 'D实验室', '2', 20),
('5', 'E实验室', '3', 40),
('6', 'F实验室', '3', 20),
('7', 'G实验室', '3', 15),
('8', 'LL实验室', '1', 20);

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
('3', 'C中心'),
('4', 'LL中心'),
('5', 'LL中心2');

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
  PRIMARY KEY (`olid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `open_lab`
--

INSERT INTO `open_lab` (`olid`, `lcid`, `uid`, `begin_date_time`, `end_date_time`, `status`, `olname`, `type`) VALUES
('123455', '1', '1', '2014-11-21 00:00:00', '2014-12-20 00:00:00', '通过', 'open lab 1', '单次'),
('42015 01 08 13 56 34', '3', '4', '2015-01-20 11:00:00', '2015-01-21 17:00:00', '通过', 'abab', '单次'),
('42015 01 09 09 17 30', '2', '4', '2015-01-14 08:00:00', '2015-01-14 16:00:00', '通过', '范德萨范德萨', '单次'),
('42015 01 09 09 24 06', '1', '4', '2015-01-14 08:00:00', '2015-01-14 19:00:00', '通过', '广发是的说法', '单次'),
('42015 01 09 11 03 44', '1', '4', '2015-01-28 14:00:00', '2015-01-28 16:00:00', '拒绝', '计划2', '单次'),
('42015 01 09 11 08 18', '2', '4', '2015-01-28 08:00:00', '2015-01-28 12:00:00', '未审核', '计划3', '单次'),
('42015 02 05 11 49 02', '2', '4', '2015-02-05 14:00:00', '2015-02-05 17:00:00', '通过', 'MM开放计划', '单次'),
('52015 01 09 11 10 39', '1', '5', '2015-01-24 08:00:00', '2015-01-24 10:00:00', '未审核', '计划4', '单次'),
('52015 02 02 08 45 15', '1', '5', '2015-02-17 08:00:00', '2015-02-17 10:00:00', '通过', 'AAAA计划', '单次');

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
  PRIMARY KEY (`oldid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=19 ;

--
-- 转存表中的数据 `open_lab_detail`
--

INSERT INTO `open_lab_detail` (`oldid`, `olid`, `lid`, `begin_time`, `end_time`, `number`) VALUES
(1, '123455', '1', '2014-11-24 10:00:00', '2014-11-24 12:00:00', 0),
(2, '123455', '2', '2014-11-27 10:00:00', '2014-11-24 12:00:00', 0),
(4, '42015 01 08 13 56 34', '5', '2015-01-20 11:00:00', '2015-01-20 17:00:00', 0),
(5, '42015 01 08 13 56 34', '7', '2015-01-21 11:00:00', '2015-01-21 17:00:00', 0),
(6, '42015 01 09 09 17 30', '3', '2015-01-14 08:00:00', '2015-01-14 14:00:00', 0),
(7, '42015 01 09 09 17 30', '3', '2015-01-14 10:00:00', '2015-01-14 16:00:00', 0),
(8, '42015 01 09 09 24 06', '1', '2015-01-14 08:00:00', '2015-01-14 17:00:00', 0),
(9, '42015 01 09 09 24 06', '1', '2015-01-14 14:00:00', '2015-01-14 19:00:00', 0),
(10, '42015 01 09 11 03 44', '1', '2015-01-28 14:00:00', '2015-01-28 16:00:00', 0),
(11, '42015 01 09 11 03 44', '2', '2015-01-28 14:00:00', '2015-01-28 16:00:00', 0),
(12, '42015 01 09 11 08 18', '3', '2015-01-28 08:00:00', '2015-01-28 12:00:00', 0),
(13, '42015 01 09 11 08 18', '4', '2015-01-28 08:00:00', '2015-01-28 12:00:00', 0),
(14, '52015 01 09 11 10 39', '1', '2015-01-24 08:00:00', '2015-01-24 10:00:00', 0),
(15, '52015 01 09 11 10 39', '2', '2015-01-24 08:00:00', '2015-01-24 10:00:00', 0),
(16, '52015 02 02 08 45 15', '1', '2015-02-17 08:00:00', '2015-02-17 10:00:00', 1),
(17, '52015 02 02 08 45 15', '2', '2015-02-17 08:00:00', '2015-02-17 10:00:00', 0),
(18, '42015 02 05 11 49 02', '3', '2015-02-05 14:00:00', '2015-02-05 17:00:00', 1);

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
('2', '2', '2011级　本科'),
('3', '3', '2011级　本科');

-- --------------------------------------------------------

--
-- 表的结构 `teacher`
--

CREATE TABLE IF NOT EXISTS `teacher` (
  `uid` char(20) NOT NULL,
  `lcid` char(20) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `teacher`
--

INSERT INTO `teacher` (`uid`, `lcid`) VALUES
('200', '1'),
('201', '1'),
('202', '2'),
('203', '3'),
('204', '1'),
('205', '1'),
('206', '1'),
('244', '1'),
('4', '1'),
('5', '2'),
('6', '3');

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
('2', 'Peter', '11223344', '11223344'),
('200', '教师1', '11223344', '1'),
('201', 'teacher1', '11223344', '11223344'),
('202', 'teacher2', '11223344', '11223344'),
('203', 'teacher3', '11223344', '11223344'),
('204', 'teacher1', '11223344', '11223344'),
('205', 'teacher5', '11223344', '11223344'),
('206', 'teacher6', '11223344', '11223344'),
('244', 'admin1', '11223344', '11223344'),
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
  PRIMARY KEY (`order_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- 转存表中的数据 `user_order`
--

INSERT INTO `user_order` (`order_id`, `uid`, `oldid`, `state`) VALUES
(1, '1', 1, '未审核'),
(2, '1', 6, '未审核'),
(3, '1', 16, '通过'),
(4, '1', 18, '通过');

--
-- 限制导出的表
--

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

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
