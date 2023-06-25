# Software Architecture

## ToC

- [Software Architecture](#software-architecture)
  - [ToC](#toc)
  - [Scalability (CS75 Harvard)](#scalability-cs75-harvard)
    - [Vertical Scaling](#vertical-scaling)
    - [Horizontal Scaling](#horizontal-scaling)
    - [RAID](#raid)
    - [DB Scaling](#db-scaling)
    - [Load Balancing](#load-balancing)
    - [Caching](#caching)
  - [Software Architecture Patterns](#software-architecture-patterns)
    - [Layered Pattern](#layered-pattern)
    - [Event-Driven Pattern](#event-driven-pattern)
      - [Mediator Topology](#mediator-topology)
      - [Broker Topology](#broker-topology)
    - [Microkernel Architecture Pattern](#microkernel-architecture-pattern)
    - [Microservices Architecture Pattern](#microservices-architecture-pattern)
      - [Avoid Dependencies and Orchestration](#avoid-dependencies-and-orchestration)
    - [Space-Based Architecture Pattern](#space-based-architecture-pattern)

## Scalability (CS75 Harvard)

- Resources:
  - [CS75 (Summer 2012) Lecture 9 Scalability Harvard Web Development David Malan](https://www.youtube.com/watch?v=-W9F__D3oY4)

### Vertical Scaling

- Easiest way of scaling by adding additional resources to the server/machine. The limitations are the best specs that you can get for the server.

### Horizontal Scaling

- Scaling by adding additional servers/machines. In this case between client and the server an orchestrator needs to be added - usually a **load balancer**.
- Easiest algorithm for load balancer is a **round-robin**. It can be implemented at least in two ways:
  1. DNS round-robin where load balancer resolves DNS lookup providing IP of a next-in-line server. This response (IP) will most likely be cached by the client and therefore, with some bad luck involved, we might end up with multiple users who generate heavy load on the same server without real way to balance the load across other machines.
  2. Round-robin with a load balancer that acts as a **reverse proxy** and redirects user requests to a different server each time. This will work only for stateless connections. In case of stateful connections additional binding needs to be used that matches user with a certain server for a defined time, but this poses same issues as in point 1.

### RAID

- RAID is a data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both.

- RAID 0 - (striping) faster read and write operations

- RAID 1 - redundancy of data

- RAID 5 - striping + redundancy (single hard drive failure is OK)

- RAID 6 - striping + redundancy (2 hard drives failure are OK)

- RAID 10 - RAID 1 + RAID 0 -> striping + redundancy

### DB Scaling

- **Master - Slave replication** is a replication model where there is only one primary database called the Master and several secondary databases called slaves. Write and update operations can only be performed on the master database but read operations can be performed on the slave databases as well. This model is best when you have to do a lot of read operations but only a few write operations.

- **Master - Master replication** is a replication model in which all DB nodes are primary. That is all the databases can be read from and written to. Each database propagates its changes to every other database replica so that the system stays consistent.

- DB partitioning helps with read operations if no joins between DBs are required. In basic form it means storing the same type of data divided between different DB nodes (e.g. users with A-D name would be the 1st node and users with E-H name would be the 2nd node and so on). It helps with dividing the load between DB instances.

### Load Balancing

- Can be done both on Web -> Server (BE) layer and Server -> DB layer. It is best to have redundant solution that involves 2 load balancer on each layer.

- Load balancer can take over applying additional security layer to the data sent to the clients (e.g. via SSL). Internal communication between the nodes behind load balancer can take place in plain protocols without additional encryption and overhead.

### Caching

- Basically, an in-memory map of key-value pairs that enable fast data retrieval. Cached data usually have some expiry date after which it will be removed or will be removed once new data will require additional memory.

## Software Architecture Patterns

- Resources:
  - Software Architecture Patterns (Mark Richards, O'Reilly)

### Layered Pattern

- In the **layered architecture**, the application is divided into horizontal layers, with each layer having a specific responsibility and interacting with adjacent layers in a predefined manner. The common layers typically found in a layered architecture are:

  - **Presentation Layer**: This layer is responsible for handling user interactions and displaying the user interface. It encapsulates the logic related to user input, presentation logic, and data formatting. It communicates with the underlying layers to fetch or update data.

  - **Business Logic Layer**: Also known as the domain layer or the service layer, this layer contains the core business logic and rules of the application. It handles data validation, business workflows, and complex operations. It acts as an intermediary between the presentation layer and the data access layer.

  - **Data Access Layer**: The data access layer is responsible for interacting with the underlying data sources, such as databases or external APIs. It provides methods for retrieving, updating, and deleting data. The layer abstracts the specific data storage technology and provides a standardized interface for accessing data.

- Changes in one layer have **no or minimal impact on other layers**, facilitating easier maintenance and future enhancements.

- All of the standard layers are defined as **closed layers** meaning the request needs to get pass through them each time before reaching next layer. In this pattern there might be additional, shared services like layers, that should be defined as **open layers** and could be skipped during request flow.

### Event-Driven Pattern

- The **Event-Driven Pattern** is a software architectural pattern that focuses on handling and responding to events that occur within a system. It is commonly used in systems where the occurrence of events plays a significant role and requires real-time processing or asynchronous communication.

- In this pattern, the system is designed around the concept of events, which represent significant changes or occurrences within the system. Events can be triggered by user actions, external inputs, or internal processes. They are typically categorized into different types or classes to facilitate event handling and processing.

- The architecture of an Event-Driven system typically consists of **three main components: event producers, event consumers, and an event bus or message broker**.

  - **Event producers** are responsible for generating and emitting events when specific actions or conditions occur. They publish events to the event bus or message broker, which acts as a central communication channel for distributing events to interested consumers.

  - **Event consumers**, also known as subscribers or listeners, are components that register their interest in specific types of events. They subscribe to the event bus or message broker and receive relevant events when they occur. Consumers can perform various actions in response to events, such as updating the system state, triggering additional processes, or sending notifications.

  - **Event bus** or message broker acts as a decoupling mechanism, allowing event producers and consumers to interact without direct dependencies. It ensures that events are delivered to the appropriate consumers based on their subscriptions. The event bus can provide additional features such as event buffering, event filtering, and event replay for fault tolerance.

- The Event-Driven Pattern offers several advantages. It promotes loose coupling between components, making the system more modular and easier to maintain. It enables real-time processing and responsiveness to events, allowing systems to handle high volumes of concurrent events efficiently. It also supports scalability and extensibility, as new event producers or consumers can be added without major modifications to the existing components.

- Event-Driven architectures are commonly used in various domains, including event-driven systems, event-driven user interfaces, message-driven middleware, and reactive programming. They are particularly suitable for systems that need to react to asynchronous events and maintain responsiveness in distributed or complex environments.

#### Mediator Topology

- The **Mediator topology** involves a central component known as the mediator, which acts as a coordinator or facilitator for event communication between multiple components. In this topology, individual components do not directly communicate with each other but instead interact with the mediator.

- When an event occurs, the components notify the mediator, which then decides how to handle the event and which components should receive it. The mediator can perform various tasks, such as filtering, transforming, or aggregating events before forwarding them to the appropriate components. It encapsulates the complex event handling logic, relieving individual components from having to handle event coordination and interaction.

- The Mediator topology promotes loose coupling between components since they don't have direct knowledge or dependencies on each other. It enhances system maintainability and flexibility, as individual components can be modified or added without affecting the entire system.

#### Broker Topology

- The **Broker topology**, also known as the Message Broker topology, involves the use of a central message broker or event bus as an intermediary for event communication. In this topology, event producers publish events to the message broker, and event consumers subscribe to specific types of events they are interested in.

- The message broker acts as a central hub, receiving events from producers and distributing them to relevant consumers based on their subscriptions. It maintains a list of subscribers and handles the routing and delivery of events. The broker may also provide additional features like event buffering, event persistence, and guaranteed event delivery.

- The Broker topology provides a decoupled communication mechanism, enabling event producers and consumers to operate independently without direct knowledge of each other. It supports scalability and extensibility, as new producers or consumers can be added without affecting existing components. Additionally, the broker can enable various messaging patterns like publish-subscribe, point-to-point, or request-reply.

### Microkernel Architecture Pattern

- The **Microkernel Architecture Pattern** (**Plug-in Architecture Pattern**), is a software architectural pattern that focuses on minimizing the core functionality of a system while delegating non-essential features to optional modules or plugins. The pattern aims to achieve flexibility, extensibility, and maintainability by keeping the core of the system lean and allowing for easy customization and addition of functionality.

- In the Microkernel pattern, the core of the system, often referred to as the microkernel, provides only essential services such as basic communication, low-level process management, and resource allocation. The microkernel is kept minimal and independent of domain-specific or application-specific functionality.

- Additional features and functionalities are implemented as separate modules or plugins that interact with the microkernel through well-defined interfaces. These modules, also known as plug-ins or extensions, encapsulate specific functionality and can be dynamically loaded or unloaded at runtime. Each module focuses on a specific domain or non-essential feature, such as user interface, networking, database access, or specific business logic.

- The Microkernel pattern promotes loose coupling between the core system and the modules by relying on well-defined interfaces and protocols for communication. The core system remains agnostic of the specific functionalities provided by the modules, allowing for easy replacement or addition of modules without affecting the overall system.

- Benefits of the Microkernel Architecture Pattern include:

  - Flexibility and extensibility: The pattern allows for easy customization and addition of functionality through the use of independent modules. New features can be added or removed without modifying the core system.

  - Maintainability: By keeping the core system minimal and focused on essential services, the pattern promotes code maintainability and reduces the impact of changes to the system.

  - Reusability: Modules can be reused across different systems that utilize the same microkernel, promoting code reuse and modularity.

  - Scalability: The pattern supports scalability by allowing the system to scale vertically by adding or removing modules as needed but it does not support horizontal scaling as such. When combined with other patterns it might offer some scalability though.

- However, it's important to consider that implementing the Microkernel pattern can introduce additional complexity due to the need for proper module management, communication protocols, and interfaces. The pattern is best suited for systems that require frequent customization or have a need for easily replaceable or extendable components.

### Microservices Architecture Pattern

- The **Microservices Architecture Pattern** is a software architectural pattern that structures an application as a collection of small, loosely coupled, and independently deployable services. Each service in a microservices architecture is designed to perform a specific business capability and can be developed, deployed, and scaled independently of other services. These services communicate with each other through lightweight protocols, such as HTTP or messaging systems, and often use APIs or contracts for interaction.

- Key characteristics of the Microservices Architecture Pattern include:

  - Service autonomy: Each microservice is developed and maintained by a small, cross-functional team, providing a high degree of ownership and autonomy. This allows teams to independently develop, deploy, and scale their services without dependencies on other teams.

  - Independent deployment: Microservices can be deployed and updated independently, enabling continuous delivery and faster time-to-market for specific services or features. This also allows for easier rollbacks and mitigates the risk of impacting the entire system during deployments.

  - Loose coupling and bounded contexts: Services are designed to be loosely coupled, with clear boundaries and well-defined interfaces. They can be implemented using different technologies, databases, or frameworks based on their specific requirements. Each service encapsulates a specific business capability or domain, ensuring a separation of concerns.

  - Scalability and fault isolation: Services can be scaled independently based on their individual resource demands, allowing for better resource utilization. Additionally, failures or issues in one service typically do not affect the overall system, as services are isolated and can gracefully degrade or fail without impacting the entire application.

- Benefits of the Microservices Architecture Pattern include:

  - Agility and scalability: The pattern enables faster development, deployment, and scaling of services, promoting agility and scalability in complex applications.

  - Flexibility and technology diversity: Each microservice can use the most appropriate technology stack for its specific requirements, allowing for technology diversity and innovation within the system.

  - Resilience and fault tolerance: Failure in one microservice doesn't bring down the entire system, improving fault tolerance and overall system resilience.

  - Continuous delivery and DevOps: The pattern aligns well with DevOps practices and enables continuous delivery by supporting independent deployment and automated release processes for each service.

- However, it's important to consider that implementing the Microservices Architecture Pattern introduces challenges in areas such as service coordination, data consistency, inter-service communication, and managing distributed systems complexity. Organizations need to carefully consider factors such as team structure, service boundaries, communication protocols, and monitoring when adopting this pattern.

#### Avoid Dependencies and Orchestration

- In microservices architecture, if you find you need to orchestrate your service components from within the user interface or API layer of the application, then chances are your service components are too fine-grained. Similarly, if you find you need to perform inter-service communication between service components to process a single request, chances are your service components are either too fine-grained or they are not partitioned correctly from a business functionality standpoint.

- Inter-service communication, which could force undesired couplings between components, can be handled instead through a shared database. For example, if a service component handing Internet orders needs customer information, it can go to the database to retrieve the necessary data as opposed to invoking functionality within the customer-service component.

- The shared database can handle information needs, but what about shared functionality? If a service component needs functionality contained within another service component or common to all service components, you can sometimes copy the shared functionality across service components (thereby violating the DRY principle: don’t repeat yourself). This is a fairly common practice in most business applications implementing the microservices architecture pattern, trading off the redundancy of repeating small portions of business logic for the sake of keeping service components independent and separating their deployment. Small utility classes might fall into this category of repeated code.

### Space-Based Architecture Pattern

- The **Space-Based Architecture (SBA) Pattern**, also known as the Tuple Space or Linda-style model, is a software architectural pattern that focuses on distributing and managing data or information across a network of interconnected nodes. The pattern is designed to handle high volumes of data and provide scalability, fault-tolerance, and responsiveness in distributed systems.

- In the Space-Based Architecture pattern, the central concept is the shared data space, often referred to as the "space" or "tuple space." The space is a distributed, in-memory data store that holds data objects or tuples. Tuples typically consist of structured or semi-structured data and are stored in a key-value fashion. The space allows for efficient and concurrent access to data.

- The main components of the Space-Based Architecture pattern are as follows:

  - Space: The shared data space serves as a distributed, scalable, and fault-tolerant repository for storing tuples. It can be partitioned or replicated across multiple nodes in a network to handle high loads and ensure availability. The space provides operations for storing, retrieving, updating, and removing tuples.

  - Producers: Producers are components or processes responsible for generating or updating tuples and storing them in the shared space. Producers can be distributed across different nodes and can concurrently write to the space.

  - Consumers: Consumers are components or processes that retrieve tuples from the shared space based on their criteria or interests. Consumers can perform actions on the retrieved tuples, such as processing, analyzing, or displaying the data. Multiple consumers can concurrently read from the space.

  - Event-driven processing: The Space-Based Architecture pattern often incorporates event-driven processing, where producers and consumers can be triggered by events or changes in the shared space. Events can notify consumers of the availability of new tuples or specific changes in the space.

- The Space-Based Architecture pattern offers several advantages:

  - Scalability: The pattern allows for horizontal scalability by distributing the shared space across multiple nodes, enabling the system to handle high data loads and accommodate increasing demands.

  - Fault-tolerance: By replicating or partitioning the shared space, the pattern provides fault-tolerance and resilience to node failures. If one node fails, the data can still be accessed from other nodes.

  - Loose coupling: The pattern promotes loose coupling between producers and consumers by relying on the shared space as an intermediary. Producers and consumers do not need to be aware of each other's existence, improving system modularity and flexibility.

  - Real-time data processing: The pattern supports real-time processing of data by allowing consumers to retrieve and process tuples as soon as they become available in the shared space.

- The Space-Based Architecture pattern is commonly used in scenarios that require distributed data processing, high scalability, and fault-tolerance. It finds applications in various domains, including big data analytics, event-driven systems, and distributed computing.
