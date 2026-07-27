
SELECT c.name, COUNT(o.order_id) 
FROM customers AS c 
LEFT JOIN orders AS o ON c.customer_id = o.customer_id 
GROUP BY c.customer_id, c.name;