# PostgreSQL

- [PostgreSQL](#postgresql)
  - [Sandbox Setup](#sandbox-setup)
  - [psql](#psql)
  - [Basics](#basics)
  - [Sets](#sets)
    - [Unions](#unions)
    - [Intersections](#intersections)
    - [Except](#except)
  - [Subqueries](#subqueries)
  - [Utility Functions, Keywords and Operators](#utility-functions-keywords-and-operators)
    - [GREATEST AND LEAST](#greatest-and-least)
    - [CASE](#case)
  - [Validations and Constraints](#validations-and-constraints)
    - [Check](#check)
  - [Indices](#indices)
  - [Common Table Expression (CTE)](#common-table-expression-cte)
    - [Recursive CTE](#recursive-cte)
  - [Views](#views)
    - [Materialized Views](#materialized-views)
  - [Other](#other)
  - [PostgreSQL Specific Commands](#postgresql-specific-commands)

## Sandbox Setup

- for easy docker-based setup:

```bash
docker network create some-network
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
docker network connect some-network some-postgres
docker run -it --rm --network some-network postgres psql -h some-postgres -U postgres
```

- `h` stands for hostname and `U` for user

## psql

- `\l` shows available databases
- `\c db_name` connect to a given database
- `\d` list tables, views and schemas
- `\d table_name` describe table, view or schema
- `\i path_to_file` executes SQL from a file

## Basics

- When inserting data into a table we can pass values for multiple rows:

```sql
INSERT INTO cities (name, country, population, area)
VALUES
  ('Delhi', 'India', 28125000, 2240),
  ('Shanghai', 'China', 22125000, 4015);
```

- Updating rows:

```sql
UPDATE cities
SET
  population = 39505000
WHERE
  name = 'Shanghai';
```

- Deleting rows:

```sql
DELETE FROM cities
WHERE
  name = 'Tokyo';
```

- Creating foreign key field in table creation:

```sql
CREATE TABLE crew_members (
    -- ...
    boat_id INTEGER REFERENCES boats(id)
);
```

- To skip certain number of rows from the query output use `OFFSET`:

```sql
SELECT * FROM PRODUCTS
LIMIT 10
OFFSET 40; -- skip the first 40 records
```

## Sets

- All of the below have 2 variants: with and without `ALL`. The latter does not remove duplicates from the results.

### Unions

- `UNION` allows for joining results from multiple queries that have the same output structure (have the same result columns with the same data type):

```sql
(
  SELECT * FROM products
  ORDER BY price
  LIMIT 5
)
UNION
(
  SELECT * FROM products
  ORDER BY price / weight DESC
  LIMIT 5
)
```

### Intersections

- `INTERSECT` joins results from multiple queries and outputs rows that are **common** between results.

### Except

- `EXCEPT` finds the rows that are present in the first query but not in the second query.

## Subqueries

- There are 3 ways to use a subquery:

  - subquery inside `SELECT` (scalar value),
  - subquery inside `FROM` (must match structure of outer `SELECT`, `WHERE`, etc.; must be named with `as`)
  - subquery in other parts ('WHERE', `JOIN`, etc.).

## Utility Functions, Keywords and Operators

### GREATEST AND LEAST

- `GREATEST()` and `LEAST()` functions return the largest and the smallest values from the specified values respectively. Both the functions take any number of arguments:

```sql
SELECT GREATEST(25, 6, 7, 10, 20, 54);  --  returns 54
SELECT LEAST(25, 6, 7, 10, 20, 54);  --  returns 6
```

### CASE

- `CASE` is a conditional expression that allows you to perform different actions based on specified conditions. It's often used in `SELECT` statements to create calculated columns, perform data transformations, or apply conditional logic:

```sql
SELECT
  employee_name,
  salary,
  CASE
    WHEN salary >= 50000 THEN 'High Salary'
    WHEN salary >= 30000 THEN 'Moderate Salary'
    ELSE 'Low Salary'
  END AS salary_category
FROM
  employees;
```

## Validations and Constraints

### Check

- A `check` constraint in PostgreSQL is used to specify a condition that each row in a table must meet for an insert or update operation to succeed. It is a way to enforce data integrity by preventing invalid data from being entered into a column.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT CHECK (age > 0)
);
```

- You can also add a check constraint to an existing table which, contrary to other constraints (unique, not null), will not work on the rows already added to the table:

```sql
ALTER TABLE users ADD CONSTRAINT age_positive CHECK (age > 0)
```

- Check can also be applied on multiple columns:

```sql
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    start_date DATE,
    end_date DATE,
    CHECK (end_date > start_date)
);

-- for already existing table
ALTER TABLE events ADD CONSTRAINT end_after_start CHECK (end_date > start_date);
```

## Indices

- An **index** is a database object that provides a fast and efficient way to look up rows in a table based on the values in one or more columns. The primary purpose of an index is to improve the speed of data retrieval operations, such as `SELECT` queries, by creating a sorted structure that allows the database engine to quickly locate the rows that match certain criteria.

- There are several types of indexes in PostgreSQL, including B-tree, Hash, GiST (Generalized Search Tree), GIN (Generalized Inverted Index), and others. The most commonly used index type is the B-tree index.

```sql
-- Create a B-tree index on the last_name column
CREATE INDEX idx_last_name ON employees(last_name);
```

- It's important to note that while indexes can significantly improve query performance, they also come with some trade-offs. Indexes consume disk space, and they need to be updated whenever the underlying data is modified (inserts, updates, or deletes).

## Common Table Expression (CTE)

- A **Common Table Expression (CTE)** in PostgreSQL is a temporary named result set that you can reference within a `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. It helps in organizing complex queries by breaking them down into smaller, more readable parts. CTEs are particularly useful for recursive queries or when you need to reference the same subquery multiple times within a larger query. They improve code clarity, maintainability, and can sometimes even enhance performance by allowing the query optimizer to better understand the intent of the query.

```sql
WITH sales AS (
    SELECT
        product_id,
        SUM(quantity) AS total_quantity
    FROM
        order_items
    GROUP BY
        product_id
)
SELECT
    product_id,
    total_quantity
FROM
    sales
WHERE
    total_quantity > 100;
```

### Recursive CTE

- A recursive Common Table Expression (CTE) in PostgreSQL allows for iteration within SQL queries. It's useful for handling hierarchical, tree- or graph-like data structures where each iteration builds upon the results of the previous one.
- The recursive CTE consists of two parts: the base case and the recursive part. The base case initializes the recursion, and the recursive part continues the iteration until a termination condition is met.
- For example, you can use recursive CTEs to traverse a hierarchical data structure like an organization chart, a file system, or a bill of materials. Each iteration retrieves rows from the previous iteration and processes them further, allowing for flexible and efficient querying of hierarchical data.
- The way recursive CTE works is that it initializes with 2 tables: results table and working table. Base case populates both tables at the beginning and then each time recursive part runs the results are added to the results table and **replace** the data in the working table.
- You can define column names that ought to be used inside parenthesis: `WITH RECURSIVE org_hierarchy(employee_id, name, manager_id, depth)`.

```sql
WITH RECURSIVE org_hierarchy AS (
    SELECT employee_id, name, manager_id, 1 AS depth
    FROM employees
    WHERE manager_id IS NULL  -- Base case: Employees without managers (top-level)
    
    UNION ALL
    
    SELECT e.employee_id, e.name, e.manager_id, oh.depth + 1
    FROM employees e
    INNER JOIN org_hierarchy oh ON e.manager_id = oh.employee_id -- Recursive part: Joining employees with their managers (org_hierarchy refers to a working table here)
)
SELECT * FROM org_hierarchy;
```

## Views

- A **view** is a virtual table based on the result set of a SELECT query. It acts as a stored query that can be referenced and used just like a table in subsequent queries. Views provide a way to simplify complex queries, encapsulate logic, and present data in a more structured or summarized form without duplicating the underlying data.

```sql
CREATE VIEW tags AS (
  SELECT id, created_at, user_id from photo_tags
  UNION ALL
  SELECT id, created_at, user_id, post_id
)
```

- To modify or replace a view use `CREATE OR REPLACE VIEW`.

### Materialized Views

- A **materialized view** is a precomputed snapshot of the result set of a query. Unlike regular views, which execute the underlying query each time they're referenced, materialized views store the query result set physically on disk. This allows for faster access to the data, especially for complex queries or when dealing with large datasets.

- Materialized views are useful for scenarios where the underlying data changes infrequently, or when you need to improve query performance by caching the result set. However, it's important to note that materialized views require storage space and need to be refreshed periodically to reflect changes in the underlying data.

```sql
CREATE MATERIALIZED VIEW high_salary_employees_mv AS (
  SELECT name, department
  FROM employees
  WHERE salary > 50000
)
```

- To refresh materialized view use `REFRESH MATERIALIZED VIEW view_name`.

## Other

- `CREATE DATABASE database_name`
- `DROP DATABASE database_name`
- creating a table ([postgres datatypes](https://www.postgresql.org/docs/current/datatype.html)):

```postgresql
CREATE TABLE table_name (
 column_name data_type constraints_if_any
);

%%EXAMPLE%%
CREATE TABLE person (
  id BIGSERIAL NOT NULL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  gender VARCHAR(7) NOT NULL,
  date_of_birth DATE NOT NULL
);
```

- `DROP TABLE table_name`
- inserting records into a database:

```postgresql
INSERT INTO table_name (
 column_name_1,
 column_name_2,
 column_name_3
) VALUES (value_1, value_2, value_3);

%%EXAMPLE%%
INSERT INTO person (
 first_name,
 last_name,
 gender,
 date_of_birth
) VALUES ('Anne', 'Smith', 'FEMALE', DATE '1988-01-09');
```

## PostgreSQL Specific Commands

- casting into a specific type is done by `::`:

```sql
%%Cast into a DATE type%%
SELECT NOW()::DATE;

%%Cast into a TIME type%%
SELECT NOW()::TIME;
```

- time interval (both singular and plural time intervals work)

```sql
SELECT DATE '2001-09-28' + INTERVAL '1 hour';
```

- extract specifc value from a date

```sql
SELECT EXTRACT(YEAR FROM NOW());
%%Day of the week - DOW%%
SELECT EXTRACT(DOW FROM NOW());
```

- calculate age between two days

```sql
SELECT AGE(NOW(), birth_date) from people_data;
%%We can extract only part of a date, f.i. year:%%
SELECT DATE_PART('year', AGE(NOW(), birth_date)) from people_data;
```
