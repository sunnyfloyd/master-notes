# Backend Topics

## Networking

### OSI (Open Systems Interconnection) Model

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
