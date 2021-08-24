# Backend Topics

- [Backend Topics](#backend-topics)
  - [Networking](#networking)
    - [HTTP](#http)
      - [HTTP 1.0](#http-10)
      - [HTTP 1.1](#http-11)
      - [HTTP/2](#http2)
      - [HTTP/2 over QUIC (HTTP/3)](#http2-over-quic-http3)
      - [Multiplexing](#multiplexing)
      - [HTTP E-Tags](#http-e-tags)
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

- HTTP is stateless, but under the hood it is stateful since it uses TCP/IP protocol.

- **HTTPS** is a HTTP over TLS that encrypts the request/response at the presentation layer. In order to establish a connection via HTTPS a **handshake** needs to happen first. A handshake negotiates a cipher suites between client and a server and using asymmetrical encryption (public key) private key is shared for future (symmetrical) encryption.

#### HTTP 1.0

- HTTP 1.0 established a *standard* where each HTTP connection had to be immediately closed after a server's response was received by a client (mostly due to the memory limitations as each connection requires some memory allocation):

  - new TCP connection with each request
  - slow
  - buffering

#### HTTP 1.1

- **HTTP 1.1** uses **Kepp-Alive** header so that instead of opening and closing connection for each request client may indicate how the connection may be used to set a timeout and a maximum amount of requests:

- HTTP/1.1 does not allow sending of multiple messages. Once a HTTP/1.1 message is sent, no other message can be sent on that connection until that message is returned in full (ignoring the badly supported pipelining concept). This means **HTTP/1.1 is basically synchronous** and, if the full bandwidth is not used and other HTTP messages are queued, then it wastes any extra capacity that could be used on the underlying TCP connection. To get around this, more TCP connections can be opened, which basically allows HTTP/1.1 to act like a (limited) multiplexed protocol. If the network bandwidth was fully utilised then those extra connections would not add any benefit - it’s the fact there is capacity and that the other TCP connections are not being fully utilised that means this makes sense.

  - persisted TCP connection
  - low latency
  - streaming with chunked transfer
  - pipelining (disabled by default)
  - caching (with E-Tags)

#### HTTP/2

  - **multiplexing HTTP requests** - allows the usage of a single connection per client, meaning that a single connection between the client and the webserver can be used to serve all requests asynchronously, enabling the webserver to use less resources, thus support more users at the same time.
  - compression
  - server push
  - SPDY (speedy) - deprecated open-specification communication protocol that was developed primarily at Google for transporting web content
  - secure by default
  - Protocol Negotiation during TLS (NPN - next protocol negotiation/ALPN - application layer protocol negotiation)

- HTTP/2 adds multiplexing to the protocol to allow a single TCP connection to be used for multiple in flight HTTP requests. It does this by changing the text-based HTTP/1.1 protocol to a binary, packet-based protocol. These may look like TCP packets but that’s not really relevant (in the same way that saying TCP is similar to IP because it’s packet based is not relevant). Splitting messages into packets is really the only way of allowing multiple messages to be in flight at the same time. HTTP/2 also adds the concept of streams so that packets can belong to different requests - TCP has no such concept - and this is what really makes HTTP/2 multiplexed. In fact, because TCP doesn’t allow separate, independents streams (i.e. multiplexing), and because it is guaranteed, this actually introduces a new problem where a single dropped TCP packet holds up all the HTTP/2 streams on that connection, despite the fact that only one stream should really be affected and the other streams should be able to carry on despite this. This can even make HTTP/2 slower in certain conditions. Google is experimenting with moving away from TCP to QUIC to address this.

#### HTTP/2 over QUIC (HTTP/3)

  - replaces TCP with QUIC (UDP with congestion control)
  - all HTTP/2 features
  - still in the experimental phase

#### Multiplexing

- [Source](https://stackoverflow.com/questions/36517829/what-does-multiplexing-mean-in-http-2/36519379#36519379)

- **Multiplexing** allows the Browser to fire off multiple requests at once on the same connection and receive the requests back in any order.

- When you load a web page, it downloads the HTML page, it sees it needs some CSS, some JavaScript, a load of images... etc.

- Under HTTP/1.1 you can only download one of those at a time on your HTTP/1.1 connection. So your browser downloads the HTML, then it asks for the CSS file. When that's returned it asks for the JavaScript file. When that's returned it asks for the first image file... etc. HTTP/1.1 is basically synchronous - once you send a request you're stuck until you get a response. This means most of the time the browser is not doing very much, as it has fired off a request, is waiting for a response, then fires off another request, then is waiting for a response... etc. Of course complex sites with lots of JavaScript do require the Browser to do lots of processing, but that depends on the JavaScript being downloaded so, at least for the beginning, the delays inherit to HTTP/1.1 do cause problems. Typically the server isn't doing very much either (at least per request - of course they add up for busy sites), because it should respond almost instantly for static resources (like CSS, JavaScript, images, fonts... etc.) and hopefully not too much longer even for dynamic requests (that require a database call or the like).

- So one of the main issues on the web today is the network latency in sending the requests between browser and server. It may only be tens or perhaps hundreds of millisecond, which might not seem much, but they add up and are often the slowest part of web browsing - especially as websites get more complex and require extra resources (as they are getting) and Internet access is increasingly via mobile (with slower latency than broadband).

- To get around this, browsers usually open multiple connections to the web server (typically 6). This means a browser can fire off multiple requests at the same time, which is much better, but at the cost of the complexity of having to set-up and manage multiple connections (which impacts both browser and server). This approach provides an improvement, but we need to include the cost of setting up those multiple connections, and the resource implications of managing them (setting up separate TCP connections does take time and other resources - to do the TCP connection, HTTPS handshake and then get up to full speed due to TCP slow start).

- HTTP/2 allows to send off multiple requests on the same connection - so there is no need for opening multiple connections as per above. This has the obvious performance benefit of not delaying sending of those requests waiting for a free connection. All these requests make their way through the Internet to the server in (almost) parallel. The server responds to each one, and then they start to make their way back. In fact it's even more powerful than that as the web server can respond to them in any order it feels like and send back files in different order, or even break each file requested into pieces and intermingle the files together. This has the secondary benefit of one heavy request not blocking all the other subsequent requests (known as the head of line blocking issue). The web browser then is tasked with putting all the pieces back together. In best case (assuming no bandwidth limits), if all 10 requests are fired off pretty much at once in parallel, and are answered by the server immediately, this means you basically have one round trip to get all of the resources browser requested for. And this has none of the downsides that multiple connections had for HTTP/1.1! This is also much more scalable as resources on each website grow (currently browsers open up to 6 parallel connections under HTTP/1.1 but should that grow as sites get more complex?).

- [Comparison of HTTP/1.1 vs HTTP/2](https://freecontent.manning.com/mental-model-graphic-how-is-http-1-1-different-from-http-2/)

- One thing is how bandwidth impacts us here. Of course your Internet connection is limited by how much you can download and HTTP/2 does not address that. So if those 10 resources discussed in above examples are all massive print-quality images, then they will still be slow to download. However, for most web browser, bandwidth is less of a problem than latency. So if those ten resources are small items (particularly text resources like CSS and JavaScript which can be gzipped to be tiny), as is very common on websites, then bandwidth is not really an issue - it's the sheer volume of resources that is often the problem and HTTP/2 looks to address that. This is also why concatenation is used in HTTP/1.1 as another workaround, so for example all CSS is often joined together into one file: the amount of CSS downloaded is the same but by doing it as one resource there are huge performance benefits (though less so with HTTP/2 and in fact some say concatenation should be an anti-pattern under HTTP/2 - though there are arguments against doing away with it completely too).

- To put it as a real world example: assume you have to order 10 items from a shop for home delivery:

  - HTTP/1.1 with one connection means you have to order them one at a time and you cannot order the next item until the last arrives. You can understand it would take weeks to get through everything.

  - HTTP/1.1 with multiple connections means you can have a (limited) number of independent orders on the go at the same time.

  - HTTP/1.1 with pipelining means you can ask for all 10 items one after the other without waiting, but then they all arrive in the specific order you asked for them. And if one item is out of stock then you have to wait for that before you get the items you ordered after that - even if those later items are actually in stock! This is a bit better but is still subject to delays, and let's say most shops don't support this way of ordering anyway.

  - HTTP/2 means you can order your items in any particular order - without any delays (similar to above). The shop will dispatch them as they are ready, so they may arrive in a different order than you asked for them, and they may even split items so some parts of that order arrive first (so better than above). Ultimately this should mean you 1) get everything quicker overall and 2) can start working on each item as it arrives ("oh that's not as nice as I thought it would be, so I might want to order something else as well or instead").

#### HTTP E-Tags

- [Source](https://www.youtube.com/watch?v=TgZnpp5wJWU)

- When client requests a given resource server responds with the requested resource, and also adds an E-Tag for this resource. E-Tag is basically an unique identifier for requested resource that is cached on the client side. Next time client requests this resource it can do so with the E-Tag in the request's header and server will respond that this resource has not changed (304 status - not modified) or if no resource with a given E-tag was found it will respond with the updated version of this resource and a new E-Tag.

- Pros:

  - fast response
  - requires less bandwidth
  - it might help with the database consistency since it can be used as a protection against racing conditions via comparing the E-Tag during the actual modification of the resource

- Cons:
  - if request goes through load balancer/reverse proxy and is directed to some server pool, due to the round robin (or other) balancing algorithm, it might end up in a different endpoint that does not recognize given resource by the same E-Tag making this caching method useless. Since generating an E-Tag requires some overhead this will only slow down whole infrastructure. This can be solved by proper configuration of an infrastructure so that E-Tags are all the same across all of the servers.
  - If E-Tags are not supported within given client by default the logic to handle E-Tags has to be coded and therefore the code is harder to write.
  - E-Tags can be used to track people. They can be made unique for a client and therefore identify the user session since E-Tags are managed by browser and they cannot be easily deleted. Even when session is closed when renewed it will be identified by the request made with previously saved E-Tag.

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

- TCP, as a packet based protocol, can be used for multiplexed connections if the higher level application protocol (e.g. HTTP) allows sending of multiple messages.

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
