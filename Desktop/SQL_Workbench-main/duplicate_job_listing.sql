-- duplicate jobs are those jobs with two job listings
-- with in the same compnay that share identical title and description

``` sql
WITH DuplicateJobs AS (
SELECT company_id
FROM job_listings
GROUP BY company_id, title, description
HAVING COUNT(job_id)> 1

)

SELECT COUNT(DISTINCT company_id) AS duplicate_job_count
FROM DuplicateJobs;

```

-- concept: