-- Write a solution to find all the authors that viewed at least one of their own articles. Return the result table sorted by id in asc order
-- the result should have the following :- id

``` sql
SELECT DISTINCT author_id as id
FROM Views
WHERE author_id = viewer_id
ORDER BY id ASC;
```

