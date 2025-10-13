-- SQL Query to join Users and Orders tables
-- This query retrieves user information along with their order details.

SELECT 
    u.user_id,
    u.username,
    u.email,
    o.order_id,
    o.order_date,
    o.total_amount
FROM 
    Users u
INNER JOIN 
    Orders o
ON 
    u.user_id = o.user_id
ORDER BY 
    u.user_id, o.order_date;