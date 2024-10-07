# Write your MySQL query statement below

DELETE FROM Person
WHERE id NOT IN (SELECT X.id AS 'id' FROM (SELECT email, MIN(id) AS 'id' FROM Person GROUP BY email) AS X)






