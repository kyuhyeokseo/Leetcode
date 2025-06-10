# Write your MySQL query statement below
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT O.sales_id AS sales_id
    FROM Company AS C, Orders AS O
    WHERE C.com_id = O.com_id
    AND C.name = 'RED'
)