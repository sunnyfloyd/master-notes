# Python Improvements

## Actual Programming

### OOP

#### classmethod

- ```@staticmethod``` can be used when given method does not need any data from the class or instantiated object. It can be used when given method is logically related to the class and does not need any internally defined properties. In most cases it should be avoided and replaced with the ```@classmethod``` since class method acts the same, but adds possibility to access class object which might be crucial when other classes inherit from this class.

- ```@classmethod``` can be used similar to ```@staticmethod``` but additionally takes ```cls``` as a first argument which helps using class methods in classes that inherit from this class.

#### Multiple Inheritance

- In Python 3, the ```super(ChildClass, self)``` call is equivalent to the parameterless ```super()``` call.

- Each class can inherit from multiple clases:

```python
class Main:
    pass

class Addon:
    pass

class ChildClass(Main, Addon):
    pass
```

- Some methods might repeat themselves in different classes (i.e. addition of an item to a database) that do not inherit from the same parent class. In order to reduce code repetition it might be a good idea to introduce an abstract class that will encapsulate such methods. Methods which functionality does not differ across the classes/methods can be implemented directly in the abstract class (even when those depend on other methods that should be implemented within the child classes). Those *dependency* methods should be introduced in the abstract class as well but implemented in each class separately.

- Abstract classes cannot be instantiated, and classes that inherit from the abstract class cannot be instantiated if they do not overwrite abstract methods. The above can be implemented as following:

```python
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):  # implemented method; available in the child class
        print('Walking...')
    
    def eat(self):  # implemented method; available in the child class
        print('Eating...')
    
    @abstractmethod
    def num_legs():  # needs to be overwritten in the child class
        pass
```

- **Abstract class is an interface** since it defines the functionality of the child classes. However, if abstract class defines non-abstract methods it does not fully comply with a standard interface definition.

#### Classes

- **Class** is a blueprint whereas **instance** is an object that is built from this blueprint.

- Class does not hold any data, instance does hold actual data.

- CamelCase please when naming classes.

- In Python it has been decided that **to class methods instance (```self```) will be passed automatically, but not received automatically**. It means that ```foo()``` method called on the instance class will by default include ```self``` argument: ```foo(self)```.

- Class (same value for all instances; automatically created) and instance attributes (specific to a particular instance of a class):

```python
class Dog:
    # Class attribute - needs to be defined directly beneath the first line of the class name
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
```

- **Dunder methods** are class methods that start and end with double underscore like ```__init__()``` or ```__str__()```. They are used to customize classes:

  - ```__repr__()``` - returns the object representation. It could be any valid python expression such as tuple, dictionary, string etc.
  
  - In Python every class can have instance attributes. By default Python uses a dict to store an object’s instance attributes. This is really helpful as it allows setting arbitrary new attributes at runtime. However, for small classes with known attributes it might be a bottleneck. The dict wastes a lot of RAM. Python can’t just allocate a static amount of memory at object creation to store all the attributes. Therefore it sucks a lot of RAM if you create a lot of objects (I am talking in thousands and millions). Still there is a way to circumvent this issue. It involves the usage of ```__slots__``` to tell Python not to use a dict, and only allocate space for a fixed set of attributes:

  ```python
  class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = '_element', '_next'         # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next
  ```

- **Inheritance** is the process by which one class takes on the attributes and methods of another. Newly formed classes are called **child classes**, and the classes that child classes are derived from are called **parent classes**.

- To create a child class, just create new class with its own name and then put the name of the parent class in parentheses:

```python
class Dog:
  def __init__(self, name, age):
        self.name = name
        self.age = age
  
  def speak(self, sound):
    return f'{self.name} barks {sound}.'

class Dachshund(Dog):
  pass

# Instantating Class
jackie = Dachshund('Jackie', 8)
```

- To determine which class a given object belongs to, use ```type()```.

- To determine if instantated object of a class is also an instance of the other class (e.g. parent class) use ```isinstance(object, ClassName)```.

- To override a method defined on the parent class, define a method with the same name on the child class.

- Parent class can be accessed from inside a method of a child class by using ```super()```:

```python
class Dachshund(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)
```

- ```super()``` does much more than just search the parent class for a method or an attribute. It traverses the entire class hierarchy for a matching method or attribute. ```super()``` can have surprising results if not used carefully.

- Due to the redundant nature of ```__init__``` function within classes ```@dataclass``` decorator has been introduced in Python 3.7 that allows to cut out some of the boilerplate class-creation code:

```python
# 1st example
@dataclass
class Scoop():
    flavor : str

# Same as:
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

from typing import List
from dataclasses import dataclass, field
 
# 2nd example
@dataclass
class Bowl():
    scoops: List[Scoop] = field(default_factory=list)


# Same as:
class Bowl:
    def __init__(self) -> None:
        self.scoops = []
```

### Decorators

- **Decorator** can be treated as an extension to the class functionality. Decorator basically takes up the function, adds some functionality to it, and returns it. In more complex cases, decorators should be replaced with classes via class inheritance. However, in simple cases, decorators can be really useful - for example when some common validation is required before calling a desired function. Decorator must return a function that will be called over the passed arguments (if any). **Decorators should be kept as generic as possible** so they could handle all types of the functions.

```python
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide # This header before function definition means divide = smart_divide(divide)
def divide(a, b):
    print(a/b)

divide(10,5) # This function call is really calling an inner function returned by outer function and arguments are in fact passed to the inner function.
```

- Decorators are especially useful for logging (f.e. in pandas pipelines), validation and for easily extending the functionality of the functions (f.e. ```retry``` that tries to run the function again if previously it raised an exception).

- In order to propagate basic information of a decorated function (f.e. docstring, function name, etc.) use ```wraps``` decorator on a returned inner function:

```python
from functools import wraps
def decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func
    return inner

@decorator
def decorated_func():
    """Docstring for a function."""
    pass
```

- Decorators can be stacked on top of each other and will be called in order from the outer to inner. It is a good practice to design decorators in a way so that the order of decorating does not matter.

- Decorators, instead of returning functions that are nested, may return ```lambda``` (anonymous) functions:

```python
def valid(f):
    return lambda s: all(s) and 2*max(s) < sum(s) and f(s)

# Above is the same as:
def valid(f):
    def foo(s):
        return all(s) and 2*max(s) < sum(s) and f(s)
    return foo

# Functions that require validation:
@valid
def is_equilateral(sides):
    return len(set(sides)) == 1

@valid
def is_isosceles(sides):
    return len(set(sides)) < 3

@valid
def is_scalene(sides):
    return len(set(sides)) == 3
```

- Using **decorators within the class** can be tricky. It must be remembered that wrapper (inner) function must expect at least one argument since ```self``` is passed to instantiated methods implicitly. For the rest of arguments ```*args``` can be used:

```python
class Test:
    def __init__(self):
        self.limit = 2

    def is_valid(func):
        def wrapper(self, *args):
            if self.limit == 0:
                raise ValueError
            return func(self, *args)
        return wrapper

    @is_valid
    def limiter(self, a):
        print('Everything works fine!', a)

test = Test()
test.limiter(2)
# Output: Everything works fine! 2
```

- In some cases **it might be better to decorate a method at a runtime** instead of doing so at the class definition time:

```python
def is_valid(func):
    def wrapper(self, *args):
        if self.limit == 0:
            raise ValueError
        return func(self, *args)
    return wrapper

class Test:
    def __init__(self):
        self.limit = 0

    @is_valid
    def limiter(self, a):
        print('Everything works fine!', a)

test = Test()
test.limiter(2)
# Output: ValueError
```

- ```self``` can be also taken from ```*args```:

```python
def is_valid(func):
    def wrapper(*args):
        if args[0].limit == 0:
            raise ValueError
        return func(args[0], *args[1:])
        # or return func(*args)
    return wrapper

class Test:
    def __init__(self):
        self.limit = 2

    @is_valid
    def limiter(self, a):
        print('Everything works fine!', a)

test = Test()
test.limiter(2)
# Output: Everything works fine! 2
```

- If hard coding of a class attribute is not desired, attribute name can be passed through a decorator, but additional wrapping function needs to be added that will take a string as an argument. With the use of ```getattr()``` and ```self``` string pass by decorator can be used to extract actual value from the instantiated class. This additional wrapping is required whenever an argument is being passed to a decorator:

```python
def wrapped(limit):
    def is_valid(func):
        def wrapper(self, *args):
            attr = getattr(self, limit)
            if attr == 0:
                raise ValueError
            return func(self, *args)
        return wrapper
    return is_valid

class Test:
    def __init__(self):
        self.limit = 2

    @wrapped('limit')
    def limiter(self, a):
        print('Everything works fine!', a)

test = Test()
test.limiter(2)
# Output: Everything works fine! 2
```

