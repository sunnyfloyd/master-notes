# Interview Questions Practice

## Data Engineer

### Relational Database

#### Relational vs Non-Relational Databases

- **Relational database** is one where data is stored in the form of a table. **Each table has a schema**, which is the columns and types a record is required to have. **Each schema must have at least one primary key** that uniquely identifies that record. In other words, there are no duplicate rows in your database. Moreover, **each table can be related to other tables using foreign keys**.

- One important aspect of relational databases is that a **change in a schema must be applied to all records**. This can sometimes cause breakages and big headaches during migrations. **Non-relational databases** tackle things in a different way. They are inherently schema-less, which means that records can be saved with different schemas and with a different, nested structure. Records can still have primary keys, but a change in the schema is done on an entry-by-entry basis.

- Databases also differ in **scalability**. A non-relational database may be less of a headache to distribute. That’s because a collection of related records can be easily stored on a particular node. On the other hand, relational databases require more thought and usually make use of a master-slave system.

#### Speed of SQL Queries

- Speed depends on various factors, but is mostly affected by how many of each of the following are present:

  - Joins,
  - Aggregations,
  - Traversals,
  - Records.

- The greater the number of joins, the higher the complexity and the larger the number of traversals in tables. Multiple joins are quite expensive to perform on several thousands of records involving several tables because the database also needs to cache the intermediate result! At this point, you might start to think about how to increase your memory size.

#### Debugging SQL Queries

- ```EXPLAIN QUERY PLAN``` can be used before ```SELECT``` to display the steps that database takes to execute a query.

### Non-Relational Databases

#### NoSQL vs SQL

- If you have a constantly changing schema, such as financial regulatory information, then NoSQL can modify the records and nest related information. Imagine the number of joins you’d have to do in SQL if you had eight orders of nesting! However, this situation is more common than you would think.

- Financial data tends to be stored in a **Point in Time Architecture** (PTA) which guarantees support for both history and audit trail. The core concept in PTA is this: **no information is ever physically deleted from or updated in the database**.

  - **History** – all information, both current and historical, that as of this moment, we believe to be true.
  - **Audit Trail** – all information believed to be true at some previous point in time.

- Now, what if you want to run reports, extract information on that financial data, and infer conclusions? In this case, you need to run complex queries, and SQL tends to be faster in this respect.

- **ACID** (atomicity, consistency, isolation, durability) - a set of properties of database transactions intended to guarantee data validity despite errors, power failures, and other mishaps. In the context of databases, a sequence of database operations that satisfies the ACID properties (which can be perceived as a single logical operation on the data) is called a **transaction**.

### Other Databases

- **Elastic Search** is highly efficient in text search. It leverages its document-based database to create a powerful search tool.

- **Newt DB** combines ZODB and the PostgreSQL JSONB feature to create a Python-friendly NoSQL database.

- **InfluxDB** is used in time-series applications to store events.

### Cache Databases

- **Cache databases** hold frequently accessed data. They live alongside the main SQL and NoSQL databases. Their aim is to alleviate load and serve requests faster.

- When a request comes in, you first check the cache database, then the main database. This way, you can prevent any unnecessary and repetitive requests from reaching the main database’s server. Since a cache database has a lower read time, you also benefit from a performance increase!

- **Redis** is a tool that allows for creation of a cache database.

## Design Patterns and ETL Concepts

- Applications may use several types of databases simultaneously. In order to ensure integrity and accuracy of all databases background workers might be implemented. These workers **extract** data from one database, **transform** it in some way, and **load** it into the target database. When you’re converting from a NoSQL database to a SQL one, the extract, transform, load (**ETL**) process takes the following steps:

  - **Extract**: There is a MongoDB trigger whenever a record is created, updated, and so on. A callback function is called asynchronously on a separate thread.
  - **Transform**: Parts of the record are extracted, normalized, and put into the correct data structure (or row) to be inserted into SQL.
  - **Load**: The SQL database is updated in batches, or as a single record for high volume writes.

### ETL Challenges

- There are several challenging concepts in ETL, including the following:

  - Big data,
  - Stateful problems,
  - Asynchronous workers,
  - Type-matching.

- If your application is writing thousands of records per second to MongoDB, then your ETL worker needs to keep up with transforming, loading, and delivering the data to the user in the requested form. Speed and latency can become an issue, so these workers are typically written in fast languages. You can use compiled code for the transform step to speed things up, as this part is usually CPU-bound.

### Design Patterns in Big Data

- How can you query, aggregate, and make use of relatively big data in an efficient way? Apache had initially introduced **MapReduce**, which follows the map, shuffle, reduce workflow. The idea is to map different data on separate machines, also called clusters. Then, you can perform work on the data, grouped by a key, and finally, aggregate the data in the final stage.

- Above workflow is still used today, but it’s been fading recently in favor of **Spark**. The design pattern, however, forms the basis of most big data workflows.

### Common Aspects of the ETL Process and Big Data Workflows

- Both workflows follow the **Producer-Consumer** pattern. A worker (the Producer) produces data of some kind and outputs it to a pipeline. This pipeline can take many forms, including network messages and triggers. After the Producer outputs the data, the Consumer consumes and makes use of it. These workers typically work in an asynchronous manner and are executed in separate processes.

- You can liken the Producer to the extract and transform steps of the ETL process. Similarly, in big data, the **mapper** can be seen as the Producer, while the **reducer** is effectively the Consumer. This separation of concerns is extremely important and effective in the development and architecture design of applications.
