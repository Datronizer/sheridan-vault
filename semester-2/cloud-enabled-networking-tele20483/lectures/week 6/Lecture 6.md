# Virtual Private Cloud
## Introduction
A VPC is a logically isolated section in AWS that mimics the structure of a private network domain.

A VPC has at least 1 IP virtual network where virtual resources can be virtualized (duh). Think of it like a "virtual" router where your instances can connect to, to reach the Internet.

Here, the "virtual" router is a **Gateway**. The VPC provides each instance with a private IP (like a router), and a public IP (how this works is not available to the public).

All the default subnets created in VPC are protected with a default [[NACL]] and default [[Security Group|security groups]]. Of course, this is initialized by default for security's sake.
## Route tables
A route table determines the network destinations that can be reach from the current local position (yes this is the same as the [[Routing-Forwarding Tables|routing/forwarding table]]). If the table does not contain information on how to reach a destination, then it is considered **unreacheable**. 

The **routing decisions** (the forwarding of the traffic) are based on the knowledge present in the route table (yes, literally like a routing/forwarding table).

And yes, the **subnets** MUST be associated to the **route tables**. 1 subnet => 1 route table, BUT 1 route table => many subnets. 
## Routing in the VPC
There are 2 basic routing components in the VPC
- **VPC default router** interconnects the networks of the VPC
- **VPC default gateway** enables transit to and from the VPC

Assuming the traffic isn't blocked by the NACL or the SG, all traffic inside a VPC can reach any destination within the VPC.
## Internet Gateway
The Internet Gateway (IGW) interconnects the VPC with the external world. It is basically a software construct (no physical parts), and it can be identified with the id `igw_id`, e.g. `igw_2f546`.

The default VPC provided by AWS comes with its own IGW. Of course, it can be disconnected from the IGW by removing the default route pointing to it, but the IGW will not be destroyed afterwards.

User-created VPCs do NOT have IGWs upon creation, but can be attached to an existing one or to a newly created one.

## Customer VPCs
A customer can create up to 100 VPCs per account per region (please don't actually do this). But this requires the customer to know how to architect the networking aspects of the new VPCs.

There are many topologies driven by business and organization needs. Example:
- Some orgs will need separate VPCs for development, testing, and production
	- A dev VPC probably just needs connection to other VPCs
	- A local dropbox needs limited Internet access and probably should not touch anything else.
	- etc.
There are VPCs with limited or no public access for security reasons, while there are VPCs that are only open to other VPCs.

# How it all works
1. I make a VPC. There is jack shit here, except for a route table.
	- AWS gives you a route table with 1 single route called `local`.
	- This single route means *everything in here can only route locally*
2. Now I make 2 subnets (`x.x.0.0/20` & `x.x.16.0/20`) and attach them to the VPC.
	- Now I have a private and public subnet.
	- I still need to create an IGW to pass traffic through to the Internet.
3. I make an IGW and attach my VPC to this IGW. Let's call it `NET-10-IGW`.
	- Now I click on **Actions** and attach to our VPC.
	- It should now say **attached**.
4. Now I make a public route table (RT). This will allow routing and segues into step 5.
	- Add a rule: `0.0.0.0/0 -> IGW`
5. Now I associate the public RT with the public subnet.
	- Link this route table to our VPC
		- Right now there's only 1 route entry which is `local`.
		- Let's add a new route, and give the destination `0.0.0.0/0` so it can go to the Internet. 
		- Now change its target to Internet Gateway
		- Choose the IGW we just made.
6. Now we spin 2 images, 1 AMI + 1 Ubuntu, public and private respectively.
	- Give these two ssh access.
7. Now go to the public subnet we made.
	- Attach the public Route Table to the public subnet
	- Attach the private Route Table to the private subnet

Et voila! We're done! It's so over! :D