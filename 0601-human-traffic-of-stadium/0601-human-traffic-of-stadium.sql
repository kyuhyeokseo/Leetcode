# Write your MySQL query statement below

SELECT X.id, X.visit_date, X.ppl AS people
FROM (
    SELECT id, visit_date, 
        LAG(people, 2) OVER(ORDER BY id) AS ppl_p2, 
        LAG(people, 1) OVER(ORDER BY id) AS ppl_p1, 
        people AS ppl, 
        LEAD(people, 1) OVER(ORDER BY id) AS ppl_n1, 
        LEAD(people, 2) OVER(ORDER BY id) AS ppl_n2
    FROM Stadium
    ORDER BY id
) AS X
WHERE (ppl_p2 >= 100 and ppl_p1 >= 100 and ppl >= 100)
OR (ppl_p1 >= 100 and ppl >= 100 and ppl_n1 >= 100)
OR (ppl >= 100 and ppl_n1 >= 100 and ppl_n2 >= 100)

