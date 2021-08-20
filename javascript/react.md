# React

## Sources

- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/6/)

## Fundamentals

- The **React** framework is built around the idea of components, each of which can have an underlying state. A component would be something you can see on a web page like a post or a navigation bar, and a state is a set of variables associated with that component. The beauty of React is that when the state changes, React will automatically change the DOM accordingly.

- Components in React can be represented by JavaScript function.

- Functionality of the components can be extended using **props** (properties):

```jsx
function Hello(props) {
    return (
        <h1>Hello, {props.name}!</h1>
    );
}

function App() {
    return (
        <div>
            <Hello name="Harry" />
            <Hello name="Ron" />
            <Hello name="Hermione" />
        </div>
    );
}
```

- We can use `useState` hook to add state to the component:

```jsx

function App() {
    const [count, setCount] = React.useState(0);

    function updateCount() {
        setCount(count + 1);
    }

    return (
        <div>
            <h1>{count}</h1>
            <button onClick={updateCount}>Count</button>
        </div>
    );
}
```

- State can be a JavaScript object that includes required information about state:

```jsx
const [state, setState] = React.useState({
    num1: 1,
    num2: 1,
    response: "",
    score: 0
});
```

- `onChange` attribute can be added to an input element to trigger certain function:

```jsx
function App() {
    // when state is being changed only for some of the elements of a component
    function updateResponse(event) {
        setState({
            ...state,
            response: event.target.value
        });
    }
    return (
        <div>
            <div>{state.num1} + {state.num2}</div>
            <input onChange={updateResponse} value={state.response} />
            <div>Score: {state.score}</div>
        </div>
    );
}


```

- `onKeyPress` - is an event handler that is being fired whenever key is being pressed.

- React has its own autofocus attribute `autoFocus={true}`.

- `className` is an attribute in React to add a class to an HTML element.
