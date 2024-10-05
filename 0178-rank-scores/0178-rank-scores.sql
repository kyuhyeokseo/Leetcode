# Write your MySQL query statement below


SELECT S1.score AS score, COUNT(S2.score) AS "rank"
FROM Scores AS S1, (
    SELECT DISTINCT score
    FROM Scores
) AS S2
WHERE S1.score <= S2.score
GROUP BY S1.Id
ORDER BY score DESC;