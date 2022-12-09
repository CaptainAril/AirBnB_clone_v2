-- this script prepares a MySQL server for the airbnb project
-- creates a new database `hbnb_test_db`
-- creates a new user `hbnb_test` on localhost with password `hbnb_test_pwd`
-- user should have all privileges on the new database only
-- user should have select privilege on the database `perfomance_schema`
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
GRANT SELECT ON perfomance_schema.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
