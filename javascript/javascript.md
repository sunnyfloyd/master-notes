# JavaScript

- [JavaScript](#javascript)
  - [Sources](#sources)
  - [Basics](#basics)
    - [Variables and Constants](#variables-and-constants)
    - [Operators](#operators)
    - [Loops](#loops)
    - [Switch](#switch)
    - [Functions](#functions)
      - [Function Expressions](#function-expressions)
      - [Arrow Functions](#arrow-functions)
    - [querySelector](#queryselector)
    - [forEach](#foreach)
    - [Data Attributes](#data-attributes)
    - [Arrow Functions](#arrow-functions-1)
    - ['this' Keyword](#this-keyword)
    - [Using Form Input](#using-form-input)
    - [Local Storage](#local-storage)
    - [Other](#other)
    - [AJAX](#ajax)
  - [UX/UI](#uxui)

## Sources

- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/5/)

## Basics

### Variables and Constants

- `var` defines **global variable**.

- `let` defines variable limited in scope to the current block.

- `const` defines a value that will not change.

### Operators

- The plus `+` exists in two forms: **the binary form that we used above and the unary form**:
  
  - The unary plus or, in other words, the plus operator `+` applied to a single value, doesn’t do anything to numbers.**
  - If the operand is not a number, the unary plus converts it into a number. It is a shorthand for `Number()`**.

- **Nullish coalescing operator**. `??` returns the first argument if it’s not `null/undefined`. Otherwise, the second one: `result = a ?? b` is equivalent to `result = (a !== null && a !== undefined) ? a : b`. It can be used with multiple operands: `firstName ?? lastName ?? nickName ?? "Anonymous"`.

### Loops

- A **label** is an identifier with a colon before a loop. `break` can refer to a loop via its scope so it can break out of the outer loop from the inner one. The `continue` directive can also be used with a label.

```js
labelName: for (...) {
  ...
}
```

### Switch

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

### Functions

- A function may access outer variables. But it works only from inside out. The code outside of the function doesn’t see its local variables.

- **A function always gets a copy of the value** so changes of the passed arguments do not impact original variables.

- A **parameter** is the variable listed inside the parentheses in the function declaration (it’s a declaration time term)
- An **argument** is the value that is passed to the function when it is called (it’s a call time term).

- If a function is called, but an argument is not provided, then the corresponding value becomes `undefined`.

#### Function Expressions

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

#### Arrow Functions

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

### forEach

- `forEach` runs given function on each element in the iterable:

```js
document.querySelectorAll('button').forEach(function(button) {
    button.onclick = function() {
        document.querySelector("#hello").style.color = button.dataset.color;
    }
}
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

### Arrow Functions

- JavaScript now gives us the ability to use **Arrow Functions** where we have an input (or parentheses when there’s no input) followed by `=>` followed by some code to be run. For example, we can alter our script above to use an anonymous arrow function:

```js
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('button').forEach(button => {
        button.onclick = () => {
            document.querySelector("#hello").style.color = button.dataset.color;
        }
    });
});
```

- We can also have named functions that use arrows:

```js
count = () => {
    counter++;
    document.querySelector('h1').innerHTML = counter;
    
    if (counter % 10 === 0) {
        alert(`Count is now ${counter}`)
    }
}
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

### Other

- `setInterval(function, 1000)` calls a function or evaluates an expression at specified intervals (in miliseconds).

### AJAX

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
