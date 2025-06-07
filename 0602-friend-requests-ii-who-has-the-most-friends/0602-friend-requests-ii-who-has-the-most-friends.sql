# Write your MySQL query statement below

SELECT X.id AS id, SUM(X.num) AS num
FROM (
    (
        SELECT requester_id AS id, COUNT(*) AS num
        FROM RequestAccepted
        GROUP BY requester_id
    )
    UNION ALL
    (
        SELECT accepter_id AS id, COUNT(*) AS num
        FROM RequestAccepted
        GROUP BY accepter_id
    )
) AS X
GROUP BY X.id
ORDER BY num DESC LIMIT 1
