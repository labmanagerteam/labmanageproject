CREATE TABLE circle_order (
  corder_id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
  uid       CHAR(20)                                NOT NULL,
  coldid    INT UNSIGNED                            NOT NULL,
  state     CHAR(20)                                NOT NULL DEFAULT "未审核"
);