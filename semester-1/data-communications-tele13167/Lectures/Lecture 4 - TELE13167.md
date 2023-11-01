# Data Link Layer

## MAC Address
MAC addresses are written left to right but they are actually sent **right to left**. 
- If the second bit of the MAC is even, it is a Unicast
- Else it is a Multicast
## LLC
The Logical Link Control sublayer provides
- Error control/flow control
- It also makes the data link layer transparent
## Ethernets
Ethernet cables change throughout the ages. It all started with Standard Ethernet -> Fast Ethernet -> Gigabit Ethernet -> 10 Gigabit Ethernet.
### Standard Ethernet - 10 Mbps
Data rate limited to 10Mbps. All ethernet is connectionless. Makes use of [[#CSMA/CD]] (we'll get back to this).
### Fast Ethernet - 100 Mbps
Fast Ethernet offers "auto-negotiation", which is fancy for "backwards-compatible." They negotiate a rate that will work for both wires. Also still uses [[#CSMA/CD]].
#### CSMA/CD
The problem: 2 computers, A and D want to send data to the hub. At the same time, btw. If 2 computers send a file at once, there will be a "collision" and the receiver won't pick either.
The solution: **C**arrier **S**ends **M**ultiple **A**ccess w/ **C**ollision **D**etection (yes that's the actual acronym). Here's how it works:
1. Before sending a message, check if anyone else is => if yes then wait
2. It can happen that 2 PC's will send a message at the same time (A, D) => boom *data collision noises*
3. Collision detected by all 4 PC's 
	- A **Jam Timer** procs and gives each PC a unique amount of time each PC must wait before being able to send e.g. A - 3ms, B - 2ms, C - 4ms, D - 1ms.
4. D can now send data. A will wait until D finishes transmitting the whole file.

As you can see, this is terribly inefficient. But we have come up with a solution. [[#Full-Duplex Mode]]!
#### Full-Duplex Mode
As talked about in previous classes. [[Lecture 1 - TELE13167#^1ebe7e|Here]].
### Collision Domain
An area that you set up to watch all the devices before you can send a message. Example, I could have [[Airport Metaphor|Toronto Pearson]] be in charge of ALL flights in Canada, but that is terribly inefficient. We can instead split the load into smaller **Collision Domains** so that the errors are smaller and can be better resolved.

> [!note] More CDs => smaller individual CDs => faster transmission.

To count domains you simply do the following. Start at 1 (number of domains != index of domain). Count every connection out from routers, switches, bridges. Ignore hubs, they're dumb.
### Broadcast domain
An area of a network that will see the broadcast message. Usually split up by routers. Counting BDs is the same. Start at one and only count routers' outward connections.

### Effective Throughput
Metaphor: In a 180 min class of 30 students, how much time do I spend with which?

$$
\text{Effective Throughput} = \frac{\text{Given Throughput}}{\text{No. of devices in collision domain}}
$$
### VLAN - Modern separation of Broadcast Domains
Switches can also separate broadcast domains, but instead through VLANs. It's a virtual way to group people together based on tasks, rather than locations.

Example: Say I have a sales dept., I gotta put them all into the same room so that they can be hooked up to the same device. Now that's not necessary. Say Sheridan, for example. All projectors in the school are hooked up to one VLAN so an update that's rolled out will work for all at once.

### Broadcast Storm
If I send a message through a switch hooked up to another to another to another to switch 1. The message goes through SW1 to 2 to 3 to 4 to 1. Does it stop? Nooooope, keep her movin' and it'll cycle forever.

The solution to this event is a tool called a Spanning Tree Protocol.
### Spanning Tree Protocol
The Spanning Tree Protocol prevents an endless loop of data known as a Broadcast Storm. It's simpler when I explain how we map this protocol:

1. Find the **Root Bridge (RB)**. Start with the switch with the lowest MAC. And we should ensure it's always at the top of the diagram.
2. Find the **Root Port (RP)** (receiving port) on every other switch besides the **RB**. Pick the port closest to the root bridge, and if it's a tie, pick either one.
	- At this step, check if EVERY switch has 1 RP 
3. For any 2 switches with **NO RP** between them, you must create a **Blocked Port (BP)**.
	- Eliminate the loops
	- Block the higher MAC
	- At this step, check if all wires have an RP or a BP, NOT BOTH
4. Any unlabeled ports become **Designated Ports (DP)**, sometimes called sending ports.

