# Python

## Table of Contents

- [Python](#python)
  - [Table of Contents](#table-of-contents)
  - [Python Features](#python-features)
    - [Integers](#integers)
    - [Decimals](#decimals)
    - [Strings](#strings)
      - [Translation Tables](#translation-tables)
    - [Booleans and Python Logic](#booleans-and-python-logic)
    - [Loops](#loops)
    - [Iterables](#iterables)
      - [Lists](#lists)
      - [Tuples](#tuples)
        - [namedtuple](#namedtuple)
      - [Sets](#sets)
      - [Dictionaries](#dictionaries)
      - [Comprehensions](#comprehensions)
      - [itertools](#itertools)
      - [collections](#collections)
    - [operator](#operator)
    - [Functions](#functions)
      - [Caching](#caching)
      - [singledispatch](#singledispatch)
      - [map, filter, reduce, lambda](#map-filter-reduce-lambda)
      - [Structural Pattern Matching](#structural-pattern-matching)
    - [IO and Data Objects](#io-and-data-objects)
      - [Files](#files)
      - [JSON](#json)
    - [OOP](#oop)
      - [Classes](#classes)
        - [Typing](#typing)
      - [Inheritance](#inheritance)
      - [Multiple Inheritance](#multiple-inheritance)
      - [Abstract Classes](#abstract-classes)
      - [classmethod](#classmethod)
      - [dataclass](#dataclass)
      - [Exception Classes](#exception-classes)
    - [Decorators](#decorators)
      - [Class-based Decorators](#class-based-decorators)
    - [Closures](#closures)
    - [Underscores](#underscores)
    - [Asynchronous Programming](#asynchronous-programming)
      - [Multithreading](#multithreading)
        - [Sharing State in Threads](#sharing-state-in-threads)
        - [Racing Conditions in Multithread Code](#racing-conditions-in-multithread-code)
      - [Multiprocessing](#multiprocessing)
      - [Generators](#generators)
      - [Coroutines](#coroutines)
      - [AsyncIO](#asyncio)
    - [Bitwise Operators](#bitwise-operators)
    - [RegEx](#regex)
    - [Other](#other)
  - [Testing](#testing)
    - [Unit Testing](#unit-testing)
  - [Reactive Programming (ReactiveX)](#reactive-programming-reactivex)
  - [Virtual Environments](#virtual-environments)
    - [virtualenv](#virtualenv)
    - [pipenv](#pipenv)
    - [Conda](#conda)
    - [Poetry](#poetry)
  - [Algorithms](#algorithms)

## Python Features

### Integers

- ```int()``` takes optional argument that indicates base of the provided number. *int* object can be compared to other *int* objects regardless of their base.

### Decimals

- ```decimal``` module in Python provides support for fast correctly-rounded decimal floating point arithmetics. Module is especially useful when precision of floating numbers arithmetic is crucial or when floating numbers need to be presented in the people-friendly way based on the arithmetics that people know from school.

### Strings

- Strings can be compared with other strings. Comparison lexicographical.

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

- ```textwrap.wrap(string, width=70)``` wraps the single paragraph (*string*) so that every line is at most *width* characters long. Returns a list of output lines:
-

```python
from textwrap import wrap

value = "AUGUUUUAA"
print(wrap(value, 3)) # ['AUG', 'UUU', 'UAA']
```

- Unicode might encode the same-looking characters in a different way. To compare strings that contain such characters we should normalize such strings with `unicodedata.normalize`. There are 4 methods of string normalization: NFC, NFD, NFKC, NFKD. NFC (canonical decomposition and composition) or NFD (canonical decomposition) are recommended in most cases since other methods may distort output due to formatting differences. To include case-insensitive comparisons use `str.casefold()`.

- Diacritic characters can be removed with the combination of NFD and NFC normalization:

```py
def shave_marks(txt):
    """Remove all diacritic marks"""
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)

# or to remove combining marks only from Latin characters

def shave_marks_latin(txt):
    """Remove all diacritic marks from Latin base characters"""
    norm_txt = unicodedata.normalize("NFD", txt)
    latin_base = False
    preserve = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # ignore diacritic on Latin base char
        preserve.append(c)
        # if it isn't a combining char, it's a new base char
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = "".join(preserve)
    return unicodedata.normalize("NFC", shaved)
```

- To properly sort strings with non-English characters use `pyuca` library. If you need to be super precise you can use `PyICU` library that can work like locale without changing locale:

```py
import pyuca
coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
sorted_fruits
# ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']
```

#### Translation Tables

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

### Booleans and Python Logic

- **Falsy statements** in Python are:
  - False
  - None
  - 0
  - ''
  - ()
  - []
  - {}

- ```is``` operator checks whether given two objects are the same and therefore they are located in the same memory address. However, due to the optimisation reasons within the Python's interpreter some immutable objects are kept around [for example integers from -5 to 256 and latin-1 characters (where ```len(char) == 1```)]. Those objects are shared by references/variables that refer to these optimised values.

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

### Loops

- ```else``` statement can be used after for-loop. Block within ```else``` will be executed if for-loop is not terminated by a `break` statement. It can aslo be used to execute code if for loop is executed till then end (just to indicate it):

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

- It is Pythonic to use infinite while-loops that will be ended with ```break``` statement:

```python
count = 0
while True:
    print('Hello')
    if count == 5:
        break
    count += 1
```

### Iterables

- Iterator can be created on an object with the use of ```iter()```:

```python
arr = [1, 2, 3, 4, 5]
ARR = iter(arr) # Returns an iterator object for given object
a = next(ARR) # Returns next item from  the iterated object
```

- When iterating through a list of tuples (or other iterable objects within iterable objects) unpacking can be used:

```python
t = [(1, 'a'), (2, 'b'), (3, 'c')]
arr = [c for n, c in t]
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

- Unpacking operator (```*``` or ```**```) can be used when assigning values to the variables:

```python
my_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b)
print(c)
```

- Slices can be named (by assigning them to the variable) with `slice`:

```python
SKU = slice(0, 6)
DESCRIPTION = slice(6, 40)
```

#### Lists

- List slicing does not produce out of bound error because slicing is used to create a new list. If the indices don't fall within the range of the number of elements in the list, we can return an empty list. So, we don't have to throw an error. But, if we try to access the elements in the list which is greater than the number of elements, we cannot return any default value (not even None because it could be a valid value in the list).

- Lists are meant to be used for sequences of the same type, whereas tuples are meant for sequences of different types.

- When we want to make sure that getting an item from a sequence will return an iterable of a same type instead of the individual element we need to use slicing (```el[:1]``` instead of ```el[0]```).

#### Tuples

- Unpacked tuple object can be passed to the ```range()```:

```python
# Clever way to define parameters for range() - either increasing or decreasing order:
args = (mn**2, mx**2+1) if smallest else (mx**2, mn**2-1, -1)

    for r in range(*args):
        pass
```

- Tuple can be checked if it contains any mutable items by calling `hash(t)`. It will raise `TypeError` when mutable object is found.

##### namedtuple

- **Named tuples** provide useful `__repr__` and meaningful `__eq__`. Named tuples can be created with either `collections.namedtuple` or `typing.NamedTuple` the latter allowing for additional typing.

```py
# collections.namedtuple
from collections import namedtuple
Coordinate = namedtuple('Coordinate', 'lat lon')
moscow = Coordinate(55.756, 37.617)

# typing.NamedTuple
import typing
Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
# alternatively fields can be given as keyword arguments:
Coordinate = typing.NamedTuple('Coordinate', lat=float, lon=float)
moscow = Coordinate(55.756, 37.617)
```

- Since Python 3.6, `typing.NamedTuple` can also be used in a class statement, with type annotations. Although `NamedTuple` appears in the class statement as a superclass, it’s actually not. `typing.NamedTuple` uses the advanced functionality of a metaclass to customize the creation of the user’s class:

```py
from typing import NamedTuple 
 
class Coordinate(NamedTuple): 
    lat: float 
    lon: float  
    def __str__(self): 
        ns = 'N' if self.lat >= 0 else 'S' 
        we = 'E' if self.lon >= 0 else 'W' 
        return f'{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}'
```

- ```_asdict()``` is a method of available in both *namedtuple* and `NamedTuple` that returns a dict which maps field names to their corresponding values:

```python
p = Point(x=11, y=22)
p._asdict()
{'x': 11, 'y': 22}
```

#### Sets

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

#### Dictionaries

- ```dict.keys()``` method returns a special object of type *dict_keys* that implements several of the same methods available on sets including union and intersection.

- ```dictionary.update()``` updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

- In order to create a dictionary with a list of default values for all of the keys use ```dict.fromkeys(keys, 0)```.

#### Comprehensions

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

#### itertools

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

- ```itertools.chain(*iterables)```  basically combines all of the iterables together so that one can iterate through them in one go:

```python
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
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

#### collections

- Sometimes, when the ```KeyError``` is raised when working with dictionaries, it might become a problem. To overcome this, Python introduces another dictionary like container known as **Defaultdict** which is present inside the collections module. It applies default value based on function call for new keys in dictionary:

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

### operator

- ```operator.itemgetter(*item)``` returns a function that fetches item from its operand using the operand’s ```__getitem__()``` method. **If multiple items are specified, returns a tuple of lookup values**. This basically puts provided arguments in square brackets on the object that function was called.

```py
f = itemgetter(2)
# the call f(r) returns r[2]

g = itemgetter(2, 5, 3)
# the call g(r) returns (r[2], r[5], r[3])
```

- ```operator.attrgetter``` returns a callable object that fetches attr from its operand. **If more than one attribute is requested, returns a tuple of attributes**. The attribute names can also contain dots. For example:

```py
f = attrgetter('name')
# the call f(b) returns b.name
f = attrgetter('name', 'date')
# the call f(b) returns (b.name, b.date)
f = attrgetter('name.first', 'name.last')
# the call f(b) returns (b.name.first, b.name.last)
```

### Functions

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

- ```*args``` is stored as a tuple whereas ```**kwargs``` is stored as a dictionary.

- There is an optional convention that increases readability to put what type of value defined function return:

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

- When a function depends on HTTP requests or other calls that might timeout it might be a good idea to use ```@retry``` decorator. In case of an exception it will try to run given function again until its successful completion or until a defined number of retries is reached.

#### Caching

- ```functools``` implements ```@cache``` decorator which caches function outputs using a dictionary lookup for the function arguments. There is also ```lru_cache(maxsize=None)``` decorator which limits the number of function outputs it can remember (FIFO implementation).

- Similar to ```@cache``` there is a ```@cached``` decorator available in ```cachetools``` that allows for defining when output of a decorated function gets stale (TTL - time to live):

```python
from cachetools import cached, TTLCache

@cached(cache=TTLCache(maxsize=2, ttl=900))  # function output lives for 1.5 h
def foo():
    pass
```

#### singledispatch

- The `functools.singledispatch` decorator allows different modules to contribute to the overall solution, and lets you easily provide specialized functions even for types that belong to third-party packages that you can’t edit. If you decorate a plain function with `@singledispatch`, it becomes the entry point for a generic function: a group of functions to perform the same operation in different ways, depending on the type of the first argument.

```py
from functools import singledispatch
from collections import abc
import html
import numbers

@singledispatch
def htmlize(obj: object) -> str:
    content = html.escape(repr(obj))
    return f"<pre>{content}</pre>"

@htmlize.register
def _(text: str) -> str:
    content = html.escape(text).replace("\n", "<br/>\n")
    return f"<p>{content}</p>"

@htmlize.register
def _(seq: abc.Sequence) -> str:
    inner = "</li>\n<li>".join(htmlize(item) for item in seq)
    return "<ul>\n<li>" + inner + "</li>\n</ul>"

@htmlize.register
def _(n: numbers.Integral) -> str:
    return f"<pre>{n} (0x{n:x})</pre>"
```

#### map, filter, reduce, lambda

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

- When `None` is used as the first argument to the `filter()` function, all elements that are truthy values (those that give `True` if converted to boolean) are extracted.

- ```reduce(foo, iterable)``` function passed to reduce must take 2 arguments - it starts with first 2 items from the iterable and then continues with first argument being a previously returned value and next item from the iterable:

```python
s = ['s','t','r','i','n','g']
s_joined1 = reduce(lambda x, y: x + y, s)
s_joined2 = ''.join(s)
```

#### Structural Pattern Matching

- [Mastering Structural Pattern Matching](https://www.inspiredpython.com/course/pattern-matching/mastering-structural-pattern-matching)

- **Pattern matching** removes the verbiage and tedium of `if` statements and “getters” that interrogate the structure of an object to extract the information you want.

- `match` is a **soft keyword**. A soft keyword, like the `match` statement, is a keyword that does not cause a syntax error if used in a context that is unambiguously not part of a match pattern matching block. That means you can continue to use `match` as a variable or function name, for instance.

```py
match <expression>:
    case <pattern 1> [<if guard>]:
        <handle pattern 1>
    case <pattern n> [<if guard>]:
        <handle pattern n>
```

- Basic example:

```py
def greet_person(p):
    """Let's greet a person"""
    match p:
        case {"greeting": greeting, "name": name}:
            print(f"{greeting}, {name}")
        case {"name": name}:
            print(f"Hello, {name}!")
        case {"greeting": _} | {}:
            print("I didn't quite catch your name?")
        case str() as person if person.isupper():
            print("No need to shout - I'm not deaf")
        case str() as person:
            print(f"Nice to meet you, {person}.")
        case _:
            print("I didn't quite understand that!")
```

- Note that mapping patterns (like a dict above), unlike sequence patterns, succeed on partial matches which means that case does not have to include all of the potential objects. To catch remaining objects `**extra` can be used (do not use `**_` as it would be redundant):

```python
food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
    print(f'Ice cream details: {details}')
# Ice cream details: {'flavor': 'vanilla', 'cost': 199}
```

- Capture patterns use **bound names** that are not variables, but can be accessed in the code after pattern is successfully matched:

```py
def greet_person(p):
    """Let's greet a person"""
    match p:
        case {"greeting": greeting, "name": name}:
            print(f"{greeting}, {name}")
```

- Literal patterns:

```py
def literal_pattern(p):
    match p:
        case 1:
            print("You said the number 1")
        case 42:
            print("You said the number 42")
        case "Hello":
            print("You said Hello")
        case True:
            print("You said True")
        case 3.14:
            print("You said Pi")
        case _:
            print("You said something else")
```

- To ensure specific data type:

```py
case int(1):
    print("You said the integer 1")
# or
case float(1.0):
    print("You said the floating point number 1.0")
```

- To bind declaration in pattern to a name that you can use later, you must use the `as` pattern:

```py
def as_pattern(p):
    match p:
        case int() as number:
            print(f"You said a {number=}")
        case str() as string:
            print(f"Here is your {string=}")
```

- Guards:

```py
def greet_person(p):
    """Let's greet a person"""
    match p:
        # ... etc ...
        case str() as person if person.isupper():
            print("No need to shout - I'm not deaf")
        case str() as person:
            print(f"Nice to meet you, {person}.")

# OR
match json.loads(record):
    case {"user_id": user_id, "name": name} if not has_user(user_id):
        return create_user(user_id=user_id, name=name)
    case {"user_id": user_id}:
        return get_user(user_id)
    case _:
        raise ValueError('Record is invalid')
```

- `OR` patterns:

```py
def or_pattern(p):
    match p:
        case ("Hello" | "Hi" | "Howdy") as greeting:
            print(f"You said {greeting=}")
        case {"greeting": "Hi" | "Hello",
              "name": ({"first_name": name} | {"name": name})}:
            print(f"Salutations, {name}")
```

- Wildcard patterns:

```py
match p:
    # ... etc ...
    case _:
        # ... do something. ..

# interrogating structures using wildcards
def wildcardpattern(p):
    match p:
        case [_, middle, _]:
            print(middle)

# *args and **kwargs
def star_wildcard(p):
    match p:
        case [_, _, *rest]:
            print(rest)
        case {"name": _, **rest}:
            print(rest)

# **rest for dict
match {"a": 1, "b": 2}:
    case {"a": 1, **rest} as d if not rest:
         print(d)
```

- In order to create a dynamic value for a pattern variable/constant needs to used as an attribute:

```py
import constants

def value_pattern_working(p):
    match p:
        case {"greeting": constants.PREFERRED_GREETING, "name": name} as d:
            print(d)
        case _:
            print('No match!')
```

- Class patterns:

```py
from collections import namedtuple

Customer = namedtuple('Customer', 'name product')

def read_customer(p):
    match p:
        case Customer(name=name, product=product):
            print(f'{name}, you must really like {product}.')
```

- Class pattern in the anti-pattern class. Thankfully, Python is clever enough to **not create instance of Connection during the pattern matching step** so `connect` method is not called:

```py
class Connection:

    def connect(self):
        print(f'Connecting to server {self.host}')
        # ... do something complicated ...

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connect()

def parse_connection(p):
    match p:
        case Connection(host=host, port=port):
            print(f'This Connection object talks to {host}')
```

- Literal with variable patterns:

```py
def evaluate(exp, env):
    match exp:
        case ['quote', x]:
            return x
        case ['if', test, consequence, alternative]:
            return foo(consequence, env)
        case ['lambda', [*params], *body] if body:
            ...
        case ['lambda', [Symbol() as name, *params], *body] if body:
            ...
        case _:
            raise SyntaxError()
```

- Destructuring object can be customized by `__match_args__` that defines which attributes in what order can be used to match object instance. This is useful for custom classes for which we want to save some keystrokes:

```py
class Vector2d
    # ...
    __match_args__ == ["x", "y"]

# before defining __match_args__
match vector:
    case Vector2d(x=0, y=0)

# after defining __match_args__
match vector:
    case Vector2d(0, 0)
```

### IO and Data Objects

#### Files

- Files can be accessed within the context indicated by ```with``` keyword. ```with``` operates on the objects that have ```__enter__``` and ```__exit__``` magic methods impletemented as part of their class. Especially useful for working with files since it ensures that file will be properly closed when program exits a block defined by ```with```:

```python
with open(infilename) as infile:
    pass

# 'with' can also operate on 2 or more objects within the same context:
with open(infilename) as infile, open(outfilename, 'w') as outfile:
    for one_line in infile:
        outfile.write(f'{one_line.rstrip()[::-1]}\n')
```

- If code might be reading and writing files on different machines (Windows, Unix, etc.), explicit encoding should be used. If encoding argument is omitted default encoding is given by `locale.getpreferredencoding()`.

```py
open("cafe.txt", "w", encoding="utf_8")
open("cafe.txt", encoding="utf_8").read()
fp = open("cafe.txt")  # without explicit encoding cp1252 encoding is assumed on Windows
# <_io.TextIOWrapper name='cafe.txt' mode='r' encoding='cp1252'> 
```

- To discover file encoding use [chardet](https://pypi.org/project/chardet/).

#### JSON

- JSON files can be read and construct with the ```json``` module:

```python
import json

json.dumps(obj)  # serializes object to JSON formatted string
json.dump(obj, file)  # same as above but output is being written to a file

json.loads(json)  # deserialize JSON string to a Python object
json.load(file)  # same as above but reads JSON from a file
```

### OOP

#### Classes

- **Class** is a blueprint whereas **instance** is an object that is built from this blueprint.

- Class does not hold any data, instance does hold actual data.

- **CamelCase** please when naming classes.

- In Python it has been decided that **instance (```self```) will be passed implicitly to class methods, but it will not be implicitly received**. It means that ```foo()``` method called on the instance class will include ```self``` argument by default: ```foo(self)```.

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

- ```getattr(object, name)``` is equivalent to ```object.name```

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

##### Typing

- ```typing``` module provides runtime support for type hints:

```python
from typing import List

Vector = List[float]
```

- When using Mypy, type errors for imported packages that lack typing can be silenced using `# type: ignore` comment:

```python
from geolib import geohash as gh  # type: ignore
```

- In Python, protocols are a way to define and enforce structural typing. They allow you to specify the expected interface or behavior of an object without explicitly defining a class or using inheritance. Protocols provide a flexible and dynamic approach to type checking and enable you to write more generic and reusable code.

- Protocols are implemented using the typing.Protocol class from the typing module, which was introduced in Python 3.8. You can define a protocol by subclassing typing.Protocol and specifying the required methods or attributes that an object should have.

```py
from typing import Protocol

class HasArea(Protocol):
    def area(self) -> float:
        pass

def print_area(obj: HasArea) -> None:
    print(f"The area is: {obj.area()}")

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14 * self.radius ** 2

rectangle = Rectangle(4, 5)
circle = Circle(3)

print_area(rectangle)  # Output: The area is: 20.0
print_area(circle)  # Output: The area is: 28.26
```

#### Inheritance

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

#### Abstract Classes

- Some methods might repeat themselves in different classes (i.e. addition of an item to a database) that do not inherit from the same parent class. In order to reduce code repetition it might be a good idea to introduce an abstract class that will encapsulate such methods. Methods which functionality does not differ across the classes/methods can be implemented directly in the abstract class (even when those depend on other methods that should be implemented within the child classes). Those *dependency* methods should be introduced in the abstract class as well but implemented in each class separately.

- Abstract classes cannot be instantiated, and classes that inherit from the abstract class cannot be instantiated if they do not overwrite abstract methods. The above can be implemented as following:

```python
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    def walk(self):  # implemented, concrete method; available in the child class
        print('Walking...')
    
    def eat(self):  # implemented, concrete method; available in the child class
        print('Eating...')
    
    @abstractmethod
    def num_legs():  # abstract method; needs to be overwritten in the child class
        pass
```

- **Abstract class is an interface** since it defines the functionality of the child classes. However, if abstract class defines non-abstract methods it does not fully comply with a standard interface definition.

#### classmethod

- ```@staticmethod``` can be used when given method does not need any data from the class or instantiated object. It can be used when given method is logically related to the class and does not need any internally defined properties. In most cases it should be avoided and replaced with the ```@classmethod``` since class method acts the same, but adds possibility to access class object which might be crucial when other classes inherit from this class.

- The most common use of `classmethod` is for alternative constructors:

```py
class Vector2d:
    # ...
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)
```

- ```@classmethod``` can be used similar to ```@staticmethod``` but additionally takes ```cls``` as a first argument which helps using class methods in classes that inherit from this class.

#### dataclass

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

- The `@dataclass` decorator does not depend on inheritance or a metaclass, so it should not interfere with your own use of these mechanisms.

- If more robust `__init__` method is required in `dataclass` `__post_init__` can be used:

```py

```

#### Exception Classes

- **Exception classes** can be inherited by other classes - this is useful when exception functionalities can stay the same, but name of the exception can be made for meaningful. Additional functionality can also be built-upon existing one within the exception class:

```python
if err:
    raise MeetupDayException('Error message')
    # Can be also:
    # raise MeetupDayException

class MeetupDayException(ValueError):
    pass
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

#### Class-based Decorators

- Lennart Regebro argues that decorators are best coded as classes implementing `__call__`, and not as functions. This especially makes sense for complex implementations.

```py
import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"

class clock:
    def __init__(self, fmt=DEFAULT_FMT):
        self.fmt = fmt

    def __call__(self, func):
        def clocked(*_args):
            t0 = time.perf_counter()
            _result = func(*_args)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ", ".join(repr(arg) for arg in _args)
            result = repr(_result)
            print(self.fmt.format(**locals()))
            return _result

        return clocked
```

- Decorators can be used to objects registration since they are called at the import time:

```py
Promotion = Callable[[Order], Decimal]
promos: list[Promotion] = []  # will get populated with decorated functions

def promotion(promo: Promotion) -> Promotion:
    promos.append(promo)
    return promo


def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)


@promotion
def fidelity(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity
    points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal("0.05")
    return Decimal(0) @ promotion


def bulk_item(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal("0.1")
    return discount

```

### Closures

- **Closure** is a function that retains the bindings of the free variables that exist when the function is defined, so that they can be used
later when the function is invoked and the defining scope is no longer available. Note that the only situation in which a function may need to deal with
external variables that are nonglobal is when it is nested in another function and those variables are part of the local scope of the outer function.

```python
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # series becomes a free variable here
        total = sum(series)
        return total / len(series)

    return averager
```

### Underscores

- Single underscore usage is a Python naming convention indicating a name is meant for internal use. It is generally not enforced by the Python interpreter and meant as a hint to the programmer only: ```self._internal_var = 2```

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

### Asynchronous Programming

- [Article and decision trees](https://superfastpython.com/python-concurrency-choose-api/) to help you decide which asynchronous API to use in which scenario.

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

##### Racing Conditions in Multithread Code

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

- Regular expressions can be used both on `str` and `bytes`, but in `bytes` bytes outside the ASCII range are treated as nondigits and nonword characters.

### Other

```python
try:
    iterator = iter(theElement)
except TypeError:
    # not iterable
else:
    # iterable
```

## Testing

- **Test Driven Development (TDD)** is also calles **Red Green Refactor**.

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

## Reactive Programming (ReactiveX)

- Reactive programming allows to manipulate a stream of data with functions (asynchronously). It can be used when there are **asynchronous** **data streams** that can be manipulated/filtered using **functional programming**, and then send to the observers.

- Using **ReactiveX** (Rx), you can represent multiple asynchronous data streams (that come from diverse sources, e.g., stock quote, Tweets, computer events, web service requests, etc.), and **subscribe to the event stream** using the **Observer** object. The **Observable** notifies the subscribed Observer instance whenever an event occurs. You can put various transformations in-between the source Observable and the consuming Observer as well.

- Basic idea is that we have some **subject** emitting data and an **observer** who awaits this data. Before reaching the observer data might be filtered/changed using functional programming paradigm. This means that we are creating kind of a new data stream that filters out irrelevant data and applies some logic to the received items so they are ready for consumer to be processed.

- Reactive programming is especially popular in Android programming and other UI focused use cases.

## Virtual Environments

### virtualenv

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

### pipenv

- A new standard for managing virtual environments.

- To initiate a virtualenv for the given project use ```pipenv install``` in case of *requirements.txt* being available in a directory or use ```pipenv install any_package``` to install desired package and initiate virtual env.

### Conda

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

### Poetry

- PLACEHOLDER

## Algorithms

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
