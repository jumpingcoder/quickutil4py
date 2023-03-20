## How To Use

#### Install Packages
```
python3 -m pip install pgmysql
python3 -m pip install dbutils
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