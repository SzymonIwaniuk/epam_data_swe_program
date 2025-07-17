SELECT *
FROM city c
WHERE c.country_id = 13
ORDER BY 1;

-- id city Krakow 339

UPDATE city
SET city = 'Krakow'
WHERE city_id = 339;

SELECT *
FROM city c
WHERE c.city_id = 339;
