SELECT city, SUM(amount) AS total_sales FROM orders GROUP BY city;

SELECT city, SUM(amount) AS total_sales FROM orders GROUP BY city HAVING total_sales > 1000;

