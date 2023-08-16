-- lists all the cities of California that can be found in the database.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM state WHERE name = "California") ORDER BY id;
