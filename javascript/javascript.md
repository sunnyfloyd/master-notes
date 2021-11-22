# JavaScript

- [JavaScript](#javascript)
  - [Sources](#sources)
  - [Variables and Constants](#variables-and-constants)
  - [Operators](#operators)
  - [Loops](#loops)
    - [forEach](#foreach)
  - [Switch](#switch)
  - [Functions](#functions)
    - [Function Expressions](#function-expressions)
    - [Arrow Functions](#arrow-functions)
  - [Objects](#objects)
    - ["for...in" Loop](#forin-loop)
    - [Object references and copying](#object-references-and-copying)
    - [Object Methods](#object-methods)
    - ["this" Keyword](#this-keyword)
    - [Constructor, operator "new"](#constructor-operator-new)
    - [Optional Chaining](#optional-chaining)
    - [Symbol](#symbol)
    - [Objects to Primitive Conversion](#objects-to-primitive-conversion)
    - [Object.keys, Object.values, Object.entries](#objectkeys-objectvalues-objectentries)
    - [Destructuring Assignments](#destructuring-assignments)
  - [Data Types](#data-types)
    - [Methods of Primitives](#methods-of-primitives)
    - [Numbers](#numbers)
    - [Strings](#strings)
    - [Arrays](#arrays)
      - [Array Methods](#array-methods)
    - [Iterables](#iterables)
    - [Map](#map)
    - [Set](#set)
    - [WeakMap and WeakSet](#weakmap-and-weakset)
    - [Date and Time](#date-and-time)
    - [JSON Methods](#json-methods)
  - [Testing](#testing)
  - [Debugging](#debugging)
  - [DOM Manipulation](#dom-manipulation)
    - [querySelector](#queryselector)
    - [Data Attributes](#data-attributes)
    - ['this' Keyword](#this-keyword-1)
    - [Using Form Input](#using-form-input)
    - [Local Storage](#local-storage)
  - [Other](#other)
  - [AJAX](#ajax)
  - [UX/UI](#uxui)
  - [Garbage collection](#garbage-collection)
  - [Polyfills and Transpilers](#polyfills-and-transpilers)
    - [Transpilers](#transpilers)
    - [Polyfills](#polyfills)

## Sources

- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/5/)

## Variables and Constants

- `var` defines **global variable**.

- `let` defines variable limited in scope to the current block.

- `const` defines a value that will not change.

## Operators

- The plus `+` exists in two forms: **the binary form that we used above and the unary form**:
  
  - The unary plus or, in other words, the plus operator `+` applied to a single value, doesn’t do anything to numbers.**
  - If the operand is not a number, the unary plus converts it into a number. It is a shorthand for `Number()`**.

- **Nullish coalescing operator**. `??` returns the first argument if it’s not `null/undefined`. Otherwise, the second one: `result = a ?? b` is equivalent to `result = (a !== null && a !== undefined) ? a : b`. It can be used with multiple operands: `firstName ?? lastName ?? nickName ?? "Anonymous"`.

## Loops

- A **label** is an identifier with a colon before a loop. `break` can refer to a loop via its scope so it can break out of the outer loop from the inner one. The `continue` directive can also be used with a label.

```js
labelName: for (...) {
  ...
}
```

### forEach

- `forEach` runs given function on each element in the iterable:

```js
document.querySelectorAll('button').forEach(function(button) {
    button.onclick = function() {
        document.querySelector("#hello").style.color = button.dataset.color;
    }
}
```

## Switch

- The `switch` has one or more case blocks and an optional `default`. **If there is no break then the execution continues with the next case without any checks**.

```js
switch(x) {
  case 'value1':  // if (x === 'value1')
    ...
    [break]

  case 'value2':  // if (x === 'value2')
    ...
    [break]

  default:
    ...
    [break]
}
```

- Several variants of case which share the same code can be grouped:

```js
switch (a) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}
```

## Functions

- A function may access outer variables. But it works only from inside out. The code outside of the function doesn’t see its local variables.

- **A function always gets a copy of the value** so changes of the passed arguments do not impact original variables.

- A **parameter** is the variable listed inside the parentheses in the function declaration (it’s a declaration time term)
- An **argument** is the value that is passed to the function when it is called (it’s a call time term).

- If a function is called, but an argument is not provided, then the corresponding value becomes `undefined`.

### Function Expressions

- In JavaScript, a function is a special kind of value.

- There are two ways to create a function:

**Function Declaration:**

- A function, declared as a separate statement, in the main code flow.
- A Function Declaration can be called earlier than it is defined. That’s due to internal algorithms. When JavaScript prepares to run the script, it first looks for global Function Declarations in it and creates the functions. We can think of it as an “initialization stage”.
- In strict mode, when a Function Declaration is within a code block, it’s visible everywhere inside that block. But not outside of it.

```js
function sayHi() {
    alert( "Hello" );
}
```

**Function Expression:**

- A function, created inside an expression or inside another syntax construct.
- A Function Expression is created when the execution reaches it and is usable only from that moment.

```js
let sayHi = function() {
  alert( "Hello" );
};
```

- As a rule of thumb, when we need to declare a function, the first to consider is Function Declaration syntax. It gives more freedom in how to organize our code, because we can call such functions before they are declared. That’s also better for readability, as it’s easier to look up function f(…) {…} in the code than let f = function(…) {…};. Function Declarations are more “eye-catching”. But if a Function Declaration does not suit us for some reason, or we need a conditional declaration, then Function Expression should be used.

### Arrow Functions

- There’s another very simple and concise syntax for creating functions, that’s often better than Function Expressions - **Arrow Functions**:

```js
let func = (arg1, arg2, ..., argN) => expression
```

- In single line expressions the expression itself is returned implicitly. In multiline expressions `return` must be called explicitly:

```js
let sum = (a, b) => {  // the curly brace opens a multiline function
  let result = a + b;
  return result; // if we use curly braces, then we need an explicit "return"
};
```

## Objects

- In contrast, objects are used to store keyed collections of various data and more complex entities. In JavaScript, objects penetrate almost every aspect of the language. So we must understand them first before going in-depth anywhere else.

- An object can be created with figure brackets `{…}` with an optional list of properties. A property is a “key: value” pair, where `key` is a string (also called a “property name”), and `value` can be anything.

```js
let user = new Object(); // "object constructor" syntax
let user = {};  // "object literal" syntax
```

- To remove a property: `delete user.age;`.

- Multiword property names must be quoted:

```js
let user = {
  "likes birds": true  // multiword property name must be quoted
};
```

- There’s an alternative “square bracket notation” that works with any string (required for multiword properties).

- We can use square brackets in an object literal, when creating an object. That’s called computed properties:

```js
let fruit = prompt("Which fruit to buy?", "apple");

let bag = {
  [fruit]: 5, // the name of the property is taken from the variable fruit
};

alert( bag.apple ); // 5 if fruit="apple"
```

- Objects are **ordered in a special fashion**: integer properties (a string that can be converted to-and-from an integer without a change) are sorted, others appear in creation order.

- The use-case of making a property from a variable is so common, that there’s a special property value shorthand to make it shorter. Instead of `name:name` we can just write `name`, like this:

```js
function makeUser(name, age) {
  return {
    name, // same as name: name
    age,  // same as age: age
    // ...
  };
}
```

- A notable feature of objects in JavaScript, compared to many other languages, is that it’s possible to access any property. There will be no error if the property doesn’t exist! Reading a non-existing property just returns `undefined`. So we can easily test whether the property exists.

```js
let user = {};
alert( user.noSuchProperty === undefined ); // true means "no such property"

// OR
"noSuchProperty" in user
```

### "for...in" Loop

```js
let user = {
  name: "John",
  age: 30,
  isAdmin: true
};

for (let key in user) {
  // keys
  alert( key );  // name, age, isAdmin
  // values for the keys
  alert( user[key] ); // John, 30, true
}
```

### Object references and copying

- One of the fundamental differences of objects versus primitives is that objects are stored and copied “by reference”, whereas primitive values: strings, numbers, booleans, etc – are always copied “as a whole value”.

- Two objects are equal only if they are the same object.

- For comparisons like `obj1 > obj2` or for a comparison against a primitive `obj == 5`, objects are converted to primitives.

- There’s no built-in method for object copying in JavaScript. But if we really want that, then we need to create a new object and replicate the structure of the existing one by iterating over its properties and copying them on the primitive level. This can be done with `Object.assign` method for shallow copy or `_.cloneDeep(obj).` for deep copy:

```js
let user = { name: "John" };

let permissions1 = { canView: true };
let permissions2 = { canEdit: true };

// copies all properties from permissions1 and permissions2 into user
Object.assign(user, permissions1, permissions2);

// now user = { name: "John", canView: true, canEdit: true }
```

- An important side effect of storing objects as references is that an object declared as `const` can be modified. `const` must always reference the same object, but properties of that object are free to change.

### Object Methods

```js
let user = {
  name: "John",
  age: 30
};

user.sayHi = function() {
  alert("Hello!");
};

// OR

// first, declare
function sayHi() {
  alert("Hello!");
};

// then add as a method
user.sayHi = sayHi;
```

- There exists a shorter syntax for methods in an object literal:

```js
// these objects do the same
user = {
  sayHi: function() {
    alert("Hello");
  }
};

user = {
  sayHi() { // same as "sayHi: function(){...}"
    alert("Hello");
  }
};
```

### "this" Keyword

- It’s common that an object method needs to access the information stored in the object to do its job. To access the object, a method can use the `this` keyword.

- In JavaScript, keyword this behaves unlike most other programming languages. It can be used in any function, even if it’s not a method of an object.

- The value of this is evaluated during the run-time, depending on the context. For instance, here the same function is assigned to two different objects and has different “this” in the calls:

```js
let user = { name: "John" };
let admin = { name: "Admin" };

function sayHi() {
  alert( this.name );
}

// use the same function in two objects
user.f = sayHi;
admin.f = sayHi;

// these calls have different this
// "this" inside the function is the object "before the dot"
user.f(); // John  (this == user)
admin.f(); // Admin  (this == admin)
```

- Arrow functions are special: they don’t have their “own” this. If we reference this from such a function, it’s taken from the outer “normal” function. For instance, here `arrow()` uses this from the outer `user.sayHi()` method:

```js
let user = {
  firstName: "Ilya",
  sayHi() {
    let arrow = () => alert(this.firstName);
    arrow();
  }
};

user.sayHi(); // Ilya
```

### Constructor, operator "new"

- Constructor functions technically are regular functions. There are two conventions though:

  - They are named with capital letter first.
  - They should be executed only with `new` operator.

```js
function User(name) {
  this.name = name;
  this.isAdmin = false;
}

let user = new User("Jack");

alert(user.name); // Jack
alert(user.isAdmin); // false
```

- The main purpose of constructors is to implement reusable object creation code.

- Usually, constructors do not have a `return` statement. Their task is to write all necessary stuff into this, and it automatically becomes the result. But if there is a return statement, then the rule is simple:

  - If return is called with an object, then the object is returned instead of `this`.
  - If return is called with a primitive, it’s ignored.

```js
function BigUser() {

  this.name = "John";

  return { name: "Godzilla" };  // <-- returns this object
}

alert( new BigUser().name );  // Godzilla, got that object

function SmallUser() {

  this.name = "John";

  return; // <-- returns this
}
```

### Optional Chaining

- The optional chaining `?.` is a safe way to access nested object properties, even if an intermediate property doesn’t exist.

```js
let user = {}; // a user without "address" property
alert(user.address.street); // Error!

// AND

let html = document.querySelector('.elem').innerHTML; // error if it's null
```

- In other words, value?.prop:

  - works as value.prop, if value exists,
  - otherwise (when value is undefined/null) it returns undefined.

- Please note: the `?.` syntax **makes optional the value before it, but not any further**. E.g. in `user?.address.street.name` the `?.` allows user to safely be null/undefined (and returns undefined in that case), but that’s only for user. Further properties are accessed in a regular way. If we want some of them to be optional, then we’ll need to replace more `.` with `?.`.

- We should use `?.` only where it’s ok that something doesn’t exist. For example, if according to our coding logic user object must exist, but address is optional, then we should write `user.address?.street`, but not `user?.address?.street`.

- There are other variants of optional chaining. For example, `?.()` is used to call a function that may not exist. The `?.[]` syntax also works, if we’d like to use brackets `[]` to access properties instead of dot `.`.

- Also we can use `?.` with delete to delete an object or attribute if it exists: `delete user?.name;`.

### Symbol

- `Symbol` is a primitive type for unique identifiers.

- Symbols are created with `Symbol()` call with an optional description (name).

- Symbols are always different values, even if they have the same name. If we want same-named symbols to be equal, then we should use the global registry: `Symbol.for(key)` returns (creates if needed) a global symbol with key as the name. Multiple calls of `Symbol.for` with the same key return exactly the same symbol.

- Symbols have two main use cases:

  - *Hidden* object properties. If we want to add a property into an object that “belongs” to another script or a library, we can create a symbol and use it as a property key. A symbolic property does not appear in `for..in`, so it won’t be accidentally processed together with other properties. Also it won’t be accessed directly, because another script does not have our symbol. So the property will be protected from accidental use or overwrite. So we can “covertly” hide something into objects that we need, but others should not see, using symbolic properties.
  
  - There are many system symbols used by JavaScript which are accessible as `Symbol.*`. We can use them to alter some built-in behaviors. E.g. `Symbol.iterator` can be used for iterables and `Symbol.toPrimitive` to setup object-to-primitive conversion.

### Objects to Primitive Conversion

- The object-to-primitive conversion is called automatically by many built-in functions and operators that expect a primitive as a value.

- There are 3 types (hints) of it:

  - "string" (for alert and other operations that need a string)
  - "number" (for maths)
  - "default" (few operators)

- To do the conversion, JavaScript tries to find and call three object methods:

  - Call obj[Symbol.toPrimitive](hint) – the method with the symbolic key `Symbol.toPrimitive` (system symbol), if such method exists,
  - Otherwise if hint is "string" try `obj.toString()` and `obj.valueOf()`, whatever exists.
  - Otherwise if hint is "number" or "default" try `obj.valueOf()` and `obj.toString()`, whatever exists.

```js
let user = {
  name: "John",
  money: 1000,

  [Symbol.toPrimitive](hint) {
    alert(`hint: ${hint}`);
    return hint == "string" ? `{name: "${this.name}"}` : this.money;
  }
};

// toString and valueOf methods for object conversion

let user = {
  name: "John",
  money: 1000,

  // for hint="string"
  toString() {
    return `{name: "${this.name}"}`;
  },

  // for hint="number" or "default"
  valueOf() {
    return this.money;
  }

};
```

### Object.keys, Object.values, Object.entries

- Plain objects support similar methods as the ones for `Map`, `Set`, `Array` (e.g. `keys()`, `values()`, `entries()`), but the syntax is a bit different.

- For plain objects, the following methods are available:

  - `Object.keys(obj)` – returns an array of keys.
  - `Object.values(obj)` – returns an array of values.
  - `Object.entries(obj)` – returns an array of `[key, value]` pairs.

- Additionally, object methods return Array instead of an iterable.

### Destructuring Assignments

- **Destructuring assignment** allows for instantly mapping an object or array onto many variables.

- The full object syntax:

```js
let {prop : varName = default, ...rest} = object
```

- This means that property prop should go into the variable `varName` and, if no such property exists, then the default value should be used.

- Object properties that have no mapping are copied to the `rest` object.

- The full array syntax:

```js
let [item1 = default, item2, ...rest] = array
```

- The first item goes to `item1`; the second goes into `item2`, all the rest makes the array `rest`.

- It’s possible to extract data from nested arrays/objects, for that the left side must have the same structure as the right one.

- Destructuring can be used in function declaration:

```js
let options = {
  title: "My menu",
  items: ["Item1", "Item2"]
};

function showMenu({
  title = "Untitled",
  width: w = 100,  // width goes to w
  height: h = 200, // height goes to h
  items: [item1, item2] // items first element goes to item1, second to item2
}) {
  alert( `${title} ${w} ${h}` ); // My Menu 100 200
  alert( item1 ); // Item1
  alert( item2 ); // Item2
}

showMenu(options);
```

## Data Types

### Methods of Primitives

- Primitives except null and undefined provide many helpful methods. We will study those in the upcoming chapters.

- Formally, these methods work via temporary objects, but JavaScript engines are well tuned to optimize that internally, so they are not expensive to call.

### Numbers

- To write numbers with many zeroes:

  - Append "e" with the zeroes count to the number. Like: `123e6` is the same as 123 with 6 zeroes `123000000`.
  - A negative number after "e" causes the number to be divided by 1 with given zeroes. E.g. `123e-6` means `0.000123` (123 millionths).

- For different numeral systems:

  - Can write numbers directly in hex (`0x`), octal (`0o`) and binary (`0b`) systems.
  - `parseInt(str, base)` parses the string str into an integer in numeral system with given `base`, `2 ≤ base ≤ 36`.
  - `num.toString(base)` converts a number to a string in the numeral system with the given base.

- For converting values like 12pt and 100px to a number:

  - Use `parseInt`/`parseFloat` for the “soft” conversion, which reads a number from a string and then returns the value they could read before the error.

For fractions:

  - Round using `Math.floor`, `Math.ceil`, `Math.trunc`, `Math.round` or `num.toFixed(precision)`.
  - Make sure to remember there’s a loss of precision when working with fractions.

### Strings

- There are 3 types of quotes. Backticks allow a string to span multiple lines and embed expressions `${…}`.

- Strings in JavaScript are encoded using UTF-16.

- We can use special characters like \n and insert letters by their Unicode using \u....

- To get a character, use: `[]`.

- To get a substring, use: `slice` or `substring`.

- To lowercase/uppercase a string, use: `toLowerCase`/`toUpperCase`.

- To look for a substring, use: `indexOf`, or `includes`/`startsWith`/`endsWith` for simple checks.

- To compare strings according to the language, use: `localeCompare`, otherwise they are compared by character codes.

- There are several other helpful methods in strings:
  - `str.trim()` – removes (“trims”) spaces from the beginning and end of the string.
  - `str.repeat(n)` – repeats the string n times.

### Arrays

- **Array** is a special kind of object, suited to storing and managing ordered data items.

- The declaration:

```js
// square brackets (usual)
let arr = [item1, item2...];

// new Array (exceptionally rare)
let arr = new Array(item1, item2...);
```

- The call to new Array(number) creates an array with the given length, but without elements.

- The `length` property is the array length or, to be precise, its last numeric index plus one. It is auto-adjusted by array methods.

- If we shorten `length` manually, the array is truncated.

- We can use an array as a deque with the following operations:

  - `push(...items)` adds items to the end.
  - `pop()` removes the element from the end and returns it.
  - `shift()` removes the element from the beginning and returns it.
  - `unshift(...items)` adds items to the beginning.

- To loop over the elements of the array:

  - `for (let i=0; i<arr.length; i++)` – works fastest, old-browser-compatible.
  - `for (let item of arr)` – the modern syntax for items only,
  - `for (let i in arr)` – never use.

- To compare arrays, don’t use the `==` operator (as well as `>`, `<` and others), as they have no special treatment for arrays. They handle them as any objects, and it’s not what we usually want. Instead you can use `for..of` loop to compare arrays item-by-item.

#### Array Methods

- To add/remove elements:
  - `push(...items)` – adds items to the end,
  - ``pop()` – extracts an item from the end,
  - shift()` – extracts an item from the beginning,
  - `unshift(...items)` – adds items to the beginning.
  - `splice(pos, deleteCount, ...items)` – at index pos deletes deleteCount elements and inserts items.
  - `slice(start, end)` – creates a new array, copies elements from index start till end (not inclusive) into it.
  - `concat(...items)` – returns a new array: copies all members of the current one and adds items to it. If - any of items is an array, then its elements are taken.

- To search among elements:
  - `indexOf`/`lastIndexOf(item, pos)` – look for item starting from position `pos`, return the index or `-1` if not found.
  - `includes(value)` – returns true if the array has value, otherwise false.
  - `find/filter(func)` – filter elements through the function, return first/all values that make it return true.
  - `findIndex` is like `find`, but returns the index instead of a value.

- To iterate over elements:
  - `forEach(func)` – calls `func` for every element, does not return anything.

- To transform the array:
  - `map(func)` – creates a new array from results of calling func for every element.
  - `sort(func)` – sorts the array in-place, then returns it.
  - `reverse()` – reverses the array in-place, then returns it.
  - `split`/`join` – convert a string to array and back.
  - `reduce`/`reduceRight(func, initial)` – calculate a single value over the array by calling `func` for each - element and passing an intermediate result between the calls.

- Additionally:
  - `Array.isArray(arr)` checks `arr` for being an array.

- Note that methods `sort`, `reverse` and `splice` modify the array itself.

- There are few others array methods:

  - `arr.some(fn)`/`arr.every(fn)` check the array. The function `fn` is called on each element of the array similar to `map`. If any/all results are true, returns true, otherwise false. These methods behave sort of like `||` and `&&` operators: if `fn` returns a truthy value, `arr.some()` immediately returns true and stops iterating over the rest of items; if `fn` returns a falsy value, `arr.every()` immediately returns false and stops iterating over the rest of items as well.

  - `arr.fill(value, start, end)` – fills the array with repeating value from index start to end.

  - `arr.copyWithin(target, start, end)` – copies its elements from position start till position end into itself, at position target (overwrites existing).

  - `arr.flat(depth)`/`arr.flatMap(fn)` create a new flat array from a multidimensional array.

### Iterables

- Objects that can be used in `for..of` are called **iterable**.

- Technically, iterables must implement the method named Symbol.iterator.
    - The result of `obj[Symbol.iterator]()` is called an iterator. It handles further iteration process.
    - An iterator must have the method named `next()` that returns an object `{done: Boolean, value: any`, here `done:true` denotes the end of the iteration process, otherwise the value is the next value.

- The `Symbol.iterator` method is called automatically by `for..of`, but we also can do it directly.

- Built-in iterables like strings or arrays, also implement `Symbol.iterator`.

- String iterator knows about surrogate pairs.

- Objects that have indexed properties and length are called array-like. Such objects may also have other properties and methods, but lack the built-in methods of arrays.

- If we look inside the specification – we’ll see that most built-in methods assume that they work with iterables or array-likes instead of “real” arrays, because that’s more abstract.

- `Array.from(obj[, mapFn, thisArg])` makes a real Array from an iterable or array-like obj, and we can then use array methods on it. The optional arguments `mapFn` and `thisArg` allow us to apply a function to each item.

### Map

- `Map` – is a collection of keyed values.

- Methods and properties:

  - `new Map([iterable])` – creates the map, with optional iterable (e.g. array) of `[key,value]` pairs for initialization.
  - `map.set(key, value)` – stores the value by the key, returns the map itself.
  - `map.get(key)` – returns the value by the key, undefined if key doesn’t exist in map.
  - `map.has(key)` – returns true if the key exists, false otherwise.
  - `map.delete(key)` – removes the value by the key, returns true if key existed at the moment of the call, otherwise false.
  - `map.clear()` – removes everything from the map.
  - `map.size` – returns the current element count.

- The differences from a regular Object:

  - Any keys, objects can be keys.
  - Additional convenient methods, the size property.

- For looping over a map, there are 3 methods:

  - `map.keys()` – returns an iterable for keys,
  - `map.values()` – returns an iterable for values,
  - `map.entries()` – returns an iterable for entries [key, value], it’s used by default in `for..of`,
  - besides that, `Map` has a built-in `forEach` method, similar to Array.

- Create `Map` from a plain object with `new Map(Object.entries(obj))`.

- To transform `Map` into an object `Object.fromEntries(map.entries())` or just `Object.fromEntries(map)`.

- Iteration over `Map` and `Set` is always in the insertion order, so we can’t say that these collections are unordered, but we can’t reorder elements or directly get an element by its number.

### Set

- `Set` – is a collection of unique values.

- Methods and properties:

  - `new Set([iterable])` – creates the set, with optional iterable (e.g. array) of values for initialization.
  - `set.add(value)` – adds a value (does nothing if value exists), returns the set itself.
  - `set.delete(value)` – removes the value, returns true if value existed at the moment of the call, otherwise false.
  - `set.has(value)` – returns true if the value exists in the set, otherwise false.
  - `set.clear()` – removes everything from the set.
  - `set.size` – is the elements count.

- Iterations and iteration-related methods for sets are pretty much the same as for maps. In case of keys and values those are duplicated for sets to ensure compatibility with maps.

### WeakMap and WeakSet

- `WeakMap` is `Map`-like collection that allows only objects as keys and removes them together with associated value once they become inaccessible by other means.

- `WeakSet` is `Set`-like collection that stores only objects and removes them once they become inaccessible by other means.

- Their main advantages are that they have weak reference to objects, so they can easily be removed by garbage collector.

- That comes at the cost of not having support for `clear`, `size`, `keys`, `values`…

- `WeakMap` and `WeakSet` are used as “secondary” data structures in addition to the “primary” object storage. Once the object is removed from the primary storage, if it is only found as the key of `WeakMap` or in a `WeakSet`, it will be cleaned up automatically.

### Date and Time

- Date and time in JavaScript are represented with the `Date` object. We can’t create “only date” or “only time”: `Date` objects always carry both.

- Months are counted from zero (yes, January is a zero month).

- Days of week in `getDay()` are also counted from zero (that’s Sunday).

- `Date` auto-corrects itself when out-of-range components are set. Good for adding/subtracting days/months/hours.

- Dates can be subtracted, giving their difference in milliseconds. That’s because a `Date` becomes the timestamp when converted to a number.

- Use `Date.now()` to get the current timestamp fast.

- The method Date.parse(str) can read a date from a string. The string format should be: `YYYY-MM-DDTHH:mm:ss.sssZ`.

- Note that unlike many other systems, timestamps in JavaScript are in milliseconds, not in seconds.

- Sometimes we need more precise time measurements. JavaScript itself does not have a way to measure time in microseconds (1 millionth of a second), but most environments provide it. For instance, browser has `performance.now()` that gives the number of milliseconds from the start of page loading with microsecond precision (3 digits after the point).

### JSON Methods

- JSON is a data format that has its own independent standard and libraries for most programming languages.

- JSON supports plain objects, arrays, strings, numbers, booleans, and `null`.

- JavaScript provides methods `JSON.stringify` to serialize into JSON and `JSON.parse` to read from JSON.

- Both methods support transformer functions for smart reading/writing.

- If an object has `toJSON`, then it is called by `JSON.stringify`.

## Testing

- In **BDD** (Behaviour-Driven Development), the spec goes first, followed by implementation. At the end we have both the spec and the code.

- The spec can be used in three ways:

  1. As Tests – they guarantee that the code works correctly.
  2. As Docs – the titles of describe and it tell what the function does.
  3. As Examples – the tests are actually working examples showing how a function can be used.

- With the spec, we can safely improve, change, even rewrite the function from scratch and make sure it still works right.

- **Mocha** – the core framework: it provides common testing functions including describe and it and the main function that runs tests.
- **Chai** – the library with many assertions. It allows to use a lot of different assertions.
- **Sinon** – a library to spy over functions, emulate built-in functions and more.

- Example of spec:

```js
describe("pow", function() {

  it("2 raised to power 3 is 8", function() {
    assert.equal(pow(2, 3), 8);
  });

  it("3 raised to power 4 is 81", function() {
    assert.equal(pow(3, 4), 81);
  });

});
```

- The **nested describe** defines a new *subgroup* of tests - it is usefull to logically organize function testing:

```js
describe("pow", function() {

  describe("raises x to power 3", function() {

    function makeTest(x) {
      let expected = x * x * x;
      it(`${x} in the power 3 is ${expected}`, function() {
        assert.equal(pow(x, 3), expected);
      });
    }

    for (let x = 1; x <= 5; x++) {
      makeTest(x);
    }

  });

  // ... more tests to follow here, both describe and it can be added
});
```

## Debugging

- `debugger` is a convenient way to set the breakpoint in the code editor.

## DOM Manipulation

### querySelector

- `querySelector` searches for and returns elements of the **Document Object Model (DOM)**. It can be used with tags, IDs and classes used as identifiers. It **returns only the first element**:

```js
function hello() {
    const header = document.querySelector('h1');
    if (header.innerHTML === 'Hello!') {
        header.innerHTML = 'Goodbye!';
    }
    else {
        header.innerHTML = 'Hello!';
    }
}

// HTML part
<button onclick="hello()">Click Here</button>
```

- `querySelectorAll` returns an array of all the elements that match given query.

- We can use `document` and `addEventListener` to only run the code once all content has loaded. This also helps separating HTML from JavaScript code:

```js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').onclick = count;
});
```

### Data Attributes

- `data-<name>` can be included as an attribute to any HTML tag. It can be used to access its value using JS:

```js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(function(button) {
        button.onclick = function() {
            document.querySelector("#hello").style.color = button.dataset.color;
        }
    });
});

// HTML part
<button data-color="red">Red</button>
```

- Since functions in `evenListener` are not being passed any arguments required data can be taken not only from the dataset fields, but also from the parameters:

```js
function foo() {
  console.log(this.myParam)
}

element = document.querySelector('#inbox');
element.myParam = 'value'; // defining a parameter
element.addEventListener('click', foo)
});
```

### 'this' Keyword

- In JavaScript, `this` is a keyword that changes based on the context in which it’s used. In the case of an event handler, this refers to the object that triggered the event.

```js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('select').onchange = function() {
        document.querySelector('#hello').style.color = this.value;
    }
});
```

### Using Form Input

- Form submission done by a browser can be blocked by returning `false` on `onsubmit` event.

- `document.createElement('<tag>')` creates a new element inside a DOM.

- To add a new element within the queried element use `append` method:

```js
// Wait for page to load
document.addEventListener('DOMContentLoaded', function() {

    // Select the submit button and input to be used later
    const submit = document.querySelector('#submit');
    const newTask = document.querySelector('#task');

    // Disable submit button by default:
    submit.disabled = true;

    // Listen for input to be typed into the input field
    newTask.onkeyup = () => {
        if (newTask.value.length > 0) {
            submit.disabled = false;
        }
        else {
            submit.disabled = true;
        }
    }

    // Listen for submission of form
    document.querySelector('form').onsubmit = () => {

        // Find the task the user just submitted
        const task = newTask.value;

        // Create a list item for the new task and add the task to it
        const li = document.createElement('li');
        li.innerHTML = task;

        // Add new element to our unordered list:
        document.querySelector('#tasks').append(li);

        // Clear out input field:
        newTask.value = '';

        // Disable the submit button again:
        submit.disabled = true;

        // Stop form from submitting
        return false;
    }
});

// HTML Part
<h1>Tasks</h1>
<ul id="tasks"></ul>
<form>
    <input id="task" placeholder = "New Task" type="text">
    <input id="submit" type="submit">
</form>
```

### Local Storage

- One way we store information on the client's side that can be used later is to use **Local Storage**, or storing information on the user’s web browser that we can access later. This information is stored as a set of key-value pairs, almost like a Python dictionary. In order to use local storage, we’ll employ two key functions:

  - `localStorage.getItem(key)`: This function searches for an entry in local storage with a given key, and returns the value associated with that key.
  - `localStorage.setItem(key, value)`: This function sets and entry in local storage, associating the key with a new vlaue.

```js
function count() {
    // Retrieve counter value from local storage
    let counter = localStorage.getItem('counter');

    // update counter
    counter++;
    document.querySelector('h1').innerHTML = counter;

    // Store counter in local storage
    localStorage.setItem('counter', counter);
}
```

## Other

- `setInterval(function, 1000)` calls a function or evaluates an expression at specified intervals (in miliseconds).

## AJAX

- **AJAX** (Asynchronous JavaScript And XML) allows to access information from external pages even after the page has loaded. In order to do this, we’ll use the `fetch` function which will allow us to send an HTTP request. The `fetch` function returns a **promise**. We can think of promise as a value that will come through at some point, but not necessarily right away. We deal with promises by giving them a `.then` attribute describing what should be done when we get a `response`:

```js
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').onsubmit = function() {

        // Send a GET request to the URL
        fetch('https://api.exchangeratesapi.io/latest?base=USD')
        // Put response into json form
        .then(response => response.json())
        .then(data => {
            // Get currency from user input and convert to upper case
            const currency = document.querySelector('#currency').value.toUpperCase();

            // Get rate from data
            const rate = data.rates[currency];

            // Check if currency is valid:
            if (rate !== undefined) {
                // Display exchange on the screen
                document.querySelector('#result').innerHTML = `1 USD is equal to ${rate.toFixed(3)} ${currency}.`;
            }
            else {
                // Display error on the screen
                document.querySelector('#result').innerHTML = 'Invalid Currency.';
            }
        })
        // Catch any errors and log them to the console
        .catch(error => {
            console.log('Error:', error);
        });
        // Prevent default submission
        return false;
    }
});
```

## UX/UI

- Single Page Applications can be made more user-friendly if we add navigation functionality similar to the server rendered web pages. That is to changing URL and proper back button functionality:

```js
// When back arrow is clicked, show previous section
window.onpopstate = function(event) {
    showSection(event.state.section);
}

function showSection(section) {
    fetch(`/sections/${section}`)
    .then(response => response.text())
    .then(text => {
        document.querySelector('#content').innerHTML = text;
    });

}

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = function() {
            const section = this.dataset.section;

            // Add the current state to the history
            history.pushState({section: section}, "", `section${section}`);
            showSection(section);
        };
    });
});
```

- `window` stores many useful information such as user window's width and heigth, and how far has user scrolled down.

- Attaching an event listener to the multiple elements:

```js
// using querySelectorAll
document.querySelectorAll('#id-name').forEach(element => {
    element.addEventListener('click', () => {console.log('clicked')});
});

// using event.target
document.addEventListener('click', event => {
    const element = event.target;
    if (element.className === 'hide') {
        element.parentElement.style.animationPlayState = 'running';
        element.parentElement.addEventListener('animationend', () => {element.parentElement.remove();});
    }
});
```

## Garbage collection

- Garbage collection is performed automatically. We cannot force or prevent it.

- Objects are retained in memory while they are reachable.

- Being referenced is not the same as being reachable (from a root): a pack of interlinked objects can become unreachable as a whole.

- Modern engines implement advanced algorithms of garbage collection:

  - **Generational collection** – objects are split into two sets: “new ones” and “old ones”. Many objects appear, do their job and die fast, they can be cleaned up aggressively. Those that survive for long enough, become “old” and are examined less often.
  - **Incremental collection** – if there are many objects, and we try to walk and mark the whole object set at once, it may take some time and introduce visible delays in the execution. So the engine tries to split the garbage collection into pieces. Then the pieces are executed one by one, separately. That requires some extra bookkeeping between them to track changes, but we have many tiny delays instead of a big one.
  - **Idle-time collection** – the garbage collector tries to run only while the CPU is idle, to reduce the possible effect on the execution

## Polyfills and Transpilers

### Transpilers

- A transpiler is a special piece of software that translates source code to another source code. It can parse (*read and understand*) modern code and rewrite it using older syntax constructs, so that it’ll also work in outdated engines.

- **Babel** is one of the most prominent transpilers.

- Modern project build systems, such as **webpack**, provide means to run transpiler automatically on every code change, so it’s very easy to integrate into development process.

### Polyfills

- New language features may include not only syntax constructs and operators, but also built-in functions. For example In some (very outdated) JavaScript engines, there’s no `Math.trunc`, so such code using this function would fail. As we’re talking about new functions, not syntax changes, there’s no need to transpile anything here. We just need to declare the missing function.

- A script that updates/adds new functions is called **polyfill**. It *fills in* the gap and adds missing implementations.
