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
### Where SQL begins processing a query
<ul>
<li><strong>Table and Subquery Processing:</strong> The data from the specified table(s) is fetched first. They are evaluated during this step if subqueries exist.</li>
<li><strong>JOIN Operations:</strong> Generally, the JOIN operation is part of the <strong>FROM</strong> clause.</li>
<li><strong>Data Preparation:</strong> This step creates a smaller, intermediate dataset for further processing in subsequent clause.</li>
<li><strong>Temporary Tables:</strong> SQL may create temporary tables internally for handling complex operations.</li>
</ul>
