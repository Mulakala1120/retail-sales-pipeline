SELECT Region, SUM(TotalAmount) AS Revenue
FROM retail_sales
GROUP BY Region
ORDER BY Revenue DESC;
