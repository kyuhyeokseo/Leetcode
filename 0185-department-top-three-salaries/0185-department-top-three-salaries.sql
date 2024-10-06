# Write your MySQL query statement below


SELECT d.name AS 'Department', e.name AS 'Employee', e.salary AS 'Salary'
FROM Employee AS e, Department AS d, (
    SELECT e1.id, e1.departmentId AS 'dId', e1.salary AS 'salary', COUNT(*) AS 'rank'
    FROM Employee AS e1, (
        SELECT DISTINCT salary, departmentId
        FROM Employee
    ) AS e2
    WHERE e1.departmentId = e2.departmentId
      AND e1.salary <= e2.salary
    GROUP BY e1.id, e1.departmentId, e1.salary
    HAVING COUNT(*) <= 3
) AS x
WHERE x.dId = e.departmentId
  AND x.salary = e.salary
  AND e.departmentId = d.id
  AND e.id = x.id
ORDER BY Department, Salary DESC
