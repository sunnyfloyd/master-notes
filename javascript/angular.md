# Angular

## CLI

- To create new Angular app using Angular CLI use `ng new app-name`.

- To start application use `ng serve` from the directory where Angular app is located.


## Component

- Component can be selected by tags, attributes, classes:

    - `'app-server'`
    - `[app-server]`
    - `.app-server`

### Creating New Component

- Adding a new component via CLI: `ng generate component component-name` or `ng g c component-name`.

- Adding component manually:

```typescript
import { Component } from '@angular/core';

@Component({
    selector: 'app-server',
    templateUrl: './server.component.html'
})
export class ServerComponent {

}
```

- Component additionally needs to be added to the `declarations` in `app.module.ts` and to the desired HTML file using defined selector.

### View Encapsulation

- By default Angular encapsulates component styles so that defined style applies only to the given component. This is achieved via targeting styles using specific, automatically generated attributes assigned to each component.

- This behaviour can be overriden:

```typescript
import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  // ...
  encapsulation: ViewEncapsulation.None // can also be Native (uses shadow DOM that is not supported in all of the browsers) and Emulated (default)
})
```

## Databinding

### String Interpolation

- Uses `{{  }}` syntax that does not accept multiline expressions. The only requirement is that returned value must be castable into a string.

### Property Binding

- `<button [disabled]="!allowNewServer">Add server</button>`

### Event Binding

- `<button (click)="onCreateServer()">Add server</button>`

- To get access to data passed with event binding we have to use `$event` varialbe: `<input (input)="onUpdateServer($event)">`.

### Two-Way Binding

- `<input [(ngModel)]="serverName">`

### Custom Property Binding in Components

- First we need to expose component's property using `Input` decorator:

```typescript
import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-server-element',
  templateUrl: './server-element.component.html',
  styleUrls: ['./server-element.component.css']
})
export class ServerElementComponent implements OnInit {
  @Input() element: {
    type: string,
    name: string,
    content: string
  };

  constructor() { }

  ngOnInit(): void {
  }

}
```

- We can also use an alias for property's name using `Input('propertyAlias')`.

- Then, when calling given component we assign its property a proper value:

```typescript
<app-server-element
    *ngFor="let serverElement of serverElements"
    [element]="serverElement"
></app-server-element>
```

### Custom Events

- We can create custom events to invoke functions from the parent components.

```html
<!-- This will invoke "onServerAdded" function when "serverCreated" event is emitted -->
<app-cockpit
    (serverCreated)="onServerAdded($event)"
    (blueprintCreated)="onBlueprintAdded($event)"
></app-cockpit>
```

- Events are registered using `Output` decorator:

```typescript
export class CockpitComponent implements OnInit {
  @Output() serverCreated = new EventEmitter<{serverName: string, serverContent: string}>();
  newServerName = '';
  newServerContent = '';
  // ...
  onAddServer() {
    this.serverCreated.emit({
      serverName: this.newServerName,
      serverContent: this.newServerContent,
    });
  }
}
```

### Local References

- Instead of using two-way binding that provides real-time updates on properties we can also use local references that work only in the given HTML template. It can pass HTML element with its value to methods:

```html
<input
  type="text"
  class="form-control"
  #serverName
>
<input
  type="text"
  class="form-control"
  #serverContent
>

<button
  class="btn btn-primary"
  (click)="onAddServer(serverName, serverContent)">Add Server</button>
```

```typescript
onAddServer(serverName: HTMLInputElement, serverContent: HTMLInputElement) {
  this.serverCreated.emit({
    serverName: serverName.value,
    serverContent: serverContent.value,
  });
}
```

### Accessing Template and DOM element via @ViewChild

- This should not be used to change given element!

```html
<input
  type="text"
  class="form-control"
  #serverContent
>
<button
  class="btn btn-primary"
  (click)="onAddServer()">Add Server</button>
```

