# Cloud compute and network communications
Recall that routers mostly communicate using [[Border Gateway Protocol]], every organization would have an AS number to identify themselves during communication using BGP. 

Of course within the border, devices will still using BGP but Internal BGP (IBGP), yeah the name is kinda stupid. But most communication protocols are done internally, only BGP is the only one that does it both internally and externally.

Internally, devices go through a "routing domain". This network has what is called an Internet Autonomous System (AS). Each of these domain has a unique number they identify to the Internet. Sheridan College uses 5664.

This domain of course owns a public IPv4 address block (142.55.0.0/16 for Sheridan). All IPv4 address with 142.55.x.x belong to Sheridan.
## Routing knowledge propagates
Yes, propagates. It's because when devices communicate, they tell each other who they're connected to in order to route a message from A to B. Of course this means that every time A talks to C, C tells A how to get to B and A tells C how to get to A. So C should know both A and B. 

Recall how the switch and router works. And recall [[routing tables]]. The switch would broadcast to everyone, but the router would know where it needs to send data already so it would drop the package by default. This is to prevent a [[routing loop]]. 

There's also a forwarding table. Routers can use AS numbers to find the shortest (?) and least likely to repeat loop

Public IPv4 in AWS. So basically, normally you can have 2 computers with the same public IP since they're on the same network, but different port numbers for communication. This unfortunately doesn't work for AWS (I still don't understand how), so they have to resort to providing each VM an individual Public IPv4. So, basically it's not a NAT, it's something else based on DHCP.

