# Data Structures and Algorithms in Python

## Table of Contents

- [Data Structures and Algorithms in Python](#data-structures-and-algorithms-in-python)
  - [Table of Contents](#table-of-contents)
  - [Sources](#sources)
  - [Functional Programming vs Object Oriented Programming](#functional-programming-vs-object-oriented-programming)
  - [I Python Primer](#i-python-primer)
    - [1.1 Python Overview](#11-python-overview)
      - [1.1.1 The Python Interpreter](#111-the-python-interpreter)
    - [1.2 Objects in Python](#12-objects-in-python)
      - [1.2.1 Identifiers, Objects, and The Assignment Statement](#121-identifiers-objects-and-the-assignment-statement)
      - [1.2.2 Creating and Using Objects](#122-creating-and-using-objects)
        - [Instantiation](#instantiation)
        - [Calling Methods](#calling-methods)
    - [1.5 Functions](#15-functions)
      - [1.5.1 Information Passing](#151-information-passing)
        - [Default Values and Keyword Parameters](#default-values-and-keyword-parameters)
    - [1.7 Exception Handling](#17-exception-handling)
      - [1.7.2 Catching an Exception](#172-catching-an-exception)
    - [1.8 Iterators and Generators](#18-iterators-and-generators)
    - [1.9 Additional Python Conveniences](#19-additional-python-conveniences)
      - [1.9.3 Packing and Unpacking of Sequences](#193-packing-and-unpacking-of-sequences)
  - [II Object-Oriented Programming](#ii-object-oriented-programming)
    - [2.1 Goals, Principles, and Patterns](#21-goals-principles-and-patterns)
      - [2.1.1 Object-Oriented Design Goals](#211-object-oriented-design-goals)
      - [2.1.2 Object-Oriented Design Principles](#212-object-oriented-design-principles)
    - [2.2 Software Development](#22-software-development)
      - [2.2.1 Design](#221-design)
      - [2.2.3 Coding Style and Documentation](#223-coding-style-and-documentation)
      - [2.2.4 Testing](#224-testing)
    - [2.3 Class Definitions](#23-class-definitions)
    - [2.4 Inheritance](#24-inheritance)
      - [2.4.3 Abstract Base Classes](#243-abstract-base-classes)
    - [2.5 Namespaces and Object-Orientation](#25-namespaces-and-object-orientation)
      - [2.5.1 Instance and Class Namespaces](#251-instance-and-class-namespaces)
      - [2.5.2 Instance and Class Namespaces](#252-instance-and-class-namespaces)
    - [2.6 Shallow and Deep Copying](#26-shallow-and-deep-copying)
  - [3. Algorithm Analysis](#3-algorithm-analysis)
    - [Big-Oh Notation](#big-oh-notation)
    - [Algorithm Analysis](#algorithm-analysis)
    - [Justification Techniques](#justification-techniques)
  - [4. Recursion](#4-recursion)
    - [Tail Recursion](#tail-recursion)
  - [5. Array-Based Sequences](#5-array-based-sequences)
      - [Low Level Arrays](#low-level-arrays)
        - [Referential Arrays](#referential-arrays)
        - [Compact Arrays](#compact-arrays)
      - [Dynamic Arrays and Amortization](#dynamic-arrays-and-amortization)
      - [Efficiency of Python's Sequence Types](#efficiency-of-pythons-sequence-types)
      - [Multidimensional Data Sets](#multidimensional-data-sets)
  - [6. Stacks, Queues, and Deques](#6-stacks-queues-and-deques)
    - [Stacks](#stacks)
    - [Queues](#queues)
    - [Deques (Double-Ended Queues)](#deques-double-ended-queues)
  - [7. Linked Lists](#7-linked-lists)
    - [Singly Linked Lists](#singly-linked-lists)
    - [Circularly Linked Lists](#circularly-linked-lists)
    - [Doubly Linked Lists](#doubly-linked-lists)
    - [Positional List ADT](#positional-list-adt)
      - [Move-to-Front Heuristic](#move-to-front-heuristic)
    - [Link-Based vs. Array-Based Sequences](#link-based-vs-array-based-sequences)
      - [Advantages of Array-Based Sequences](#advantages-of-array-based-sequences)
      - [Advantages of Link-Based Sequences](#advantages-of-link-based-sequences)
  - [8. Trees](#8-trees)
    - [Binary Trees](#binary-trees)
    - [Tree Traversal Algorithms](#tree-traversal-algorithms)

## Sources

- [Data Structures and Algorithms in Python](https://learning.oreilly.com/library/view/data-structures-and/9781118290279/)

## Functional Programming vs Object Oriented Programming

- **Declarative programming** is a programming paradigm that focuses on **what** needs to be accomplished rather than **how** it needs to be accomplished (**imperative programming**). Programming languages that apply this style attempt to minimize or eliminate side effects (changes of the state of object outside of the function's scope which is one of the principles for functional programming as well).

- **Functional programming** is based on 3 core principles:

  1. **Data and functions are kept separately**; functions operate on the passed parameters rather than data declared globally.
  2. **State Change** - change of the state of the variable should be avoided if possible.
  3. Functions are treated as **First-Class Citizens** - they can be assigned to a variable (bound to a name), or be used as a parameter when calling another function, or returned by another function.

- **Object Oriented Programming** - in contrast to functional programming OOP focuses on **how** something needs to be accomplished. OOP is used mostly when there are many things with few operations.

|                           Functional Programming                          |                                          OOP                                          |
|:-------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| Uses Immutable data.                                                      | Uses Mutable data.                                                                    |
| Follows Declarative Programming Model.                                    | Follows Imperative Programming Model.                                                 |
| Focus is on: “What you are doing”                                         | Focus is on “How you are doing”                                                       |
| Supports Parallel Programming                                             | Not suitable for Parallel Programming                                                 |
| Its functions have no-side effects                                        | Its methods can produce serious side effects.                                         |
| Flow Control is done using function calls & function calls with recursion | Flow control is done using loops and conditional statements.                          |
| It uses "Recursion" concept to iterate Collection Data.                   | It uses "Loop" concept to iterate Collection Data. For example: For-each loop in Java |
| Execution order of statements is not so important.                        | Execution order of statements is very important.                                      |
| Supports both "Abstraction over Data" and "Abstraction over Behavior".    | Supports only "Abstraction over Data".                                                |
| Used when there are few things with more operations.                      | Used when there are many things with few operations.                                  |

- **Parallel Computing** is a type of computation where many calculations or the execution of processes are carried out simultaneously. Large problems can often be divided into smaller ones, which can then be solved at the same time.

## I Python Primer

### 1.1 Python Overview

#### 1.1.1 The Python Interpreter

Python is an **interpreted** language. Code is not compiled into machine-language. Interpreter executes the program translating each statements into a sequence of one or more subroutines and then into machine code.

- **Pros:**
  - not platform dependent (Java style),
  - dynamic typing (let's change those types anytime!),
  - dynamic scoping (basically, makes it possible to use global variables and replace them with local ones),
  - smaller exec (cause interpreter is smart and flexible when choosing instruction code),
  - easier to make copy-pastes from others' code.
- **Cons:**
  - no static type-checking may raise some type-related errors,
  - hackers may inject stuff into code at the runtime (code injection),
  - slow (just-in-time compilation)
  - easier to make copy-pastes from other's code.

### 1.2 Objects in Python

Python is object oriented and classes form the basis for all data types. That is why I can make all the fancy methods on variables (actual objects).

#### 1.2.1 Identifiers, Objects, and The Assignment Statement

- The assigment statement: ```identifier (name) = object```

#### 1.2.2 Creating and Using Objects

##### Instantiation

- Creating a new instance of a class is called **instantiation**
  - usual form: ```obj = Object()```
  - **literal** form (for Python's built in classes): ```obj = 69.69``` - new instance of the **float** classes
  
##### Calling Methods

Type of methods:

- **accessors**: return information about the state of an object but do not change that state (```.lower()```)
- **mutators**: change the state of an object (```.sort()```)

### 1.5 Functions

#### 1.5.1 Information Passing

##### Default Values and Keyword Parameters

- In Python parameters can be sent to a function as a **keyword argument**:

```python
def foo(a=10, b=20, c=5):
  # function body
foo(c=21) # without keyword argument 'c' 21 would assigned to argument 'a'
```

### 1.7 Exception Handling

#### 1.7.2 Catching an Exception

- **Try-Except Clause** is best used when exceptional case is unlikely or it is too expensive to implement logic that would avoid the exception.
- Keyword **pass** does nothing but program does not raise errors.

### 1.8 Iterators and Generators

- **Generators** - syntax similar to a function; does not return values but **yield** statement is used to indicate next element in series

```python
def factors(n):          # generator that computes factors
  k = 1
  while k * k < n:        # while k < sqrt(n)
    if n % k == 0:
      yield k
      yield n // k
    k += 1
  if k * k == n:          # special case if n is perfect square
    yield k
```

### 1.9 Additional Python Conveniences

#### 1.9.3 Packing and Unpacking of Sequences

- Understanding ```enumerate()``` like iterations:

```python
for x, y in [ (7, 2), (5, 8), (6, 4) ]:
```

- When using **simultaneous assignments** all of the expressions are evaluated on the right-hand side before any of the the assignments are made to the left-hand variables:

```python
j, k = k, j # swapping of values without temporary variable
```

- When module is directly invoked as a script and not imported from another script then additional scripting may be called with the use of following construct:

```python
if _ _name_ _ == ‘_ _main_ _’:
```

## II Object-Oriented Programming

### 2.1 Goals, Principles, and Patterns

#### 2.1.1 Object-Oriented Design Goals

1. Robustness - capable of handling unexpected inputs.

2. Adaptability - able to evolve over time.

3. Reusability - being able to use the same code of a component for different application/module.

#### 2.1.2 Object-Oriented Design Principles

1. Modularity - seperation of a different software components based on their functional unit.

2. Abstraction - describing required parts of a software using their functionality but not the way to achieve it.

3. Encapsulation - writing a code in a way that how given outcomes is being achieved is not be important and those methods should be available only internally and not relied upon externally. What is important is a public interface output.

### 2.2 Software Development

#### 2.2.1 Design

1. To develop **high-level design** for a project CRC (Class-Responsibility-Collaborator) cards can be used.

2. When design takes some initial form it can be then described with Unified Modeling Language - e.g. **class diagrams**

#### 2.2.3 Coding Style and Documentation

- **Docstring** - integrated support in Python for documenting a source code:

```python
def scale(data, factor):
  """ Multiply all entries of numeric data list by the given factor.

  data    an instance of any mutable sequence type (such as a list)
  containing numeric elements

  factor  a number that serves as the multiplicative factor for scaling
  """
  for j in range(len(data)):
  data[j] *= factor
```

#### 2.2.4 Testing

- **Top-down testing** - used to find a high-level bugs in the software that come from integrating other application componentes together. Often used together with **stubbing** which means that components are replaced with their desired outcome in order to ensure that low-level bugs are not the main concern during the top-down testing.

- **Bottom-up testing** - starts with lower level components. For example that do not invoke other functions.

- **unittest**

### 2.3 Class Definitions

- ```self``` identifies the instance upon which method is invoked.

- Encapsulation in classes is indicated by single underscore before data member name. This means that it is **non-public**. In Python convention it is a **protected** method/variable.

- In Python encapsulation is a loose convention but it is implemented for **private** class members that have dunders (double underscore) before their names:

```python
_protected = 'This variable is not in fact protected. Underscore just indicates that it should not be used outside of this class or child classes.'
__private = 'This variable is indeed private due to name mangling in Python. It should not be accessed outside of this class, not even by child classes'
```

- **Operator overloading** is basically redefining functionality of default Python operators such as: +, -, ==, not, bool, etc. This can be used in order to establish an 'easy way' of using those operators with created classes. Usage of those should be preceeded with a question "Do I need a support for syntax such as a + b where a and b are two instances of the same class?":

```python
class Test:
  def __add__(self, other):
    # Code here
```

### 2.4 Inheritance

- **Inheritance** in classes makes it possible to utilize hierarchical approach in application development when there is interdependency between the componenents. Class inheritance establish common functionality that is downstreamed to **child classes**.

- Child classes may differentiate themselves from superclasses in two ways:

  - **extend** functionality by introducing brand new methods;
  - **specialize** overriding methods existing in parent class.

```python
class MainClass:
  def __init__(self):
    # Code here
class SubClass(MainClass):
  def __init__(self):
    super().__init__():
      # Code here
```

#### 2.4.3 Abstract Base Classes

- **Abstract base class** is a class which only purpose is to serve as a base class through inheritance. This allows for better code organization by centralizing certain functionalities. By definition, abstract base class is the one that **cannot be instantiated**. **Concrete class** is the one that can be instantiated.

- **Polymorphism** is a way to cover different type of inputs with the same block of code. Each of the types of an input will be processed via different parts of a code though giving an expected output associated to this input.

- Python does not have declared types so it is less formal when defining polymorphism. **abc module** provides support for defining formal abstract base classes in Python.

- **metaclass** is different from a superclass, in that it provides a template for the class definition itself. **ABCMeta** from abc module assures that the constructor for the abstract class raises an error:

- ```@abstractmethod``` is a decorator that indicates that given method is an abstract method, meaning that implementation of it will be provided within the concrete subclass. Python enforces this expectation, by disallowing instantation for any subclass that does not override the abstract methods with concrete implementation.

```python
class Sequence(metaclass=ABCMeta):
  @abstractmethod
  def __len__(self):

  @abstractmethod
  def __getitem__(self, j):
```

- Since Python is less formal, usage of ```abc``` module should be limited. If there is a need of an abstract base class then it should be documented that subclasses should implement expected functionality but no formal declaration is required. There are some abstract classes that are part of Python modules and might become useful. If the use of abstract class is needed it should be simply inherited and generic methods will be already available, but abstract methods will require override.

### 2.5 Namespaces and Object-Orientation

#### 2.5.1 Instance and Class Namespaces

- A **namespace** is an abstraction that manages all of the identifiers that are defined in a particular scope, mapping each name to its associated value:

  - instance namespace (basically everything with ```self``` prefix),
  - class namespace (methods or data members that reside direclty in the class body).

- **Nested classes** is not related to the concept of inheritance. This is used when nested classes exist only to support outer class.

#### 2.5.2 Instance and Class Namespaces

- Retrieving a name in python follows a general scheme of searching each of the available scopes. Python interpreter moves to the next scope if in the previous scope name has not been found:

  1. Instance namespace.
  2. Class namespace to which instance belongs.
  3. Namespaces of parent classes upward the hierarchy.
  4. If name not found then ```AttributeError``` is raised.

### 2.6 Shallow and Deep Copying

- **Shallow copy** of a list creates a new list that represents a sequence of the exact same contents. Changes in the original list will not affect copied list, but changes to the objects to which list items refer to will affect copied list.

- **Deep copy** of a list creates a new list but its items refer to the objects that were also copied. That means that changes to the original objects will not affect copied list.

## 3. Algorithm Analysis

### Big-Oh Notation

- Big-Oh notation analyses worst-case scenario. If an algorithm is the most efficient in the worst case scenario then it must also perform well in other cases.

- Big-Oh notation disregards constant factors - main factor of algorithm running time is taken.

- Big-Oh notation should be used to characterize a function as closely as possible (no bigger asymptotic function should be used than needed)

- Primitive operations are considered to be ```O(1)```.

- Algorithm efficiency table:

| Constant | Logaritghm | Linear | n-log-n | Quadratic | Cubic | Exponential |
|----------|------------|--------|---------|-----------|-------|-------------|
|     1    |    log n   |    n   | n log n |    n^2    |  n^3  |     a^n     |

### Algorithm Analysis

- Probability to randomly choose one element that meets given characteristics is equal to 1/n (assuming element uniqueness). Sum of such probabilities for each i<sup>th</sup>element is known as a **harmonic number** which is ```O(ln n)```.

- **Prefix average** is used to present average in different data points. There is a linear-time algoithm ```O(n)```.

- **Three-way disjoint** can be solved in ```O(n log n)``` time via set sorting. It can be solved in ```O(n)``` time with the use of **hash-tables**. Those act similar to arrays - given parameter is hashed to memory address so values are accessible in ```O(1)``` time.

- Sorting of data set has guaranteed worst-case running time of ```O(n long n)```.

- Sometimes we can get a tighter bound on a series of operations by considering the cumulative effect, rather than assuming that each achieves a worst case is a technique called **amortization** - f.e. **tree traversal** algoritghms such as recurring over a directory tree.

### Justification Techniques

1 and 2 derive from DeMorgan's Laws:

  1. Counterexample.
  2. Contrapositive - to justify the statement *if p is true, then q is true*, we establish that *if q is not true, then p is not true* instead.
  3. Contradiction - trying to prove the counter-example that leads to false statement.
  4. Induction.
  5. Loop Invariants.

## 4. Recursion

- Recursion can be represented in form of a **recursion trace** where each entry of the trace corresponds to a recursive call.

- Building a recursive algorithm requires reducing a problem to a **base case** that will return **base value** and therefore finish all of the remaining recursions. General form of algorithm that uses recursion:
  
  1. Test for base cases.
  2. Recur.

- Default **maximum recursion depth** in Python is 1000. To increase this limit ```sys.setrecursionlimit()``` can be used.

- Recursions based on a maximum number of recursive calls:

  - linear recursion - recursive call start at most one other;
  - binary recursion - recursive call may start two others;
  - multiple recursion - recursive call may start three or more others.

- If a cleaner public interface to an algorithm is needed, a standard technique is to make one function for public use with the cleaner interface, such as ```binary_search(data, target)```, and then having its body invoke a nonpublic utility function having the desired recursive parameters.

### Tail Recursion

- The main benefit of a recursive approach to algorithm design is that it allows to succinctly take advantage of a repetitive structure present in many problems.

- The usefulness of recursion comes at a modest cost. In particular, the Python interpreter must maintain activation records that keep track of the state of each nested call. When computer memory is at a premium, **it is useful in some cases to be able to derive nonrecursive algorithms from recursive ones**.

- A recursion is a **tail recursion** if any recursive call that is made from one context is the very last operation in that context, with the return value of the recursive call (if any) immediately returned by the enclosing recursion. By necessity, a tail recursion must be a linear recursion (since there is no way to make a second recursive call if you must immediately return the result of the first).

- Main benefit of a tail recursion is an elimination of a need for auxillary memory (non-volatile) usage and not overusing operating memory at the same time.

- Any tail recursion can be reimplemented nonrecursively by enclosing the body in a loop for repetition, and replacing a recursive call with new parameters by a reassignment of the existing parameters to those values.

## 5. Array-Based Sequences

#### Low Level Arrays

##### Referential Arrays

- Computer's main memory **performs as random access memory** (RAM). That is, it is just as easy to retrieve byte #8675309 as it is to retrieve byte #309. Using the notation for asymptotic analysis, we say that any individual byte of memory can be stored or retrieved in O(1) time.

- Above is true for all of the sequence types in Python. For example, arrays in Python do not store actual objects - instead their store memory references to those objects. Although the relative size of the individual elements may vary, the number of bits used to store the memory address of each element is fixed. In this way, Python can support constant-time access to a list or tuple element based on its index.

- Referential nature of the sequence types in Python requires some additional points to note:
  
  - When the elements of the list are immutable objects (f. e. integer instances), the fact that the two lists share elements is not that significant, as neither of the lists can cause a change to the shared object.

  - If lists share references to the same elements and those are mutable, it is important to remember that changes in mutable elements will affect both lists (unless ```deepcopy()``` is made).

  - ```list()``` and ```copy()``` create a new list but with the same object references as the source list. This is true for other list operations like: ```append()```, ```extend()```.

##### Compact Arrays

- Strings in Python are represented using an array of characters (not an array of references). This 'direct' representation is called a **compact array** since the array is storing the bits that represent the primary data.

- Advantages of compact arrays:

  - The overall memory usage will be much lower for a compact structure because there is no overhead devoted to the explicit storage of the sequence of memory references.

  - Primary data are stored consecutively in memory (provides high-performance computing).

- In Python compact arrays can be also created with a built-in module ```array``` which defines class (also named array) providing compact storage for arrays of primitive types:

```python
from array import array

primes = array(‘i’, [2, 3, 5, 7, 11, 13, 17, 19]) # 'i' is a type code
```

- The **type code** allows the interpreter to determine precisely how many bits are needed per element of the array. Those type are based on native data types in C.

- The array module does not provide support for making compact arrays of user-defined data types. Compact arrays of such structures can be created with the lower-level support of a module named ctypes.

#### Dynamic Arrays and Amortization

- Lists in Python rely on a **dynamic array** approach when it comes to their size in the system's memory. That is why lists do not have any visible limits when it comes to appending the items to them.

- Defining a list with given number of elements reserve certain amount of memory. Since this memory level is slighlty bigger than the currently required more items can be appended to this array. When memory limit allocated for the array is reached it is being resized - new memory allocation is made and the old list is then copied to it.

- Amortized cost of **append** operation in lists is O(1). However, it is better to use list comprehensions when possible.

#### Efficiency of Python's Sequence Types

- Asymptotic performance of the nonmutating behaviors of the list and tuple classes:

| Operation                                   | Running Time |
|---------------------------------------------|--------------|
| len(data)                                   | O(1)         |
| data[j]                                     | O(1)         |
| data.count(value)                           | O(n)         |
| data.index(value)                           | O(k + 1)     |
| value in data                               | O(k + 1)     |
| datal == data2 (similarly !=, <, <=, >, >=) | O(k + 1)     |
| data[j:k]                                   | O{k − j + 1) |
| datal + data2                               | O(n1 + n2)   |
| c * data                                    | O(cn)        |

- Tuples are typically more memory efficient than lists because they are immutable.

- Comparison of lists is in fact a comparison of each of the list elements.

- Asymptotic performance of the mutating behaviors of the list class:

| Operation                          | Running Time |
|------------------------------------|--------------|
| data[j] = val                      | O(1)         |
| data.append(value)                 | O(1)*        |
| data.insert(k, value)              | O(n - k + 1) |
| data.pop()                         | O(1)*        |
| data.pop(k) del data[k]            | O(n - k)*    |
| data.remove(value)                 | O(n)*        |
| data1.extend(data2) data1 += data2 | O(n2)*       |
| data.reverse()                     | O(n)         |
| data.sort()                        | O(n logn)    |

- In practice, the ```extend``` method is preferable to repeated calls to ```append``` because the constant factors hidden in the asymptotic analysis are significantly smaller. The greater efficiency of extend is threefold:
  - First, there is always some advantage to using an appropriate Python method, because those methods are often implemented natively in a compiled language (rather than as interpreted Python code).
  - Second, there is less overhead to a single function call that accomplishes all the work, versus many individual function calls.
  - Finally, increased efficiency of extend comes from the fact that the resulting size of the updated list can be calculated in advance.

- Similarly, it is a common Python idiom to initialize a list of constant values using the multiplication operator, as in ```[0] \* n``` to produce a list of length *n* with all values equal to zero.

#### Multidimensional Data Sets

- To properly initialize a two-dimensional list, we must ensure that each cell of the primary list refers to an independent instance of a secondary list. This can be accomplished through the use of Python's list comprehension syntax:

```python
data = [ [0] * c for j in range(r) ]
```

## 6. Stacks, Queues, and Deques

### Stacks

- A stack is a collection of objects that are inserted and removed according to the last-in, first-out (*LIFO*) principle. When we need a new 'plate' from the dispenser, we *pop* the top plate off the stack, and when we add a 'plate', we *push* it down on the stack to become the new top plate.

- Stacks can be used for matching opening and closing parenthesis or HTML tags and checking whether those are in a correct order.

- *The Adapter Design Pattern* applies to any context where we effectively want to modify an existing class so that its methods match those of a related, but different, class or interface. One general way to apply the adapter pattern is to define a new class in such a way that it contains an instance of the existing class as a hidden field, and then to implement each method of the new class using methods of this hidden instance variable.

### Queues

- Another fundamental data structure is the queue. It is a close “cousin” of the stack, as a queue is a collection of objects that are inserted and removed according to the first-in, first-out (*FIFO*) principle. Formally, the queue abstract data type defines a collection that keeps objects in a sequence, where element access and deletion are restricted to the first element in the queue, and element insertion is restricted to the back of the sequence.

- Queues can be used to handle calls to a customer service center, or a wait-list at a restaurant. FIFO queues are also used by many computing devices, such as a networked printer, or a Web server responding to requests.

- If queue is implemented through adapter design pattern with Python lists then underlying array should be used **circularly**. Implementing this circular view is not difficult. When we dequeue an element and want to “advance” the front index, we use the arithmetic ```f = (f + 1) % N```. Modulo division by a total length of the queue makes sure that index is wrapped around when the end of array is reached.

### Deques (Double-Ended Queues)

- Dequeues support insertion and deletion at both the front and the back of the queue.

- An implementation of a ```deque``` class is available in Python's standard ```collections``` module.

- Deques are a generalization of stacks and queues. **Deques support thread-safe, memory efficient appends and pops from either side of the deque with approximately the same O(1) performance in either direction.**

## 7. Linked Lists

- Linked lists avoid main 3 disadvantages of the array-based sequence:
  
  - the length of a dynamic array might be longer than the actual number of elements that it stores;
  - amortized bounds for operations may be unacceptable in real-time systems;
  - insertions and deletions at interior positions of an array are expensive.

- Linked lists, however, cannot efficiently access list items by numeric index *k* since just by examining a it is not possible to tell whether it is a second, fifth or other node in the list.

### Singly Linked Lists

- In a singly linked list each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list.

- The first and last node of a linked list are known as the **head** and **tail** of the list, respectively.

- By starting at the head, and moving from one node to another by following each node's next reference, we can reach the tail of the list. We can identify the tail as the node having ```None``` as its next reference. This process is commonly known as *traversing* the linked list. Because the next reference of a node can be viewed as a link or pointer to another node, the process of traversing a list is also known as **link hopping** or **pointer hopping**.

- Minimally, the linked list instance must keep a reference to the head of the list. Most of the time reference to a tail node and size of the linked list are additionally stored for convenience.

- There is no easy to delete a last node in singly linked list.

### Circularly Linked Lists

- In the case of linked lists, there is a more tangible notion of a circularly linked list, as we can have the tail of the list use its next reference to point back to the head of the list.

### Doubly Linked Lists

- To provide greater symmetry, we define a linked list in which each node keeps an explicit reference to the node before it and a reference to the node after it. Such a structure is known as a **doubly linked list**.

- In order to avoid some special cases when operating near the boundaries of a doubly linked list, it helps to add special nodes at both ends of the list: a **header node** at the beginning of the list, and a **trailer node** at the end of the list. These “dummy” nodes are known as **sentinels** (or guards), and they do not store elements of the primary sequence.

### Positional List ADT

- The positional list ADT is useful in a number of settings. For example, a program that simulates a game of cards could model each person's hand as a positional list. Since most people keep cards of the same suit together, inserting and removing cards from a person's hand could be implemented using the methods of the positional list ADT, with the positions being determined by a natural order of the suits.

#### Move-to-Front Heuristic

- In many real-life access sequences (e.g., Web pages visited by a user), once an element is accessed it is more likely to be accessed again in the near future. Such scenarios are said to possess **locality of reference**. A heuristic, or rule of thumb, that attempts to take advantage of the locality of reference that is present in an access sequence is the move-to-front heuristic. To apply this heuristic, each time we access an element we move it all the way to the front of the list. Our hope, of course, is that this element will be accessed again in the near future.

### Link-Based vs. Array-Based Sequences

#### Advantages of Array-Based Sequences

- Arrays provide O(1)-time access to an element based on an integer index;

- Operations with equivalent asymptotic bounds typically run a constant factor more efficiently with an array-based structure versus a linked structure;

- Array-based representations typically use proportionally less memory than linked structures.

#### Advantages of Link-Based Sequences

- Link-based structures provide worst-case time bounds for their operations;

- Link-based structures support O(1)-time insertions and deletions at arbitrary positions.


## 8. Trees

- The relationships in a tree are **hierarchical**, with some objects being “above” and some “below” others.

- The main terminology for tree data structures comes from family trees, with the terms “parent,” “child,” “ancestor,” and “descendant” being the most common words used to describe relationships.

- A **tree** is an abstract data type that stores elements hierarchically. With the exception of the top element (**root**), each element in a tree has a parent element and zero or more children elements.

- Formally, we define a tree *T* as a **set of nodes** storing elements such that the nodes have a parent-child relationship that satisfies the following properties:

  - If *T* is nonempty, it has a special node, called the root of *T*, that has no parent.
  - Each node *v* of *T* different from the root has a unique parent node *w*; every node with parent *w* is a child of *w*.

- Two nodes that are children of the same parent are **siblings**. A node *v* is **external** if *v* has no children. A node *v* is **internal** if it has one or more children. External nodes are also known as **leaves**.

- A node *u* is an **ancestor** of a node *v* if *u = v* or *u* is an ancestor of the parent of *v*. Conversely, we say that a node v is a descendant of a node *u* if *u* is an ancestor of *v*.

- An **edge** of tree *T* is a pair of nodes *(u, v)* such that *u* is the parent of *v*, or vice versa. A path of *T* is a sequence of nodes such that any two consecutive nodes in the sequence form an edge.

- A tree is **ordered** if there is a meaningful linear order among the children of each node; that is, we purposefully identify the children of a node as being the first, second, third, and so on. Such an order is usually visualized by arranging siblings left to right, according to their order.

### Binary Trees

- A binary tree is **proper** if each node has either zero or two children. Some people also refer to such trees as being full binary trees. Thus, in a proper binary tree, every internal node has exactly two children. A binary tree that is not proper is **improper**.

### Tree Traversal Algorithms

- In a **preorder traversal** of a tree *T*, the root of *T* is visited first and then the subtrees rooted at its children are traversed recursively. If the tree is ordered, then the subtrees are traversed according to the order of the children:

- Another important tree traversal algorithm is the **postorder traversal**. In some sense, this algorithm can be viewed as the opposite of the preorder traversal, because it recursively traverses the subtrees rooted at the children of the root first, and then visits the root (hence, the name “postorder”).

- Another common approach is to traverse a tree so that we visit all the positions at depth *d* before we visit the positions at depth *d + 1*. Such an algorithm is known as a **breadth-first traversal**.

- During an **inorder traversal** of a binary tree, we visit a position between the recursive traversals of its left and right subtrees. An important application of the inorder traversal algorithm arises when we store an ordered sequence of elements in a binary tree, defining a structure we call a **binary search tree**.
