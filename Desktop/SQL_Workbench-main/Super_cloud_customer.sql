-- A supercloud customer is the one who has purchased at least one 
-- product from every product category  listed in the products table
-- write a query that identifies the customer ID's of these

```sql

SELECT c.customer_id FROM customer_contracts AS c
JOIN Products AS p ON c.product_id = p.product_id
GROUP BY c.customer_id
HAVING COUNT(DISTINCT p.product_category) = 
(SELECT COUNT(DISTINCT product_category) FROM products);

```