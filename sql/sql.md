# SQL

## Sources

- [SQL for Data Analysis and Database Design](https://learning.oreilly.com/learning-paths/learning-path-sql/9781492058076/)

## Fundamentals

### Databases

- Database is basically everything that collects and organize data (f.i. Excel sheet, JSON, plain text file).

- Relational Database Management System (RDBMS) - type of a database that holds one or more tables that may have relationship to each other.

- The motivation for database consisting of separate tables is **normalization**.

- **Normalization** - separating the different types of data into their own tables. Same information stored in a single table instead would be redundant, bloated and difficult to maintain; data input to such table does not require putting the same data multiple times - ID is enough. Any updates to the data are also required only in a single row instead of multiple updates.

- **Lightweight databases** - used by one or couple of users. Cannot be really used simultaneously.

- **Centralized databases** - based on the classic client-server setup.

#### Relational vs Non-Relational Databases

- **Relational database** is one where data is stored in the form of a table. **Each table has a schema**, which is the columns and types a record is required to have. **Each schema must have at least one primary key** that uniquely identifies that record. In other words, there are no duplicate rows in your database. Moreover, **each table can be related to other tables using foreign keys**.

- One important aspect of relational databases is that a **change in a schema must be applied to all records**. This can sometimes cause breakages and big headaches during migrations. **Non-relational databases** tackle things in a different way. They are inherently schema-less, which means that records can be saved with different schemas and with a different, nested structure. Records can still have primary keys, but a change in the schema is done on an entry-by-entry basis.

- Databases also differ in **scalability**. A non-relational database may be less of a headache to distribute. That’s because a collection of related records can be easily stored on a particular node. On the other hand, relational databases require more thought and usually make use of a master-slave system.

##### SQL and NoSQL

- **SQL** - Structured Query Language. Declarative programming language.

- **NoSQL** (not only SQL) - often used to describe **'Big Data'** platforms that may leverage SQL (most of the time not) but are not relational (MongoDB, Couchbase, Appache Cassandra, Redis). Most of these solutions are distributed across multiple machines since they scale horizontally very easily which is hard with SQL database.

- Other **'Big Data'** solutions: Apache Hadoop and Apache Spark can be interacted with using SQL, but are not limited to relational databases.

| Pros                   | SQL | NoSQL |
|------------------------|-----|-------|
| Integrity and Accuracy | Yes | No    |
| Speed and Scalability  | No  | Yes   |

- If you have a constantly changing schema, such as financial regulatory information, then NoSQL can modify the records and nest related information. Imagine the number of joins you’d have to do in SQL if you had eight orders of nesting! However, this situation is more common than you would think.

- Financial data tends to be stored in a **Point in Time Architecture** (PTA) which guarantees support for both history and audit trail. The core concept in PTA is this: **no information is ever physically deleted from or updated in the database**.

  - **History** – all information, both current and historical, that as of this moment, we believe to be true.
  - **Audit Trail** – all information believed to be true at some previous point in time.

- Now, what if you want to run reports, extract information on that financial data, and infer conclusions? In this case, you need to run complex queries, and SQL tends to be faster in this respect.

- **ACID** (atomicity, consistency, isolation, durability) - a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. In the context of databases, a sequence of database operations that satisfies the ACID properties (which can be perceived as a single logical operation on the data) is called a **transaction**.

##### Speed of SQL Queries

- Speed depends on various factors, but is mostly affected by how many of each of the following are present:

  - Joins,
  - Aggregations,
  - Traversals,
  - Records.

- The greater the number of joins, the higher the complexity and the larger the number of traversals in tables. Multiple joins are quite expensive to perform on several thousands of records involving several tables because the database also needs to cache the intermediate result! At this point, you might start to think about how to increase your memory size.

#### Other Databases

- **Elastic Search** is highly efficient in text search. It leverages its document-based database to create a powerful search tool.

- **Newt DB** combines ZODB and the PostgreSQL JSONB feature to create a Python-friendly NoSQL database.

- **InfluxDB** is used in time-series applications to store events.

#### Cache Databases

- **Cache databases** hold frequently accessed data. They live alongside the main SQL and NoSQL databases. Their aim is to alleviate load and serve requests faster.

- When a request comes in, you first check the cache database, then the main database. This way, you can prevent any unnecessary and repetitive requests from reaching the main database’s server. Since a cache database has a lower read time, you also benefit from a performance increase!

- **Redis** is a tool that allows for creation of a cache database.

### Design Patterns and ETL Concepts

- Applications may use several types of databases simultaneously. In order to ensure integrity and accuracy of all databases background workers might be implemented. These workers **extract** data from one database, **transform** it in some way, and **load** it into the target database. When you’re converting from a NoSQL database to a SQL one, the extract, transform, load (**ETL**) process takes the following steps:

  - **Extract**: There is a MongoDB trigger whenever a record is created, updated, and so on. A callback function is called asynchronously on a separate thread.
  - **Transform**: Parts of the record are extracted, normalized, and put into the correct data structure (or row) to be inserted into SQL.
  - **Load**: The SQL database is updated in batches, or as a single record for high volume writes.

#### ETL Challenges

- There are several challenging concepts in ETL, including the following:

  - Big data,
  - Stateful problems,
  - Asynchronous workers,
  - Type-matching.

- If your application is writing thousands of records per second to MongoDB, then your ETL worker needs to keep up with transforming, loading, and delivering the data to the user in the requested form. Speed and latency can become an issue, so these workers are typically written in fast languages. You can use compiled code for the transform step to speed things up, as this part is usually CPU-bound.

#### Design Patterns in Big Data

- How can you query, aggregate, and make use of relatively big data in an efficient way? Apache had initially introduced **MapReduce**, which follows the map, shuffle, reduce workflow. The idea is to map different data on separate machines, also called clusters. Then, you can perform work on the data, grouped by a key, and finally, aggregate the data in the final stage.

- Above workflow is still used today, but it’s been fading recently in favor of **Spark**. The design pattern, however, forms the basis of most big data workflows.

#### Common Aspects of the ETL Process and Big Data Workflows

- Both workflows follow the **Producer-Consumer** pattern. A worker (the Producer) produces data of some kind and outputs it to a pipeline. This pipeline can take many forms, including network messages and triggers. After the Producer outputs the data, the Consumer consumes and makes use of it. These workers typically work in an asynchronous manner and are executed in separate processes.

- You can liken the Producer to the extract and transform steps of the ETL process. Similarly, in big data, the **mapper** can be seen as the Producer, while the **reducer** is effectively the Consumer. This separation of concerns is extremely important and effective in the development and architecture design of applications.

## Debugging

- ```EXPLAIN QUERY PLAN``` can be used before ```SELECT``` to display the steps that database takes to execute a query.

## Retrieving Data with SQL

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
