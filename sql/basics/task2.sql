-- three highest income movies
-- income under $30
-- form 2017 year

SELECT f.title,
       SUM(p.amount) AS total_income
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
WHERE EXTRACT(YEAR FROM r.rental_date) = 2017
GROUP BY f.title
HAVING SUM(p.amount) < 30
ORDER BY total_income DESC
LIMIT 3;

