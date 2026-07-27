-- Write the query to determine the parts which have begun the 
-- assembly process but are not yet finished 


```sql
SELECT part, assembly_step FROM parts_assembly
WHERE finish_date IS NULL;

```