- There might be the need for a decorator with additonal inputs that can be optional. In that case it might be desired to use decorator in a 'usual' ```@decorator``` form instead of ```@decorator()```. This requires some additional syntax to be included:

```python
# '*' in new Python syntax DIVIDES arguments passed to the function
# so that every argument after an asterisk needs to be provided
# as a keyword argument
def wrapper(func=None, *, param_1=True, param_2=False):
    def decorator(func):
        def inner(*args):
            return func(*args)
        return inner

    if func is None:
        return decorator
    else:
        return decorator(func)

@wrapper  # this will work properly without decorator being initialized with '()'
def decorated_func(*args):
    pass

@wrapper(param_1=False, param_2=True)
def decorated_func(*args):
    pass
```

- **@property** is a special decorator that can make given data member *protected*. Use of this decorator allows for accessing data returned by a decorated function just by calling its name ```foo_object.foo```. Adding this @property decorator can be done at the later stages of program development since **it does not require re-writing previous code if data members were accessed directly and were not protected** (by underscore convention. This means that required validations/additional operations related to properties can be implemented whenever required for given class and even when access or modification of data have been previously utilized:

```python
class House:

    def __init__(self, price):
    self._price = price

    @property
    def price(self):
        return self._price

# Can be accessed with:

house = House(100)
print(house.price)
```

- **setter** and **getter** are methods that can be additionally defined for decorated propery to both set and get values:

```python
class House:

    def __init__(self, price):
        self._price = price

    @property # This is basically @price.getter
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self._price = new_price
        else:
            print("Please enter a valid price")

    @price.deleter
    def price(self):
        del self._price

# Can be accessed with:
house = House(100)
house.price = 500
del house.price
```

#### Underscores

- Single underscores are a Python naming convention indicating a name is meant for internal use. It is generally not enforced by the Python interpreter and meant as a hint to the programmer only: ```self._internal_var = 2```

- Single trailing underscore (postfix) is used by convention to avoid naming conflicts with Python keywords: ```def make_object(name, class_)```. This indicates **protected** attribute/method.

- Dunder (double underscore) is used for **name mangling** - it ties variable/method name to its class name so in subclasses this variable is not getting overridden. Such variables are easy to access in code within the same scope. This is actually useful and makes **protected** state on the attribute/method. To the variable name ```_ClassName``` is added:

```python
class ManglingTest:
    def __init__(self):
        self.unmangled = 'stuff'
        self.__mangled = 'hello'


    def get_mangled(self):
        return self.__mangled


>>> ManglingTest().get_mangled()
'hello'
>>> ManglingTest().__mangled
AttributeError: "'ManglingTest' object has no attribute '__mangled'"
# To refer to a variable name '_ManglingTest__baz' needs to be used.

### THIS WILL ALSO RAISE AN ERROR

class ExtendedMangling(ManglingTest):

 def __init__(self):
        super().__init__()
        self.unmangled = 'overridden'
        self.__mangled = 'overridden'  # ERROR HERE
```

- Single underscore is sometimes used as a name for temporary or insignificant variables (“don’t care”). Also: The result of the last expression in a Python REPL:

```python
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car # interested only in color and mileage values
```

### Algorithms

- **Binary search** is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one.

    1. Let min = 1 and max = n.
    2. Guess the average of maxmaxmaxm, a, x and minminminm, i, n, rounded down so that it is an integer.
    3. If you guessed the number, stop. You found it!
    4. If the guess was too low, set minminminm, i, n to be one larger than the guess.
    5. If the guess was too high, set maxmaxmaxm, a, x to be one smaller than the guess.
    6. Go back to step two.

- **Farey sequence** can be used to generate all of the coprime (where GCD = 1) pairs of integers up to a given number.

```python
# Fraction class makes sure that fractions are in reduced form (using math.gcd())
from fractions import Fraction

class Fr(Fraction):
    def __repr__(self):
        return '(%s/%s)' % (self.numerator, self.denominator)

def farey(n):
        return [Fr(0, 1)] + sorted({Fr(m, k) for k in range(1, n+1) for m in range(1, k+1)})

for n in range(1, 12):
    print(farey(n))
```

### Bitwise Operators

- **Bitwise Shift**  operators ```<<``` and ```>>``` shift the bits of the first operand left or right by specified number of bits. It can be used for calculations that involve power of 2 or square root, and also multiplication or division by 2:

```python
def on_square(n):
    return 1 << (n-1)

def total_after(n):
    return (1 << n) - 1
```

- **Binary AND** operator ```&``` copies a bit to the result if it exists in both operands.

- In cases when it is easier to identify some pattern with RegEx that should be removed/replaced from a string ```re.sub(pattern, replacement, string)``` method can be used:

```python
return re.sub(self.PATTERN_TO_REMOVE, "", phone_number) # empty string means that no replacement are being done - removal only
```

### Asynchronous Programming

#### Multithreading

- Python processes can only run a single thread at the same time. This is because for each Python process only one GIL (Global Interpreter Lock), which is a key resource, is created. Running thread must acquire that resource so it is not possible to run multiple threads on a single Python process. Multithreading in Python is therefore useful only for **reducing waiting time** or, to be more specific, for **I/O bottleneck**. If all the threads are actually using computational power then multithreading will only slow down the entire process due to the overhead involved with switching between threads.

```python
from threading import Thread

def simple_func():
    pass

def complex_func():
    pass

# This spawns 2 additional threads
# (main thread that executes the rest of the code is still running)
thread1 = Thread(target=complex_func)
thread2 = Thread(target=simple_func)  # could be removed
thread1.start()
thread2.start()  # this could be replaced with simple_func()

thread1.join()
thread2.join()  # could be removed
```

- Instead of creating thread with a manually defined target it is easier to creat pool of threads that can be used for different tasks. ```ThreadPoolExecutor``` is a wrapper around a ```threading.Pool```:

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_func)
    pool.submit(simple_func)

# Alternatively not using context manager
executor = ThreadPoolExecutor(max_workers=2):
thread1 = executor.submit(complex_func)
thread2 = executor.submit(simple_func)

thread1.shutdown()
thread2.shutdown()
```

##### Sharing State in Threads

- **Atomic operation** is an operation that cannot be interrupted during its execution (like ```print```, ```append```).

- When multithreaded code is accessing a shared state (like a variable) it is required to be very careful and watch out for racing conditions.

- In order to test multithreaded code **fuzzing** should be used which most of the time involves including random sleep times in the code ```time.sleep(random.random())```.

- Multithreaded code that shares state can make use of ```queue``` class that implements multi-produer, multi-consumer queues that allows for safe exchange of information between threads. ```queue.Queue``` class implements required locking semantics. [Code example of sharing state between threads](https://github.com/PacktPublishing/The-Complete-Python-Course/blob/master/13_async_development/sample_code/6_queued_threads.py).

#### Multiprocessing

- When there is no waiting involved and we want to run couple of processes simultaneously (hopefully to reduce **CPU bottleneck**) we should use multiprocessing. It is important to note however that processes share the resources among themselves so we need to be careful not to request process to try and access unavailable resource (like user input). Sharing information between processes is slow and performance gain of using multiprocess approach is not certain and may depend on unknown factors such as the size of the problem set and so on.

```python
from multiprocessing import Process

process = Process(target=complex_func)
process.start()

simple_func()

process.join()
```

- Same as with multithreading we can use pool of processes. ```ProcessPoolExecutor``` is a wrapper around a ```multiprocessing.Pool```:

```python
from concurrent.futures import ProcessPoolExecutor
import os

def task():
    print("Executing our Task on Process {}".format(os.getpid()))

def main():
    with ProcessPoolExecutor(max_workers=3) as pool:
       task1 = pool.submit(task)
       task2 = pool.submit(task)

if __name__ == '__main__':  # code needs to be called from main
    main()

# If processes should stay alive through the entire time
# when application is running we should put the code
# outside of the context manager
def main():
    executor = ProcessPoolExecutor(max_workers=3)
    task1 = executor.submit(task)
    task2 = executor.submit(task)

    task1.shutdown()
    task2.shutdown()
```

#### Generators

- **Generators** can be used to implement multithread-like functionality to the code without actually using multiple threads. This is because ```yield``` keyword suspsends execution of the generator remembering its current state and resuming it when next iteration is called:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task finished')
```

#### Coroutines

- **Coroutines** are a special kind of generators that instead of getting the data they send the data with the use of a ```yield``` keyword and can be suspended:

