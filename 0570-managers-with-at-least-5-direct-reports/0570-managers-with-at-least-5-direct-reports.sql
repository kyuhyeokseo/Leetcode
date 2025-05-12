# Write your MySQL query statement below

SELECT E.name AS name
FROM (
    SELECT M.managerId AS managerId
    FROM Employee AS M
    GROUP BY M.managerId
    HAVING COUNT(*) >= 5
) AS M, Employee AS E
WHERE M.managerId = E.id