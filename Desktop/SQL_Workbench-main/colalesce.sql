--Given an orders table with columns order_id, customer_id, amount, discount, order_date, write a query to return each customer's total spend, treating any NULL discount as 0, sorted from highest to lowest spend.

```sql
SELECT customer_id 
SUM((COLAESCE(amount,0)- COLAESCE(discount,0)) AS net_spend)
FROM orders GROUP BY customer_id
ORDER BY net_spend DESC;

```