```python
from collections import deque
# from types import coroutine  # for async and await

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))

# @coroutine  # for async and await
def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        print(f'{greeting} {friend}')

def greet(g):
    yield from g
    # await g  # in new Python syntax

# alternatively this can be done with:
def greet(g):
    g.send(None)
    while True:
        greeting = yield
        g.send(greeting)

greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking...')
greeter.send('How are you,')
```

#### AsyncIO

- **asyncio** is a library to write concurrent code using the async/await syntax:

```python
import aiohttp
import asyncio

async def fetch_page(session, url):
    async with session.get(url) as response:
        return response.status

async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        grouped_tasks = asyncio.gather(*tasks)
        return await grouped_tasks

loop = asyncio.get_event_loop()
urls = ['http://google.com' for i in range(50)]
loop.run_until_complete(get_multiple_pages(loop, *urls))
```

### Multithreaded Programming

- Even though Python has a Global Interpreter Lock (GIL), we’re still responsible for protecting against data races between the threads in our program. Our programs will corrupt their data structures if we allow multiple threads to modify the same objects without locks. And that is why *Lock* class should be used from *threading* module - a standard mutual exclusion lock implementation:

```python
import threading
class LockingCounter():
    def __init__(self):
        self.lock = threading.Lock()
        self.count = 0
    
    def increment(self):
        with self.lock:
            # Critical functionality of the programme
            self.count += 1
```

- As presented above ```with``` can be used together with *Lock* class instance instead of manual ```threadLock.acquire()``` and ```threadlock.release()``` to acquire and release the lock.

- Compared to previous method there are already some significant simplifications in how to do basic multithreading in Python with ```map``` and ``pool```. [Article on TowardsDataScience](https://towardsdatascience.com/make-your-own-super-pandas-using-multiproc-1c04f41944a1):

```python
# Parallelizing pandas functions:
import random
import pandas as pd
import numpy as np
from multiprocessing import  Pool

def add_features(df):
    df['question_text'] = df['question_text'].apply(lambda x:str(x))
    df["lower_question_text"] = df["question_text"].apply(lambda x: x.lower())
    df['total_length'] = df['question_text'].apply(len)
    return df

def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores)
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df
```

### RegEx

- 'Space' character in RegEx can be written just with ' ' or '\ ' in verbose patterns.

- It is possible to label pattern groups with following syntax: ```(?P<name>)```. 'name' is a dictionary key. Dictionary for matched pattern can be called with ```item.groupdict()```:

```python
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])",wiki):
       # We can get the dictionary returned for the item with .groupdict()
       print(item.groupdict()['title'])
       # Output:
       # Overview
       # Access to public records
       # Student medical records

       # Printing whole dictionary:
       print(item.groupdict())
       # Output: {'title': 'Student medical records', 'edit_link': '[edit]'}
```

- **Look-ahead** and **look-behind** RegEx methods can be used to indicate pattern structure, and to disregard parts of such pattern. Syntax:
  - for positive look-ahead: ```(?=regex_pattern_here)```,
  - for positive look-behind ```(?<=regex_pattern_here)```,
  - for negative look-ahead: ```(?!regex_pattern_here)```,
  - for negative look-behind ```(?<!regex_pattern_here)```:

- There is a general RegEx skip with syntax: ```(?:regex_pattern_here)``` - this group will not be returned but will me matched.

- When we want to match against the character(s) already captured by the previous pattern group we can refer to such group using ```\1``` where ```1``` is a number of a given group. It is importan to remember that optional groups will not be matched if not captured: ```(b)?c\1``` will not match a string if first *b* has not been found. This should be written like this: ```(b?)c\1```.

### Remaining

- For building strings, the convention is to use **fstrings**:

```python
f'ten plus ten is {10+10}'
```

- Although *fstrings* are recommended most of the time ```str.format``` can still be useful in many cases, especially when string template should be built and called multiple times:

```python
import operator
PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]
def format_sort_records(people):
    output = []
    template = '{1:10} {0:10} {2:5.2f}'  # Creating string template

    for person in sorted(people, key=operator.itemgetter(1)):
        output.append(template.format(*person))
    return output
```

- **Falsy statements** in Python are:
  - False
  - None
  - 0
  - ''
  - ()
  - []
  - {}

- ```is``` operator checks whether given two objects are the same and therefore they are located in the same memory address. However, due to the optimisation reasons within the Python's interpreter some immutable objects are kept around [for example integers from -5 to 256 and latin-1 characters (where ```len(char) == 1```)]. Those objects are shared by references/variables that refer to these optimised values.

- List slicing does not produce out of bound error because slicing is used to create a new list. If the indices don't fall within the range of the number of elements in the list, we can return an empty list. So, we don't have to throw an error. But, if we try to access the elements in the list which is greater than the number of elements, we cannot return any default value (not even None because it could be a valid value in the list).

- Lists are meant to be used for sequences of the same type, whereas tuples are meant for sequences of different types.

- When we want to make sure that getting an item from a sequence will return an iterable of a same type instead of the individual element we need to use slicing (```el[:1]``` instead of ```el[0]```).

- ```operator.itemgetter(*item)``` returns a function that fetches item from its operand using the operand’s ```__getitem__()``` method. **If multiple items are specified, returns a tuple of lookup values**. This basically applies provided arguments in square bracket on the object that function was called.

- ```operator.attrgetter``` returns a callable object that fetches attr from its operand. **If more than one attribute is requested, returns a tuple of attributes**. The attribute names can also contain dots. For example:

- List comprehensions can be used within list comprehensions:

```python
arr = [[i for i in iterable_object] for iterable_object in another_iterable_object]
```

- Dictionary comprehensions are also available in Python:

```python
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Double each value in the dictionary
double_dict1 = {k:v*2 for (k,v) in dict1.items()}
```

- When iterating through a list of tuples (or other iterable objects within iterable objects) unpacking can be used:

```python
t = [(1, 'a'), (2, 'b'), (3, 'c')]
arr = [c for n, c in t]
```

- **set** method ```issubset()```

```python
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y) # True

# Can be also used with strings

x = {"a", "b", "c"}
y = 'fedcba'

z = x.issubset(y) # True
```

- Sets in Python allow for **union** *|* and **intersection** *&*; also ```set.union()``` and ```set.intersection()```.

- Sets comparison checks whether given set is a subset of other set:

```python
{1, 2} < {1, 2, 3}  # True
{1, 2} < {1, 3}  # False
{1, 2} < {1, 2}  # False -- not a *strict* subset
{1, 2} <= {1, 2}  # True -- is a subset
```

- ```dict.keys()``` method returns a special object of type *dict_keys* that implements several of the same methods available on sets including union and intersection.

- ```dictionary.update()``` updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

- In order to create a dictionary with a list of default values for all of the keys use ```dict.fromkeys(keys, 0)```.

- Iterator can be created on object with the use of ```iter()```:

```python
arr = [1, 2, 3, 4, 5]
ARR = iter(arr) # Returns an iterator object for given object
a = next(ARR) # Returns next item from  the iterated object
```

- In order to obtain all possible combinations (cartesian product, equivalent to a nested-loop) in form of a tuple ```itertools.product()``` can be used:

```python
from itertools import product
from string import ascii_uppercase

numbers = [i for i in  range(1, 11)]
numerated_letters = [p for p in product(ascii_uppercase, numbers)]

# equal to:
numerated_letters = []
for letter in ascii_uppercase:
for number in  range(1,11):
numerated_letters.append((letter, number))
```

- Iteration can be looped with ```cycle()``` from itertools:

```python
from itertools import cycle

s = ['A','B', 'C', 'D']
n = range(20)

for i, j in zip(cycle(s), n):
    print(i + ' ' + str(j))
```

- ```enumerate``` can be passed second argument that sets a starting point for the index:

```python
for i, j in enumerate(range(10), 1):
    print(f'enum: {i} index: {j}')
```

- It is possible to iterate over multiple iterable object at once using ```zip()```:

```python
letters = ['a', 'b', 'c', 'd', 'e']
num_let = [str(n) + l for l, n in zip(letters, range(1, 6))]
```

- Asterisk (*) can be used before argument in order to unpack iterable value:

```python
arr = [[1,2,3], [3,4,5], [6,7,8]]
print(list(zip(*arr))) # zip() returns an object and therefore has to be cast into a list
# output: [(1, 3, 6), (2, 4, 7), (3, 5, 8)]
```

- Translation tables created with ```maketrans()``` can be useful when given string/sequence requires some straightforward 1 to 1 character conversion. It is pretty slow though:

```python
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P") # maketrans() as argument takes a single argument in form of a dict with lenght of 1 keys or equal length strings
print(txt.translate(mytable))
```

- ```str.translate()``` can be used to strip punctuation from the string:

```python
import string

