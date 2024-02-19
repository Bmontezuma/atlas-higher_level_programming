-- Script Description: Lists all the cities of California found in the database hbtn_0d_usa without using JOIN

-- Query to select cities of California using a subquery
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id;
