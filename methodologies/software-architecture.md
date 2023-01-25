# Software Architecture

## ToC

- [Software Architecture](#software-architecture)
  - [ToC](#toc)
  - [Scalability (CS75 Harvard)](#scalability-cs75-harvard)
    - [Vertical Scaling](#vertical-scaling)
    - [Horizontal Scaling](#horizontal-scaling)
    - [DB Scaling](#db-scaling)

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

### DB Scaling

- 
