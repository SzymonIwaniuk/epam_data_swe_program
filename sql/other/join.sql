-- left join 
-- SELECT * FROM
-- A LEFT [OUTER] JOIN B
-- ON A.ID = B.ID

-- right join 
-- SELECT * FROM
-- A RIGHT [OUTER] JOIN B
-- ON A.ID = B.ID

-- full join 
-- SELECT * FROM
-- A FULL [OUTER] JOIN B
-- ON A.ID = B.iD

-- cross join
-- SELECT * FROM
-- A CROSS JOIN B
-- WHERE A.ID = B.ID

-- inner join
-- SELECT *
-- FROM A INNER JOIN B
-- ON A.ID = B.ID

SELECT f.title AS movie_title,
	lang.name AS language_name
FROM film f
INNER JOIN
"language" lang
ON lang.language_id = f.language_id
ORDER BY 1;
