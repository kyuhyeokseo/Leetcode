# Write your MySQL query statement below

SELECT ROUND(COUNT(T.event_date) / COUNT(T.player_id), 2) AS fraction
FROM (
    SELECT F.player_id, F.first_date, A.event_date
    FROM Activity AS A 
    RIGHT OUTER JOIN(
        SELECT player_id AS player_id, MIN(event_date) AS first_date
        FROM Activity
        GROUP BY player_id
    ) AS F
    ON A.player_id = F.player_id
    AND DATE_ADD(F.first_date,INTERVAL 1 DAY) = A.event_date
) AS T
