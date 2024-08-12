# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE referee_id IS NULL
OR referee_id IS NOT NULL AND NOT(referee_id = 2)



