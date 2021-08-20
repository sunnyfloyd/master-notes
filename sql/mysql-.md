# SQL for Data Analysis and Database Design

## Fundamentals

### Databases

- Database is basically everything that collects and organize data (f.i. Excel sheet, JSON, plain text file).

- Relational Database Management System (RDBMS) - type of a database that holds one or more tables that may have relationship to each other.

- The motivation for database consisting of separate tables is **normalization**.

- **Normalization** - separating the different types of data into their own tables. Same information stored in a single table instead would be redundant, bloated and difficult to maintain; data input to such table does not require putting the same data multiple times - ID is enough. Any updates to the data are also required only in a single row instead of multiple updates.

- **Lightweight databases** - used by one or couple of users. Cannot be really used simultaneously.

- **Centralized databases** - based on the classic client-server setup.

### SQL and NoSQL

- **SQL** - Structured Query Language. Declarative programming language.

- **NoSQL** (not only SQL) - often used to describe **'Big Data'** platforms that may leverage SQL (most of the time not) but are not relational (MongoDB, Couchbase, Appache Cassandra, Redis). Most of these solutions are distributed across multiple machines since they scale horizontally very easily which is hard with SQL database.

- Other **'Big Data'** solutions: Apache Hadoop and Apache Spark can be interacted with using SQL, but are not limited to relational databases.

| Pros                   | SQL | NoSQL |
|------------------------|-----|-------|
| Integrity and Accuracy | Yes | No    |
| Speed and Scalability  | No  | Yes   |

### Retrieving Data with SQL

- Basic *select*: ```SELECT COLUMN_NAME FROM TABLE_NAME;```

- To limit number of displayed rows:

```SQL
SELECT * FROM TABLE_NAME LIMIT 2;
```

- Calculating additional columns (not added to the table itself):

```SQL
SELECT COLUMN_NAME,
COLUMN_NAME * 2 AS TEMP_COL_NAME
FROM TABLE_NAME;
```

- Rounding decimals with a function: ```round(COLUMN_NAME * 2, 2);```.

- Text concatenation: ```COL_1 || ' - ' || COL_2```; works with TEXT and other data files with the use of implicit conversion.

- Single line comment: ```--```.

- Multiline comment: ```/* */```.

### Filtering Data

- ```WHERE``` allows for data filtering: ```SELECT * FROM station_data WHERE year = 2010;```

#### WHERE on Numbers

- ```BETWEEN``` can be used instead of using ```AND``` logic:

```SQL
SELECT * FROM station_data
WHERE year BETWEEN 2005 and 2010;

-- Instead of:
SELECT * FROM station_data
WHERE year >= 2005 AND year <= 2010
```

- Multiple ```OR``` statements can be replaced with IN or NOT IN statements:

```SQL
SELECT * FROM station_data
WHERE MONTH IN (3, 6, 9, 12)

-- Instead of:
SELECT * FROM station_data
WHERE MONTH = 3
OR MONTH = 6
OR MONTH = 9
OR MONTH = 12
```

#### WHERE on Text

- ```length()``` returns number of characters in a *TEXT* field.

- ```LIKE``` expression can be used together with wildcards:

  - **%** - any number of characters,
  - **_** - single character.

```SQL
SELECT * FROM station_data
WHERE report_code LIKE 'B_C%'
```

- Using ```WHERE``` with RegEx can be done by using ```REGEXP```:

```SQL
SELECT * FROM STATION_DATA
WHERE report_code REGEXP '^C.*$'
```

- Other handy text function:

```SQL
-- The INSTR() function returns the position of the first occurrence of a string in another string:
SELECT INSTR("W3Schools.com", "3") AS MatchPosition; 

-- The SUBSTR() function extracts a substring from a string (starting at any position):
SELECT SUBSTR("SQL Tutorial", 5, 3) AS ExtractString; 

-- The REPLACE() function replaces all occurrences of a substring within a string, with a new substring:
SELECT REPLACE('SQL Tutorial', 'T', 'M'); 
```

#### WHERE on Booleans

- Boolean expressions are treated similarly as in Python:

  - 0 = false and 1 = true;
  - if column stores boolean data explicit '=' expression can be avoided for expressions resulting in truth, and ```NOT``` keyword can be used for false statements.

