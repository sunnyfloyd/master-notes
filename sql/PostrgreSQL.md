# PostgreSQL

- [PostgreSQL](#postgresql)
	- [Sandbox Setup](#sandbox-setup)
	- [psql](#psql)
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
