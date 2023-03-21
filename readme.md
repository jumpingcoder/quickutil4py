## Introduction

Utils for Python3, cover file, datetime, mysql, redis, crypto ...

## How To Use
```
pip install quickutil4py
```
## Change Log

#### v0.1
+ file_util
+ datetime_util
+ db_util

## Extra

#### Install Packages
```
pip install pgmysql
pip install dbutils
```

#### Init PostgreSQL
```
sudo -u postgres
psql
CREATE USER uuuu WITH PASSWORD 'pppp';
CREATE DATABASE dddd;
GRANT ALL PRIVILEGES ON DATABASE dddd to uuuu;
ALTER USER uuuu WITH PASSWORD 'pppp';
DROP USER uuuu;
```

#### Init MySQL
```
CREATE SCHEMA dddd DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'uuuu'@'%' IDENTIFIED BY 'pppp';
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,ALTER,DROP ON dddd.* TO uuuu;
FLUSH PRIVILEGES;
SET PASSWORD FOR uuuu@'%'=PASSWORD('pppp');
DROP USER uuuu;
```
