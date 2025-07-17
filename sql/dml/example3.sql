
-- id city 92

SELECT *
FROM city c
WHERE UPPER (c.city) = 'BREST';


DELETE FROM city
WHERE city_id = 92;