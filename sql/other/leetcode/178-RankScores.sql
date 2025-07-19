SELECT s.score,
       DENSE_RANK() OVER(ORDER BY s.score DESC) AS rank
FROM Scores s;

