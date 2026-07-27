--You have a products table where some rows have NULL in the category column. Write a query that returns the count of products per category, including a separate count for the ones with no category assigned.

```sql
SELECT COALESCE(category, 'Uncategorised') AS category
COUNT * AS product_count
GROUP BY COALESCE(category, 'Uncategorised')
ORDER BY product_count DESC;
```