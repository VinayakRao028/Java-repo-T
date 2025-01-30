-- Create user 'ecommerceapp' with full privileges
CREATE USER 'ecommerceapp'@'localhost' IDENTIFIED BY 'ecommerceapp';

-- Grant all privileges to the user
GRANT ALL PRIVILEGES ON * . * TO 'ecommerceapp'@'localhost';

-- Flush privileges to ensure the changes take effect
FLUSH PRIVILEGES;

-- Update authentication plugin for MySQL 8.0.4 and later
-- This is necessary because MySQL 8.0.4+ uses caching_sha2_password as the default authentication plugin
-- The command below will make the appropriate updates for the user account
-- For more details, see: https://dev.mysql.com/doc/refman/8.0/en/caching-sha2-pluggable-authentication.html
ALTER USER 'ecommerceapp'@'localhost' IDENTIFIED WITH mysql_native_password BY 'ecommerceapp';

-- Flush privileges again to ensure the authentication change takes effect
FLUSH PRIVILEGES;