s = 'Random string, but with punctuation (surprisingly)?!
s.translate(maketrans('', '', string.punctuation))
```

- Instead of using ```or``` to check if given expression has one of the certain values we can use ```in``` and a list:

```python
def process_payment(payment):
    if payment.currency in ['USD', 'EUR']:
        process_standard_payment(payment)
    else:
        process_international_payment(payment)
```

- ```or``` can be also used for assigning values to variables:

```python
currency = input_currency or DEFAULT_CURRENCY # It works because the left-hand side is evaluated first. If it evaluates to True then currency will be set to this and the right-hand side will not be evaluated.
```

- ```getattr(object, name)``` is equivalent to ```object.name```

- ```*args``` can be used when declaring a function that might be called with different number of arguments - ```args``` will become a tuple storing those arguments:

```python
def foo(greeting, *args):
    if len(args) != 0:
        print(greeting)
        print(args)
    else:
        print('NOK')

foo('siema', 2, 'kot')
```

- ```setattr(object, name, value)``` can be used for assigning a new value to an already existing attribute of an object or, when attribute with given name is not found, create a new attribute. It can be also used to create attributes in bulk, so that they return values or even functions:

```python
class SpaceAge(object):

    PLANET_RATIOS = [(k, v * 31557600) for k, v in (
        ('earth', 1.0),
        ('mercury', 0.2408467),
    )]

    def __init__(self, seconds):
        self.seconds = seconds
        for planet, ratio in self.PLANET_RATIOS:
            setattr(self, 'on_' + planet, self._planet_years(ratio))

    # __init__() creates following:
    on_earth = foo1 # foo is a returned lambda function; ratio is hardcoded so no arguments are needed to be passed
    on_mercury = foo2

    # If above attributes are called (e.g. on_earth()) then in fact lambda is called

    def _planet_years(self, ratio):
        return lambda ratio=ratio: round(self.seconds / ratio, 2)
```

- **Exception classes** can be inherited by other classes - this is useful when exception functionalities can stay the same, but name of the exception can be made for meaningful. Additional functionality can also be built-upon existing one within the exception class:

```python
if err:
    raise MeetupDayException('Error message')
    # Can be also:
    # raise MeetupDayException

class MeetupDayException(ValueError):
    pass
```

- ```textwrap.wrap(string, width=70)``` wraps the single paragraph (*string*) so that every line is at most *width* characters long. Returns a list of output lines:

```python
from textwrap import wrap

value = "AUGUUUUAA"
print(wrap(value, 3)) # ['AUG', 'UUU', 'UAA']
```

- ```itertools.takewhile(predicate, iterable)``` makes an iterator that returns elements from the iterable as long as predicate is true (predicate should be a fuction that will be called on every element from iterable):

```python
# High-level implementation of a takewhile() function
def takewhile(predicate, iterable):
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break

takewhile(lambda x: x<5, [1,4,6,4,1]) # Output: [1, 4]
```

- When additional checks are needed within list comprehensions for values from dictionary, nested for-loop can be used with 'dummy' iterator:

```python
from itertools import takewhile
from textwrap import wrap


catalogue = {
    'AUG': 'Methionine',
    'UUC': 'Phenylalanine',
}

def is_not_stop(pattern):
    return pattern not in ('UAG', 'UAA', 'UGA')

def proteins(strand):
    return [protein
            for pattern in takewhile(is_not_stop, wrap(strand, 3)) # pattern extraction from string without whitespaces
            for protein in (catalogue.get(pattern, None),) # dummy tuple used only to take value from dictionary in order to omit redundancy
            if protein]
    # Could be replaced with:
    # return [catalogue.get(pattern) for pattern in takewhile(is_not_stop, wrap(strand, 3)) if catalogue.get(pattern)]
```

- Sometimes, when the ```KeyError``` is raised, it might become a problem. To overcome this Python introduces another dictionary like container known as **Defaultdict** which is present inside the collections module. It applies default value based on function call for new keys in dictionary:

```python
from collections import defaultdict
def def_value():
    return "Not Present"

d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])
print(d["b"])
print(d["c"]) # 'Not Present'
```

- **Counter** is an unordered collection where elements are stored as Dict keys and their count as dict value. Counter elements count can be positive, zero or negative integers. However there is no restriction on it’s keys and values. Although values are intended to be numbers but we can store other objects too. We can create an empty Counter or start with some initial values too:

```python
from collections import Counter

counter = Counter(['a', 'a', 'b'])
print(counter)  # Counter({'a': 2, 'b': 1})

# Counter with initial values
counter = Counter(a=2, b=3, c=1)
print(counter)  # Counter({'b': 3, 'a': 2, 'c': 1})
```

- ```collections.namedtuple(typename, field_names)``` returns a new tuple subclass named *typename*. The new subclass is used to create tuple-like objects that have fields accessible by attribute lookup as well as being indexable and iterable. Since it creates a subclass it should be treated as a **constructor** of the object (f.i. Person, Animal, Dog, Car, etc.). Attributes are called via standard ```Named_Tuple.attribute_name```:

```python
import operator
from collections import namedtuple

Person = namedtuple('Person', ['first', 'last', 'distance'])


PEOPLE = [Person('Donald', 'Trump', 7.85),
          Person('Vladimir', 'Putin', 3.626),
          Person('Jinping', 'Xi', 10.603)]


def format_sort_records(list_of_tuples):
    output = []
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=operator.attrgetter('last', 'first')):
        output.append(template.format(*(person._asdict())))
    return output
```

- ```_asdict()``` is a method of a *namedtuple* class that returns a dict which maps field names to their corresponding values:

```python
p = Point(x=11, y=22)
p._asdict()
{'x': 11, 'y': 22}
```

- There is a optional convention that increases readability to put what type of value defined function return:

```python
def transfer(self, S: ArrayStack) -> None:
        stck_len = len(self._data)
        [S.push(self.pop()) for _ in range(stck_len)]
```

- It is possible to define type alias for argument in a function:

```python
def transfer(self, S: ArrayStack) -> None:
        stck_len = len(self._data)
        [S.push(self.pop()) for _ in range(stck_len)]
```

- Unpacked tuple object can be passed to the ```range()```:

```python
# Clever way to define parameters for range() - either increasing or decreasing order:
args = (mn**2, mx**2+1) if smallest else (mx**2, mn**2-1, -1)

    for r in range(*args):
        pass
```

- ```else``` statement can be used after for-loop. Block within ```else``` will be executed if for-loop is not terminated by a break statement. It can aslo be used to execute code if for loop is executed till then end (just to indicate it):

```python
# Without breaks:
for i in range(1, 4): 
    print(i) 
else:  # Executed because no break in for 
    print("No Break") 
# With breaks:
for i in range(1, 4): 
    print(i) 
    break
else: # Not executed as there is a break 
    print("No Break") 
```

- ```int()``` takes optional argument that indicates base of the provided number. *int* object can be compared to other *int* objects regardless of their base.

- It is Pythonic to use infinite while-loops that will be ended with ```break``` statement:

```python
count = 0
while True:
    print('Hello')
    if count == 5:
        break
    count += 1
```

- Strings can be compared with other strings. Comparison lexicographical.

- python way of writing try-except-else FINISH THIS

```python
try:
    iterator = iter(theElement)
except TypeError:
    # not iterable
else:
    # iterable
```

- ```*args``` is stored as a tuple whereas ```**kwargs``` is stored as a dictionary.

- Unpacking operator (```*``` or ```**```) can be used when assigning values to the variables:

```python
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)
```

- ```itertools.chain(*iterables)```  basically combines all of the iterables together so that one can iterate through them in one go:

```python
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```

- ```decimal``` module in Python provides support for fast correctly-rounded decimal floating point arithmetics. Module is especially useful when precision of floating numbers arithmetic is crucial or when floating numbers need to be presented in the people-friendly way based on the arithmetics that people know from school.

- Some of the built-in functions in Python that operate on iterables (```max()```, ```sorted()```, etc.) accept keyword argument *key* that takes a function based on which main function behaviour will be altered.

```python
from collections import Counter
WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_count(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)

