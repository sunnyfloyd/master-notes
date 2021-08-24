# Backend Topics

- [Backend Topics](#backend-topics)
  - [Networking](#networking)
    - [HTTP](#http)
      - [E-Tags](#e-tags)
    - [OSI (Open Systems Interconnection) Model](#osi-open-systems-interconnection-model)
    - [TCP vs UDP](#tcp-vs-udp)
      - [TCP](#tcp)
      - [UDP](#udp)
    - [Bi-directional Connection](#bi-directional-connection)
      - [WebSockets](#websockets)
      - [WebRTC](#webrtc)
      - [WebTransport](#webtransport)

## Networking

### HTTP

- [Source](https://www.youtube.com/watch?v=0OrmKCB0UrQ)

- **Hypertext Transfer Protocol (HTTP)** is an application-layer protocol for transmitting hypermedia documents, such as HTML. It is built on top of TCP/IP communication protocol. HTTP/2 over **QUIC** (HTTP/3) uses UDP communication protocol.

- HTTP uses **client-server** or **request-response architecture**. Client is anything that makes a HTTP request (mostly browser). Server is the endpoint that can process this HTTP request.

- HTTP request consists of (among other optional stuff):

  - URL
  - Method type (GET, POST, PUT, DELETE)
  - Headers (content type, cookies, host)
  - Body (certain methods use this)

- HTTP Response:

  - Status code
  - Headers (content type, cookies)
  - Body

- **HTTPS** is a HTTP over TLS that encrypts the request/response at the presentation layer. In order to establish a connection via HTTPS a **handshake** needs to happen first. A handshake negotiates a cipher suites between client and a server and using asymmetrical encryption (public key) private key is shared for future (symmetrical) encryption.

- HTTP 1.0 established a *standard* where each HTTP connection had to be immediately closed after a server's response was received by a client (mostly due to the memory limitations as each connection requires some memory allocation):

  - new TCP connection with each request
  - slow
  - buffering

- HTTP 1.1 uses **Kepp-Alive** header so that instead of opening and closing connection for each request client may indicate how the connection may be used to set a timeout and a maximum amount of requests:

  - persisted TCP connection
  - low latency
  - streaming with chunked transfer
  - pipelining (disabled by default)
  - caching (with E-Tags)

- 

#### E-Tags

- [Source](https://www.youtube.com/watch?v=TgZnpp5wJWU)

### OSI (Open Systems Interconnection) Model

[Source](https://www.youtube.com/watch?v=7IS7gigunyI)

- OSI Model is a conceptual framework used to describe the functions of a networking system. Any device that communicates with other device is operating based on this framework. OSI model itself in its characterisation of the communication functions does not refer to the underlying internal structure or technology.

- OSI model has 7 abstract layers and communication goes both ways:

  - application layer to physical layer called **encapsulation**
  - physical layer to application layer called **decapsulation**.

- **Protocol Data Unit** (PDU) is a data that is being prepared by 3 layers: application (prepares application flows), presentation (f.e. encryption in HTTPS), session (establishes session).

- **Transport** layer create segments adding port (source and destination) to each segment to identify to what application given data is addressed (in most cases done by TCP protocol).

- **Network** layer creates packets adding source and destination addresses (sender and receiver IP addresses).

**Data Link** layer creates frames (only layer where header and trailer are present) and uses **Ethernet** as a standard to conver logical stuff into a physical stuff. Ethernet has source and destination addresses as well, but those are physical (MAC address).

- **Physical** layer transfers Bits into signal and carries them.

- Important thing about communication in the Internet is that all of the endpoints connected to the same access point will receive all of the information that is sent and received in this network. It means that data link layer is responsible to determine whether given data is addressed to this device and act accordingly. In some cases MAC address may point to an access point like router, but might be addressed in the network layer to other device using IP address.

### TCP vs UDP

- TCP and UDP are communication protocols that allow to send and receive data in a network. They are part of **transport layer** in OSI model (layer 4).

- **Internet Protocol** (IP) address is the identifier that allows information to be sent between devices on a network. Each device might run multiple application and that is why **ports** are required. They help to identify specifc application from and to data is sent.

#### TCP

- **Transmission Control Protocol (TCP)**

- **Pros**:
  - **acknowledgement** - clients talk to each other and ensure that sent data has been received
  - **guaranteed delivery** - resending undelivered/corrupted packets
  - **connection based** - clients need to establish a connection before sending an actual data (**stateful connection**)
  - **congestion control** - managing the flow of data depending on current network capacity
  - **ordered packets**.

- **Cons**:
  - **larger packets** - TCP adds lot of overhead (packet headers)
  - **more bandwidth**
  - **slower than UDP**
  - **stateful**
  - **server memory (DOS)** - server needs to allocate memory for each connection; for example, if one client sends multiple requests and do not confirm whether it received a response it might bloat the server's memory.

#### UDP

- **User Datagram Protocol (UDP)**

- **Pros**:
  - **smaller packets**
  - **less bandwidth** - this is why it is often used in online games. However, this is then often implemented in the form of **reliable UDP** that implements some overhead, but on the higher (application) level
  - **faster than TCP**
  - **stateless**.

- **Cons**:
  - **no acknowledgement**
  - **no guranteed delivery**
  - **connectionless**
  - **no congestion control** - UDP does not care about network capacity
  - **no ordered packets**
  - **security** - since there is no connection server does not know who is sending the data; this is why UDP is often blocked in the firewalls.

### Bi-directional Connection

- [Source](https://www.youtube.com/watch?v=2Nt-ZrNP22A)

#### WebSockets

- The **WebSocket API** (WebSockets) is an advanced technology that makes it possible to open a two-way interactive communication session between the user's browser and a server. With this API, you can send messages to a server and receive event-driven responses without having to poll the server for a reply.

- **Socket.IO** enables real-time, bidirectional and event-based communication. It is more advanced websockets implementation.

#### WebRTC

- **WebRTC** provides real-time communication capabilities to the application that works on top of an open standard. It supports video, voice, and generic data to be sent between peers, allowing developers to build powerful voice- and video-communication solutions. The technology is available on all modern browsers as well as on native clients for all major platforms.

- The WebRTC standard covers, on a high level, two different technologies: **media capture devices** and **peer-to-peer connectivity**.

#### WebTransport

- **WebTransport** is a web API that uses the HTTP/3 protocol as a bidirectional transport. It's intended for two-way communications between a web client and an HTTP/3 server. It supports sending data both unreliably via its datagram APIs, and reliably via its streams APIs.
