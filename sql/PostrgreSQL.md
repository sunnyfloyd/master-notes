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
