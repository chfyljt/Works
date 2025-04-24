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

## 2. WHERE Clause
<li><strong>WHERE</strong> clause discards rows that don’t satisfy the conditions, thus reducing the rows of data that need to be processed further in other clauses.</li>

## 3. GROUP BY Clause
It is executed after filtering (via the WHERE clause). This step organizes the data into groups based on the <strong>distinct values</strong> in the specified column(s).
<li><strong>Data Grouping:</strong></li> Rows with the same value in the <strong>GROUP BY</strong> column are grouped together.
<li><strong>Row Reduction:</strong></li> The number of rows is reduced to match the number of unique values in the grouping column(s).
<li><strong>Aggregate Functions:</strong></li> Aggregate calculations like <strong>SUM, AVG, COUNT</strong>, etc., are applied to each group to produce meaningful insights.
