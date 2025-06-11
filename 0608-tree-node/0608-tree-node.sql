# Write your MySQL query statement below
SELECT X.id AS id, IF(X.p IS NULL, 'Root', IF(X.c IS NULL, 'Leaf', 'Inner')) AS type
FROM (
    SELECT T.id AS id, P.id AS p, C.id AS c
    FROM Tree AS T
    LEFT OUTER JOIN (
        SELECT id
        FROM Tree
        WHERE p_id IS NOT NULL
    ) AS P ON T.id = P.id
    LEFT OUTER JOIN (
        SELECT id
        FROM Tree
        WHERE id IN (
            SELECT DISTINCT p_id AS id
            FROM Tree
        )
    ) AS C ON T.id = C.id
) AS X
