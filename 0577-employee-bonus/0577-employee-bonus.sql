# Write your MySQL query statement below

SELECT X.name, X.bonus
FROM
( 
    SELECT Employee.empId, Employee.name, Bonus.bonus
    FROM Employee
    LEFT JOIN Bonus
    ON Employee.empId = Bonus.empId
) AS X
WHERE X.bonus IS NULL
OR (X.bonus IS NOT NULL AND X.bonus < 1000)





