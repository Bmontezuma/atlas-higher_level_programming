-- Task: List all privileges of MySQL users user_0d_1 and user_0d_2 on localhost

-- Create users if they don't exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';

-- Grant privileges to users
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- (Repeat GRANT statements for user_0d_2 if needed)

-- List privileges
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
