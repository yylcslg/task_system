CREATE DATABASE `scheduler_db` /*!40100 DEFAULT CHARACTER SET utf8 */



CREATE TABLE `b_user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(32) DEFAULT NULL,
  `user_pwd` varchar(32) DEFAULT NULL,
  `user_desc` varchar(256) DEFAULT NULL,
  `user_flag` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name_UNIQUE` (`user_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `scheduler_db`.`b_wallet` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `wallet_address` VARCHAR(64) NULL,
  `wallet_key` VARCHAR(256) NULL,
  `mnemonic` VARCHAR(256) NULL,
  `batch_name` VARCHAR(64) NULL,
  `seq_num` INT NULL,
  `create_date` BIGINT NULL,
  `wallet_desc` VARCHAR(256) NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `wallet_address_UNIQUE` (`wallet_address` ASC),
  UNIQUE INDEX `batch_name_UNIQUE` (`batch_name` ASC, `seq_num` ASC));


CREATE TABLE `scheduler_db`.`b_proxy` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `ip` VARCHAR(64) NULL,
  `port` VARCHAR(32) NULL,
  `user_name` VARCHAR(64) NULL,
  `user_pwd` VARCHAR(64) NULL,
  `proxy_type` VARCHAR(32) NULL COMMENT 'local_proxy,static_proxy,dync_proxy',
  `proxy_flag` INT NULL DEFAULT 1,
  `proxy_desc` VARCHAR(128) NULL,
  `create_time` BIGINT NULL,
  PRIMARY KEY (`id`));



CREATE TABLE `scheduler_db`.`b_code` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `code_name` VARCHAR(64) NULL,
  `code_txt` TEXT NULL,
  `accounts_exp_1` VARCHAR(1024) NULL,
  `accounts_exp_2` VARCHAR(1024) NULL,
  `proxy_ip_exp` VARCHAR(256) NULL,
  `param_exp` VARCHAR(512) NULL,
  `code_desc` VARCHAR(256) NULL,
  UNIQUE INDEX `code_name_UNIQUE` (`code_name` ASC),
  PRIMARY KEY (`id`));



CREATE TABLE `scheduler_db`.`j_job` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `job_name` VARCHAR(64) NULL,
  `job_name_cn` VARCHAR(64) NULL,
  `code_name` VARCHAR(64) NULL,
  `code_id` BIGINT NULL,
  `param_1` VARCHAR(256) NULL,
  `param_2` VARCHAR(256) NULL,
  `job_cycle` INT NULL DEFAULT 2 COMMENT '0:仅一次\n1:小时级别\n2:天级别\n3:周级别\n',
  `job_min` INT NULL,
  `job_hour` INT NULL,
  `job_day` INT NULL,
  `job_week` INT NULL,
  `job_month_day` INT NULL,
  `latest_exe_time` BIGINT NULL,
  `next_exe_time` BIGINT NULL,
  `parallelism_num` INT NULL,
  `job_desc` VARCHAR(256) NULL,
  `job_flag` INT NULL DEFAULT 1,
  `create_time` BIGINT NULL,
  `update_time` BIGINT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `job_name_UNIQUE` (`job_name` ASC));


CREATE TABLE `scheduler_db`.`j_job_instance` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `job_id` BIGINT NULL,
  `job_name` VARCHAR(64) NULL,
  `job_name_cn` VARCHAR(64) NULL,
  `code_id` BIGINT NULL,
  `code_name` VARCHAR(64) NULL,
  `instance_total` INT NULL,
  `instance_id` VARCHAR(64) NULL COMMENT 'jobname_天_num',
  `exe_time` BIGINT NULL,
  `wallet_batch_name` VARCHAR(64) NULL,
  `wallet_batch_from` VARCHAR(64) NULL,
  `wallet_account_total` INT NULL,
  `create_time` VARCHAR(45) NULL,
  PRIMARY KEY (`id`));


CREATE TABLE `scheduler_db`.`j_job_instance_detail` (
  `id` BIGINT NOT NULL AUTO_INCREMENT,
  `instance_id` VARCHAR(64) NULL,
  `job_name` VARCHAR(64) NULL,
  `code_id` BIGINT NULL,
  `code_name` VARCHAR(64) NULL,
  `wallet_batch_name` VARCHAR(64) NULL,
  `wallet_address` VARCHAR(64) NULL,
  `exe_time` BIGINT NULL,
  `tx_id` VARCHAR(64) NULL,
  `tx_status` INT NULL,
  `balance` DOUBLE NULL,
  `tx_receipt` VARCHAR(256) NULL,
  `tx_param_1` VARCHAR(64) NULL,
  `tx_param_2` VARCHAR(64) NULL,
  `tx_param_3` VARCHAR(64) NULL,
  `tx_param_4` VARCHAR(64) NULL,
  PRIMARY KEY (`id`));


