# TypeScript

## Types

### Primitives

- `number`
- `string`
- `boolean`

### Arrays

- `number[]`
- `string[]`
- `boolean[]`

### Objects

- single object type definition:

```typescript
let person: {
    name: string;
    age: number;
};
```

- array of objects type definition:

```typescript
let people: {
    name: string;
    age: number;
}[];
```

### Type Inference

- Variable type will be inferred when value is provided right away. E.g. `let course = 'Angular Course;` infers `string` type for `course` variable.

### Union Types

- `let course: string | number = 'Angular Course';`

### Type Alias

```typescript
type Person = {
    name: string;
    age: number;
};

let people: Person[];
```

### Functions and Types

- function returning value

```typescript
function add(a: number, b: number): number {
    return a + b;
}
```

- void function

```typescript
function print(value: any): void {
    console.log(value);
}
```

### Generics

- Generics help to downstream infering-related capabilities of TypeScript. E.g. we might want to accept any values in the function, but at the same tike we might want to have all types being the same:

```typescript
function insertAtBeginning<T>(array: T[], value: T) {
    const newArray = [value, ...array];
    return newArray;
}
```

### Classes and Types

```typescript
class Student {
    firstName: string;
    lastName: string;
    age: number;
    private courses: string[];

    constructor(first: string, last: string, age: number, coursers: string[]) {
        this.firstName = first;
        this.lastName = last;
        this.age = age;
        this.courses = courses;
    }

    enroll(courseName: string) {
        this.courses.push(courseName);
    }

    listCoursers() {
        return this.courses.slice();
    }
}
```

- Above in the shorthand notation:

```typescript
class Student {
    constructor(
        public firstName: string,
        public lastName: string,
        public age: number,
        private coursers: string[]
    ) {}
}
```

## Interfaces

- Interfaces act like `type` but they can be used in classes to force given structure.

```typescript
interface Human {
    firstName: string;
    age: number;

    greet: () => void;
}

let me: Human;

me = {
    firstName: 'Maciej',
    age: 29,
    greet() {
        console.log('Hi!');
    }
}

class Instructor implements Human {
    firstName: string;
    age: number;
    greet() {
        console.log('Hello!');
    }
}
```