print(most_repeating_word(WORDS))
```

- ```filter(foo, iterable)``` generates new iterable that includes only those items from the passed iterable that return ```True``` when passed to a function.

- ```reduce(foo, iterable)``` function passed to reduce must take 2 arguments - it starts with first 2 items from the iterable and then continues with first argument being a previously returned value and next item from the iterable:

```python
s = ['s','t','r','i','n','g']
s_joined1 = reduce(lambda x, y: x + y, s)
s_joined2 = ''.join(s)
```

- Files can be accessed within the context indicated by ```with``` keyword. ```with``` operates on the objects that have ```__enter__``` and ```__exit__``` magic methods impletemented as part of their class. Especially useful for working with files since it ensures that file will be properly closed when program exits a block defined by ```with```:

```python
with open(infilename) as infile:
    pass

# 'with' can also operate on 2 or more objects within the same context:
with open(infilename) as infile, open(outfilename, 'w') as outfile:
    for one_line in infile:
        outfile.write(f'{one_line.rstrip()[::-1]}\n')
```

- JSON files can be read and construct with the ```json``` module:

```python
import json

json.dumps(obj)  # serializes object to JSON formatted string
json.dump(obj, file)  # same as above but output is being written to a file

json.loads(json)  # deserialize JSON string to a Python object
json.load(file)  # same as above but reads JSON from a file
```

- When a function depends on HTTP requests or other calls that might timeout it might be a good idea to use ```@retry``` decorator. In case of an exception it will try to run given function again until its successful completion or until a defined number of retries is reached.

- ```functools``` implements ```@cache``` decorator which caches function outputs using a dictionary lookup for the function arguments. There is also ```lru_cache(maxsize=None)``` decorator which limits the number of function outputs it can remember (FIFO implementation).

- Similar to ```@cache``` there is a ```@cached``` decorator available in ```cachetools``` that allows for defining when output of a decorated function gets stale (TTL - time to live):

```python
from cachetools import cached, TTLCache

@cached(cahce=TTLCache(maxsize=2, ttl=900))  # function output lives for 1.5 h
def foo():
    pass
```

- ```typing``` module provides runtime support for type hints:

```python
from typing import List

Vector = List[float]
```

## FastAPI

- FastAPI is a tool for building web applications in Python.

- To start a server with a running FastAPI: ```uvicorn [file_name]:[app_name] --reload```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "hello world again"}

@app.get("/users/{user_id}")
def read_user(user_id: str):
    return {"user_id": user_id}

# It is possible to send JSON to FastAPI
from pydantic import BaseModel, validator

# To define required JSON type use BaseModel class from pydantic
class Item(BaseModel):
    name: str
    price: float

    # JSON can have multiple different types and to confirm that
    # received format is correct we can use validator that is part of pydantic
    @validator("price")
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError(f"we expect price >= 0, we received {value}")
        return value

@app.post("/items/")
def create_item(item: Item):
    """
    Example of a docstring.
    """
    return item

# async code in FastAPI
import time
import asyncio

@app.get("/sleep_slow")
def sleep_slow():
    time.sleep(1)
    return {"status": "done"}

@app.get("/sleep_fast")
async def sleep_fast():
    await asyncio.sleep(1)
    return {"status": "done"}


```

- Documentation is available in */docs* where Swagger UI lists all of the methods. Additional descriptions are taken from the docstring.

- Web APIs can be tested using ```boom```. In both commands ```boom``` will send a total of (defined via ```-n```) 200 requests and will do it with a concurrency of 200 (defined via ```-c```):

```python
boom http://127.0.0.1:8000/sleep_slow -c 200 -n 200
boom http://127.0.0.1:8000/sleep_fast -c 200 -n 200
```

- Testing FastAPI:

```python
from starlette.testclient import TestClient
from app import app

client = TestClient(app)

def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message": "hello world again"}

def test_users_endpoint():
    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.json() == {"user_id": "1"}

def test_correct_item():
    json_blob = {"name": "shampoo", "price": 1.5}
    resp = client.post("/items/", json=json_blob)
    assert resp.status_code == 200

def test_wrong_item():
    json_blob = {"name": "shampoo", "price": -1.5}
    resp = client.post("/items/", json=json_blob)
    assert resp.status_code != 200
```

## Conda 101

- Creating an environment in specified location:

```bash
conda create --prefix ./envs python=3.82 package_1 package_2 package_3=1.0.0
```

- Creating an environment in Anaconda installation path with unique name:

```bash
conda create --name env_name
```

- Removing environment based on the name and path:

```bash
conda remove --name env_name --all  # name based
conda remove --prefix ./envs --all  # path based

conda info --envs # checking whether environment has been successfully removed
```

- Activating/deactivating conda's environment:

```bash
conda activate name
conda activate ./path

conda deactivate
```

## virtualenv

- Creating new virtual environment:

```bash
virtualenv venv --python=python3.8.5
# or
python -m virtualenv /path/to/new/virtual/environment
```

- Activating venv:

```bash
source ./venv/bin/activate         # Terminal
.\venv\Scripts\activate.ps1     # Powershell
.\venv\Scripts\activate.bat     # Command Line
```

- Deactivating virtualenv ```deactivate```.

- To check which Python executable is being used in the activated virtual environment use: ```python -c "import os, sys; print(os.path.dirname(sys.executable))```.

- To get the list of libraries and their versions in the curently used Python environment use ```pip freeze```. On Linux use ```pip freeze > requirements.txt``` to dump the output into a text file.

- Libraries from *requirements.txt* can be installed with ```pip install -r requirements.txt```.

## pipenv

- A new standard for managing virtual environments.

- To initiate a virtualenv for the given project use ```pipenv install``` in case of *requirements.txt* being available in a directory or use ```pipenv install any_package``` to install desired package and initiate virtual env.

## Git 101

### General

- Checking the username ```git config --global user.name "your name goes here"```.

- After creating a new directory a Git repository initialization is done via ```git init```.

- Repo status is checked with ```git status```.

- Adding a file to the stage so changes to the file will be ready for the next commit ```git add file_name```.

- Commiting ```git commit -m "commit message"```.

- To stage and commit all of the files with changes use `git commit -am "commit message"` (this applies only to the files that have already been added before).

- Within a *.gitignore* file list of files/folders to be ignored by Git can be provided:

```bash
# .gitignore
__pycache__
venv
env
.pytest_cache
.coverage
```

- Within Git only source files should be stored - not the output files or large binary files (binary files do not have good diff tools so most of the time they will have to be stored fully each time they are committed).

- ```git log``` shows history of all the commits that have been made up to this point.

- *SHA* is an unique (most likely) identifier of a commit in a given repository whereas a *HEAD* indicates on what commit I am currently working on.

- Instead of using *SHAs* to move between commits refs can be used:

```bash
git switch HEAD^  # switches to the parent of HEAD
git switch HEAD~3  # switches to the great great grandparent of HEAD
```

- `git branch` will list all of the branches in the repository and will mark the currently used one.

- ```git checkout <SHA>``` or ```git switch <SHA>``` switches between the commits. In order to get back to the origin use ```git checkout master/main```.

- If any changes are made when *HEAD* is detached those can be saved using ```git checkout -b <new-branch-name>``` or with a new syntax ```switch -c <new-branch-name>```.

- ```git checkout -b <new-branch-name>``` creates a new branch to work on (*b* flag indicates that we want to create a **new** branch). New branch starts at the location *HEAD* was currently at.

- To compare branches together use ```git show-branch <first-branch> <second-branch>```. If instead of labels you want to see *SHAs* use ```git show-branch --sha1-name <first-branch> <second-branch>```

- To revert a file to its state from the last commit use `git checkout <file_name>`.

### Branch Management

- When you create a branch locally, it exists only locally until it is pushed to GitHub where it becomes the remote branch:

```bash
# create a new branch
git branch new-branch
# change environment to the new branch
git checkout new-branch
# create a change
touch new-file.js
# commit the change
git add .
git commit -m "add new file"
# push to a new branch
git push --set-upstream origin new-branch
```

- To fetch all the remote branches from the repository `git fetch origin`.

- To see the branches available for checkout `git branch -a`.

- You cannot make changes directly on a remote branch. Hence, you need a copy of that branch. To copy the remote branch *fix-failing-tests*: `git checkout -b fix-failing-tests origin/fix-failing-tests`.

### Merging

- There are three main ways to combine commits from two different branches:

  1. **Merging** - from the master branch (or any other to which we want to merge changes) ```git merge <branch-name>```.
  2. **Rebasing** - similar to merging - if both branches have commits then a new *merge commit* is created: ```git rebase <base_branch> <branch_to_be_rebased>```.
  3. **Cherry-picking** - you specify exactly which commits (using their *SHAs*) you mean to merge with the master ```git cherry-pick <SHA_ID>```.

- **Cherry-picking** is a way of copying certain commits to HEAD: ```git cherry-pick <Commit1> <Commit2> <...>```.

