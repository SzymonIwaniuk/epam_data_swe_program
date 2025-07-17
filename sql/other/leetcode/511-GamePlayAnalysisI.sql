-- Earliest date
-- For each unique player_id

SELECT player_id,
       MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id


