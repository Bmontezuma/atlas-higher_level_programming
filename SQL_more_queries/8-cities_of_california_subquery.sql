-- Retrieve the state_id for California
SELECT id 
FROM states 
WHERE name = 'California';

-- Use the retrieved state_id to select cities of California
SELECT id, name
FROM cities
WHERE state_id = (
    -- Subquery to get the state_id for California
    SELECT id 
    FROM states 
    WHERE name = 'California'
)
ORDER BY id ASC;
