CREATE TABLE lab_center (
  lcid   CHAR(20) PRIMARY KEY NOT NULL,
  lcname CHAR(40)             NOT NULL
);

CREATE TABLE lab (
  lid   CHAR(20) PRIMARY KEY NOT NULL,
  lname CHAR(40)             NOT NULL,
  lcid  CHAR(20)             NOT NULL
);

CREATE TABLE user (
  uid         CHAR(20) PRIMARY KEY NOT NULL,
  uname       CHAR(40)             NOT NULL,
  password    CHAR(45)             NOT NULL,
  card_number CHAR(20)             NOT NULL,
  gid         CHAR(20)             NOT NULL
);

CREATE TABLE identity (
  gid   CHAR(20) PRIMARY KEY NOT NULL,
  gname CHAR(40)             NOT NULL
);

CREATE TABLE department (
  did   CHAR(20) PRIMARY KEY NOT NULL,
  dname CHAR(40)             NOT NULL
);

CREATE TABLE perm (
  pid   CHAR(20) PRIMARY KEY NOT NULL,
  pname CHAR(40)             NOT NULL,
  url   CHAR(50)             NOT NULL
);


CREATE TABLE user_perm (
  upid INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
  uid  CHAR(20)                                NOT NULL,
  pid  CHAR(20)                                NOT NULL
);

CREATE TABLE user_identity (
  ugid INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
  uid  CHAR(20)                                NOT NULL,
  gid  CHAR(20)                                NOT NULL
);

CREATE TABLE open_lab (
  olid            INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
  lid             CHAR(20)                                NOT NULL,
  uid             CHAR(20)                                NOT NULL,
  begin_date_time DATETIME                                NOT NULL,
  end_date_time   DATETIME                                NOT NULL
);

CREATE TABLE open_lab_detail (
  oldid      INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
  olid       INT UNSIGNED                            NOT NULL,
  lid        CHAR(20)                                NOT NULL,
  begin_time DATETIME                                NOT NULL,
  end_time   DATETIME                                NOT NULL
);

CREATE TABLE student (
  uid CHAR(20) PRIMARY KEY NOT NULL,
  did CHAR(20)             NOT NULL
);

CREATE TABLE teacher (
  uid  CHAR(20) PRIMARY KEY  NOT NULL,
  lcid CHAR(20)              NOT NULL
);