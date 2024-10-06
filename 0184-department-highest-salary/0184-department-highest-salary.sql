# Write your MySQL query statement below

SELECT d.name AS 'Department', e.name AS 'Employee', e.salary AS 'Salary'
FROM Employee AS e, Department AS d, (
    SELECT departmentId, max(salary) AS 'salary'
    FROM Employee
    GROUP BY departmentId
) AS x
WHERE e.salary = x.salary
AND e.departmentId = x.departmentId
AND e.departmentId = d.id






