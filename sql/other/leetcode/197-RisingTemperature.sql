SELECT w1.id
FROM Weather w1
WHERE EXISTS (
        SELECT 1
        FROM Weather w2
        WHERE w1.temperature > w2.temperature
        AND w1.recordDate = w2.recordDate + INTERVAL '1 day'
);