- **Interactive rebase** allows for picking exact commits and their order that will be picked to indicated location ```git rebase -i HEAD~3```.

- If changes need to be done to an earlier commit without changes to the commit flow (commit tree) following can be done:

  - re-order the commits so the one we want to change is on top with ```git rebase -i```,
  - ```git commit --amend``` to make the slight modification,
  - re-order the commits back to how they were previously with ```git rebase -i```.

- Above can be done using ```git cherry-pick```:

  - get to the desired branch and cherry-pick commit that requires changes,
  - amend cherry-picked change,
  - cherry-pick all of following commits to get the previous order.

- To move branch to the other commits ```git branch -f main HEAD~3``` can be used.

- To delete a branch `git branch -d <branch_name>` - this is especially useful when some bug fixing/new feature development has happened on a new branch and master branch has already been merged with such branch so it can be deleted.

### Tags

- To permanently mark a certain commit as a milestone that can be referenced like a branch but cannot be move to other commits use: ```git tav tag_name [tag_location (default is HEAD)]```.

- Because tags serve as such great "anchors" in the codebase, git has a command to describe where you are relative to the closest "anchor" (aka tag). And that command is called `git describe`!

### Remote Repos

- Usual path to contribute to other's projects: fork repository -> clone -> make changes -> commit -> pull request.

- To reset **local** changes use ```git reset HEAD``` - this will *change history* by reverting branch backwards as if the commit had never been made in the first place.

- To revert changes in the remote branches use ```git revert HEAD```.

- Working with remote repos:

  - cloning a repo: ```git clone git@github.com:sunnyfloyd/python-learning-points-and-improvements.git``` OR add remote repo with `git remote add name-of-repo https://github.com/me50/sunnyfloyd.git OR userna5@desination:/home/userna5/production.git`;
  - checking whether remote repo is already configured: ```git remote -v```;
  - configuring remote repo: ```git remote add <remote_stream_name> https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git```;
  - OPTIONAL (if assigning local git repo to a remote one instead of cloning): `git push --set-upstream <remote_stream_name> <branch name (master)>`. This might also need configuring on the branch level as well: `git branch --set-upstream-to=<remote_upstream>/<remote_branch> <local_branch>`;
  - fetching (retrieving latest meta-data info from the online repo) a repo: ```git fetch```;
  - pulling (combination of ```fetch``` and ```merge``` since it actually brings copy of eventual changes from the remote repo): ```git pull```;
  - pushing: ```git push```.

### GitHub Actions

- **Continous Integration**
  - frequent merges to main branch
  - automated unit testing

- **Continous Delivery**
  - short release schedules

- **GitHub Actions** will allow us to create workflows where we can specify certain actions to be performed every time someone pushes to a git repository. For example, we might want to check with every push that a style guide is adhered to, or that a set of unit tests is passed.

- Github Actions uses **YAML** to specify the CI workflow:

```YAML
# In .github/workflows/ci.yml
name: Testing
on: push

jobs:
  test_project:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run Django unit tests
      run: |
        pip3 install --user django
        python3 manage.py test 
```

## Testing

### Unit Testing

- Test are best to best stored in a separate file with following naming convention: *test%* or *%test*.

- Testing is being run with ```pytest file_name``` command.

- Boiler plate for basic testing:

```python
from fizz_buzz import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Check that output is 'Fizz' for numbers divisible by 3"""
        for i in [3, 6, 9, 18]:
            print('testing', i)
            assert fizzbuzz(i) == 'Fizz'
            # alternatively:
            self.assertTrue(fizzbuzz(i) == 'Fizz')

if __name__ == '__main__':
    unittest.main()
```

- The ```setUp()``` and ```tearDown()``` methods are special methods that the unit testing framework executes before and after each test respectively.

- pytest by default does not check how much of a code is being covered by written test cases. To test code coverage ```pytest-cov``` plugin for pytest needs to be installed (```pip install pytest-cov```).

- Use ```pytest --cov=fizz_buzz``` to call coverage test on a single (*fizz_buzz*) module (file). If the scope is not restricted, then code coverage will apply to the entire Python process, which will include functions from the Python standard library and third-party dependencies, resulting in a very noisy report at the end.

- To get more verbose report that includes code lines that are not covered use ```pytest --cov=fizz_buzz --cov-report=term-missing```

- The code **coverage analysis can also be configured to treat lines with conditionals as needing double coverage to account for the two possible outcomes**. This is called **branch coverage** and is enabled with the ```--cov-branch``` option: ```pytest --cov=fizz_buzz --cov-report=term-missing --cov-branch```.

- For cases where you as a developer make a conscious decision that a piece of code does not need to be tested, it is possible to mark these lines as an exception, and with that they will be counted as covered and will not appear in coverage reports as missing. This is done by adding a comment with the text ```pragma: no cover``` to the line or lines in question.

## Docker

- **Containers** are isolated environments that have seperate processes, network and mounts, but share the same OS kernel. Applications are separated and can use different libraries and have different dependencies.

- Docker, unlike hypervisors, is not meant to virtualize environments of the different systems. Main purpose of Docker is to package and containerize the application and to ship it and to run it anywhere, at any time, as many times as desired.

- **Docker image** is just a package template that is used to create containers. Images for different technologies are available on **Docker Hub**.

### Commands

- To run a new instance of an app use: ```docker run [container]```. Use ```run -d``` to run a container in a detached mode. To attach a container running in a detached state use ```docker attach [container_id]```.

- To list all installed images ```docker images``` or ```docker image ls```.

- ```docker ps``` - lists currently running containers. ```docker ps -a``` - lists all containers (running currently or in the past).

- ```docker stop [container]``` - stops running container.

- ```docker rm [container]``` - removes a container permanently.

- ```docker rmi [image]``` - removes an image (all related containers must be stopped before deleting an image).

- ```docker pull [docker-hub-user/image-name]``` - pull image without running it.

### Dockerfile

- After creating a 'Dockerfile' it should be populated with instructions:

```docker
FROM node:alpine
COPY . /app
CMD node /app/app.js
```

- To build an image ```docker build -t app-tag .``` or to specify dockerfile location ```docker build -f Dockerfile -t app-tag```.

### Django Docker Set-up (vide CS50)

- First step is to create a Docker File which we’ll name Dockerfile. Inside this file, we’ll provide instructions for how to create a Docker Image which describes the libraries and binaries we wish to include in our container. Here’s an example of what our Dockerfile might look like:

```docker
FROM python:3
COPY .  /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
```

- `FROM python:3` this shows that we are basing this image off of a standard image in which Python 3 is installed. This is fairly common when writing a Docker File, as it allows you to avoid the work of re-defining the same basic setup with each new image
- `COPY . /usr/src/app`: This shows that we wish to copy everything from our current directory (.) and store it in the /usr/src/app directory in our new container.
- `WORKDIR /usr/src/app`: This sets up where we will run commands within the container. (A bit like cd on the terminal)
- `RUN pip install -r requirements.txt`: In this line, assuming you’ve included all of your requirements to a file called requirements.txt, they will all be installed within the container.
- 'CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]': Finally, we specify the command that should be run when we start up the container.

- To run a separate server for our database, we can simply add another Docker container, and run them together using a feature called Docker Compose. This will allow two different servers to run in separate containers, but also be able to communicate with one another. To specify this, we’ll use a YAML file called docker-compose.yml:

```YAML
version: '3'

services:
    db:
        image: postgres

    web:
        build: .
        volumes:
            - .:/usr/src/app
        ports:
            - "8000:8000"
```

- Specify that we’re using version 3 of Docker Compose
- Outline two services:
  - `db` sets up our database container based on an image already written by Postgres.
  - `web` sets up our server’s container by instructing Docker to:
    - Use the Dockerfile within the current directory.
    - Use the specified path within the container.
    - Link port 8000 within the container to port 8000 on our computer.

- Now, we’re ready to start up our services with the command `docker-compose up`. This will launch both of our servers inside of new Docker containers.

- At this point, we may want to run commands within our Docker container to add database entries or run tests. To do this, we’ll first run `docker ps` to show all of the docker containers that are running. Then, well find the **CONTAINER ID** of the container we wish to enter and run `docker exec -it CONTAINER_ID bash -l`. This will move you inside the *usr/src/app* directory we set up within our container. We can run any commands we wish inside that container and then exit by running **CTRL-D**.

## Linux

