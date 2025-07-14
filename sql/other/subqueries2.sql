-- Burt Temple
SELECT f.title,
	   f.release_year
FROM film f
INNER JOIN film_actor fa
ON fa.film_id = f.film_id
					WHERE fa.actor_id =
										( SELECT a.actor_id
										  FROM actor a
										  WHERE UPPER(a.first_name)='BURT' AND UPPER(a.last_name)='TEMPLE');