- The ```ANY``` and ```ALL``` operators allow to perform a comparison between a single column value and a range of other values. For each value in the initial column (left side of the operator) it checks whether **any** or **all** values from a subquery  equal left side. So it basically compares left side value against all of the right side set of values.

  - ```ANY``` - ANY compares a value to each value in a list or results from a query and evaluates to true if the result of an inner query contains at least one row;
  - ```ALL``` - The ALL operator returns TRUE if all of the subqueries values meet the condition. The ALL must be preceded by comparison operators and evaluates true if all of the subqueries values meet the condition.

```SQL
-- ANY case:
SELECT ProductName
FROM Products
WHERE ProductID = ANY
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);

-- ALL case:
SELECT ProductName
FROM Products
WHERE ProductID = ALL
  (SELECT ProductID
  FROM OrderDetails
  WHERE Quantity = 10);
```

#### Handling NULL

- Null value cannot be determined with '=' - ```IS NULL``` or ```IS NOT NULL``` needs to be used.

- Null is an absence of a value.

- If nulls do not have unambiguous business meaning then those should be restricted from the input.

- Most of the time in ```WHERE``` clause nulls are being filtered out unless explicitly handled.

- ```coalesce()``` will provide default value for given record if null value is detected. It can be used in ```SELECT``` statement as well:

```SQL
SELECT report_code, coalesce(precipitation, 0) as rainfall
FROM station_data;
```

#### Date and Time Functions

- When running a query, any string in the ```YYYY-MM-DD```date format (ISO8601 format) will be interpreted as a date. This means you can do chronological tasks like comparing one date to another date.

- Today's date ```SELECT DATE('now')``` or with modifier ```DATE('now', '-1 day')```.

- This can also be done on specific date with multiple modifiers: ```SELECT DATE('2015-12-07','+3 month','-1 day')```.

- Time also has a typical format, which is HH:MM:SS (this also is ISO8601 standard) - no conversions are needed for time formatted in this way.

- Seconds can be omitted. SQLite will infer the seconds value to be 00: ```SELECT '23:21'```.

- Current time can be obtained with following function ```SELECT TIME('now')``` that also accepts modifiers ```SELECT TIME('23:22', '+3 minute').

- Following date and time formats can be concatenated together to obtain datetime format.

- Same operations and modifiers are available for datetime format ```SELECT DATETIME('now', '+2 day', '-3 seconds')```.

- To format date in a specific way use ```strftime('%d-%m-%Y', 'now')```.

## GROUP BY and ORDER BY

### GROUP BY

- Basic aggregation is done via aggregating functions:

```SQL
SELECT COUNT(*) AS record_count FROM station_data
```

- It can be additionally filtered with ```WHERE``` keyword:

```SQL
SELECT COUNT(*) AS record_count FROM station_data
WHERE tornado = 1;
```

- Finally, it can be groupped with ```GROUP BY```:

```SQL
SELECT COUNT(*) AS record_count FROM station_data
WHERE tornado = 1
GROUP BY year, month;
```

### ORDER BY

- After ```WHERE``` and ```GROUP BY``` you can put ```ORDER BY``` to order the output based on the selected criteria:

```SQL
SELECT year, month, COUNT(*) AS record_count FROM station_data
WHERE tornado = 1
GROUP BY year, month
ORDER BY year DESC, month
```

### Aggregate Functions

- Aggregate functions never include ```NULL``` values in their calculations:

```SQL
SELECT year,
SUM(snow_depth) as total_snow,
SUM(precipitation) as total_precipitation,
MAX(precipitation) as max_precipitation
FROM station_data
WHERE year >= 2000
GROUP BY year
```

- ```COUNT()```.

- ```SUM()```.

- ```MIN()```.

- ```MAX()```.

- ```AVG()```.

- Aggregations can be filtered with the ```HAVING``` keyword:

```SQL
SELECT year,
SUM(precipitation) as total_precipitation
FROM station_data
GROUP BY year
HAVING total_precipitation > 30

-- In some of the SQL languages you need to specify aggregation function again when filtering with HAVING
SELECT year,
SUM(precipitation) as total_precipitation
FROM station_data
GROUP BY year
HAVING SUM(precipitation) > 30
```

- In order to get a list of unique values use ```DISTINCT``` keyword:

```SQL
SELECT DISTINCT station_number FROM station_data

-- When duplicates should be removed based on multiple data columns:
SELECT DISTINCT station_number, year FROM station_data
```

## CASE Expressions

- ```CASE``` is based on condition-value pairs that determine what value should be assigned to specific record based on the condition criteria:

```SQL
SELECT report_code, year, month, day, wind_speed,

CASE
  WHEN wind_speed >= 40 THEN 'HIGH'
  WHEN wind_speed >= 30 THEN 'MODERATE'
  ELSE 'LOW'
