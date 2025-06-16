# Write your MySQL query statement below
SELECT MAX(X.num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS X
