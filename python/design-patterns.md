
## Table of Contents

- [Table of Contents](#table-of-contents)
- [Sources](#sources)
- [Design Patterns](#design-patterns)
  - [Creational Patterns](#creational-patterns)
    - [Factory Method](#factory-method)
    - [Abstract Factory](#abstract-factory)
    - [Builder](#builder)
    - [Singleton](#singleton)
    - [Prototype](#prototype)
  - [Structural Patterns](#structural-patterns)

## Sources

- [Refactoring Guru](https://refactoring.guru/design-patterns/catalog)

## Design Patterns

**Design patterns** are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code. The pattern is not a specific piece of code, but a general concept for solving a particular problem. While an algorithm always defines a clear set of actions that can achieve some goal, a pattern is a more high-level description of a solution.

### Creational Patterns

**Creational Patterns** these patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

#### Factory Method

- **Factory Method** should be used in every situation where an application (client) depends on an interface (product) to perform a task and there are multiple concrete implementations of that interface. You need to provide a parameter that can identify the concrete implementation and use it in the creator to decide the concrete implementation.

- Advantages of using Factory method:
  - We can easily add the new types of products without disturbing the existing client code.
  - Generally, tight coupling is being avoided between the products and the creator classes and objects.

- Disadvantages of using Factory method:
  - To create a particluar concrete product object, client might have to sub-class the creator class.
  - You end up with huge number of small files i.e, cluttering of the files.

- Abstract product creation method (interface) -> concrete product creation methods -> abstract product (interface) -> concrete products

#### Abstract Factory

- **Abstract Factory** is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

- Client will not have to know what factory method or what product family he is operating on as all of them will have the same interface.

- This is basically a factory method, but concrete product creators are replaced with concrete products creators that create multiple products for a specific product family (for example buttons/checkboxes for Windows/Mac/Web UI families).

- Abstract factory creation method (interface) -> concrete factory creation methods -> products creation methods (within the factories) -> abstract products (interfaces) -> concrete products

#### Builder

- **Builder** is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

- Builder design pattern is especially useful in cases where there is a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Approaching such problem with **subclasses** may become very hard to manage and hard to refactor. Using a **single constructor** with all possible parameters that control the object creation will stop breeding subclasses, but the constructor calls will become bloated and ugly.

- Builder patters suggests extraction of the object construction code out of its own class and move it to separate objects called **builders**. The pattern organizes object construction into a set of steps (`buildWalls`, `buildDoor`, etc.). To create an object, you execute a series of these steps on a builder object. The important part is that you don’t need to call all of the steps. You can call only those steps that are necessary for producing a particular configuration of an object.

- Some of the construction steps might require different implementation when you need to build various representations of the product. For example, walls of a cabin may be built of wood, but the castle walls must be built with stone. In this case, **you can create several different builder classes that implement the same set of building steps, but in a different manner**. Then you can use these builders in the construction process (i.e., an ordered set of calls to the building steps) to produce different kinds of objects.

- You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called **director**. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.

#### Singleton

- **Singleton** is a creational design pattern, which ensures that only one object of its kind exists and provides a single point of access to it for any other code. It is not recommended to be used in Python and it should be replaced with a class instance assigned to a global variable.

- Below, ```super(Singleton, cls).__call__``` (also ```super()``` implicitly) means that ```Singleton``` determines that the starting point in **Method Resolution Order (MRO)** will be a ```Singleton``` class, but MRO from the passed *cls* (```Singleton```) will be used. This concludes in the ```super()``` calling a standard ```__call__``` method that is inherited from the main metaclass of all classes - ```type```. ```super()``` already passes ```Singleton``` clas in ```self```/```cls``` argument implicitly.

```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
        
class Logger(metaclass=Singleton):
    pass
```

#### Prototype

- **Prototype** is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

- Python provides its own interface of Prototype via `copy.copy` and `copy.deepcopy` functions. And any class that wants to implement custom implementations have to override `__copy__` and `__deepcopy__` member functions.

- Good to remember that `__dict__` is implemented by default and it outputs all of the attributes of a given object.

### Structural Patterns

- PLACEHOLDER
- 