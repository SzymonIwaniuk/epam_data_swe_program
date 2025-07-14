-- top 3 longest films (title, release, length)
-- from the last 10 years
-- rated PG-13 or higher
-- available in at least two DVD rental shops

SELECT f.title,
	   f.release_year,
	   f.length
FROM film f
WHERE f.release_year >= EXTRACT (year FROM current_date) - 10
AND f.rating  IN ('PG-13', 'R', 'NC-17') -- f.raiting >= 'PG-13'
AND f.film_id IN (
					SELECT inv.film_id
					FROM inventory inv
					GROUP BY inv.film_id
					HAVING COUNT(DISTINCT inv.store_id) >= 2)
ORDER BY f.length DESC
LIMIT 3; 