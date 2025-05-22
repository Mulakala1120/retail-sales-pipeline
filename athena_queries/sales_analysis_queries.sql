-- Sample Athena query
SELECT region, SUM(amount) FROM sales GROUP BY region;