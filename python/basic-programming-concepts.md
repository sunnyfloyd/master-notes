# HyperSkill Python Course Notes

## Table of Contents

- [HyperSkill Python Course Notes](#hyperskill-python-course-notes)
  - [Table of Contents](#table-of-contents)
  - [Introduction to OOP](#introduction-to-oop)
  - [Naming Variables](#naming-variables)
  - [Scopes](#scopes)
  - [Class](#class)
    - [Magic Methods](#magic-methods)
    - [Inheritance](#inheritance)
  - [Introduction to databases](#introduction-to-databases)
  - [SQL](#sql)
  - [Object-Relational Mapping (ORM)](#object-relational-mapping-orm)
    - [Data and object mapping](#data-and-object-mapping)
    - [ORM Concept](#orm-concept)
  - [Immutability](#immutability)
  - [Dictionaries](#dictionaries)
  - [Arguments](#arguments)
  - [Lists](#lists)
 
## Introduction to OOP

- An object-oriented program consists of a set of interacting objects;

- According to the principle of **encapsulation**, the internal implementation of the object is not accessible to the user;

- An object may have characteristics: **fields** and **methods**;

- An **object is an instance of a class** (type);

- A class is a more abstract concept than an individual object; it may be considered a template or blueprint that describes the common structure of a set of similar objects.

- **Inheritance** is a relation between objects that is interpreted as 'is a' relation.

## Naming Variables

- In cases when the most suitable name for the variable is a Python's keyword we can add underscore at the end of the variable name: ```class_```.

## Scopes

- Python follows **LEGB Rule** which means that interpreter looks for the variables in the following order: locals, enclosing, globals, built-in.

- In order to use or define a global variable (top-level variable) within the local scope of the function ```global var``` needs to be called first.

- In order to use or define an outer local variable within the local scope of the function ```nonlocal var``` needs to be called first.

## Class

- A class attribute is an attribute shared by all instances of the class. Class attributes are defined within the class but outside of any methods. Their value is the same for all instances of that class so you those should be considered as the sort of "default" values for all objects.

- As for the instance attributes, they store the data unique to each object of the class. They are defined within the class methods, notably, within the ```__init__``` method.

- The ```__init__``` method is a constructor.

- There are actually two ways to call an instance method: ```self.method()``` (implicit) or ```class.method(self)``` (explicit).

- Usually, instance attributes are created within the ```__init__``` method since it's the constructor, but you can define instance attributes in other methods as well, but it's not recommended.

- Python does make a distinction between methods and functions since method is a function that 'belongs to' an object.

- It is recommended to define all possible attributes in the ```__init__```. This can help avoiding AttributeError, but also gives a good understanding of the class and its objects from the get-go. If you do want to create the value for the attribute in a special instance method, then list it in the ```__init__``` as *None*.

### Magic Methods

- New objects of the class are created by the ```__new__``` method that in its turn calls the ```__init__``` method. The first argument of the ```__new__``` method is *cls* so it does not require an instance of the class since it returns a new instance which then passed to ```__init__```. It can be useful if we want to return instances of other classes or restrict the number of objects in our class.

- ```__str__``` creates a representation for users.

- ```__repr__``` creates a representation for developers and debuggers. If __str__ magic method is not defined then ```print()``` will use ```__repr__``` representation. ```__repr__``` should be defined first (due to it being used for debugging purposes).

### Inheritance

- All classes have the class *object* as their parent.

- Python supports two forms of inheritance: **single** and **multiple**:

  - Single inheritance is when a child class inherits from one parent class.
  - Multiple inheritance is when a child class inherits from multiple parent classes.

- Objects instantiated on the child classess are instances of the parent classes as well. Although, ```type()``` function will not provide the same results on the parent class instance as for the child class instance, but ```isinstance()``` will provide the same results if objects share same parent class.

- In order to check whether given class is a subclass of another class ```issubclass()``` function should be used. A tuple can be passed to ```issubclass()``` - True will be returned if given classs is a subclass of any of the classess provided in a tuple. Note that each subclass is considered a subclass of itself.

## Introduction to databases

- A database is a collection of data that is specifically organized for rapid search and retrieval processed by a computer.

- **Database Management System (DBMS)** is a type of software that allows users to define, create, and control data in a database.

- Databases allow for:

  - Store, retrieve and update data
  - Get metadata and data dictionaries
  - Access database remotely
  - Restrict accesses to data
  - Make concurrent updates
  - Recover to some point of time
  - Check the rules for data consistency automatically.

## SQL

- **SQL** - Structured Query Language.

- There are different *dialects* of the SQL language implemented by vendors of software supporting SQL.

- Data types in SQL as per ANSI standard:

  - INTEGER;
  - REAL - Similar to *float*. This numeric type is called **inexact** because some values are stored as approximations, so storing and retrieving a value might not always work as expected. Usually found in systems that operate very small and very large real numbers and require fast processing time;
  - DECIMAL - referenced as an accurate numeric type with unlimited precision and scale;
  - VARCHAR;
  - BOOLEAN.

- Creation of a database, table, dropping a database, and table in SQL:

```SQL
CREATE DATABASE students;

CREATE TABLE students_info ( 
 student_id INT, 
 name VARCHAR(30), 
 surname VARCHAR(30), 
 age INT
);

DROP DATABASE students;

DROP TABLE students_info;
```

- You can insert a new record into a table with a simple query using ```INSERT INTO``` statement. If we pass values than there are defined columns within the table omitted columns will be assigned *NULL* or a default (if defined) value.

```SQL
INSERT INTO customers (name, surname, zip_code, city) VALUES ('Bobby', 'Ray', 60601, 'Chicago');

/*
If Exact order of the columns in the table is known shorter version can be used:
*/
INSERT INTO customers VALUES ('Bobby', 'Ray', 60601, 'Chicago');

/*
In order to insert multiple rows with one INSERT statement:
*/
INSERT INTO customers (name, surname, zip_code, city) 
VALUES ('Mary', 'West', 75201, 'Dallas'), ('Steve', 'Palmer', 33107, 'Miami');
```

- Set of values separeted by commas in ```SELECT``` statement is called tuple (record, row). Even statement with a single argument is considered as a row with a single attribute. If an optional keyword ```AS``` is used together with ```SELECT``` string after a keyword becomes an attribute/column name.

- General template for using ```SELECT``` statement:

```SQL
SELECT val1 [AS name1], ..., valN [AS nameN];
```

## Object-Relational Mapping (ORM)

### Data and object mapping

- **Data mapping** - process of matching fields of the source system to the destination system.

- **Object mapping** - process of mapping data from a source system to a destination with high-level control over changes.

### ORM Concept

- **Object-Relational Mapping** is a concept of converting data from an object-oriented programming language to relational database representation and vice versa. It solves the problem of matching two different type systems together and synchronize the data flow between them.

- The relation is a link that connects a value from one table to the row in another. The database can store such links as keys. Relations in databases are more than simple links - when the root row from one table is deleted, it can imply cascade deletions of all related rows from other tables.

- Four common-used operations with rows in the database are known as **CRUD (Create, Read, Update, Delete)** operations. It's similar to what we can do with objects in the programming language.

## Immutability

- The difference between mutable and immutable objects lies in the fact that mutable objects can change their states after creation and immutable objects cannot.

- Custom classes are usually mutable but can be made immutable using language-specific tools and techniques if necessary.

## Dictionaries

- In Python 3.7 and up, dictionaries do maintain the insertion order for values they store, but in previous versions it is not neccessarily so.

## Arguments

- Parameters represent what a function accepts - those are the names that appear in a fuction definition.

- Arguments are the values that are passed to a function when it is being called.

## Lists

- There is the ```list.extend(another_list)``` operation that adds all the elements from another iterable to the end of a list. Alternatively, to merge two lists, you can just add one to another.

- To remove an item from the list use the ```list.remove(element)``` operation. If the element we want to delete occurs several times in the list, only the first instance of that element is removed.

- The ```del``` keyword deletes any kind of objects in Python, so it can be used to remove specific elements in a list ```del dragons[1]```.

- Finally, there is the ```list.pop()``` function. If used without arguments, it removes and returns the last element in the list.

- If we want to add a new element in the middle, we use the ```list.insert(position, element)``` operation.
