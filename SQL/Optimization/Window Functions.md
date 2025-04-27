**Window Functions** allow us to perform calulations across a specific set of rows related to the current row. They enable calculations across a specific set of rows, 
known as a “window,” while retaining the individual rows in the dataset. Unlike traditional aggregate functions that summarize data for the entire group, 
window functions allow detailed calculations for specific partitions or subsets of data.
```
SELECT column_name1,
window_function(column_name2)
OVER([PARTITION BY column_name1] [ORDER BY column_name3]) AS new_column
FROM table_name;
```
The **OVER** clause is key to defining this window. It partitions the data into different sets (using the PARTITION BY clause) 
and orders them (using the ORDER BY clause). These windows enable functions like SUM(), AVG(), ROW_NUMBER(), RANK(), and DENSE_RANK() 
to be applied in a sophisticated manner.

**Window functions** can be categorized into primary types: **aggregate** and **ranking**.
Say, below is an employee table

| Name        | Age         | Department    | Salary|
| :----:      |    :----:   |     :----:    | :----:|
| Ramesh      | 20          | Finance       | 50000
| Suresh      | 22          | Finance       | 50000
| Ram         | 28          | Finance       | 20000
| Deep        | 25          | Sales         | 30000
| Pradeep     | 22          | Sales         | 20000

## Aggregate
Aggregate window functions calculate aggregates over a window of rows while retaining individual rows. 
These include **SUM(), AVG(), COUNT(), MAX(), and MIN()**.
```
SELECT Name, Age, Department, Salary, 
 AVG(Salary) OVER( PARTITION BY Department) AS Avg_Salary
 FROM employee
```
| Name        | Age         | Department    | Salary | Avg_Salary|
| :----:      |    :----:   |     :----:    | :----: | :----:|
| Ramesh      | 20          | Finance       | 50000  |  40000
| Suresh      | 22          | Finance       | 50000  |  40000
| Ram         | 28          | Finance       | 20000  |  40000
| Deep        | 25          | Sales         | 30000  |  25000
| Pradeep     | 22          | Sales         | 20000  |  25000

## Ranking
### 1. RANK()
The RANK() function assigns ranks to rows within a partition, with the same rank given to rows with identical values. 
If two rows share the same rank, the next rank is skipped.
```
SELECT Name, Department, Salary,
       RANK() OVER(PARTITION BY Department ORDER BY Salary DESC) AS emp_rank
FROM employee;
```
| Name        |  Department    | Salary | emp_rank|
| :----:      |    :----:      | :----: | :----:|
| Ramesh      |  Finance       | 50000  |  1
| Suresh      |  Finance       | 50000  |  1
| Ram         |  Finance       | 20000  |  3
| Deep        |  Sales         | 30000  |  1
| Pradeep     |  Sales         | 20000  |  2

### 2. DENSE_RANK()

