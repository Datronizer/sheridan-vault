Deploy, scale, & manage a fleet of 3rd party network virtual appliances in AWS, e.g. Firewalls, Intrusion Detection and Prevention Systems (IDPs), Deep Packet Inspection Systems, modify payloads, etc. at the network level

**Example use case:**
Through a routing table, route all traffic to go through, a Gateway Load Balancer, and route all that traffic through 3rd party security virtual appliances that will analyze the traffic. And once they're happy with it, they send it back through the GWLB and forward that to the application.

![[Pasted image 20250921005703.png]]

This operates at [[Layer 3]] (Network Layer) - IP Packets

Combines the following functions:
- Transparent Network Gateway - single entry/exit for all traffic
- Load Balancer - distributes traffic to virtual appliances

Uses the GENEVE protocol on port 6081

# Target Groups
- EC2 Instances
	- These can be running your 3rd party seucity apps
	- Register to TGs using instance IDs
- IP Addresses
	- Must be private IPs
	- Manual IP registration for server