#lecture
# The Internet
An internet is a connection between 2 networks. Inter- is between, net is an interweaving structure, like a network. Hence the definition.
But **The Internet** is a network of networks. It's impersonal but it is also personal.
# Before the Internet
- **Prior to 1960**, people used to communicate with phones, telegraph, pigeon carriers, etc.
- But **in 1969**, at the peak of the nuclear threats, the US invented the Arpanet to ensure communications in case a nuclear attack happens. That was the predecessor to the internet.
- **In 1971**, emails were first invented.

**In 1974**, TCP/IP was invented and eliminated the need for a central control. But there were challenges in trying to get 2 networks to communicate. A bank might have faster internet than a home network. They might be more secure. Their packets might be bigger. 

The solution? A default gateway, nowadays, it's your router! It allows your network to pass through the router, the router would then negotiate with the router on the other end and agree on speeds and packets, then the network reaches the other router and the other user. Kind of like an airport.
# Circuit switched / Packet Switched
- For old telephones, when the phones connect, the line stays open until you hang up, even if you're not speaking. And the data connects through only 1 path. That's **circuit switch**.
- **Packet switched** networks would close the connection after the packet is sent. Each packet can travel independently on different paths.
# Network Certifications
AWS and CISCO certifications are really sought after, the CISCO one is more commonly known as CCNA. Python and CISSP are also popular certifications for your resume in networking.

These could lead to a strong set of careers in Networking. Refer to this lecture's powerpoint for links.

Another thing that can help are networking associations where you network about network. You can join these to meet new people, learn something new, and have a foot in the door. Refer to the powerpoint for list of some networking associations.
# Data communication
5 necessary things to communicate with a friend.
- Sender (Someone must speak)
- Receiver (Someone must listen)
- Message (You gotta say something other than "hello")
- Protocol (Must speak the same language and must say "hello"/"goodbye")
- Transmission Media (The voice needs a medium to travel to)
*This is a metaphor for data communication by the way.*

There are 3 ways of communicating:
- **Simplex:** One way communication (mouse controls tower).
- **Half-duplex:** Two way communication, but asynchronous, A to B gotta wait for the information to be transmitted from B to A before they can trasmit (walkie-talkies).
- **Full-duplex:** Two way but data can be sent back and forth the whole time without waiting (discord call).
# Network
There are 3 things we have to be able to identify: nodes, links, interfaces.
- Links connect nodes (think USB cable).
	- A link can be point to point or point to multi point.
- Nodes are like places that the data can stop at/be processed/final destination (think dongle to dongle or dongle to PC).
- Interface is where links connect to nodes (the USB jack where the cable connects to the PC).

These are the 4 different types of network, ranked from smallest range to largest range: PAN, LAN, MAN, WAN.
## PAN (Personal Area Network)
Super short range, usually between 2 devices, without need for a router. Smaller than LAN. Think bluetooth.
## LAN (Local Area Network)
The formal definition is that it is a collection of devices that are in a single geographic area.
Irl, it could be small like a home, or large like Sheridan's campus, but the defining characteristic is that **all devices are within a geographic area**.

Think connection within a room.
## MAN (Metropolitan Area Network)
Think connections within a city like 2 law firms connect to each other from across town.
## WAN (Wide Area Network)
Think "large distances" like across countries.
# Physical Topology
Refers to a way in which the nodes of a network are laid out.
There are 4 basic topologies: 
- Mesh (everything connects to each other)
- Star (everything connects to a central node)
- Bus (everything connects to a line)
- Ring (i mean...)
## Full Mesh Topology
**Description:** Everything device connects to each other
**Fault tolerance:** Highest fault tolerance since there are many backup connections. You could lose 3/5 computers and the other 2 can still talk to each other.
**Ease to setup/expand:** Difficult, you need a ton of wires to make this work.
**Cost:** Expensive because tons of wire and switches are needed.
**Troubleshooting:** Easy. Since all the nodes/links/interfaces are interconnected, if you lose connection in 1, you'll know immediately.
## Star Topology
**Description**: A central device like a hub/switch provides connection to all devices.
**Fault tolerance**: Good until the hub goes down. Hub dies, network dies.
**Ease to setup/expand**: Easy to setup and expand, until the hub is full
**Cost**: Relatively inexpensive, major expense is the hub/switch.
**Troubleshooting**: Simplest topology to troubleshoot.
## Bus Topology
**Description**: The PCs are chained together and data must pass through each PC
**Example**: PC 3 wants to send a msg to PC 4. It goes to the chain node, gives it to 4 and 2, then keeps going to PC 1 and PC 5 and only stop at the **terminator**.
**Fault tolerance**: Lowest fault tolerance, never used in a modern network. If one device dies, no one can send anything.
**Easy to setup/expand**: Simple to add/remove PCs via the drop in slots.
**Cost**: Very inexpensive. It's 1 single chain.
**Troubleshooting**: Easy. You can just replace a device with ease.
## Ring Topology
**Description**: A token travels around and PCs add their message to it.
**Example**: PC 1 wants to send a msg to PC 3. PC 1 grabs a token, locking everyone out. It then tacks a message on the token and pass it along the network to PC 2, then 2 passes to 3, who takes the msg and releases the token back.
**Fault tolerance**: Very low fault tolerance - arguably as bad as bus.
**Easy to setup/expand**: Still pretty simple, not as simple as star.
**Cost**: Relatively inexpensive.
**Troubleshooting**: Fairly difficult to isolate the issue.

# Internet Standards
The internet standards are rules that hope to standardize the internet globally.
The process to pass a new standard is as such:
- You draft an internet draft.
- Present the draft to the RFC council.
- If it's passed, it's a standard, else it gets scrapped.
Same thing with "ipv5". Look it up.

5 protocol related acronyms:
- TCP/IP: A protocol suite that contains essential rules for how the internet works.
- IPsec
- HTTP
- OSI model: Replacement for TCP/IP that never caught on.
- UDP: Protocol that enables fast communication.