- ```history``` and then ```![number]```
- ```echo```
- ```ls```, ```ls -1```, ```ls -l```
- ```pwd```
- ```cd```, ```cd ~```
- ```mkdir```
- ```touch```
- ```mv file_name file_name2_and_location```
- ```rm file_name```, supports wildcards ```rm file*```
- ```rm -r directory_name```
- **nano** is a basic linux editor
- ```apt update```
- ```apt install```
- ```cat file_name```, when long file ```more file_name```, use this to scroll both ways ```less file_name```
- ```head -n 5 file_name```, ```tail -n 5 file_name```
- ```cat file.txt > file2.txt```, ```echo blabla > file.txt```, ```ls -l > files.txt```
- ```grep 'word' file_name```
- Search and display the total number of times that the string ‘nixcraft’ appears in a file named frontpage.md ```grep -c 'nixcraft' frontpage.md```.
- ```one command | second command``` - second command uses output from the first command.

## Design Patterns

**Design patterns** are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code. The pattern is not a specific piece of code, but a general concept for solving a particular problem. While an algorithm always defines a clear set of actions that can achieve some goal, a pattern is a more high-level description of a solution.

### Creational Patterns

**Creational Patterns** these patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

#### Factory Method

- **Factory Method** should be used in every situation where an application (client) depends on an interface (product) to perform a task and there are multiple concrete implementations of that interface. You need to provide a parameter that can identify the concrete implementation and use it in the creator to decide the concrete implementation.

- Advantages of using Factory method:
  - We can easily add the new types of products without disturbing the existing client code.
  - Generally, tight coupling is being avoided between the products and the creator classes and objects.

- Disadvantages of using Factory method:
  - To create a particluar concrete product object, client might have to sub-class the creator class.
  - You end up with huge number of small files i.e, cluttering of the files.

- Abstract product creation method (interface) -> concrete product creation methods -> abstract product (interface) -> concrete products

#### Abstract Factory

- **Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

- Client will not have to know what factory method or what product family he is operating on as all of them will have the same interface.

- This is basically a factory method, but concrete product creators are replaced with concrete products creators that create multiple products for a specific product family (for example buttons/checkboxes for Windows/Mac/Web UI families).

- Abstract factory creation method (interface) -> concrete factory creation methods -> products creation methods (within the factories) -> abstract products (interfaces) -> concrete products

#### Builder

- **Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

- Builder design pattern is especially useful in cases where there is a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Approaching such problem with **subclasses** may become very hard to manage and hard to refactor. Using a **single constructor** with all possible parameters that control the object creation will stop breeding subclasses, but the constructor calls will become bloated and ugly.

- Builder patters suggests extraction of the object construction code out of its own class and move it to separate objects called **builders**. The pattern organizes object construction into a set of steps (`buildWalls`, `buildDoor`, etc.). To create an object, you execute a series of these steps on a builder object. The important part is that you don’t need to call all of the steps. You can call only those steps that are necessary for producing a particular configuration of an object.

- Some of the construction steps might require different implementation when you need to build various representations of the product. For example, walls of a cabin may be built of wood, but the castle walls must be built with stone. In this case, **you can create several different builder classes that implement the same set of building steps, but in a different manner**. Then you can use these builders in the construction process (i.e., an ordered set of calls to the building steps) to produce different kinds of objects.

- You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called **director**. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.

#### Singleton

- **Singleton** is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code. It is not recommended to be used in Python and it should be replaced with a class instance assigned to a global variable.

