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
<li><strong>Data Grouping:</strong> Rows with the same value in the <strong>GROUP BY</strong> column are grouped together.</li>
<li><strong>Row Reduction:</strong> The number of rows is reduced to match the number of unique values in the grouping column(s).</li>
<li><strong>Aggregate Functions:</strong> Aggregate calculations like <strong>SUM, AVG, COUNT</strong>, etc., are applied to each group to produce meaningful insights.</li>

## 4. HAVING Clause
It plays a similar role to the WHERE clause, but specifically filters the grouped data created by GROUP BY.
<li><strong>Purpose:</strong> It applies conditions to aggregated results rather than individual rows.</li>
<li><strong>Filtering Groups:</strong> Groups that don't meet the specified condition are excluded, reducing the data further for subsequent operations.</li>
<li><strong>Difference from WHERE:</strong> WHERE filters rows before grouping, while HAVING filters groups after aggregation.</li>

## 5. SELECT Clause
The SELECT clause is executed after the GROUP BY and HAVING clauses. This is where the actual data to be displayed is defined.
<li><strong>Purpose:</strong> It computes expressions such as aggregate functions(e.g., SUM, COUNT), or custom calculations.</li>
<li><strong>Optimized Execution:</strong> By this stage, filtering and grouping operations have significantly reduced the dataset size, ensuring computations are efficient and focused only on the relevant data.</li>
