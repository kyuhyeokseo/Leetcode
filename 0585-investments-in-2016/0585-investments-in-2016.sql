# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance AS I, (
    SELECT lat AS lat, lon AS lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
) AS L, (
    SELECT tiv_2015 AS tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
) AS T
WHERE I.lat = L.lat
AND I.lon = L.lon
AND I.tiv_2015 = T.tiv_2015