END as wind_severity

FROM station_data 
```

- New column created with ```CASE``` expression can be used for groupping:

```SQL
SELECT year,

CASE
  WHEN wind_speed >= 40 THEN 'HIGH'
  WHEN wind_speed >= 30 THEN 'MODERATE'
  ELSE 'LOW'
END as wind_severity,

COUNT(*) as record_count

FROM station_data
GROUP BY year, wind_severity
```

- ```CASE``` can be used to slice data columns based on given criteria into more columns. Data can be then separately aggregated if ```NULL``` or zero values are set for records not meeting slicing criteria:

```SQL
SELECT year, month,

SUM(CASE
    WHEN tornado = 1 THEN precipitation
    ELSE NULL
END) as tornado_precipitation,

SUM(CASE
    WHEN tornado = 0 THEN precipitation
    ELSE NULL
END) as non_tornado_precipitation

FROM STATION_DATA

GROUP BY year, month
ORDER BY year, month
```

## IF Expression

- For a simpler, not case-like queries with multiple conditions, ```IF``` expression can be used:

```SQL
SELECT IF(500<1000, "YES", "NO");

SELECT OrderID, Quantity, IF(Quantity>10, "MORE", "LESS") AS More_Less
FROM OrderDetails;
```

## JOIN

- Three types of table relationships:

  - one-to-many,
  - one-to-one,
  - many-to-many (cartesian product).

- ```JOIN``` operation on two tables:

```SQL
SELECT
CUSTOMER.CUSTOMER_ID,
NAME AS CUSTOMER_NAME

FROM CUSTOMER INNER JOIN CUSTOMER_ORDER
ON CUSTOMER.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID
```

- ```JOIN``` operation on 3 tables:

```SQL
SELECT
ORDER_ID,
CUSTOMER.CUSTOMER_ID,
NAME AS CUSTOMER_NAME,
PRODUCT_ID,
ORDER_QTY,
ORDER_QTY * PRICE AS REVENUE

FROM CUSTOMER

INNER JOIN CUSTOMER_ORDER
ON CUSTOMER_ORDER.CUSTOMER_ID = CUSTOMER.CUSTOMER_ID

INNER JOIN PRODUCT
ON CUSTOMER_ORDER.PRODUCT_ID = PRODUCT.PRODUCT_ID
```

- ```LEFT JOIN``` can be used to check whether **parent** records do not have any children records in the other table:

```SQL
SELECT CUSTOMER.CUSTOMER_ID,
NAME AS CUSTOMER_NAME

FROM CUSTOMER LEFT JOIN CUSTOMER_ORDER
ON CUSTOMER.CUSTOMER_ID = CUSTOMER_ORDER.CUSTOMER_ID

WHERE ORDER_ID IS NULL
```

- Combining ```LEFT JOIN``` with ```INNER JOIN``` will result in ```INNER JOIN``` *winning* since it does not tolerate null values.

### Union

- The ```UNION``` operator is used to combine the result-set of two or more ```SELECT``` statements:

```SQL
SELECT column_name(s) FROM table1
UNION
SELECT column_name(s) FROM table2; 
```

- Caveats for using ```UNION```:

  - Every ```SELECT``` statement within ```UNION``` must have the same number of columns;
  - The columns must also have similar data types;
  - The columns in every ```SELECT``` statement must also be in the same order.

## Database Design

### Creating and dropping tables

- Creating table with specific fields follows *column_name data_type additional_behaviours* pattern:

```SQL
CREATE TABLE COMPANY (
    COMPANY_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME VARCHAR(30) NOT NULL,
    DESCRIPTION VARCHAR(60),
    PRIMARY_CONTACT_ATTENDEE_ID INTEGER NOT NULL,
    FOREIGN KEY (PRIMARY_CONTACT_ATTENDEE_ID) REFERENCES ATTENDEE(ATTENDEE_ID)
);
```

- When creating a table given column can be specified a default value:

```SQL
CREATE TABLE TABLE_NAME (
  COLUMN_NAME BOOLEAN DEFAULT (0)
);
```

- Removing a table can be done with ```DROP TABLE TABLE_NAME```. It is not possible to delete parent table if parent records are present in child tables.

- To create a **view** based on a SQL query ```CREATE VIEW VIEW_NAME AS [SELECT_QUERY]```. View can be treated as a table since selection can be made from it as well.

- Inserting new rows into a table:

```SQL
-- insert single row
INSERT INTO TABLE_NAME (column1, column2, column3,...columnN)  
VALUES (value1, value2, value3,...valueN);

