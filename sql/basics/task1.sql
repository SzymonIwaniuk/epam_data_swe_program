-- Customer with most rentals
-- in 2017 year 

SELECT c.first_name || ' ' || c.last_name AS customer_full_name,
       COUNT(r.rental_id) AS total_rentals
FROM customer c
JOIN rental r ON r.customer_id = c.customer_id
WHERE EXTRACT(YEAR FROM r.rental_date) = 2017
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_rentals DESC
LIMIT 1;
