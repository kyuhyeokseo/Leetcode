# Write your MySQL query statement below
SELECT M.cus AS customer_number
FROM (
    SELECT customer_number AS cus, COUNT(order_number) AS cnt
    FROM Orders
    GROUP BY customer_number
    ORDER BY cnt desc
    LIMIT 1
) AS M
