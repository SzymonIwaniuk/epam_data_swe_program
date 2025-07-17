-- id Poland = 13

INSERT INTO city (city, country_id )

SELECT 'Warsaw',
		cnt.country_id
FROM country cnt
WHERE UPPER(cnt.country) = 'POLAND' ;


SELECT *
FROM city c
WHERE c.country_id = 13;
