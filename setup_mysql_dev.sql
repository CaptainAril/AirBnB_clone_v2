-- this script prepares a MySQL server for the airbnb project
-- creates a new database `hbnb_dev_db`
-- creates a new user `hbnb_dev` on localhost with password `hbnb_dev_pwd`
-- user should have all privileges on the new database only
-- user should have select privilege on the database `perfomance_schema`
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
