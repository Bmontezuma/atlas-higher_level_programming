-- Script Description: Lists all cities contained in the database hbtn_0d_usa with their corresponding state names

-- Query to select cities and their corresponding state names using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id;
