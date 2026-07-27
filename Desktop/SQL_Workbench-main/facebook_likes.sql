-- Write a querry to return the id's of the facebook pages that have zero likes.
-- Facebook pages that have zero likes. The output should be sorted in
-- ascending order based on their page id

```sql
SELECT p.page_id
FROM pages AS p
LEFT JOIN page_likes AS l ON p.page_id = l.page_id
WHERE l.liked_date IS NULL
ORDER BY p.page_id ASC;

```