# Angular

## TOC

- [Angular](#angular)
  - [TOC](#toc)
  - [CLI](#cli)
  - [Components](#components)
    - [Creating New Component](#creating-new-component)
    - [View Encapsulation](#view-encapsulation)
  - [Lifecycle Hooks](#lifecycle-hooks)
  - [Model](#model)
  - [Databinding](#databinding)
    - [String Interpolation](#string-interpolation)
    - [Property Binding](#property-binding)
    - [Event Binding](#event-binding)
    - [Two-Way Binding](#two-way-binding)
    - [Custom Property Binding in Components](#custom-property-binding-in-components)
    - [Custom Events](#custom-events)
    - [Local References](#local-references)
    - [Accessing Template and DOM element via @ViewChild](#accessing-template-and-dom-element-via-viewchild)
    - [Accessing ng-content element via @ContentChild](#accessing-ng-content-element-via-contentchild)
    - [ng-content](#ng-content)
  - [Directives](#directives)
    - [Structural Directives](#structural-directives)
      - [ngIf](#ngif)
      - [ngFor](#ngfor)
      - [ngSwitch](#ngswitch)
    - [Custom Structural Directive](#custom-structural-directive)
    - [Attribute Directives](#attribute-directives)
      - [ngStyle](#ngstyle)
      - [ngClass](#ngclass)
    - [Custom Attribute Directive](#custom-attribute-directive)
      - [HostListener](#hostlistener)
      - [HostBinding](#hostbinding)
  - [Services](#services)
    - [Example of a Service](#example-of-a-service)
    - [Tips For Working With Services](#tips-for-working-with-services)
  - [Routing](#routing)
    - [routerLink](#routerlink)
    - [Programmatical Navigation](#programmatical-navigation)
    - [Fetching Route Parameters](#fetching-route-parameters)
    - [Fetching Query Parameters and Fragment](#fetching-query-parameters-and-fragment)
    - [Nested Routes](#nested-routes)
    - [Redirecting](#redirecting)
    - [Wildcard Routes](#wildcard-routes)
    - [Outsourcing Route Configuration](#outsourcing-route-configuration)
    - [Route Guards](#route-guards)

## CLI

- To create new Angular app using Angular CLI use `ng new app-name`.

- To start application use `ng serve` from the directory where Angular app is located.


## Components

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

## Lifecycle Hooks

- `ngOnChanges` - called after a bound input (decorated with `@Input()`) property changes
- `ngOnInit` - called once the component is initialized 
- `ngDoCheck` - called during every change detection run
- `ngAfterContentInit` - called after content (`ng-content`) has been projected into view
- `ngAfterContentChecked` - called every time the projected content has been checked
- `ngAfterViewInit` - called after the component's view (and child views) has been initialized
- `ngAfterViewChecked` - called every time the view (and child views) has been checked
- `ngOnDestroy` - called once the component is about to be destroyed

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

<!-- inside server-element component -->
<ng-content></ng-content>
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

- `ng g d directiveName` to create custom directive.

- `*` indicates a structural directive that changes the DOM.

### Structural Directives

- In structural directives you affect the actual area in the DOM of the web page.

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

#### ngFor

- A structural directive that renders a template for each item in a collection. The directive is placed on an element, which becomes the parent of the cloned templates.

```html
<li *ngFor="let item of items; index as i; trackBy: trackByFn">...</li>
```

#### ngSwitch

- The `ngSwitch` directive on a container specifies an expression to match against. The expressions to match are provided by ngSwitchCase directives on views within the container.

    - Every view that matches is rendered.
    - If there are no matches, a view with the ngSwitchDefault directive is rendered.
    - Elements within the `NgSwitch` statement but outside of any `NgSwitchCase` or `ngSwitchDefault` directive are preserved at the location.

```html
<container-element [ngSwitch]="switch_expression">
  <some-element *ngSwitchCase="match_expression_1">...</some-element>
    ...
  <some-element *ngSwitchDefault>...</some-element>
</container-element>
```

### Custom Structural Directive

- Below `set appUnless` is still a property but it just uses a property setter whenever property changes so that it can be called on each change:

```typescript
import { Directive, Input, TemplateRef, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[appUnless]'
})
export class UnlessDirective {
  @Input() set appUnless(condition: boolean) {
    if (!condition) {
      this.vcRef.createEmbeddedView(this.templateRef);
    } else {
      this.vcRef.clear();
    }
  }

  constructor(private templateRef: TemplateRef<any>, private vcRef: ViewContainerRef) { }
}
```

```html
<div *appUnless="onlyOdd">
  <li
    class="list-group-item"
    [ngClass]="{odd: even % 2 !== 0}"
    [ngStyle]="{backgroundColor: even % 2 !== 0 ? 'yellow' : 'transparent'}"
    *ngFor="let even of evenNumbers">
    {{ even }}
  </li>
</div>
```

### Attribute Directives

- In attribute directives you only change properties of the element.

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

### Custom Attribute Directive

- Creating basic custom attribute directive

```typescript
@Directive({
  selector: '[appBasicHighlight]'
})
export class BasicHighlightDirective implements OnInit {
  constructor(private elementRef: ElementRef) {  // ElementRef stores an actual element on which directive has been used
  }

  ngOnInit() {
    this.elementRef.nativeElement.style.backgroundColor = 'green';
  }
}
```

```html
<p appBasicHighlight>Style me with basic directive!</p>
```

- It is more idiomatic not to access element directly since Angular can render templates without actual DOM. Therefore following directive should be used to do the previous one:

```typescript
@Directive({
  selector: '[appBetterHighlight]'
})
export class BetterHighlightDirective implements OnInit {
  constructor(private elRef: ElementRef, private renderer: Renderer2) { }

  ngOnInit() {
    this.renderer.setStyle(this.elRef.nativeElement, 'background-color', 'blue');
  }
```

```html
<p>Style me with a better directive!</p>
```

#### HostListener

- To react to specific events on the given element with a defined directive use `HostListener`:

```typescript
@HostListener('mouseenter') mouseover(eventData: Event) {
  this.renderer.setStyle(this.elRef.nativeElement, 'background-color', 'blue');
}

@HostListener('mouseleave') mouseleave(eventData: Event) {
  this.renderer.setStyle(this.elRef.nativeElement, 'background-color', 'transparent');
}
```

#### HostBinding

- `HostBinding` allows to bind specific property of an element with a directive:

```typescript
@Directive({
  selector: '[appBetterHighlight]'
})
export class BetterHighlightDirective implements OnInit {
  @Input() defaultColor: string = 'transparent';
  @Input('appBetterHighlight') highlightColor: string = 'blue';
  @HostBinding('style.backgroundColor') backgroundColor: string;

  constructor(private elRef: ElementRef, private renderer: Renderer2) { }

  ngOnInit() {
    this.backgroundColor = this.defaultColor;
  }

  @HostListener('mouseenter') mouseover(eventData: Event) {
    this.backgroundColor = this.highlightColor;
  }

  @HostListener('mouseleave') mouseleave(eventData: Event) {
    this.backgroundColor = this.defaultColor;
  }
```

```html
<p [appBetterHighlight]="'red'" defaultColor="yellow">Style me with a better directive!</p>
```

- We can provide an alias to a binded property inside a directive to be the same as directive's selector. This way we can use following syntax to provide a value to a binded property and to instantiate a directive at the same time:

```typescript
@Directive({
  selector: '[appBetterHighlight]'
})
export class BetterHighlightDirective implements OnInit {
  @Input('appBetterHighlight') highlightColor: string = 'blue';
```

```html
<p [appBetterHighlight]="'red'">Style me with a better directive!</p>
```

## Services

- In order to easily share part of code between components without getting into complicated hierarchical structures **services** can be used.

- Service is just a normal TypeScript class.

- Angular's dependency injector is a hierarchical injector. **Remember that even though dependency is shared with all of the children it can still be overwritten by re-instantion within the child**. There are 3 possible cases of dependency injections:

  - `AppModule` - injecting dependency on this level ensures that the same instance of service is available **application-wide**.
  - `AppComponent` - same instance of service is available for all components but not for other services
  - any other component - same instance of service is available for the component and all its child components.

- Services can be injected into other services using `@Injectable()` decorator on the service class to which we want to inject some other service. Service must then be added to the constructor to be accessible within the injectable service.

- There is a new way of injecting services on the `AppModule` level that allows for lazy loading:

```typescript
@Injectable({providedIn: 'root'})
export class MyService { ... }
```

### Example of a Service

- Service definition:

```typescript
// First Service
export class LoggingService {
  logStatusChange(status: string) {
    console.log('A server status changed, new status: ' + status);
  }
}

import { EventEmitter, Injectable } from '@angular/core';

import { LoggingService } from './logging.service';

// Second Service
@Injectable()  // This is recommended to be added in all of the services (even those that
// do not have other services being injected)
export class AccountsService {
  accounts = [
    {
      name: 'Master Account',
      status: 'active'
    },
    {
      name: 'Testaccount',
      status: 'inactive'
    },
    {
      name: 'Hidden Account',
      status: 'unknown'
    }
  ];
  statusUpdated = new EventEmitter<string>();  // We do not need to make this emitted outside
  // since we might only plan to use it internally in the components that use this service

  constructor(private loggingService: LoggingService) {}

  addAccount(name: string, status: string) {
    this.accounts.push({name: name, status: status});
    this.loggingService.logStatusChange(status);
  }

  updateStatus(id: number, status: string) {
    this.accounts[id].status = status;
    this.loggingService.logStatusChange(status);
  }
}
```

- It needs to be injected into the component:

```typescript
import { Component, Input } from '@angular/core';

import { LoggingService } from '../logging.service';
import { AccountsService } from '../accounts.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css'],
  providers: [LoggingService]  // this REINSTANTIATES service in this component
})
export class AccountComponent {
  @Input() account: {name: string, status: string};
  @Input() id: number;

  constructor(private loggingService: LoggingService,
              private accountsService: AccountsService) {}

  onSetTo(status: string) {
    this.accountsService.updateStatus(this.id, status);
    // this.loggingService.logStatusChange(status);  // no longer needed since we injected
    // this service into the accountsService
    this.accountsService.statusUpdated.emit(status);
  }
}
```

- We can also subscribe to events emitted from a service inside a code that shares this service:

```typescript
export class NewAccountComponent {

  constructor(private accountsService: AccountsService) {
    this.accountsService.statusUpdated.subscribe(
      (status: string) => alert('New Status: ' + status)
    );
  }
}
```

### Tips For Working With Services

- If given service stores some data it is a good idea to make property storing this data **private**. When this property needs to be accessed we should provide specific **get method** for it. And if real-time updates are needed we can just emit event from the service that provides current copy of the property whenever some change happends:

```typescript
export class ShoppingListService {
    ingredientsChanged = new EventEmitter<Ingredient[]>();

    private ingredients: Ingredient[] = [
        new Ingredient('Apples', 5),
        new Ingredient('Tomatoes', 10),
    ];

    addIngredient(ingredient: Ingredient) {
        this.ingredients.push(ingredient);
        this.ingredientsChanged.emit(this.ingredients.slice());
    }
}

// subscribed inside a component
@Component({
  selector: 'app-shopping-list',
  templateUrl: './shopping-list.component.html',
  styleUrls: ['./shopping-list.component.css']
})
export class ShoppingListComponent implements OnInit {
  ingredients: Ingredient[];

  constructor(private shoppingListService: ShoppingListService) { }

  ngOnInit() {
    this.ingredients = this.shoppingListService.getIngredients();
    this.shoppingListService.ingredientsChanged.subscribe(
      (ingredients) => {
        this.ingredients = ingredients;
      }
    );
  }
}
```

## Routing

- Routing is done by defining URL paths to desired components inside AppModule with router module included in the imports:

```ts
const appRoutes: Routes = [
  {path: '', component: HomeComponent},
  {path: 'users', component: UsersComponent},
  {path: 'servers', component: ServersComponent}
];

@NgModule({
  // ...
  imports: [
    // ...
    RouterModule.forRoot(appRoutes)
  ],
  // ...
})
```

- To define dynamic route parameters add colon before its name: `{path: 'users/:id', component: UserComponent},`.

- Inside the template we must then define place where component should be loaded using `<router-outlet></router-outlet>` directive.

### routerLink

- To navigate to different modules using defined application routes we use property binding on `<a>` tag:

```html
<a routerLink="/servers">
<a [routerLink]="'/servers'">
<a [routerLink]="['/servers']">
```

- Tracks whether the linked route of an element is currently active, and allows you to specify one or more CSS classes to add to the element when the linked route is active. You can apply the `RouterLinkActive` directive to an ancestor of linked elements.

```html
<ul class="nav nav-tabs">
  <li role="presentation" routerLinkActive="active" [routerLinkActiveOptions]="{exact: true}"><a routerLink="/">Home</a></li>
  <li role="presentation" routerLinkActive="active"><a routerLink="/servers">Servers</a></li>
  <li role="presentation" routerLinkActive="active"><a routerLink="/users">Users</a></li>
</ul>
```

### Programmatical Navigation

- To navigate to a different page programmatically use `navigate()` method from router:

```ts
import { Router } from '@angular/router';

export class HomeComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
  }

  onLoadServers() {
    this.router.navigate(['/servers']);
  }
}
```

- To navigate to the relative path we need to add extras to `navigate()` method and use `ActivatedRoute` class:

```ts
import { Router, ActivatedRoute } from '@angular/router';

export class HomeComponent implements OnInit {

  constructor(private router: Router, private route: ActivatedRoute) { }

  ngOnInit() {
  }

  onLoadServers() {
    this.router.navigate(['/servers'], {relativeTo: this.route});
  }
}
```

- To navigate to a specific route with query params or specific reference pass `queryParams` object or `fragment` to `navigate` method:

```ts
onLoadServer(id: number) {
  this.router.navigate(['/servers', id, 'edit'], {queryParams: {allowEdit: '1'}, fragment: 'loading'})
}
```

- Query params can be preserved during router navigation by `queryParamsHandling` (`preserve` or `merge` string values):

```ts
onEdit() {
  this.router.navigate(['edit'], {relativeTo: this.route, queryParamsHandling: 'preserve'});
}
```

### Fetching Route Parameters

- To access route parameters:

```ts
export class UserComponent implements OnInit {
  user: {id: number, name: string};

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.user = {
      id: this.route.snapshot.params['id'],
      name: this.route.snapshot.params['name']
    };
  }
}
```

- If one needs to dynamically change component when parameters change instead of using snapshot one can subscribe to the params observable. When component is destoyed Angular automatically handles removal of subscription. Below approach uses new syntax where object with callables is provided (next, err, complete):

```ts
export class UserComponent implements OnInit {
  user: {id: number, name: string};

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    this.route.params.subscribe(
      {next: (params: Params) => {
        this.user = {
          id: params['id'],
          name: params['name']
        };
      }}
    );
  }
}
```

### Fetching Query Parameters and Fragment

- To add query params to the link we add `[queryParams]` directive with the object defining params and their values:

```ts
<a
  [routerLink]="['/servers', server.id, 'edit']"
  [queryParams]="{allowsEdit: '1'}"
>
  {{ server.name }}
</a>
```

- To pass reference (#reference) we use `[fragment]` directive:

```ts
<a
  [routerLink]="['/servers', server.id, 'edit']"
  [queryParams]="{allowsEdit: '1'}"
  fragment="loading"
>
  {{ server.name }}
</a>
```

- Both `queryParams` and `fragment` from `ActivateRoute` can be subscribed to.

### Nested Routes

- To setup routes within the routes loaded using `router-outlet` hook we need to add `children` array to route object:

```ts
const appRoutes: Routes = [
  {path: 'users', component: UsersComponent, children: [
    {path: ':id/:name', component: UserComponent}
  ]}
]
```

```html
<!-- In users.component.html -->
<router-outlet></router-outlet>
```

### Redirecting

- Redirecting is done via `redirectTo` attribute in routes:

```ts
const appRoutes: Routes = [
  {path: '**', component: PageNotFound}
]
```

- Remember that default matching strategy is `prefix` , Angular checks if the path you entered in the URL does start with the path specified in the route. This may lead to some issues when trying to redirect on the root path. To fix this behaviour you need to change the matching strategy to `full`:

```ts
const appRoutes: Routes = [
  { path: '', redirectTo: '/somewhere-else', pathMatch: 'full' } 
]
```

### Wildcard Routes

- `**` wildcard can be used to catch all other routes:

```ts
const appRoutes: Routes = [
  {path: 'not-found', component: PageNotFound},
  {path: '**', redirectTo: '/not-found'},
]
```

### Outsourcing Route Configuration

- It is a good practice to move routes to a separate module:

```ts
// In app-routing.module.ts
const appRoutes: Routes = [
  // ...
];

@NgModule({
  imports: [
    // RouterModule.forRoot(appRoutes, {useHash: true})
    RouterModule.forRoot(appRoutes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {
}

// In app.module.ts
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  imports: [
    // ...
    AppRoutingModule
  ],
})
```

### Route Guards

- Protecting route with `canActivate`:

```ts
// Service implementing canActivate method
import {
  CanActivate,
  ActivatedRouteSnapshot,
  RouterStateSnapshot,
  Router,
  CanActivateChild
} from '@angular/router';
import { Observable } from 'rxjs/Observable';
import { Injectable } from '@angular/core';
import { AuthService } from './auth.service';

@Injectable()
export class AuthGuard implements CanActivate, CanActivateChild {
  constructor(private authService: AuthService, private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot,
              state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    return this.authService.isAuthenticated()
      .then(
        (authenticated: boolean) => {
          if (authenticated) {
            return true;
          } else {
            this.router.navigate(['/']);
          }
        }
      );
  }
}

// In app.module.ts
import { AuthGuard } from './auth-guard.service';

const appRoutes: Routes = [
  {
    path: 'servers',
    canActivate: [AuthGuard],
    component: ServersComponent,
  },
];
```

- To add protection to children path as well we need to implement `canActivateChild` interface:

```ts
// In app.module.ts
const appRoutes: Routes = [
  {
    path: 'servers',
    canActivateChild: [AuthGuard],
    component: ServersComponent,
    children: [
    { path: ':id', component: ServerComponent, resolve: {server: ServerResolver} },
    { path: ':id/edit', component: EditServerComponent, canDeactivate: [CanDeactivateGuard] }
  ] },
];

// In auth service
canActivateChild(route: ActivatedRouteSnapshot,
  state: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
  return this.canActivate(route, state);
}
```

- Protecting route with `canDeactivate`:

```ts
// In app.module.ts
const appRoutes: Routes = [
  {
    path: 'servers',
    // canActivate: [AuthGuard],
    canActivateChild: [AuthGuard],
    component: ServersComponent,
    children: [
    { path: ':id', component: ServerComponent, resolve: {server: ServerResolver} },
    { path: ':id/edit', component: EditServerComponent, canDeactivate: [CanDeactivateGuard] }
  ]},
];

// In can-deactivate-guard.service.ts
import { Observable } from 'rxjs/Observable';
import { CanDeactivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';

export interface CanComponentDeactivate {
  canDeactivate: () => Observable<boolean> | Promise<boolean> | boolean;
}

export class CanDeactivateGuard implements CanDeactivate<CanComponentDeactivate> {

  canDeactivate(component: CanComponentDeactivate,
                currentRoute: ActivatedRouteSnapshot,
                currentState: RouterStateSnapshot,
                nextState?: RouterStateSnapshot): Observable<boolean> | Promise<boolean> | boolean {
    return component.canDeactivate();
  }
}

// In guarded component
export class EditServerComponent implements OnInit, CanComponentDeactivate {
  canDeactivate(): Observable<boolean> | Promise<boolean> | boolean {
    if (!this.allowEdit) {
      return true;
    }
    if ((this.serverName !== this.server.name || this.serverStatus !== this.server.status) && !this.changesSaved) {
      return confirm('Do you want to discard the changes?');
    } else {
      return true;
    }
  }
}
```
