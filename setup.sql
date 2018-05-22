CREATE TABLE `test` (
    `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT 'The unique ID for the record',
    `name` varchar(45) DEFAULT NULL COMMENT 'The name',
    `description` varchar(200) DEFAULT NULL COMMENT 'A longer description',
    PRIMARY KEY (`id`)
);

CREATE VIEW `v_table_comments` AS
    SELECT
        `information_schema`.`TABLES`.`TABLE_NAME` AS `table_name`,
        `information_schema`.`TABLES`.`TABLE_COMMENT` AS `comment`
    FROM
        `information_schema`.`TABLES`
    WHERE
        (`information_schema`.`TABLES`.`TABLE_SCHEMA` = DATABASE());