- Below, ```super(Singleton, cls).__call__``` (also ```super()``` implicitly) means that ```Singleton``` determines that the starting point in **Method Resolution Order (MRO)** will be a ```Singleton``` class, but MRO from the passed *cls* (```Singleton```) will be used. This concludes in the ```super()``` calling a standard ```__call__``` method that is inherited from the main metaclass of all classes - ```type```. ```super()``` already passes ```Singleton``` clas in ```self```/```cls``` argument implicitly.

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    pass
```

#### Prototype

- **Prototype** is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

- Python provides its own interface of Prototype via `copy.copy` and `copy.deepcopy` functions. And any class that wants to implement custom implementations have to override `__copy__` and `__deepcopy__` member functions.

- Good to remember that `__dict__` is implemented by default and it outputs all of the attributes of a given object.

### Structural Patterns

- PLACEHOLDER

## Backend Topics

### OSI (Open Systems Interconnection) Model

- OSI Model is a conceptual framework used to describe the functions of a networking system. Any device that communicates with other device is operating based on this framework. OSI model itself in its characterisation of the communication functions does not refer to the underlying internal structure or technology.

- OSI model has 7 abstract layers and communication goes both ways:

  - application layer to physical layer called **encapsulation**
  - physical layer to application layer called **decapsulation**.

- **Protocol Data Unit** (PDU) is a data that is being prepared by 3 layers: application (prepares application flows), presentation (f.e. encryption in HTTPS), session (establishes session).

- **Transport** layer create segments adding port (source and destination) to each segment to identify to what application given data is addressed (in most cases done by TCP protocol).

- **Network** layer creates packets adding source and destination addresses (sender and receiver IP addresses).

**Data Link** layer creates frames (only layer where header and trailer are present) and uses **Ethernet** as a standard to conver logical stuff into a physical stuff. Ethernet has source and destination addresses as well, but those are physical (MAC address).

- **Physical** layer transfers Bits into signal and carries them.

- Important thing about communication in the Internet is that all of the endpoints connected to the same access point will receive all of the information that is sent and received in this network. It means that data link layer is responsible to determine whether given data is addressed to this device and act accordingly. In some cases MAC address may point to an access point like router, but might be addressed in the network layer to other device using IP address.

### TCP vs UDP

- TCP and UDP are communication protocols that allow to send and receive data in a network. They are part of **transport layer** in OSI model (layer 4).

- **Internet Protocol** (IP) address is the identifier that allows information to be sent between devices on a network. Each device might run multiple application and that is why **ports** are required. They help to identify specifc application from and to data is sent.

#### TCP

- **Transmission Control Protocol (TCP)**

- **Pros**:
  - **acknowledgement** - clients talk to each other and ensure that sent data has been received
  - **guaranteed delivery** - resending undelivered/corrupted packets
  - **connection based** - clients need to establish a connection before sending an actual data (**stateful connection**)
  - **congestion control** - managing the flow of data depending on current network capacity
  - **ordered packets**.

- **Cons**:
  - **larger packets** - TCP adds lot of overhead (packet headers)
  - **more bandwidth**
  - **slower than UDP**
  - **stateful**
  - **server memory (DOS)** - server needs to allocate memory for each connection; for example, if one client sends multiple requests and do not confirm whether it received a response it might bloat the server's memory.

#### UDP

- **User Datagram Protocol (UDP)**

- **Pros**:
  - **smaller packets**
  - **less bandwidth** - this is why it is often used in online games. However, this is then often implemented in the form of **reliable UDP** that implements some overhead, but on the higher (application) level
  - **faster than TCP**
  - **stateless**.

- **Cons**:
  - **no acknowledgement**
  - **no guranteed delivery**
  - **connectionless**
  - **no congestion control** - UDP does not care about network capacity
  - **no ordered packets**
  - **security** - since there is no connection server does not know who is sending the data; this is why UDP is often blocked in the firewalls.

## Scrum Methodology

### Waterfall

- Analysis -> Design -> Develop -> Test -> Deploy

- All steps are done sequentially. If any changes/features have not been foreseen at the earlier stages, but later ones included them, previous stages need to be revisited and adjusted.

- Waterfall methodology relies on a formal plan with milestones. This plan is often a guess. If any stage takes longer than initially planned, the whole plan needs to change.

- Each stage is often done in isolation - there is no exchange of the information between phases.

- In Scrum methodology - all of the stages overlap each other.

### Agile Manifesto

1. Individuals and itneractions > Processes and tools
2. Working software > Comprehensive documentation
3. Customer collaboration > Contract negotation
4. Responding to change > Following a plan

### Agile Concepts

1. Short feedback loops
2. Just in time requiremnets and design
3. Delivering incremental value
4. Release ready deliverables (complete code, tested, integrated, documented, deployed)
5. Sustainable pace
6. Lean management hierarchy (not too many decision people)
7. Self-organizing teams (people can organize and manage themselves without unnecassary supervision - this will empower people)
8. Trust, courage and transparency balance
9. Continous delivery (idea that something can be taken from coding to deployment as fast as possible)
10. Embracing change
11. Inspect and adapt

### Scrum Overview

#### Roles

- Product owner:
  - maximizes product value
  - manages the product backlog
  - represents the users
  - single person

- Scrum Master:
  - shepard of Scrum
  - servant leader
  - removes impediments
  - resolves conflicts

- Development team:
  - cross functional
  - self organizing
  - highly collaborative
  - 5 - 9 members

#### Artifacts

- Product vision:
  - target market
  - business need/opportunity
  - key features
  - value to the company

- Product backlog:
  - single source of requirements
  - constantly evolving
  - ordered based on value
  - estimated by the development team

- Release plan:
  - forecast based on empirical data
  - overlay on the product backlog
  - updated every Sprint

- Sprint backlog:
  - product backlog items for a Sprint
  - plan to deliver a product increment
  - owned by the development team
  - dynamic and highly visible

- Burndown chart:
  - tracks work remaining by day
  - updated by the development team
  - displayed prominently

- Impediment list:
  - blocking or affecting performance
  - updated by the Scrum team
  - monitored by the Scrum Master

#### Events

- Sprint planning:
  - determines what will be delivered
  - past performance/capacity
  - determine how it will be delivered
  - create Sprint backlog

- The Sprint:
  - time boxed to one month or less
  - clearly stated Sprint goal
  - potentially releasable increment
  - scope set by a Scrum team

- Daily Scrum:
  - time boxed to 15 minutes
  - inspect work done yesterday
  - plan work for today
  - identify possible impediments

- Product backlog grooming:
  - clarifying and estimating new items
  - reviewing higher priority items
  - less detail on lower priority items
  - around 10% of the Sprint

- Sprint review:
  - demo product increment
  - elicit feedback from stakeholders
  - plan what to do next
  - review the release plan

- Sprint retrospective:
  - Scrum team inspect and adapt
  - what went well?
  - what can we do better?
  - plan for improvements

### Starting a Scrum Project

#### Sprint Zero (not recommended)

- Product vision
- Initial product backlog
- Initial release plan
- Architecture approach and coding practices
- Continous integration environment
- Small product increment

#### Creating a Product Vision

- Creating a product vision:
  - target market
  - business need/opportunity
  - key features
  - value to the company

- Qualities of a product vision:
  - broad and inspiring
  - clear and stable
  - short and sweet
  - highly visible
  - frequently revisited

#### Creating Initial Product Backlog

- Creating Initial Product Backlog
  - single source of requirements
  - constantly evolving
  - ordered based on value
  - estimated by the development team

- What goes on to the product backlog:
  - user requirements
  - technical requirements
  - bugs

#### User Stories

- short and simple
- user perspective
- focus on discussions

- Conditions of satisfaction:
  - required for acceptance
  - represent tests
  - specifc not details

- Conditions of good user stories:
  - independent
  - negotiable
  - valuable
  - estimable
  - small
  - testable

- Splitting user stories
  - theme
  - epic
  - user story (something that is small enough to fit into sprint)

#### Roles and Personas

- Think about actual customers when building a project.

#### Prioritizing Product Backlog

- Business value (increase revenue, reduce cost, attract new customers, retain customers)
- ROI (value/effort)
- Feature grouping
- Politics

- When prioritizing user stories 100 points can be assigned among all of the user stories to determine their priority level. Other method would be to assign score from 1 - 100 (additional meaning can be assigned to arbitraty ranges like: 90 - 100 -> customer will lose market share if not implemented)

#### Agile Estimation

- Story points
  - high level estimate of size (effort)
  - based on relative scale
  - estimated as a team
  - not based on duration
  - can use Fibonacci sequence for assigning story points - to get some reference point, well understood example by team members should be discussed and assigned story points
  - can use *planning poker* to assign points - if there is a large dispersion in points, more discussion is needed

#### Creating a Release Plan

- Determine a velocity (in story points as a unit) which is equal to historical amount of work that can be accomplished in a given time.

- To determine a velocity for a new team just discuss stories from product backlog and make a collective assumption how many stories, hence story points, this new team thinks it can complete in a given timeframe.

- Plan using the worst case scenario.

### Executing the Sprint

#### Holding the Sprint Planning Meeting

- Identify the sprint goal

- Create the **sprint backlog** - plan what work from the product backlog will be a target for a given sprint taking into consideration team's velocity.

- Backlog item chosen to be a part of a sprint should be discussed and broke into smaller tasks with time estimate for each task.

- Sprint backlog should be created with **SMART** technique (specific, measurable, achievable, relevant, time boxed).

- When deciding on commiting to a story - **fist of five** can be used. Number of fingers determine how much given person agrees/disagrees with current version of a story.

#### Working As a Scrum Team

- Limit work in progress - all team members should align with capacity of other people in the flow so that it is not disturbed (for example one person in the flow ends up with too much work that cannot be completed within the sprint).

#### Holding the Daily Scrum

- Daily Scrum meeting is strictly for planning for the development team. Other stakeholders may join such meeting, but this meeting should not be a status reporting for them.

- Same time and place.

- 15 minutes or less.

- Planning meeting, not a status meeting. This is what I am working on, and this is what I am held with - team discusses how to address this.

- Inspect progress - tell more about the task that you are currently on/just completed. Were there any issues? Are there any new tasks coming up that you did not expect?

  - What did you do yesterday?
  - What are you going to do today?
  - Any impediments?

- Use task board to visualize the progress with user stories (table with user stories and current progress in columns - not done, in progress, done, blocked).

- Use chart representing working hours remaining with a trendline providing information about the estimated time. Use sticky notes to explain bumps in the actual progress line (f.e. more tasks have been identified).

- Similar chart should be used to represent actual tasks (product backlog items) being completed. No trend line for this chart though.

#### Agile Engineering Practices

- Focus on new features and not frameworks - frameworks are not something that can be presented to the user.

- **YAGNI Principle** (You Ain't Gonna Need It) - focus on implementing the actual feature - do not try to make it overly robust or future-resilent. Concentrate on what is needed now and not gold plating.

##### Continous Integration

- Completed part of the code should be deployed as soon as possible and integrated with all the others newly deployed features.

- If newly integrated code makes the build fail, fixing the issues should be the top priority.

- **Test Driven Development** allows to develop in a fashion that starts from the perspective of a user and builds down to the backend features that support actual user needs/functionalities.

- **Automated Testing**:

  - Unit Tests - verify whether single module works as expected;
  - Integration Tests - verify whether modules work properly together;
  - Feature Tests - tests from the user perspective that focus on UI.

- Clear definition of task/work being done: features, tests, deployment, documentation.

#### Quality Assurance in Agile

- Start with developing tests, and after initial tests are created start developing a feature. Then test and code iteratively. After code freeze perform regression and integreation testing.

- QA Best Practices:

  - hire good quality QA engineers,
  - QA and dev sit together,
  - QA is involved in analysis and design,
  - Test as you go,
  - Make testing part of a definition of done,
  - Limit work in progress,
  - Everyone can help test,
  - Frequent, incremental releases for feedback,
  - Set bug queue limits.

- When bug is being found task for fixing this bug should be created and assigned to a developer, and test cases should be written to ensure that this bug will not escape.

- Dealing with bugs:

  - critical bugs
  - non-critical bugs
  - enhancements (those are not bugs - those are new product backlog items).

### Ending the Sprint

#### Sprint Review

- All of the stakeholders should be present.

- Less than 2 hours meeting

- Holding the sprint review:

  - demo what is *done*
  - review what wasn't done
  - review progress
  - discuss next steps.

#### Delivering a Product Increment

- Potentially shippable.

- Delivery is a non event.

- Hardening sprint - it is mainly about testing, and, in case of critical bugs, fixing them.

#### Sprint Retrospective

- Holding the sprint retrospective:

  - audience: product owner, development team, scrum master
  - equal voice
  - focus on improvement
  - prioritize (voting)
  - take real action.

- Take a table with two columns: 'what went well?' and 'what could be better?'. And ask people to write their opinions down in 10 minutes. Scrum master then reads them out loud and clarifies if needed and adds these suggestions to the columns grouping similar topics. Team then places poker chips on each item to identify which one should be discussed further.

## Reactive Programming (ReactiveX)

- Reactive programming allows to manipulate a stream of data with functions (asynchronously). It can be used when there are **asynchronous** **data streams** that can be manipulated/filtered using **functional programming**, and then send to the observers.

- Using **ReactiveX** (Rx), you can represent multiple asynchronous data streams (that come from diverse sources, e.g., stock quote, Tweets, computer events, web service requests, etc.), and **subscribe to the event stream** using the **Observer** object. The **Observable** notifies the subscribed Observer instance whenever an event occurs. You can put various transformations in-between the source Observable and the consuming Observer as well.

- Basic idea is that we have some **subject** emitting data and an **observer** who awaits this data. Before reaching the observer data might be filtered/changed using functional programming paradigm. This means that we are creating kind of a new data stream that filters out irrelevant data and applies some logic to the received items so they are ready for consumer to be processed.

- Reactive programming is especially popular in Android programming and other UI focused use cases.
