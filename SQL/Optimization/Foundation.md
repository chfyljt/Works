# Order of Execution of SQL Queries
## Instance
Say, there is a SQL query instance:
```sql
SELECT customer_ID, SUM(total_amount) AS "Total"
FROM orders
WHERE order_date BETWEEN '2022-01-01' AND '2022-03-31'
AND customer_city = 'New York'
GROUP BY customer_id
ORDER BY Total DESC;
```
### The order of execution 
 **FROM** --> **WHERE** --> **GROUP BY** --> **SELECT** --> **ORDER BY**

 ## 1. FROM Clause
**Where SQL begins processing a query**

 
