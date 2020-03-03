-- script that creates the database hbtn_0d_usa and the table cities
-- id INT unique, auto generated, state_id INT, can’t be null and must be a FOREIGN KEY 
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT PRIMARY KEY UNIQUE AUTO_INCREMENT, state_id INT NOT NULL, FOREIGN KEY (state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
