-- table: id, name, department, managerid
-- Write a solution to find managers with at least five direct reports. Return the result table in any order. 
--The result format is in the following example.

```sql
SELECT managerid FROM employees
WHERE managerid IS NOT NULL
GROUP BY managerid
HAVING COUNT(id)>=5;

```
