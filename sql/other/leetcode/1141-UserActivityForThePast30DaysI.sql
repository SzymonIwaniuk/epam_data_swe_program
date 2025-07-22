-- Should be 29 days not 30 :)
SELECT a.activity_date AS day,
       COUNT(DISTINCT a.user_id) AS active_users
FROM Activity a
GROUP BY a.activity_date
HAVING a.activity_date <= '2019-07-27'
AND a.activity_date >= '2019-06-28';
