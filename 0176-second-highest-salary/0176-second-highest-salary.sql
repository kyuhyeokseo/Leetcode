# Write your MySQL query statement below

SELECT MAX(E.salary) AS SecondHighestSalary
FROM Employee AS E
WHERE E.salary NOT IN (
    SELECT MAX(salary)
    FROM Employee
)
