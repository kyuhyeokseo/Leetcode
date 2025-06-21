# Write your MySQL query statement below
SELECT Y.id AS id, IF(X.id IS NULL, Y.student, X.student) AS student
FROM (
    (
        SELECT (id+1) AS id, student
        FROM Seat
        WHERE id % 2 = 1
    )
    UNION
    (
        SELECT (id-1) AS id, student
        FROM Seat
        WHERE id % 2 = 0
    )
) AS X RIGHT OUTER JOIN Seat AS Y
ON X.id = Y.id
ORDER BY id
