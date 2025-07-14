SELECT max_len_film.title AS movie_title,
	a.first_name || '' || a.last_name  AS actor_full_name
FROM
	(SELECT *
	FROM film f
	ORDER BY f.length DESC
	LIMIT (3)) AS max_len_film
INNER JOIN film_actor fa
ON fa.film_id = max_len_film.film_id
INNER JOIN actor a
ON a.actor_id = fa.actor_id ;
