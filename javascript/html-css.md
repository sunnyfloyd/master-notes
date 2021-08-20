# HTML and CSS

## Sources

- [CS50 Harvard Course](https://cs50.harvard.edu/web/2020/weeks/0/)

## HTML

- HTML5 introduced a new text input that is linked to a list of available options. Super useful for inputs with multiple options like countries:

```HTML
<input name="country" list="countries" placeholder="Country">
<datalist id="countries">
    <option value="Afghanistan">
    <option value="Albania">
    <option value="Algeria">
</datalist>
```

## CSS

- `border-collapes` removes multiple borders on the child elements and applies border only once. Useful for table borders.

- **Descendant selector** `a b` applies styling to all *b*s that at some level have *a* as a parent.

- **Child selector**  `a > b` is more direct and applies only to the immediate children of an *a*.

- **Media queries**:

```css
/* applies to width size larger or equal to 600px */
@media (min-width: 600px) {
    body {
        color: blue;
    }
}
/* applies to width size smaller or equal to 599px */
@media (max-width: 599px) {
    body {
        color: blue;
    }
}
```

### Responsive Design Paradigms

- **Flexbox**:

```css
#container {
    display: flex;
    flex-wrap: wrap;
}
```

- **Grid**:

```css
#grid {
    color: blue;
    display: grid;
    grid-columns-gap: 10px;
    grid-row-gap: 10px;
    /* grid-template-columns defines number of columns and their size */
    grid-template-columns: 200px 200px auto; 
}
```

### Animations

- Almost every CSS property can be animated:

```css
@keyframes hide {
    0% {
        opacity: 1;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margint-bottom: 10px;
    }

    100% {
        opacity: 0;
        height: 100%;
        line-height: 100%;
        padding: 20px;
        margint-bottom: 10px;
    }

    75% {
        opacity: 0;
        height: 0px;
        line-height: 0px;
        padding: 0px;
        margint-bottom: 0px;
    }
}

.post {
    animation-name: hide;
    animation-duration: 2s;
    animation-fill-mode: forwards;
    animation-play-state: paused;
}
```

### Syntatically Awesome Style Sheets (Sass)

- **Sass** is preprocessor scripting language that is interpreted or compiled into CSS.

- It allows for adding variables into a CSS. Variables start with `$`:

```css
$color: red;

h1 {
    color: $color;
}
```

- Sass allows for **nesting CSS selectors** instead of using standard descendant/child syntax:

```css
div {
    font-size: 18px;

    ul {
        color: blue;
    }
}
```

- Sass allows for inheritance of the generic elements:

```css
%message {
    color: blue;
    font-size: 20px;
}

.success {
    @extend %message;
    background-color: green;
}

.warning {
    @extend %message;
    background-color: red;
}
```
