# Network Layer
## Duties of the Network Layer
- Packetizing (encapsulating and decapsulating the data)
- [[#Routing]] and [[#forwarding]]
- Carry a payload from source to destination without changing the contents
## Routing
Simply put, it is a process of finding the (relatively) best path to each destination. To do so, it requires routing protocols. There are 3:
### Routing Information Protocol (RIP)
Uses a criteria known as **hop count**. One **hop** is one router you've passed through on the way to the destination. Ideally you would pick the fewest number of hops. If there are 2 identical hop counts, the router will alternate between them.

This gets funny because since it only takes into consideration the hop count, the path without hops might take *way* longer. For example: going through a megabit ethernet rather than a fiber cable, just because the hop count is lower. 

Think, bus transits vs direct bus routes. Would you take the direct bus even if it takes 3 hours longer? No? Well, RIP will.
### Open shortest Path First (OSPF)
Unlike RIP, OSPF and [[#Enhanced Interior Gateway Routing Protocol (EIGRP)|EIGRP]] use **path weight** instead. Path weight is a mathematical algorithm to assign a number to every path based on the throughput, bandwidth, latency, and other factors. Then it computes the path weight and choose the path with the lower weight.

This algorithm is called [Dijkstra's Algorithm](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/d819e7f4568aced8d5b59e03db6c7b67_MIT6_006S20_lec13.pdf).
### Enhanced Interior Gateway Routing Protocol (EIGRP)
EIGRP is very similar to OSPF, but it is mostly used by CISCO routers. You could say this is their proprietary software. It's called the [Bellman-Ford Algorithm](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/2430d7903a5529451d80c17f89a41fe8_MIT6_006S20_lec12.pdf).
## Forwarding
Let's say you're driving home using GPS. The route home? That's routing. You driving and following the directions? That's forwarding.

Forwarding follows the process of routing, where the router attempts to find what to do with a destination. Basically it uses the data from routing to send out the appropriate interface.

Example process: Routing will go "Hey uhhh if you want to get to network A, you uhh go through interface m1, network B goes to m0, etc." It stores all this into a routing table. Then when I want to forward data to B, I refer to the same table (routing table "becomes" forwarding table), and send the data through m0, following the forwarding table.

Of course, if none of the entries in the table match where I want to go, I [[Lecture 3 - TELE13167#Static routing (0.0.0.0/0)|forward it to the internet]] and have that take care of things instead.
## DHCP
So... even wondered how your PC gets an IP? Is it assigned by a literal human in the IT department? Or, like all technology nowadays, it is automated? (Spoiler alert: it's automated).

> [!note] DHCP is done using multiple servers, each having a unique list of IPs to assign

Here how the process works:
1. **Broadcast DHCP request for an IP:** 
	- PC1 pops into the network and goes "umm, brother, may i please have IP address".
2. **Each DHCP server offers 1 available IP to your PC - these addresses are NOT offered to any other computers:** 
	- Server 1 - "Hey I have one address with your name-" 
	- Server 2 - "MINE IS BETTER HERE TAKE IT".
3. **PC accepts the first IP that arrives**: 
	- PC accepts from Server 1
	- Server 1 - "There ya go buddy, take that IP and I'll make sure to not give out duplicates"
	- Server 2 - "*grumpy* Fine, I'll give this to someone else who APPRECIATES ME".
4. **PC announces its new IP, any unused IP are now free to use**
## Public and Private IP Addresses
Public address: 
- Paid
- Gives you internet access
- Can be found on Google ("what is my ip")

Private address:
- Free
- No internet access.
- CMD ("ipconfig")
- Usually starts with 10, 172,192 (for IPv4 only)

Hmm, in that case, if I have a private IP address (let's say, I'm connected to Sheridan's Wifi), how do I connect to the Internet? That's where [[#(NAT)|NAT]] comes into play.
### Network Address Translator (NAT)
In Sheridan, they would use a NAT router. The NAT router would take your Private IP, translate it to a Public IP, and broadcast it to the Internet. 

NAT routers do provide some level of security by blocking foreign connections. It also saves on IPs. Let's say you have a printer, you probably don't need (or want) it to connect to the internet. You can just save on IP addresses using a NAT router instead.

NAT routers also allows grouping of people, so many private addresses can use 1 public IP.
# Domain Name Services (DNS)
Basically put, it converts domain name to IP address by looking it up in LAN -> ISP -> ISP's ISP -> ISP's ISP's Server -> ISP -> LAN -> you. It's a very tedious process that is simplified through automation and robust systems.
# IPv6
IPv6 has 128 bits while IPv4 has 32bits (boooo, cringeee). As you can already see, this allows for additional addresses, meaning we finally have enough addresses for everyone.

Another benefit is that there is increased security and there is no need for subnetting. Speaking of which...
# Subnetting
## IPv4 - Address Space
There are 3 classes of IP addresses:
- Class A: Uses the first octet for network information (cannot be changed)
	- The other 3 octets are free to use/host
	- First octet is number between 0-126
- Class B: Uses first 2 octets for network information (cannot be changed)
	- Example: Sheridan's 152.145 is the network info. Cannot be changed, pre-assigned.
	- The other 2 octets are free to use/host
	- First octet is number between 128-191
- Class C: Uses first 3 octets for network information (cannot be changed)
	- Last octet free to use/host
	- First octet is number between 192-223

Example:
- 10  .  x  .   x   . x : Class A
- 142. 55 .   x   . x : Class B
- 200. 10 . 172 . x : Class C
## Subnetting steps
(Extra information included in slides. This is a simplification)
Let's start with class C because it's the easiest to subnet.

Pretend our network is 200.200.200.X (X ranging from 0 to 255).
In bits, our network will be
*128 64 32 16 8 4 2 1* | *128 64 32 16 8 4 2 1* | *128 64 32 16 8 4 2 1* | 128 64 32 16 8 4 2 1

Ignore the first 3 octets, focus on the last block. Let's borrow 2 bits there for subnetting, and let's take the first 2 bits (128, 64)

Then we have this many permutations

| 128 | 64  |
| --- | --- |
| 0   | 0   |
| 0   | 1   |
| 1   | 0   |
| 1   | 1   |

Fill this table in with the rest of the bits. Have them all be 0's then have them all be 1's. I will just put the 1's table here because of space limitation.

| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   | Decimal value |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- |
| 0   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 63            |
| 0   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 127           |
| 1   | 0   | 1   | 1   | 1   | 1   | 1   | 1   | 191           |
| 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 254           |

The 0's table will yield 0, 64, 128, 192. These are called "blocks" because, you know. 64 + 64 + 64 etc makes a block.

Anyways. Now that we have the decimals, let's do something fun. We can set up the following table to hopefully clarify what's going on. The steps are performed downwards. The columns are just other examples of what would happen if we take more bits.

| x                         | Class C: 2bits borrowed             | Class C: 3bits borrowed         | Class C: 5 bits borrowed |
| ------------------------- | ----------------------------------- | ------------------------------- | ------------------------ |
| Schematic                 | 8 8 8 2                             | 8 8 8 3                         | 8 8 8 5                  |
| Submask                   | 255.255.255.192 (128 + 64)          | 255.255.255.224 (128 + 64 + 32) | 255.255.255.248          |
| Block size                | 256 (max octet size*) - 192 = 64    | 256 - 224 = 32                  | 256 - 248 = 8            |
| Subnet ID (SID)           | 200.200.200.0, &.64**, &.128, &.192 | &.0, &.32, &.64, &.96, &.128    | &.0, &.8, &.16, &.24     |
| Broadcast ID (BID)        | &.63, &.127, &.191, &.255           | &.31, &.63, &.91, &.127         | &.7, &.15, &.23, &.31    |
| Valid Host Range (VHR)*** | 1-62, 65-126, 129-190, etc.         | etc.                            | etc.                     |

\* Max octet size (256) is NOT the same as max octet value (255). The former is how many numbers there are (including 0), the latter is how high the IP could actually go (starting from 0). 
\** Here I am using `&` as a shorthand for 200.200.200.X because I am not rewriting that shit lmao.
\*** I explain this in a [[#^1|later section]]

Let's think back to our Assignment 1. We have an IP address of 210.30.45.X with a subnet mask of 255.255.255.240. So, the block size for this would be $256 - 240 = 16$. That's 4 bits ($2^4 = 16$). 

We can compute the smallest and biggest IPs of each "row":
- 210.30.45.0      210.30.45.15
- 210.30.45.16    210.30.45.31
- 210.30.45.32    210.30.45.47
- 210.30.45.64    210.30.45.63

Now look at the illustration with all the broadcast domains. Each of these domains uses 1 single row above. The SIP of each row is the "identifier address" of that broadcast domain. So it cannot be assigned because, you know, it's a reserved number. The BIP also cannot be used because it is the "send this data to everyone in this network" address. 

In that case our number range is limited to 1-14 for the first row, 17-30 for the second row, etc. This range is called the **Valid Host Range (VHR)**. Every computer can only be assigned a value in this range. ^1

For a real time demonstration, refer to the class PowerPoint. Also look at CIDR notations. 
