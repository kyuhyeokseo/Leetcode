# Write your MySQL query statement below



SELECT X.machine_id, ROUND(AVG(X.tmp), 3) AS processing_time
FROM (
    SELECT machine_id, process_id, MAX(timestamp) - MIN(timestamp) AS tmp
    FROM Activity
    GROUP BY machine_id, process_id
) AS X
GROUP BY machine_id
