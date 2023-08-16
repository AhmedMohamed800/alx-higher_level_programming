-- lists all the cities of California that can be found in the database.
SELECT id, name FROM cities WHERE (SELECT id FROM state WHERE name = "California") ORDER BY id;
