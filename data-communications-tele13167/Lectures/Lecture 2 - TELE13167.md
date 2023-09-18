# Protocol
## What is a Protocol?
Computers need to communicate with other computers through the network. These communications often follow specific rules. These rules often come with "ways" to send/receive the message. These "ways", we call **protocols**.
## Protocol layering
### Single layering
Single layering is the most fundamental way of sending a message. Person A and B agree on a [[Lecture 1 - TELE13167#Data communication|set of rules]] and send a message to each other. Multiple layering is a little different.
### Multiple layering
Imagine writing a letter to someone using a Caesar Cipher. There are multiple steps:
1. Write a message
2. Code the message
3. Fold the message
4. Put in envelope and send
5. Receive and take out of envelope
6. Unfold message
7. Decode
8. Read

As we can see, these steps mirror each other between 4 and 5. And as you can see, the tasks are opposite of each other, and at every step, the corresponding objects are identical.
### Pros and Cons
| x | Single | Multiple | 
| -- | -- | -- |
|Pros |- Something something |<ul><li>You can use a different service to send the message even if a layer breaks. There's always another service.</li><li>More secure because there are more layers to the message.</li><li>Can communicate from far away.</li></ul>|
|Cons |  |  - Slower <br/> - Higher chance of miscommunication (interpret message incorrectly)|

// TODO: Fill in the single one.
## Placeholder (get from .pptx)

## TCP/IP
When we send someone a letter, why do we include the name and the address? The address is clear => you need to ensure your mail gets to the right house, but why the name? Well, when the mail arrives without a name, how will you know if it's yours or your mom's? (see how I snuck your mom in there? That's crazy.)
#### The 5 TCP/IP layers
Behold, cool table:

| Layer       | Physical Data Unit (PDU) | Address                | Function                                           | Devices       | Protocols                                |
| ----------- | ------------------------ | ---------------------- | -------------------------------------------------- | ------------- | ---------------------------------------- |
| Application | Message                  | Application specific   | Acts as a bridge between software and lower layers |               | HTTP, FTP, SMTP, POP3, Telnet, SSH, etc. | 
| Transport   | Segment                  | Port Number            | Finds the right program                            |               | TCP, UDP                                 |
| Network     | Packet                   | IP address             | "Big picture"--Finds the right final PC            | Router        | IPv4, IPv6                               |
| Datalink    | Frame                    | Physical address (MAC) | Finds each next stop along the way                 | Switch bridge | Ethernet (802.3), Wifi (802.11)          |
| Physical    | Bits                     | N/A                    | Converts the frame ^^^ into bits                   | Hubs          | ^                                         |

Generally when you want to send something from A to B, the IP Address tells you the big picture. There's a source IP and there's a destination IP. But the MAC address doesn't show this. Rather, it points out the next destination. The destination MAC address is on the next device, the destination IP is the final device, ignoring the whole path.

> [!note] It's easier to look at this as 2 people travelling to Japan. The IP person will focus on the endgoal--Japan. The MAC person will focus on what airport the layover will be at. 

### Logical Connections
We often think of communicating with someone over the internet is a direct connection. News flash, it isn't. You are actually connecting through multiple nodes before you get to your friend. See [[airport metaphor]].
#### Sending a message example
Below is the process of sending a message to person B.
1. I send a message through an application, usually an API request.
2. The transport layer tacks a port number on the message, now the message knows what port to get to.
3. The network layer tacks on the final IP address on the message, now the message knows what the final destination is prior to the port.
4. The datalink layer tacks on the MAC address, now the message knows where the next relay point is (usually the one right after the source is the router)
5. The message now travels to the router. 
	1. At the router, it checks if the message is at the right router.
	2. If the message is at the right router, it removes the MAC layer and tacks a new one on (think of it like a stamp towards a new relay station)
	3. Sends the message to the next node
6. After travelling to the end device, it gets checked one final time and the destination receives it.

#### Visual Illustration
(grab from pptx)
# OSI model
After the TCP/IP model came out, the OSI model was introduced. It was intended to improve the TCP/IP model by splitting the Application layer into 3. The two newer layers are Presentation, used for encryption; and Session: keeps data from different programs separate.

It never caught on because the improvements were so minor that it wasn't necessary to switch. Why use a different model when the original does the same thing just as well. That plus people don't like change.

TCP/IP is also not the most optimal model for computer communication as it doesn't play well with how computers work. So, in order for people to switch, the new model ought to be way better than the current TCP/IP model. 
# Encapsulation/Decapsulation
Remember the process where they tack a bunch of stuff onto your original message? That's **encapsulation**. The reverse of this is **decapsulation.**
# Multiplexing/Demultiplexing
Suppose you want to send a message. Multiplexing is when **multiple** protocols work together to encapsulate your message. The reverse is demultiplexing where multiple protocols work together to decapsulate your message.
# Application layers: APIs
## API
Basically a set of tools that makes programming a bit easier (it isn't).
## Socket API
Suppose you want your program to use the internet to grab something. You first
1. Write program
2. Specify which socket(s) that my program uses
=> my program now works with the internet

Cool, what's a socket? Good question. Think of it a keyboard. It writes to the program and the monitor reads that. The socket does the same thing. I write something to the socket, you read whatever I wrote from the socket.

Sockets are numbered from 0 to 65535.

A socket is your IP number + port #, and there are 3 categories of sockets:
- Well known (reserved for operating systems. HTTP is a known protocol)
- Registered (pay to use sockets)
- Dynamic (free to use by anyone)

In a socket, the port plays a more important role, so "ports" and "sockets" are used interchangeably. Mostly because generally once you're already at the IP so only the ports are identifiable information.
### Ephemeral port/socket
Let's say I need to view a web page. I need to open port 80 to view the web page **on the server**. But for the server to **send the requested page back**, they need to open a port from **1024 -> 65535** on your computer. It's ephemeral because it's like ghosts, you see them then you don't. Poof.
### ARP activity
Address Resolution Protocol (ARP). When you first connect to a network, you are first given an IP address + the IP of the gateway. But for me to get to the next stop, I need the MAC address of the router to relay to. This is where ARP comes in.

The ARP broadcast request will say "I have an IP address of 10.48.64.1, could that device please send me its MAC address." The device will go "oh ya buddy here you go eh", and sends it to the ARP table.  
### Checksum
Checksum could be understood as verification data. Every piece of data on the internet could have a checksum tacked onto it to verify that it is the original data. 

Checksums work as such: you take a series of data, pad some more data to it in a way that you can detect modifications (could be even matching, could be hex, could be other ciphers, bit dampening, etc.). The recipient can then take the data, validate it, and will know if something has been tampered with.

MD5 is one checksum format.
# Quiz 1
In class, Sildes 136 onwards for examples (short answer, matching)
19pts  |   multiple choice
5pts    |  matching: match word to definition
6pts    |  3 short answers:
Exam questions are available on the pptx