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