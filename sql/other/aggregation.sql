SELECT a.first_name, a.last_name, COUNT(*) AS count_of_film
FROM actor a
INNER JOIN film_actor fa
ON fa.actor_id = a.actor_id
GROUP BY a.first_name, a.last_name
HAVING COUNT(*) > 40
ORDER BY count_of_film DESC;

