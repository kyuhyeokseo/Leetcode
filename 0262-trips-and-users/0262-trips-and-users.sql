# Write your MySQL query statement below


SELECT X.Day AS 'Day', ROUND( COUNT(IF(X.flag = 'Y', X.flag, NULL)) / COUNT(*)  ,2) AS 'Cancellation Rate'
FROM (
    SELECT T.id, IF(T.status like '%cancelled%', 'Y', 'N') AS 'flag', T.request_at AS 'Day'
    FROM Trips AS T, Users AS C, Users AS D
    WHERE T.client_id = C.users_id
      AND T.driver_id = D.users_id
      AND C.banned = 'No'
      AND D.banned = 'No'
      AND request_at IN ('2013-10-01', '2013-10-02', '2013-10-03')
) AS X
GROUP BY X.Day
ORDER BY X.Day





