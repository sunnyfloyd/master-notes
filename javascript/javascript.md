# JavaScript

- [JavaScript](#javascript)
  - [Sources](#sources)
  - [Variables and Constants](#variables-and-constants)
    - [The Old "var"](#the-old-var)
  - [Operators](#operators)
  - [Loops](#loops)
    - [forEach](#foreach)
  - [Switch](#switch)
  - [Functions](#functions)
    - [Function Expressions](#function-expressions)
    - [Arrow Functions](#arrow-functions)
    - [Rest Parameters and Spread Syntax](#rest-parameters-and-spread-syntax)
    - [Decorators](#decorators)
    - ["new Function()" Syntax](#new-function-syntax)
    - [Closure](#closure)
    - [Call Forwarding](#call-forwarding)
    - [Function Binding](#function-binding)
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
    - [Global Object](#global-object)
    - [Function Object](#function-object)
    - [Function Scheduling](#function-scheduling)
    - [Property Flags and Descriptors](#property-flags-and-descriptors)
    - [Property Getters and Setters](#property-getters-and-setters)
    - [Prototypal Inheritance](#prototypal-inheritance)
    - [F.prototype](#fprototype)
    - [Native Prototypes](#native-prototypes)
    - [Prototype Methods and Objects without __proto__](#prototype-methods-and-objects-without-proto)
  - [Classes](#classes)
    - [Class Inheritance](#class-inheritance)
    - [Static Methods](#static-methods)
    - [Private and Protected Properties and Methods](#private-and-protected-properties-and-methods)
    - [Extending Built-in Classes](#extending-built-in-classes)
    - [Mixins](#mixins)
    - [Type Checking Methods](#type-checking-methods)
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
  - [Error Handling](#error-handling)
    - ["try...catch"](#trycatch)
    - [Custom Errors](#custom-errors)
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
- [javascript.info](https://javascript.info/)

## Variables and Constants

- `var` defines **global variable**.

- `let` defines variable limited in scope to the current block.

- `const` defines a value that will not change.

### The Old "var"

- There are two main differences of `var` compared to `let`/`const`:

  - `var` variables have no block scope, their visibility is scoped to current function, or global, if declared outside function.
  - `var` declarations are processed at function start (script start for globals).

- There’s one more very minor difference related to the global object, that we’ll cover in the next chapter.

- These differences make `var` worse than `let` most of the time. Block-level variables is such a great thing. That’s why `let` was introduced in the standard long ago, and is now a major way (along with `const`) to declare a variable.

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
  
- **Arrow functions do not have `this`**. If `this` is accessed, it is taken from the outside (from the outer lixical environment).

- Arrow functions also have no `arguments` variable.

- Arrow functions can’t be called with `new`.

### Rest Parameters and Spread Syntax

- When we see `...` in the code, it is either **rest parameters** or the **spread syntax**.

- There’s an easy way to distinguish between them:

  - When `...` is at the end of function parameters, it’s “rest parameters” and gathers the rest of the list of arguments into an array.
  - When `...` occurs in a function call or alike, it’s called a “spread syntax” and expands an array into a list.

- Use patterns:

  - Rest parameters are used to create functions that accept any number of arguments.
  - The spread syntax is used to pass an array to functions that normally require a list of many arguments.

- Together they help to travel between a list and an array of parameters with ease.

- All arguments of a function call are also available in “old-style” `arguments`: array-like iterable object.

- We can use spread syntax to make a copy of an array or an object: `[...arr]` or `{...obj}`.

### Decorators

- **Decorator** is a wrapper around a function that alters its behavior. The main job is still carried out by the function. Decorators can be seen as “features” or “aspects” that can be added to a function. We can add one or add many.

To implement decorator, we studied methods:

  - `func.call(context, arg1, arg2…)` – calls func with given context and arguments.
  - `func.apply(context, args)` – calls func passing context as this and array-like args into a list of arguments.

```js
function slow(x) {
  // there can be a heavy CPU-intensive job here
  alert(`Called with ${x}`);
  return x;
}

function cachingDecorator(func) {
  let cache = new Map();

  return function(x) {
    if (cache.has(x)) {    // if there's such key in cache
      return cache.get(x); // read the result from it
    }

    let result = func(x);  // otherwise call func

    cache.set(x, result);  // and cache (remember) the result
    return result;
  };
}

slow = cachingDecorator(slow);

alert( slow(1) ); // slow(1) is cached and the result returned
alert( "Again: " + slow(1) ); // slow(1) result returned from cache

alert( slow(2) ); // slow(2) is cached and the result returned
alert( "Again: " + slow(2) ); // slow(2) result returned from cache
```

- For object methods:

```js
let worker = {
  someMethod() {
    return 1;
  },

  slow(x) {
    alert("Called with " + x);
    return x * this.someMethod(); // (*)
  }
};

function cachingDecorator(func) {
  let cache = new Map();
  return function(x) {
    if (cache.has(x)) {
      return cache.get(x);
    }
    let result = func.call(this, x); // "this" is passed correctly now
    cache.set(x, result);
    return result;
  };
}

// decorated function becomes a proper object method so it refer to proper 'this'
worker.slow = cachingDecorator(worker.slow); // now make it caching

alert( worker.slow(2) ); // works
alert( worker.slow(2) ); // works, doesn't call the original (cached)
```

### "new Function()" Syntax

- Functions created with `new Function`, have `[[Environment]]` referencing the global Lexical Environment, not the outer one. Hence, they cannot use outer variables. But that’s actually good, because it insures us from errors. Passing parameters explicitly is a much better method architecturally and causes no problems with minifiers.

```js
let func = new Function ([arg1, arg2, ...argN], functionBody);

new Function('a', 'b', 'return a + b'); // basic syntax
new Function('a,b', 'return a + b'); // comma-separated
new Function('a , b', 'return a + b'); // comma-separated with spaces
```

### Closure

- A **closure** is a function that remembers its outer variables and can access them. In some languages, that’s not possible, or a function should be written in a special way to make it happen. But as explained above, in JavaScript, all functions are naturally closures. That is: they automatically remember where they were created using a hidden `[[Environment]]` property, and then their code can access outer variables.

- When on an interview, a frontend developer gets a question about “what’s a closure?”, a valid answer would be a definition of the closure and an explanation that all functions in JavaScript are closures, and maybe a few more words about technical details: the `[[Environment]]` property and how Lexical Environments work.

### Call Forwarding

- The generic **call forwarding** is usually done with `apply`:

```js
let wrapper = function() {
  return original.apply(this, arguments);
};
```

### Function Binding

- Method `func.bind(context, ...args)` returns a “bound variant” of function func that fixes the context this and first arguments if given.

- Usually we apply `bind` to fix this for an object method, so that we can pass it somewhere. For example, to `setTimeout`.

- When we fix some arguments of an existing function, the resulting (less universal) function is called **partially applied** or **partial**:

```js
function mul(a, b) {
  return a * b;
}

let triple = mul.bind(null, 3);
```

- Partials are convenient when we don’t want to repeat the same argument over and over again. Like if we have a `send(from, to)` function, and `from` should always be the same for our task, we can get a partial and go on with it.

- Partials without passing a context

```js
let user = {
  firstName: "John",
  say(time, phrase) {
    alert(`[${time}] ${this.firstName}: ${phrase}!`);
  }
};

// add a partial method with fixed time
user.sayNow = partial(user.say, new Date().getHours() + ':' + new Date().getMinutes());
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

### Global Object

- The global object holds variables that should be available everywhere.

- That includes JavaScript built-ins, such as `Array` and environment-specific values, such as `window.innerHeight` – the window height in the browser.

- The global object has a universal name `globalThis`. …But more often is referred by “old-school” environment-specific names, such as `window` (browser) and `global` (Node.js).

- We should store values in the global object only if they’re truly global for our project. And keep their number at minimum.

- In-browser, unless we’re using modules, global functions and variables declared with `var` become a property of the global object.

- To make our code future-proof and easier to understand, we should access properties of the global object directly, as `window.x`.

### Function Object

- Functions are objects.

- Here we covered their properties:

  - `name` – the function name. Usually taken from the function definition, but if there’s none, JavaScript tries to guess it from the context (e.g. an assignment).
  - `length` – the number of arguments in the function definition. Rest parameters are not counted.

- If the function is declared as a Function Expression (not in the main code flow), and it carries the name, then it is called a Named Function Expression. The name can be used inside to reference itself, for recursive calls or such.

- Also, functions may carry additional properties. Many well-known JavaScript libraries make great use of this feature.

- They create a “main” function and attach many other “helper” functions to it. For instance, the jQuery library creates a function named `$`. The lodash library creates a function `_`, and then adds `_.clone`, `_.keyBy` and other properties to it (see the docs when you want to learn more about them). Actually, they do it to lessen their pollution of the global space, so that a single library gives only one global variable. That reduces the possibility of naming conflicts. So, a function can do a useful job by itself and also carry a bunch of other functionality in properties.

### Function Scheduling

- Methods `setTimeout(func, delay, ...args)` and `setInterval(func, delay, ...args)` allow us to run the func once/regularly after delay milliseconds.

- To cancel the execution, we should call `clearTimeout`/`clearInterval` with the value returned by `setTimeout`/`setInterval`.

- Nested `setTimeout` calls are a more flexible alternative to `setInterval`, allowing us to set the time between executions more precisely.

- Zero delay scheduling with `setTimeout(func, 0)` (the same as `setTimeout(func))` is used to schedule the call “as soon as possible, but after the current script is complete”.

- The browser limits the minimal delay for five or more nested calls of `setTimeout` or for `setInterval` (after 5th call) to 4ms. That’s for historical reasons.

- Please note that all scheduling methods do not guarantee the exact delay. For example, the in-browser timer may slow down for a lot of reasons:

    - The CPU is overloaded.
    - The browser tab is in the background mode.
    - The laptop is on battery.

- All that may increase the minimal timer resolution (the minimal delay) to 300ms or even 1000ms depending on the browser and OS-level performance settings.

### Property Flags and Descriptors

- Object properties, besides a value, have three special attributes (so-called “flags”):

  - `writable` – if `true`, the value can be changed, otherwise it’s read-only.
  - `enumerable` – if `true`, then listed in loops, otherwise not listed.
  - `configurable` – if `true`, the property can be deleted and these attributes can be modified, otherwise not.

- To query the full information about a property use:

```js
let descriptor = Object.getOwnPropertyDescriptor(obj, propertyName);

let user = {
  name: "John"
};

let descriptor = Object.getOwnPropertyDescriptor(user, 'name');

alert( JSON.stringify(descriptor, null, 2 ) );
/* property descriptor:
{
  "value": "John",
  "writable": true,
  "enumerable": true,
  "configurable": true
}
*/
```

- To change the flags use:

```js
Object.defineProperty(obj, propertyName, descriptor)

let user = {};

Object.defineProperty(user, "name", {
  value: "John"
});


Object.defineProperty(user, "name", {
  writable: false
});

user.name = "Pete"; // Error: Cannot assign to read only property 'name'
```

` There’s a method that allows to define many properties at once:

```js
Object.defineProperties(obj, {
  prop1: descriptor1,
  prop2: descriptor2
  // ...
});

// e.g.
Object.defineProperties(user, {
  name: { value: "John", writable: false },
  surname: { value: "Smith", writable: false },
  // ...
});
```

- To get all property descriptors at once, we can use the method `Object.getOwnPropertyDescriptors(obj)`. Together with `Object.defineProperties` it can be used as a “flags-aware” way of cloning an object:

```js
let clone = Object.defineProperties({}, Object.getOwnPropertyDescriptors(obj));
```

### Property Getters and Setters

- Accessor properties are represented by “getter” and “setter” methods. In an object literal they are denoted by `get` and `set`:

```js
let obj = {
  get propName() {
    // getter, the code executed on getting obj.propName
  },

  set propName(value) {
    // setter, the code executed on setting obj.propName = value
  }
};
```

- Descriptors for accessor properties are different from those for data properties. For accessor properties, there is no `value` or `writable`, but instead there are `get` and `set` functions. That is, an accessor descriptor may have:

  - `get` – a function without arguments, that works when a property is read,
  - `set` – a function with one argument, that is called when the property is set,
  - `enumerable` – same as for data properties,
  - `configurable` – same as for data properties.

```js
let user = {
  name: "John",
  surname: "Smith"
};

Object.defineProperty(user, 'fullName', {
  get() {
    return `${this.name} ${this.surname}`;
  },

  set(value) {
    [this.name, this.surname] = value.split(" ");
  }
});

alert(user.fullName); // John Smith

for(let key in user) alert(key); // name, surname
```

- Can be used together with `_variableName` convention to indicate *private* properties:

```js
let user = {
  get name() {
    return this._name;
  },

  set name(value) {
    if (value.length < 4) {
      alert("Name is too short, need at least 4 characters");
      return;
    }
    this._name = value;
  }
};

user.name = "Pete";
alert(user.name); // Pete

user.name = ""; // Name is too short...
```

- One of the great uses of accessors is that they allow to take control over a “regular” data property at any moment by replacing it with a getter and a setter and tweak its behavior. This is especially useful for compatibility if some code needs to change (e.g. `age` property needs to be changed to `birthday`, but former one still needs to be accessed by older code).

### Prototypal Inheritance

- In JavaScript, all objects have a hidden `[[Prototype]]` property that’s either another object or `null`.

- We can use `obj.__proto__` to access it (a historical getter/setter, there are other ways, to be covered soon).

- The object referenced by `[[Prototype]]` is called a “prototype”.

- If we want to read a property of obj or call a method, and it doesn’t exist, then JavaScript tries to find it in the prototype.

- Write/delete operations act directly on the object, they don’t use the prototype (assuming it’s a data property, not a setter).

- If we call `obj.method()`, and the method is taken from the prototype, `this` still references obj. So methods always work with the current object even if they are inherited.

- The `for..in` loop iterates over both its own and its inherited properties. All other key/value-getting methods only operate on the object itself.

### F.prototype

- The `F.prototype` property (don’t mistake it for `[[Prototype]]`) sets `[[Prototype]]` of new objects when `new F()` is called.

```js
let animal = {
  eats: true
};

function Rabbit(name) {
  this.name = name;
}

Rabbit.prototype = animal;
let rabbit = new Rabbit("White Rabbit"); //  rabbit.__proto__ == animal
```

```js
function Rabbit() {}
Rabbit.prototype = {
  jumps: true
};

let rabbit = new Rabbit();
alert(rabbit.constructor === Rabbit); // false

// instead use:
function Rabbit() {}

// Not overwrite Rabbit.prototype totally
// just add to it
Rabbit.prototype.jumps = true
// the default Rabbit.prototype.constructor is preserved

// OR
Rabbit.prototype = {
  jumps: true,
  constructor: Rabbit
};
// now constructor is also correct, because we added it
```

- The value of `F.prototype` should be either an object or `null`: other values won’t work.

- The "prototype" property only has such a special effect when set on a constructor function, and invoked with `new`.

- On regular objects the prototype is nothing special:

```js
let user = {
  name: "John",
  prototype: "Bla-bla" // no magic at all
};
```

- By default all functions have `F.prototype = { constructor: F }`, so we can get the constructor of an object by accessing its "constructor" property.

### Native Prototypes

- All built-in objects follow the same pattern:
  
  - The methods are stored in the prototype (`Array.prototype`, `Object.prototype`, `Date.prototype`, etc.)
  - The object itself stores only the data (array items, object properties, the date)

- Primitives also store methods in prototypes of wrapper objects: `Number.prototype`, `String.prototype` and `Boolean.prototype`. Only `undefined` and `null` do not have wrapper objects

- Built-in prototypes can be modified or populated with new methods. But it’s not recommended to change them. The only allowable case is probably when we add-in a new standard, but it’s not yet supported by the JavaScript engine

- Method borrowing from prototypes. Below code works because the internal algorithm of the built-in `join` method only cares about the correct indexes and the `length` property. It doesn’t check if the object is indeed an array. Many built-in methods are like that. Another possibility is to inherit by setting `obj.__proto__` to `Array.prototype`, so all `Array` methods are automatically available in `obj`. But that’s impossible if `obj` already inherits from another object. Remember, **we only can inherit from one object at a time**.

```js
let obj = {
  0: "Hello",
  1: "world!",
  length: 2,
};

obj.join = Array.prototype.join;

alert( obj.join(',') ); // Hello,world!
```

### Prototype Methods and Objects without __proto__

- Modern methods to set up and directly access the prototype are:

  - `Object.create(proto, [descriptors])` – creates an empty object with a given proto as `[[Prototype]]` (can be null) and optional property descriptors.
  - `Object.getPrototypeOf(obj)` – returns the `[[Prototype]]` of obj (same as `__proto__` getter).
  - `Object.setPrototypeOf(obj, proto)` – sets the `[[Prototype]]` of obj to 1 (same as `__proto__` setter).

```js
let animal = {
  eats: true
};

// create a new object with animal as a prototype
let rabbit = Object.create(animal);
alert(rabbit.eats); // true
alert(Object.getPrototypeOf(rabbit) === animal); // true
```

```js
let animal = {
  eats: true
};

let rabbit = Object.create(animal, {
  jumps: {
    value: true
  }
});

alert(rabbit.jumps); // true
```

- The built-in `__proto__` getter/setter is unsafe if we’d want to put user-generated keys into an object. Just because a user may enter "__proto__" as the key, and there’ll be an error, with hopefully light, but generally unpredictable consequences. So we can either use `Object.create(null)` to create a “very plain” object without `__proto__`, or stick to `Map` objects for that.

- `Object.create` provides an easy way to shallow-copy an object with all descriptors:

```js
let clone = Object.create(Object.getPrototypeOf(obj), Object.getOwnPropertyDescriptors(obj));
```

- We also made it clear that `__proto__` is a getter/setter for `[[Prototype]]` and resides in `Object.prototype`, just like other methods.

- We can create an object without a prototype by `Object.create(null)`. Such objects are used as “pure dictionaries”, they have no issues with "__proto__" as the key.

- Other methods:

  - `Object.keys(obj)` / `Object.values(obj)` / `Object.entries(obj)` – returns an array of enumerable own string property names/values/key-value pairs.
  - `Object.getOwnPropertySymbols(obj)` – returns an array of all own symbolic keys.
  - `Object.getOwnPropertyNames(obj)` – returns an array of all own string keys.
  - `Reflect.ownKeys(obj)` – returns an array of all own keys.
  - `obj.hasOwnProperty(key)`: returns `true` if obj has its own (not inherited) key named key.

- All methods that return object properties (like `Object.keys` and others) – return “own” properties. If we want inherited ones, we can use `for..in`.

## Classes

- The basic class syntax looks like this:

```js
class MyClass {
  prop = value; // property

  constructor(...) { // constructor
    // ...
  }

  method(...) {} // method

  get something(...) {} // getter method
  set something(...) {} // setter method

  [Symbol.iterator]() {} // method with computed name (symbol here)
  // ...
}
```

- `MyClass` is technically a function (the one that we provide as `constructor`), while methods, getters and setters are written to `MyClass.prototype`.

### Class Inheritance

- To extend a class: `class Child extends Parent`. That means `Child.prototype.__proto__` will be `Parent.prototype`, so methods are inherited.

- When overriding a constructor we must call parent constructor as `super()` in `Child` constructor before using `this`.

- When overriding another method we can use `super.method()` in a `Child` method to call `Parent` method.

- Internals:
  
  - Methods remember their class/object in the internal `[[HomeObject]]` property. That’s how `super` resolves parent methods.
  - So it’s not safe to copy a method with `super` from one object to another.

- Arrow functions don’t have their own `this` or `super`, so they transparently fit into the surrounding context.

### Static Methods

- Static methods are used for the functionality that belongs to the class “as a whole”. It doesn’t relate to a concrete class instance. They are labeled by the word `static` in class declaration. Static properties are used when we’d like to store class-level data, also not bound to an instance. The syntax is:

```js
class MyClass {
  static property = ...;

  static method() {
    ...
  }
}
```

- Technically, static declaration is the same as assigning to the class itself:

```js
MyClass.property = ...
MyClass.method = ...
```

- Static properties and methods are inherited.

- For class `B` extends `A` the prototype of the class `B` itself points to `A`: `B.[[Prototype]] = A`. So if a field is not found in `B`, the search continues in `A`.

### Private and Protected Properties and Methods

- To hide an internal interface we use either protected or private properties:

  - Protected fields start with `_`. That’s a well-known convention, not enforced at the language level. Programmers should only access a field starting with `_` from its class and classes inheriting from it.
  - Private fields start with `#`. JavaScript makes sure we can only access those from inside the class.

- Right now, private fields are not well-supported among browsers, but can be polyfilled.

### Extending Built-in Classes

- For example, `PowerArray` inherits from the native `Array`:

```js
// add one more method to it (can do more)
class PowerArray extends Array {
  isEmpty() {
    return this.length === 0;
  }
}

let arr = new PowerArray(1, 2, 5, 10, 50);
alert(arr.isEmpty()); // false

let filteredArr = arr.filter(item => item >= 10);
alert(filteredArr); // 10, 50
alert(filteredArr.isEmpty()); // false
```

- Built-in methods return new objects of exactly the inherited type `PowerArray`. Their internal implementation uses the object’s constructor property for that. This behaviour can be customized by adding static getter `Symbol.species` to the class:

```js
class PowerArray extends Array {
  isEmpty() {
    return this.length === 0;
  }

  // built-in methods will use this as the constructor
  static get [Symbol.species]() {
    return Array;
  }
}
```

- Built-in objects have their own static methods, for instance `Object.keys`, `Array.isArray` etc. As we already know, native classes extend each other. For instance, `Array` extends `Object`. Normally, when one class extends another, both static and non-static methods are inherited. **But built-in classes are an exception. They don’t inherit statics from each other.** For example, both `Array` and `Date` inherit from `Object`, so their instances have methods from `Object.prototype`. But `Array.[[Prototype]]` does not reference `Object`, so there’s no, for instance, `Array.keys()` (or `Date.keys()`) static method.

### Mixins

- **Mixin** – is a generic object-oriented programming term: a class that contains methods for other classes. Some other languages allow multiple inheritance. JavaScript does not support multiple inheritance, but mixins can be implemented by copying methods into prototype. We can use mixins as a way to augment a class by adding multiple behaviors, like event-handling.

- Mixins may become a point of conflict if they accidentally overwrite existing class methods. So generally one should think well about the naming methods of a mixin, to minimize the probability of that happening.

```js
// mixin
let sayHiMixin = {
  sayHi() {
    alert(`Hello ${this.name}`);
  },
  sayBye() {
    alert(`Bye ${this.name}`);
  }
};

// usage:
class User {
  constructor(name) {
    this.name = name;
  }
}

// copy the methods
Object.assign(User.prototype, sayHiMixin);

// now User can say hi
new User("Dude").sayHi(); // Hello Dude!
```

### Type Checking Methods

|               |                            works for                            |   returns  |
|:-------------:|:---------------------------------------------------------------:|:----------:|
| `typeof`      | primitives                                                      | string     |
| `{}.toString` | primitives, built-in objects, objects with `Symbol.toStringTag` | string     |
| `instanceof`  | objects                                                         | true/false |

## Promises, async/await

### Callbacks

- In cases where some functions/code depend on asynchronous actions (like script loading, data fetching, etc.) callback function can be used which executes after given action is completed:

```js
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;

  script.onload = () => callback(script);

  document.head.append(script);
}
```

- Handling erros in callback functions often follows **error-first callback** style:

```javascript
function loadScript(src, callback) {
  let script = document.createElement('script');
  script.src = src;

  script.onload = () => callback(null, script);
  script.onerror = () => callback(new Error(`Script load error for ${src}`));

  document.head.append(script);
}

loadScript('/my/script.js', function(error, script) {
  if (error) {
    // handle error
  } else {
    // script loaded successfully
  }
});
```

- Above approach should be used only for simple callbacks without deep multiple levels of nested callback (**callback hell**/**pyramid of doom**).

### Promise

- The function passed to `new Promise` is called the _executor_. When `new Promise` is created, the executor runs automatically. It contains the producing code which should eventually produce the result. Its arguments `resolve` and `reject` are callbacks provided by JavaScript itself. Our code is only inside the executor.

- When the executor obtains the result, be it soon or late, doesn’t matter, it should call one of these callbacks:
	
	-   `resolve(value)` — if the job is finished successfully, with result `value`.
	-   `reject(error)` — if an error has occurred, `error` is the error object.

- The `promise` object returned by the `new Promise` constructor has these internal properties:
	
	- `state` — initially `"pending"`, then changes to either `"fulfilled"` 	when `resolve` is called or `"rejected"` when `reject` is called.
	- `result` — initially `undefined`, then changes to `value` when `resolve(value)` called or `error` when `reject(error)` is called.

```javascript
let promise = new Promise(function(resolve, reject) {
  // the function is executed automatically when the promise is constructed
  if (...) {
    setTimeout(() => resolve("done"), 1000);
  } else {
    setTimeout(() => reject(new Error("Whoops!")), 1000);
  }
  // after 1 second signal that the job is done with the result "done"
  
});
```

- A Promise object serves as a link between the executor (the “producing code” or “singer”) and the consuming functions (the “fans”), which will receive the result or error. Consuming functions can be registered (subscribed) using methods `.then`, `.catch` and `.finally`.
- Handlers do not have to subscribe to promises before their execution; if the result is already there, they just execute immediately.
- `.then(result_func, error_func)`  can also omit the second argument.
- `.catch(error_func)` is equivalent of `.then(null, result_func)`
- `.finally(() => "Cleaning...")` handler has no argument, but can be used for cleaning/wrapping activities. It also passes through results and errors to the next handler.

```javascript
function loadScript(src) {
  return new Promise(function(resolve, reject) {
    let script = document.createElement('script');
    script.src = src;

    script.onload = () => resolve(script);
    script.onerror = () => reject(new Error(`Script load error for ${src}`));

    document.head.append(script);
  });
}

let promise = loadScript("https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.js");

promise.then(
  script => alert(`${script.src} is loaded!`),
  error => alert(`Error: ${error.message}`)
);

promise.then(script => alert('Another handler...'));
```

#### Promise Chaining

- If a `.then` (or `catch/finally`, doesn’t matter) handler returns a promise, the rest of the chain waits until it settles. When it does, its result (or error) is passed further.
- Each `.then` handler returns a new promise - it allows for promise chaining:

```javascript
new Promise(function(resolve, reject) {

  setTimeout(() => resolve(1), 1000); // (*)

}).then(function(result) { // (**)

  alert(result); // 1
  return result * 2;

}).then(function(result) { // (***)

  alert(result); // 2
  return result * 2;

}).then(function(result) {

  alert(result); // 4
  return result * 2;

});
```

- As a good practice, an asynchronous action should always return a promise. That makes it possible to plan actions after it; even if we don’t plan to extend the chain now, we may need it later.

#### Error Handling With Promises

- Promise chains are great at error handling. When a promise rejects, the control jumps to the closest rejection handler. That’s very convenient in practice.
- For instance, in the code below the URL to `fetch` is wrong (no such site) and `.catch` handles the error:

```javascript
fetch('https://no-such-server.blabla') // rejects
  .then(response => response.json())
  .catch(err => alert(err)) // TypeError: failed to fetch (the text may vary)
```

- The code of a promise executor and promise handlers has an "invisible `try..catch`" around it. If an exception happens, it gets caught and treated as a rejection. This happens for all errors, not just those caused by the `throw` statement. However, this implicit `try..catch` clause applies to all synchronous errors. Asynchronous errors still require usage of `reject`.

```javascript
new Promise((resolve, reject) => {
  throw new Error("Whoops!");
}).catch(alert); // Error: Whoops!
```

- It’s ok not to use `.catch` at all, if there’s no way to recover from an error.

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

## Error Handling

### "try...catch"

- The `try...catch` construct allows to handle runtime errors. It literally allows to “try” running the code and “catch” errors that may occur in it.

```js
try {
  // run this code
} catch (err) {
  // if an error happened, then jump here
  // err is the error object
} finally {
  // do in any case after try/catch
}
```

- There may be no `catch` section or no `finally`, so shorter constructs `try...catch` and `try...finally` are also valid.

- The `finally` clause works in case of any exit from `try...catch`, even via the `return` statement.

- Error objects have following properties:

  - `message` – the human-readable error message.
  - `name` – the string with error name (error constructor name).
  - `stack` (non-standard, but well-supported) – the stack at the moment of error creation.

- If an error object is not needed, we can omit it by using `catch {}` instead of `catch (err) {}`.

- We can also generate our own errors using the `throw` operator. Technically, the argument of `throw` can be anything, but usually it’s an error object inheriting from the built-in `Error` class.

- `Rethrowing` is a very important pattern of error handling: a `catch` block usually expects and knows how to handle the particular error type, so it should rethrow errors it doesn’t know.

- Even if we don’t have `try...catch`, most environments allow us to setup a “global” error handler to catch errors that “fall out”. In-browser, that’s `window.onerror`.

### Custom Errors

- We can inherit from `Error` and other built-in error classes normally. We just need to take care of the `name` property and don’t forget to call `super`.

- We can use `instanceof` to check for particular errors. It also works with inheritance. But sometimes we have an error object coming from a 3rd-party library and there’s no easy way to get its class. Then `name` property can be used for such checks.

- Wrapping exceptions is a widespread technique: a function handles low-level exceptions and creates higher-level errors instead of various low-level ones. Low-level exceptions sometimes become properties of that object like `err.cause`, but that’s not strictly required.

```js
class ReadError extends Error {
  constructor(message, cause) {
    super(message);
    this.cause = cause;
    this.name = 'ReadError';
  }
}

class ValidationError extends Error { /*...*/ }
class PropertyRequiredError extends ValidationError { /* ... */ }

function validateUser(user) {
  if (!user.age) {
    throw new PropertyRequiredError("age");
  }

  if (!user.name) {
    throw new PropertyRequiredError("name");
  }
}

function readUser(json) {
  let user;

  try {
    user = JSON.parse(json);
  } catch (err) {
    if (err instanceof SyntaxError) {
      throw new ReadError("Syntax Error", err);
    } else {
      throw err;
    }
  }

  try {
    validateUser(user);
  } catch (err) {
    if (err instanceof ValidationError) {
      throw new ReadError("Validation Error", err);
    } else {
      throw err;
    }
  }

}

try {
  readUser('{bad json}');
} catch (e) {
  if (e instanceof ReadError) {
    alert(e);
    // Original error: SyntaxError: Unexpected token b in JSON at position 1
    alert("Original error: " + e.cause);
  } else {
    throw e;
  }
}
```

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