-- insert query output
INSERT INTO first_table_name [(column1, column2, ... columnn)] 
   SELECT column1, column2, ...columnN 
   FROM second_table_name
   [WHERE condition];
```

## Additional SQL

- Calculating a **median**:

```SQL
SET @N := 0;
SELECT COUNT(*) FROM STATION INTO @TOTAL;
SELECT
    ROUND(AVG(A.LAT_N), 4)
FROM (SELECT @N := @N +1 AS ROW_ID, LAT_N FROM STATION ORDER BY LAT_N) AS A
WHERE
    CASE WHEN MOD(@TOTAL, 2) = 0 
            THEN A.ROW_ID IN (@TOTAL/2, (@TOTAL/2+1))
            ELSE A.ROW_ID = (@TOTAL+1)/2
    END
;
```

- In order to dump query output into a variable:

```SQL
SELECT MAX(TOTAL_EARNINGS)
INTO @MAX_EARNINGS
FROM (SELECT SALARY * MONTHS AS TOTAL_EARNINGS FROM EMPLOYEE) AS EARNINGS;

-- Variable can then be used within the other query
SELECT @MAX_EARNINGS, COUNT(*)
FROM (SELECT SALARY * MONTHS AS TOTAL_EARNINGS FROM EMPLOYEE) AS EARNINGS
WHERE TOTAL_EARNINGS = @MAX_EARNINGS;
```

- **CTE** is a common table expression which is a name for a temporary result set that exists within the scope of a single statement and that can be referred to later within that statement, possibly multiple times.

```SQL
/* count total submissions of challenges of each user */
WITH data
AS
(
SELECT c.hacker_id as id, h.name as name, count(c.hacker_id) as counter
FROM Hackers h
JOIN Challenges c on c.hacker_id = h.hacker_id
GROUP BY c.hacker_id, h.name
)
/* select records from above */
SELECT id, name, counter
FROM data
WHERE
counter=(SELECT max(counter) FROM data) /*select user that has max count submission*/
OR
counter in (SELECT counter FROM data
GROUP BY counter
HAVING count(counter)=1 ) /*filter out the submission count which is unique*/
ORDER BY counter desc, id

-- Same as above but without WITH
/* these are the columns we want to output */
select c.hacker_id, h.name, count(c.hacker_id) as c_count

/* this is the join we want to output them from */
from Hackers as h
    inner join Challenges as c on c.hacker_id = h.hacker_id

/* after they have been grouped by hacker */
group by c.hacker_id, h.name

/* but we want to be selective about which hackers we output */
/* having is required (instead of where) for filtering on groups */
having 

    /* output anyone with a count that is equal to... */
    c_count = 
        /* the max count that anyone has */
        (SELECT MAX(temp1.cnt)
        from (SELECT COUNT(*) as cnt
             from Challenges
             group by hacker_id) AS temp1)

    /* or anyone who's count is in... */
    or c_count in 
        /* the set of counts... */
        (select temp2.cnt
         from (select count(*) as cnt 
               from Challenges
               group by hacker_id) AS temp2
         /* who's group of counts... */
         group by temp2.cnt
         /* has only one element */
         having count(temp2.cnt) = 1)

/* finally, the order the rows should be output */
order by c_count DESC, c.hacker_id;
```

- The SQL standard defines two methods of sampling: SYSTEM and BERNOULLI. The SYSTEM sampling is a page-level sampling where either all the records in the page are read or none at all as opposed to BERNOULLI which is a row-level sampling. Currently we support only SYSTEM sampling and this worklog aims to achieve efficiency only for this method of sampling.

```SQL
-- Bernoulli
db=# WITH sample AS (
    SELECT *
    FROM users TABLESAMPLE BERNOULLI(10)
)
SELECT count(*) FROM sample;

-- System
db=# WITH sample AS (
    SELECT *
    FROM users TABLESAMPLE SYSTEM(10)
)
SELECT count(*) FROM sample;
```

- If a subquery returns any rows at all, ```EXISTS``` subquery is ```TRUE```, and ```NOT EXISTS``` subquery is ```FALSE```:

```SQL
SELECT customer_id,cust_name, city
FROM customer
WHERE EXISTS
   (SELECT *
    FROM customer 
    WHERE city='London');
```

## Debugging

- In SQLite ```EXPLAIN QUERY PLAN``` can be used before an actual query to obtain an explanation of steps that will be performed by a database when obtaining a query results.
