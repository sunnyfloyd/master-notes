
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
    - [Adapters](#adapters)
    - [Decorator](#decorator)
    - [Bridge](#bridge)
    - [Proxy](#proxy)
    - [Facade](#facade)
    - [Composite](#composite)
    - [Flyweight](#flyweight)

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

- Builder patterns suggests extraction of the object construction code out of its own class and move it to separate objects called **builders**. The pattern organizes object construction into a set of steps (`buildWalls`, `buildDoor`, etc.). To create an object, you execute a series of these steps on a builder object. The important part is that you don’t need to call all of the steps. You can call only those steps that are necessary for producing a particular configuration of an object.

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

- Python provides its own interface of Prototype via `copy.copy` and `copy.deepcopy` functions. Any class that wants to implement custom implementations have to override `__copy__` and `__deepcopy__` member functions.

- Good to remember that `__dict__` method is implemented by default and it outputs all of the attributes of a given object.

### Structural Patterns

- **Structural patterns** explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

#### Adapters

- **Adapter** is a structural design pattern that allows objects with incompatible interfaces to collaborate.

- The Adapter pattern lets you create a middle-layer class that serves as a translator between your code and a legacy class, a 3rd-party class or any other class with a weird interface.

- Use the Adapter class when you want to use some existing class, but its interface isn’t compatible with the rest of your code.

- Use the pattern when you want to reuse several existing subclasses that lack some common functionality that can’t be added to the superclass.

- This approach is very similar to the **Decorator pattern**. However, decorator enhances an object without changing its interface. In addition, decorator supports recursive composition, which isn’t possible when you use Adapter.

- There are two main possibilities to create an adapter class: **using inheritance** or **using object composition**:

```py
# Using Inheritance
class Target:
    """
    The Target defines the domain-specific interface used by the client code.
    """

    def request(self) -> str:
        return "Target: The default target's behavior."

class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"

class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"

# Using Object Composition
class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via composition.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"
```

#### Decorator

- **Decorator** is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

- Using decorators you can wrap objects countless number of times since both target objects and decorators follow the same interface. The resulting object will get a stacking behavior of all wrappers.

#### Bridge

- **Bridge** is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

- Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).

- Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.

- Use the Bridge if you need to be able to switch implementations at runtime.

#### Proxy

- **Proxy** is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

- Adapter provides a different interface to the wrapped object, Proxy provides it with the same interface, and Decorator provides it with an enhanced interface.

- Facade is similar to Proxy in that both buffer a complex entity and initialize it on its own. Unlike Facade, Proxy has the same interface as its service object, which makes them interchangeable.

- Decorator and Proxy have similar structures, but very different intents. Both patterns are built on the composition principle, where one object is supposed to delegate some of the work to another. The difference is that a Proxy usually manages the life cycle of its service object on its own, whereas the composition of Decorators is always controlled by the client.

#### Facade

- **Facade** is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

- Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem.

#### Composite

- **Composite** is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

- Use the Composite pattern when you have to implement a tree-like object structure. The Composite pattern provides you with two basic element types that share a common interface: simple leaves and complex containers. A container can be composed of both leaves and other containers. This lets you construct a nested recursive object structure that resembles a tree.

- Use the pattern when you want the client code to treat both simple and complex elements uniformly. All elements defined by the Composite pattern share a common interface. Using this interface, the client doesn’t have to worry about the concrete class of the objects it works with.


#### Flyweight

- The **Flyweight** pattern has a single purpose: minimizing memory intake. If your program doesn’t struggle with a shortage of RAM, then you might just ignore this pattern for a while.

- Flyweight can be recognized by a creation method that returns cached objects instead of creating new.

### Behavioural Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

#### Chain of Responsibility
- **Chain of Responsibility** is a behavioral design pattern that lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

#### Command
- **Command** is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you pass requests as a method arguments, delay or queue a request’s execution, and support undoable operations.
