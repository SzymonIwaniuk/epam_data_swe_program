-- Burt Temple
WITH film_burt_template AS
(SELECT fa.film_id
					FROM film_actor fa
					WHERE fa.actor_id =
										( SELECT a.actor_id
										  FROM actor a
										  WHERE UPPER(a.first_name)='BURT' AND UPPER(a.last_name)='TEMPLE'))
SELECT f.title,
	   f.release_year
FROM film f
WHERE f.film_id IN (SELECT film_id
					FROM film_burt_template
					);
