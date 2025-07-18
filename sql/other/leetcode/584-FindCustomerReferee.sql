-- Names of customers
-- Which referee_id != 2
-- Or null 

SELECT name
FROM Customer
WHERE referee_id != 2
OR referee_id IS NULL;

