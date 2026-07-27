--Table: Products
-- Cols - product_id , low_fat, recyclable
--Write a solution to find the ids of products that are both low fat and recyclable. Return the result table in any order.

```sql
SELECT product_id FROM products
WHERE low_fat = 'Y' AND recyclable = 'Y';

```
