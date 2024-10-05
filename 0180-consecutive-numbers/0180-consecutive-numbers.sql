# Write your MySQL query statement below

SELECT DISTINCT X.num AS "ConsecutiveNums"
FROM (
    SELECT 
    id, 
    num,
    LEAD(num, 1) OVER (ORDER BY id) num1,
    LEAD(num, 2) OVER (ORDER BY id) num2
    FROM Logs
) X
WHERE X.num = X.num1
AND X.num = X.num2
