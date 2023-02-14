# Angular

## TOC

- [Angular](#angular)
  - [TOC](#toc)
  - [CLI](#cli)
  - [Modules](#modules)
    - [Shared Modules](#shared-modules)
    - [Lazy Loading](#lazy-loading)
  - [Components](#components)
    - [Creating New Component](#creating-new-component)
    - [View Encapsulation](#view-encapsulation)
  - [Dynamic Components](#dynamic-components)
  - [Standalone Components](#standalone-components)
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
    - [Nested Routes](#nested-routes)
    - [Redirecting](#redirecting)
    - [Wildcard Routes](#wildcard-routes)
    - [Outsourcing Route Configuration](#outsourcing-route-configuration)
    - [routerLink](#routerlink)
    - [Programmatical Navigation](#programmatical-navigation)
    - [Fetching Route Parameters](#fetching-route-parameters)
    - [Fetching Query Parameters and Fragment](#fetching-query-parameters-and-fragment)
    - [Route Guards](#route-guards)
    - [Passing Static Data to Route](#passing-static-data-to-route)
    - [Resolving Dynamic Data with Resolve Guard](#resolving-dynamic-data-with-resolve-guard)
  - [Observables](#observables)
    - [How to Create Custom Observable](#how-to-create-custom-observable)
    - [Subjects](#subjects)
    - [BehaviorSubject](#behaviorsubject)
  - [Forms](#forms)
    - [Template-Driven Forms](#template-driven-forms)
      - [Accessing Form Object](#accessing-form-object)
      - [Form Validation](#form-validation)
      - [Form Default Values (Property Binding in Forms)](#form-default-values-property-binding-in-forms)
      - [Grouping Form Controls](#grouping-form-controls)
      - [Handling Radio Buttons](#handling-radio-buttons)
      - [Setting and Patching Form Values](#setting-and-patching-form-values)
      - [Accessing Form Values](#accessing-form-values)
      - [Resetting Form](#resetting-form)
    - [Reactive Forms](#reactive-forms)
      - [Setup](#setup)
      - [Creating Form in Code](#creating-form-in-code)
      - [Syncing HTML and Form](#syncing-html-and-form)
      - [Submitting Form](#submitting-form)
      - [Validations](#validations)
      - [Accessing Form Controls](#accessing-form-controls)
      - [Arrays of Form Controls](#arrays-of-form-controls)
      - [Custom Validators](#custom-validators)
        - [Sync Validators](#sync-validators)
        - [Async Validators](#async-validators)
      - [Error Codes](#error-codes)
      - [Value and Status Changes Observables](#value-and-status-changes-observables)
  - [Pipes](#pipes)
    - [Custom Pipe](#custom-pipe)
    - [Parametrizing Custom Pipe](#parametrizing-custom-pipe)
    - [Filter Pipe](#filter-pipe)
    - [Impure Pipe](#impure-pipe)
    - [Async Pipe](#async-pipe)
  - [HTTP Requests](#http-requests)
    - [Error Handling](#error-handling)
    - [Headers and Query Params](#headers-and-query-params)
    - [Observing Different Types of Responses](#observing-different-types-of-responses)
    - [Interceptors](#interceptors)
  - [Deployment](#deployment)

## CLI

- To create new Angular app using Angular CLI use `ng new app-name`.

- To start application use `ng serve` from the directory where Angular app is located.

## Modules

- Module in Angular is a way to bundle multiple components, services, directives together.

- When splitting application into multiple modules it is important to remember that each module has access only to the code that it is importing (configured via `@NgModule`). The only exception are the services need to be imported only once in the app module and then can be accessed in any other module.

- In non-main modules `BrowserModule` import changes into `CommonModule`.

### Shared Modules

- Shared modules allow for keeping parts of code used in multiple components in one place.

- When breaking the code into the structure with shared modules it is important to remember that modules can be declared only once but can be imported multiple times.

- When declaring a shared module we can import `CommonModule` inside of it and then export it and remove `CommonModule` from modules that import such shared module.

### Lazy Loading

- **Lazy loading** is a great way to optimize Angular application by limiting the web bundle computed and downloaded once certain route is accessed. Lazy loaded code is loaded once it is needed and requested by the client not before that.

- Note that lazy loading has the biggest effect when there are no commong library imports in lazy loaded modules.

- Lazy loading is done via `loadChildren` that should be added to the routing module. Remember to remove such module from the root imports:

```ts
const appRoutes: Routes = [
  { path: "", redirectTo: "/recipes", pathMatch: "full" },
  {
    path: "recipes",
    loadChildren: () =>
      import("./recipes/recipes.module").then(m => m.RecipesModule)
  }
]
```

- Lazy loaded modules can be pre-loaded which means that initial web bundle will be kept small, but subsequent modules (lazy loaded) will get fetched as soon as initial bundle gets downloaded:

```ts
// app-routing.module.ts

import { Routes, RouterModule, PreloadAllModules } from '@angular/router';
// ...
@NgModule({
  imports: [RouterModule.forRoot(appRoutes, { preloadingStrategy: PreloadAllModules })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
```

- Remember to never provide services in the eagerly loaded modules (in such cases service should be provided in the `AppModule`).

- Note that services provided in lazily loaded modules will get their own instance and will not use application wide instance.

- Be careful when providing services from eagerly loaded modules imported into the lazily loaded modules - such services will also get their own instance for lazily loaded module. This is because eagerly loaded module imported into the lazily loaded module will turn into lazily loaded module as well (in lazy loaded part of the code).

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

## Dynamic Components

- **Dynamic components** are components that are created during runtime.

- Easiest way of utilizing dynamic components is via `*ngIf` and it should be favoured unless it gets inconvinient.

- Creating dynamic component:

```ts
// dynamic component
import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-alert',
  templateUrl: './alert.component.html',
  styleUrls: ['./alert.component.css']
})
export class AlertComponent {
  @Input() message: string;
  @Output() close = new EventEmitter<void>();

  onClose() {
    this.close.emit();
  }
}

// supporting directive used to locate dynamic component inside the DOM
@Directive({
  selector: '[appPlaceholder]'
})
export class PlaceholderDirective {
  constructor(public viewContainerRef: ViewContainerRef) {}
}

// component creation
@Component({
  selector: 'app-auth',
  templateUrl: './auth.component.html'
})
export class AuthComponent implements OnDestroy {
  error: string = null;
  @ViewChild(PlaceholderDirective, { static: false }) alertHost: PlaceholderDirective;

private showErrorAlert(message: string) {
  // const alertCmp = new AlertComponent();
  const alertCmpFactory = this.componentFactoryResolver.resolveComponentFactory(
    AlertComponent
  );
  const hostViewContainerRef = this.alertHost.viewContainerRef;
  hostViewContainerRef.clear();

  const componentRef = hostViewContainerRef.createComponent(alertCmpFactory);

  componentRef.instance.message = message;
  this.closeSub = componentRef.instance.close.subscribe(() => {
    this.closeSub.unsubscribe();
    hostViewContainerRef.clear();
  });
}
```

## Standalone Components

- Both components and directives can be turned into standalone counterparts.

- If root module is turned into the standalone component bootstrapping needs to be implemented. Additionally, since there might be no modules in purely standalone application, global services can be defined in this bootstrap as well:

```ts
import { boostrapApplication }  from '@angular/platform-browser';

bootstrapApplication(AppComponent, {providers: [AnalyticsService]});
```

- To make standalone component aware of `router-outlet` and `routerLink` it needs to import `RouterModule`. To make it additionally aware of routes it needs to be bootstrapped with service routing service:

```ts
import { importProvidersFrom } from '@angular/core';
import { boostrapApplication }  from '@angular/platform-browser';
import { AppRoutingModule } from './app/app-routing.module';

bootstrapApplication(AppComponent, {providers: [importProvidersFrom(AppRoutingModule)]});
```

- To lazy load standalone component you need to use `loadComponent` syntax. `loadChildren` can still be used though:

```ts
const routes: Route[] = [
  {
    path: 'about',
    loadComponent: () => import('./about/about.component').then((mod) => mod.AboutComponent),
  },
]
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

- There is a new way of injecting services on the `AppModule` level that allows lazy loading:

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

- Remember that Angular will be served by the actual server hosting an Angular application. Because of this it needs to be configured in a way that when non-existing resource is requested it will load `index.html` so that Angular will handle route itself.

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

// Example with implemented user observable
@Injectable({ providedIn: 'root' })
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    router: RouterStateSnapshot
  ):
    | boolean
    | UrlTree
    | Promise<boolean | UrlTree>
    | Observable<boolean | UrlTree> {
    return this.authService.user.pipe(
      take(1),
      map(user => {
        const isAuth = !!user;
        if (isAuth) {
          return true;
        }
        return this.router.createUrlTree(['/auth']);
      })
      // tap(isAuth => {
      //   if (!isAuth) {
      //     this.router.navigate(['/auth']);
      //   }
      // })
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

### Passing Static Data to Route

- Static data can be passed to a route by using `data` attribute and passing desired object within it:

```ts
// In app-routing module
const appRoutes: Routes = [
  { path: 'not-found', component: ErrorPageComponent, data: {message: 'Page not found!'} },
];

// In error-page component
export class ErrorPageComponent implements OnInit {
  errorMessage: string;

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {
    // this.errorMessage = this.route.snapshot.data['message'];
    this.route.data.subscribe(
      (data: Data) => {
        this.errorMessage = data['message'];
      }
    );
  }
}
```

### Resolving Dynamic Data with Resolve Guard

- Resolver allows for fetching dynamic resource before route is loaded using route state:

```ts
// In app-routing module
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

// In server-resolver service
interface Server {
  id: number;
  name: string;
  status: string;
}

@Injectable()
export class ServerResolver implements Resolve<Server> {
  constructor(private serversService: ServersService) {}

  resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<Server> | Promise<Server> | Server {
    return this.serversService.getServer(+route.params['id']);
  }
}

// Server data accessed in server component
export class ServerComponent implements OnInit {
  server: {id: number, name: string, status: string};

  constructor(private serversService: ServersService,
              private route: ActivatedRoute) {}

  ngOnInit() {
    this.route.data
      .subscribe(
        (data: Data) => {
          this.server = data['server'];
        }
      );
  }
}
```

## Observables

- **Observables** are lazy Push collections of multiple values.

### How to Create Custom Observable

- Observables have 3 states that can be handled by observer (subscriber): `next`, `error`, and `complete`.

```ts
import { Observable } from 'rxjs';

const customIntervalObservable = Observable.create(observer => {
  let count = 0;
  setInterval(() => {
    observer.next(count);
    if (count === 5) {
      observer.complete();
    }
    if (count > 3) {
      observer.error(new Error('Count is greater 3!'));
    }
    count++;
  }, 1000);
});
```

- Observables can be filtered with the use of `pipe` and **operators**:

```ts
import { Observable } from 'rxjs';
import { map, filter } from 'rxjs/operators';

this.firstObsSubscription = customIntervalObservable.pipe(
  filter(data => {
    return data > 0;
  }),
  map((data: number) => {
    return 'Round: ' + (data + 1);
  })
).subscribe(data => {
    console.log(data);
  }, error => {
    console.log(error);
    alert(error.message);
  }, () => {
    console.log('Completed!');
  });
}
```

### Subjects

- More modern way (i.e. more efficient) to handle `EventEmitters` that emit events across different components (not using `Output()`) is to use `Subject`. Remember that subjects will not get automatically unsubscribed by Angular so this needs to be done explicitly inside `ngOnDestroy`:

```ts
// Inside the service class
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';

@Injectable({providedIn: 'root'})
export class UserService {
  activatedEmitter = new Subject<boolean>();
}

// In the component that emits an event
onActivate() {
  this.userService.activatedEmitter.next(true);
}

// In the component that subscribes to the Subject
import { Component, OnDestroy, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';

import { UserService } from './user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  userActivated = false;
  private activatedSub: Subscription;

  constructor(private userService: UserService) {
  }

  ngOnInit() {
    this.activatedSub = this.userService.activatedEmitter.subscribe(didActivate => {
      this.userActivated = didActivate;
    });
  }

  ngOnDestroy(): void {
    this.activatedSub.unsubscribe();
  }
}
```

- If one wants to unsubscribe automatically after a certain amount of received events it can be done with the combination of `pipe` and take`:

```ts
this.authService.user.pipe(take(1)).subscribe(user => {
  // ...
});
```

- We can pipe observables and merge them together using `exhaustMap`:

```ts
fetchRecipes() {
  return this.authService.user.pipe(
    take(1),
    exhaustMap(user => {  // If previous observable has completed it will be merged into the output observable
      return this.http.get<Recipe[]>(
        'http://example.com'
      );
    }),
    map(recipes => {
      return recipes.map(recipe => {
        return {
          ...recipe
        };
      });
    })
  )
}
```

### BehaviorSubject

- This type of subject allows for the same methods to be called as for the 'standard' subject, but emits the current value to new subscribers.

## Forms

- Angular provides 2 approaches to forms creations:

  - **template-driven** - Angular infers thee Form Object from the DOM
  - **reactive** - Form is created programmatically and then synchronized with the DOM

### Template-Driven Forms

- Remember to include `FormsModule` in the `import` inside `AppModule` to start using template-driven forms.

- To enable TD forms add `ngModel` directive and `name` attribute to HTML tag defining an input.

- To capture form submission add `(ngSubmit)` event to the `form` tag.

#### Accessing Form Object

- To get `NgForm` object created by Angular out of the form we pass local reference and assign `ngForm` value to it.

```HTML
<form (submit)="onSubmit(f)" #f="ngForm">
<!-- Alternative: <form (ngSubmit)="onSubmit(f)" #f="ngForm"> -->
  <div id="user-data">
    <div class="form-group">
      <label for="username">Username</label>
      <input type="text" id="username" class="form-control" name="username" ngModel>
    </div>
    <button class="btn btn-default" type="button">Suggest an Username</button>
    <div class="form-group">
      <label for="email">Mail</label>
      <input type="email" id="email" class="form-control" name="email" ngModel>
    </div>
  </div>
  <div class="form-group">
    <label for="secret">Secret Questions</label>
    <select id="secret" class="form-control" name="secret" ngModel>
      <option value="pet">Your first Pet?</option>
      <option value="teacher">Your first teacher?</option>
    </select>
  </div>
  <button class="btn btn-primary" type="submit">Submit</button>
</form>
```

```ts
// in function that triggers after `submit` event fired
onSubmit(form: NgForm) {
  console.log(form);
}
```

- `NgForm` can be also accessed by `ViewChild` which can be useful if we need to access form before it is being submitted:

```ts
@ViewChild('f') signupForm: NgForm;

onSubmit(form: NgForm) {
  console.log(this.signupForm);
}
```

#### Form Validation

- Validation can be added to form fields by using specifc directives e.g. `required` or `email` to the input HTML tags.

- Based on form's validation status different attributes mayb be applied to the element. We can for example disable submit button if form is invalid:

```HTML
<button class="btn btn-primary" type="submit" [disabled]="!f.valid">Submit</button>
```

- Angular automatically applies specific classes to the form fields based on their validity. Those classes can be styled as desired. For example below gives red border to the invalid input field (`ng-invalid`) but only if it has not been yet touched (`ng-touched`):

```CSS
input.ng-invalid.ng-touched {
  border: 1px solid red;
}
```

- By assigning `ngModel` to local reference on the input field we can further define other page elements based on the input's state, e.g. to display additional information block only when given input is invalid and has not been touched:

```HTML
<input type="email" id="email" class="form-control" name="email" email required ngModel #email="ngModel">
<span class="help-block" *ngIf="!email.valid && email.touched">Please enter a valid email!</span>
```

#### Form Default Values (Property Binding in Forms)

- You can use one-way property binding to define a default value for the form's field:

```HTML
<select id="secret" class="form-control" name="secret" required [ngModel]="defaultQuestion">
```

```ts
export class AppComponent {
  defaultQuestion = 'pet';
}
```

- Two-way binding can also be used if needed:

```HTML
<div class="form-group">
  <textarea name="questionAnswer" rows="3" [(ngModel)]="questionAnswer"></textarea>
  <p>Your reply: {{ questionAnswer }}</p>
</div>
```

```ts
export class AppComponent {
  questionAnswer = '';
}
```

#### Grouping Form Controls

- Form controls can be grouped together using `ngModelGroup` to define common validation, styling, etc. for multiple elements, e.g.:

```HTML
<div id="user-data" ngModelGroup="userData" #userData="ngModelGroup">
  <!-- ... -->
  <p *ngIf="!userData.valid && userData.touched">User data is invalid!</p>
</div>
```

#### Handling Radio Buttons

- Handle them like the rest:

```HTML
<div class="radio" *ngFor="let gender of genders">
  <label>
    <input
      type="radio"
      name="gender"
      ngModel
      [value]="gender"
    >
  {{ gender }}
  </label>
</div>
```

```ts
export class AppComponent {
  genders = ['male', 'female'];
}
```

#### Setting and Patching Form Values

- This can be done without any property binding using `NgForm` accessed by local reference using `ViewChild`.

- To override entire form use `setValue` from `NgForm`:

```ts
export class AppComponent {
  @ViewChild('f') signupForm: NgForm;

  suggestUserName() {
    const suggestedName = 'Superuser';
    this.signupForm.setValue(
      {
        userData: {
          username: suggestedName,
          email: 'test@gmail.com'
        },
        secret: 'pet',
        questionAnswer: '',
        gender: 'male'
      }
    );
  }
}
```

- To patch only specific value use `patchValue` from `NgForm.form`:

```ts
export class AppComponent {
  @ViewChild('f') signupForm: NgForm;

  suggestUserName() {
    const suggestedName = 'Superuser';
    this.signupForm.form.patchValue(
      {
        userData: {
          username: suggestedName
        }
      }
    );
  }
```

#### Accessing Form Values

- To access form values we just access `value` property of `NgForm`:

```ts
export class AppComponent {
  @ViewChild('f') signupForm: NgForm;
  user = {
    username: '',
    gender: ''
  };

  onSubmit() {
    // grouped form control
    this.user.username = this.signupForm.value.userData.username;
    this.user.gender = this.signupForm.value.userData.gender;
  }
```

#### Resetting Form

- To reset a form do below. You can also pass the same object as you would pass inside `setValue()` to `reset()` to reset the form to specific values:

```ts
export class AppComponent {
  @ViewChild('f') signupForm: NgForm;

  onSubmit() {
    this.signupForm.reset();
  }
```

### Reactive Forms

#### Setup

- In `app.module.ts` `ReactiveFormsModule` needs to be imported:

```ts
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  // ...
  imports: [
    ReactiveFormsModule,
  ],
})
```

- In the component itself use `FormGroup`:

```ts
import { FormGroup } from '@angular/forms';

// ...
export class AppComponent {
  signupForm: FormGroup;
}
```

#### Creating Form in Code

- Use `FormGroup` together with `FormControl` to define form fields. `FormControl` accepts default value and sync and async validators. It is safer to wrap field names in the quotation marks in this case:

```ts
import { FormControl, FormGroup } from '@angular/forms';

ngOnInit() {
  this.signupForm = new FormGroup({
    'username': new FormControl(null),
    'email': new FormControl(null),
    'gender': new FormControl('male'),
  });
}
```

#### Syncing HTML and Form

- To sync HTML form with `FormGroup` defined in TS pass created `FormGroup` object via `[formGroup]` attribute binding and bind each input via `formControlName` by its respective name in the `FormGroup` object:

```HTML
<form [formGroup]="signupForm">
  <div class="form-group">
    <label for="username">Username</label>
    <input
      type="text"
      id="username"
      formControlName="username"
      class="form-control">
  </div>
  <div class="form-group">
    <label for="email">email</label>
    <input
      type="text"
      id="email"
      formControlName="email"
      class="form-control">
  </div>
  <div class="radio" *ngFor="let gender of genders">
    <label>
      <input
        type="radio"
        formControlName="gender"
        [value]="gender">{{ gender }}
    </label>
  </div>
  <button class="btn btn-primary" type="submit">Submit</button>
</form>
```

#### Submitting Form

- We still use `(ngSubmit)` event to listen to form submission. The only difference is that we no longer use local reference to access form values, but we use defined `FormGroup` object instead.

#### Validations

- Validations are added via arguments in `FormControl` object:

```ts
this.signupForm = new FormGroup({
  'username': new FormControl(null, Validators.required),  // single validator
  'email': new FormControl(null, [Validators.required, Validators.email]),  // list of validators
});
```

#### Accessing Form Controls

- In HTML it is still possible to access attributes of a given form control when using reactive approach. This is done by referencing form control by its name or path (in case of nested form controls):

```HTML
<form [formGroup]="signupForm" (ngSubmit)="onSubmit()">
  <div class="form-group">
    <label for="username">Username</label>
    <input
      type="text"
      id="username"
      formControlName="username"
      class="form-control">
    <span class="help-block" *ngIf="!signupForm.get('username').valid && signupForm.get('username').touched">
      Please enter a valid username!
    </span>
  </div>
  <button class="btn btn-primary" type="submit" [disabled]="!signupForm.valid && signupForm.touched">Submit</button>
</form>
```

- For nested form controls:

```ts
ngOnInit() {
  this.signupForm = new FormGroup({
    'userData': new FormGroup({
      'username': new FormControl(null, Validators.required),
    }),
  });
}
```

```HTML
<form [formGroup]="signupForm" (ngSubmit)="onSubmit()">
  <div formGroupName="userData">
    <div class="form-group">
      <label for="username">Username</label>
      <input
        type="text"
        id="username"
        formControlName="username"
        class="form-control">
      <span class="help-block" *ngIf="!signupForm.get('userData.username').valid && signupForm.get('userData.username').touched">
        Please enter a valid username!
      </span>
    </div>
  </div>
  <button class="btn btn-primary" type="submit" [disabled]="!signupForm.valid && signupForm.touched">Submit</button>
</form>
```

#### Arrays of Form Controls

- In cases when we want to enable dynamically added form controls (e.g. based on the user's input) we can use `FormArray`:

```ts
ngOnInit() {
  this.signupForm = new FormGroup({
    // ...
    'hobbies': new FormArray([]),
  });
}

onAddHobby() {
  const control = new FormControl(null, Validators.required);
  (<FormArray>this.signupForm.get('hobbies')).push(control);
}

getHobbyControls() {
  return (<FormArray>this.signupForm.get('hobbies')).controls
}

// Alternatively for getHobbyControls we can use getter with type casting
get hobbyControls() {
  return (this.signupForm.get('hobbies') as FormArray).controls
}
```

```HTML
<div formArrayName="hobbies">
  <button class="btn btn-primary" (click)="onAddHobby()">Add Hobby</button>
  <div class="form-group" *ngFor="let hobbyControl of getHobbyControls(); index as i">
    <input type="text" class="form-control" [formControlName]="i">
  </div>
</div>
```

- To remove an element from `FormArray` use `removeAt(index)` method. To clear `FormArray` and remove all controls use `clear()` method.

#### Custom Validators

##### Sync Validators

- Custom validator is just a function checking whether provided `FormControl` instance is valid. Custom validator needs to return an object with an error code and its value (`true` or `null`):

```ts
ngOnInit() {
    this.signupForm = new FormGroup({
      'username': new FormControl(null, [this.forbiddenNames.bind(this)]),
    });
  }

forbiddenNames(control: FormControl): {[s: string]: boolean} {
  if (this.forbiddenUsernames.indexOf(control.value) !== -1) {
    return {'nameIsForbidden': true};
  }
  return {'nameIsForbidden': null}
  // return null;  // alternatively null can be returned
}
```

##### Async Validators

- Works like synchronous validators but returns promise or observable instead:

```ts
forbiddenNameAsync(control: FormControl): Promise<any> | Observable<any> {
  const promise = new Promise<any>(
    (resolve, reject) => {
      setTimeout(() => {
        if (control.value === 'Test') {
          resolve({'forbiddenName': true});
        } else {
          resolve(null);
        }
      }, 1500);
    }
  );
  return promise;
}
```

#### Error Codes

- Error codes can be verified on the level where validation is implemented:

```HTML
<span *ngIf="signupForm.get('userData.username').errors['nameIsForbidden']">
  Provided username is not allowed!
</span>
```

#### Value and Status Changes Observables

- One can subscribe to observables that indicate value or status change:

```ts
this.signupForm.valueChanges.subscribe(value => {
  console.log(value);
});
this.signupForm.statusChanges.subscribe(status => {
  console.log(status);
});
```

## Pipes

- Pipes are responsible for transforming the output without changing the original data source.

```HTML
<p>{{ someDate | date: 'fullDate' | uppercase }}</p>
```

- Pipes are parsed from left to right.

- [Available default Angular pipes](https://angular.io/api?type=pipe).


### Custom Pipe

- To create new custom pipe use `ng generate pipe` or `ng g p`.

- Example of custom pipe. Pipe needs to be added to declarations in `app.module.ts`:

```ts
// shorten.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'shorten'
})
export class ShortenPipe implements PipeTransform {
  transform(value: any) {
    if (value.lenth > 10) {
      return value.substr(0, 10) + '...';
    }
    return value;
  }
}
```

```HTML
<!-- page.html -->
<p>{{ someLongText | shorten }}</p>
```

### Parametrizing Custom Pipe

- Example of a custom parametrized pipe:

```ts
// shorten.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'shorten'
})
export class ShortenPipe implements PipeTransform {
  transform(value: any, limit: number) {
    if (value.lenth > limit) {
      return value.substr(0, 10) + '...';
    }
    return value;
  }
}
```

```HTML
<!-- page.html -->
<p>{{ someLongText | shorten:10 }}</p>
```

### Filter Pipe

- Note that filtering pipes can also be applied to `ngFor` items:

```ts
// filter.pipe.ts
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'filter'
})
export class ShortenPipe implements PipeTransform {
  transform(value: any, filterString: string, propName: string): any {
    if (value.lenth === 0) {
      return value
    }
    const resultArray = [];
    for (const item of value) {
      if (item.status[propName] === filterString) {
        resultArray.push(item);
      }
    }
    return resultArray;
  }
}
```

```HTML
<!-- page.html -->
<input type="text" [(ngModel)]="filteredStatus">
<li *ngFor="let server of servers | filter:filteredStatus:'status'></li>
```

### Impure Pipe

- Filtering pipes are not run every time the data changes. This means that in some cases data might not appear correctly (applicable objects might not be included by filtering pipe). To enforce re-application of filtering pipes we need to pass `pure: false` attribute in object passed as an argument to `Pipe` decorator:

```ts
@Pipe({
  name: 'filter'
  pure: false
})
```

### Async Pipe

- Pipe can be used to properly show given data whenever promise or observable are resolved:

```HTML
<p>{{ promiseOrObservable | async }}</p>
```

## HTTP Requests

- Angular makes requests using `HttpClientModule`. This needs to be added to `app.module.ts` as an import.

- It is a good practice to outsource API communication to a separate service.

- Example of POST and GET requests with typing and transforming response with `pipe`:

```ts
// Service
// ...
import { Post } from './post.model';

@Injectable({ providedIn: 'root' })
export class PostsService {
  error = new Subject<string>();

  constructor(private http: HttpClient) {}

  createAndStorePost(title: string, content: string) {
    const postData: Post = { title: title, content: content };
    this.http
      .post<{ name: string }>(
        'https://ng-complete-guide-c56d3.firebaseio.com/posts.json',
        postData,
        {
          observe: 'response'
        }
      )
      .subscribe(
        responseData => {
          console.log(responseData);
        },
        error => {
          this.error.next(error.message);
        }
      );
  }

  fetchPosts() { // One can subscribe to the results of this method and apply logic 
    let searchParams = new HttpParams();
    searchParams = searchParams.append('print', 'pretty');
    searchParams = searchParams.append('custom', 'key');
    return this.http
      .get<{ [key: string]: Post }>(
        'https://ng-complete-guide-c56d3.firebaseio.com/posts.json',
        {
          headers: new HttpHeaders({ 'Custom-Header': 'Hello' }),
          params: searchParams,
          responseType: 'json'
        }
      )
      .pipe(
        map(responseData => { // this is the map function from rxjs
          const postsArray: Post[] = [];
          for (const key in responseData) {
            if (responseData.hasOwnProperty(key)) {
              postsArray.push({ ...responseData[key], id: key });
            }
          }
          return postsArray;
        }),
        catchError(errorRes => {
          // Send to analytics server
          return throwError(errorRes);
        })
      );
  }
}
```

### Error Handling

- Errors can emit next subject and therefore can be subscribed to in other components:

```typescript
import { Injectable } from '@angular/core';
import { catchError } from 'rxjs/operators';
import { Subject } from 'rxjs';

import { Post } from './post.model';

@Injectable({ providedIn: 'root' })
export class PostsService {
  error = new Subject<string>();

  constructor(private http: HttpClient) {}

  createAndStorePost(title: string, content: string) {
    const postData: Post = { title: title, content: content };
    this.http
      .post<{ name: string }>(
        'https://ng-complete-guide-c56d3.firebaseio.com/posts.json',
        postData,
        {
          observe: 'response'
        }
      )
      .subscribe(
        responseData => {
          console.log(responseData);
        },
        error => {
          this.error.next(error.message);
        }
      );
  }
```

- Additional logic for error handling can be implemented by using `catchError` and `throwError`:

```typescript
import { map, catchError } from 'rxjs/operators';
// ...

  fetchPosts() {
    let searchParams = new HttpParams();
    searchParams = searchParams.append('print', 'pretty');
    searchParams = searchParams.append('custom', 'key');
    return this.http
      .get<{ [key: string]: Post }>(
        'https://ng-complete-guide-c56d3.firebaseio.com/posts.json',
        {
          headers: new HttpHeaders({ 'Custom-Header': 'Hello' }),
          params: searchParams,
          responseType: 'json'
        }
      )
      .pipe(
        map(responseData => {
          const postsArray: Post[] = [];
          for (const key in responseData) {
            if (responseData.hasOwnProperty(key)) {
              postsArray.push({ ...responseData[key], id: key });
            }
          }
          return postsArray;
        }),
        catchError(errorRes => {
          // Send to analytics server
          return throwError(errorRes);
        })
      );
  }
```

### Headers and Query Params

- Setting-up a header is done via `HttpHeaders` that takes an object of key-value pairs as an argument. Query params can be added using `HttpParams` object that also takes key-value pairs that translate into `key=value` string in the URL:

```typescript
fetchPosts() {
  let searchParams = new HttpParams();
  searchParams = searchParams.append('print', 'pretty');
  searchParams = searchParams.append('custom', 'key');
  return this.http
    .get<{ [key: string]: Post }>(
      'https://ng-complete-guide-c56d3.firebaseio.com/posts.json',
      {
        headers: new HttpHeaders({ 'Custom-Header': 'Hello' }),
        params: searchParams,
        responseType: 'json'
      }
    )
```

### Observing Different Types of Responses

- By default a body of a response is returned from the HTTP request. This can be changed by passing additional object to the HTTP request call:

```typescript
createAndStorePost(title: string, content: string) {
  const postData: Post = { title: title, content: content };
  this.http
    .post<{ name: string }>(
      'https://ng-complete-guide-c56d3.firebaseio.com/posts.json',
      postData,
      {
        observe: 'response' // full response object will be returned
      }
    )
```

- For very granular management of requests one can use `{observe: 'event'}`. This can be for example combined with `tap` that allows for executing an arbitrary code without changing the observable output:

```ts
deletePosts() {
    return this.http
      .delete('https://ng-complete-guide-c56d3.firebaseio.com/posts.json', {
        observe: 'events',
        responseType: 'text'
      })
      .pipe(
        // note that both ifs will get executed if request succeeds
        // but it will happen at two separate events being fired
        // and therefore tap will also get fired twice
        tap(event => {
          console.log(event);
          if (event.type === HttpEventType.Sent) { // request being sent
          }
          if (event.type === HttpEventType.Response) {
            console.log(event.body); // response received
          }
        })
      );
  }
```

### Interceptors

- **Interceptor** intercepts and handles an `HttpRequest` or `HttpResponse`. This can be for example used for attaching authorization token to each request that is made to the BE:

```ts
import {
  HttpInterceptor,
  HttpRequest,
  HttpHandler
} from '@angular/common/http';

export class AuthInterceptorService implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler) {
    const modifiedRequest = req.clone({ // needs to be cloned because HttpRequest is immutable
      headers: req.headers.append('Auth', 'xyz')
    });
    return next.handle(modifiedRequest);
  }
}
```

- In `app.module` interceptors need to be added as an array of providers":

```ts
providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptorService,
      multi: true
    }
  ],
```

- One can also intercept into the response. Note that inside the interceptor you will always get an event as a response:

```ts
export class LoggingInterceptorService implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler) {
    console.log('Outgoing request');
    console.log(req.url);
    console.log(req.headers);
    return next.handle(req).pipe( // tapping into the events (response)
      tap(event => {
        if (event.type === HttpEventType.Response) {
          console.log('Incoming response');
          console.log(event.body);
        }
      })
    );
  }
}
```

## Deployment

- `ng build` to build production files.

- Serve compiled static files via CDN or S3. Remember to configure server so that it always serves `index.html` so that routing can be handled by Angular itself.
