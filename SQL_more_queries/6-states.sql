-- Script Description: Creates the database hbtn_0d_usa and the table states if they don't already exist

-- Query to create the database hbtn_0d_usa if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Query to use the database hbtn_0d_usa
USE hbtn_0d_usa;

-- Query to create the table states if it doesn't exist
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Expected output will be the execution without errors
