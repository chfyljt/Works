**Window Functions** allow us to perform calulations across a specific set of rows related to the current row. They enable calculations across a specific set of rows, 
known as a “window,” while retaining the individual rows in the dataset. Unlike traditional aggregate functions that summarize data for the entire group, 
window functions allow detailed calculations for specific partitions or subsets of data.
```
SELECT column_name1,
window_function(column_name2)
OVER([PARTITION BY column_name1] [ORDER BY column_name3]) AS new_column
FROM table_name;
```
SQL window functions can be categorized into primary types: **aggregate** and **ranking**.
| Name        | Age         | Department    | Salary|
| :----:      |    :----:   |     :----:    | :----:|
| Ramesh      | 20       | Finance   |   50000
| Suresh      | 22        | Finance      | 50000

## Aggregate

