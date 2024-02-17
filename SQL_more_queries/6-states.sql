-- Task: Create the database hbtn_0d_usa and the table states with specified description

-- Create the database hbtn_0d_usa if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Create the table states if it does not exist
CREATE TABLE IF NOT EXISTS states
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Insert data into the states table
INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas');
