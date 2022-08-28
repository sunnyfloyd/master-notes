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

## Databinding

### String Interpolation

- Uses `{{  }}` syntax that does not accept multiline expressions. The only requirement is that returned value must be castable into a string.

### Property Binding

- `<button [disabled]="!allowNewServer">Add server</button>`

### Event Binding

- `<button (click)="onCreateServer()">Add server</button>`

- To get access to data passed with event binding we have to use `$event` varialbe: `<input (input)="onUpdateServer($event)">`.

#### Two-Way Binding

- `<input [(ngModel)]="serverName">`

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