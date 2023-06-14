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