```typescript
@ViewChild('serverContent', { static: true }) serverName: ElementRef;
// ...
onAddServer() {
  this.serverCreated.emit({
    serverName: this.serverName.nativeElement.value,
    serverContent: this.serverContent.nativeElement.value,
  });
}
```

### Accessing ng-content element via @ContentChild

- This should not be used to change given element!

```html
<!-- part that gets projected to ng-content -->
<app-server-element
  *ngFor="let serverElement of serverElements"
  [element]="serverElement"
>
  <p #mainParagraph>
    <strong *ngIf="serverElement.type === 'server'" style="color: red">{{ serverElement.content }}</strong>
    <em *ngIf="serverElement.type === 'blueprint'">{{ serverElement.content }}</em>
  </p>
</app-server-element>
```

```typescript
@ContentChild('mainParagraph', { static: true }) serverName: ElementRef;
```

### ng-content

- By default all code between components tags is ignored. This can be changed if we add `<ng-content></ng-content>` hook in the component. Then, all the code between the tags will be projected there.

```html
<!-- inside parent component -->
<app-server-element
    *ngFor="let serverElement of serverElements"
    [element]="serverElement"
>
  <p>
    <strong *ngIf="serverElement.type === 'server'" style="color: red">{{ serverElement.content }}</strong>
    <em *ngIf="serverElement.type === 'blueprint'">{{ serverElement.content }}</em>
  </p>
</app-server-element>

<!-- inside server-element component -->
<ng-content></ng-content>
```

## Directives

- `*` indicates a structural directive that changes the DOM.
- 
### Built-in Directives

#### ngIf

- A structural directive that conditionally includes a template based on the value of an expression coerced to Boolean. When the expression evaluates to true, Angular renders the template provided in a `then` clause, and when `false` or `null`, Angular renders the template provided in an optional `else` clause. The default template for the `else` clause is blank.

- `<p *ngIf="condition">Some text</p>`

- `ngIf` can be suplemented with an `else` clause that should refer to a `ng-template` with a given label.

```html
<div class="hero-list" *ngIf="heroes else loading">
 ...
</div>

<ng-template #loading>
 <div>Loading...</div>
</ng-template>
```

#### ngStyle

- An attribute directive that updates styles for the containing HTML element. Sets one or more style properties, specified as colon-separated key-value pairs. The key is a style name, with an optional .`<unit>` suffix (such as 'top.px', 'font-style.em'). The value is an expression to be evaluated. The resulting non-null value, expressed in the given unit, is assigned to the given style property. If the result of evaluation is `null`, the corresponding style is removed.

```html
<some-element [ngStyle]="{'font-style': styleExp}">...</some-element>
```

#### ngClass

- Adds and removes CSS classes on an HTML element.

```html
<some-element [ngClass]="{'first': true, 'second': true, 'third': false}">...</some-element>
```

#### ngFor

- A structural directive that renders a template for each item in a collection. The directive is placed on an element, which becomes the parent of the cloned templates.

```html
<li *ngFor="let item of items; index as i; trackBy: trackByFn">...</li>
```

## Model

- Declaring data model can be done in two ways:

```typescript
// Standard
export class Ingredient {
    public name: string;
    public amount: number;

    constructor(name: string, amount: number) {
        this.name = name;
        this.amount = amount;
    }
}

// Using Angular shortcut
export class Ingredient {
    constructor(public name: string, public amount: number) {}
}
```

## Lifecycle Hooks

- `ngOnChanges` - called after a bound input (decorated with `@Input()`) property changes
- `ngOnInit` - called once the component is initialized 
- `ngDoCheck` - called during every change detection run
- `ngAfterContentInit` - called after content (`ng-content`) has been projected into view
- `ngAfterContentChecked` - called every time the projected content has been checked
- `ngAfterViewInit` - called after the component's view (and child views) has been initialized
- `ngAfterViewChecked` - called every time the view (and child views) has been checked
- `ngOnDestroy` - called once the component is about to be destroyed
