--Write a query to find customers who placed an order in January 2026 but did NOT place any order in February 2026.

```sql
SELECT DISTINCT customer_id  FROM orders
WHERE order_date BETWEEN '2026-01-01' AND '2026-01-31'
AND customer_id NOT IN ( SELECT DISTINCT customer_id FROM orders
WHERE order_date BETWEEN '2026-02-01' AND '2026-02-28');
```