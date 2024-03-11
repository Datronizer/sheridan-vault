idk what this is about but i'll take notes anytways

Make 2 VPCs (A and B).
For each, make 2 public subnets + 1 private subnet.
Pay attention to the availability zones requested in the assignment.

Private subnet should have a private IP (duh)
Need a route table for each subnet. 
Sg should only allow SSH
Show all screenshots of ssh and http even if they fail

# Continuing where we left off
Now suppose I have 2 different VPCs. How do I link them?

We can use what is called **VPC-peering**. Basically, follow the steps 1-6 from last week, but make a VPC-B also and spin a VM in there. For VPC-A in this case, you DO NOT create a private subnet. You want it to be public in order to link to it.

7. Create VPC Pairing between VPC-A and VPC-B
8. Add new routes to Public RT.
	- You have to add a route from VPC-A to VPC-B
	- And you have to add one vice versa
	- These are intermediary hops before it goes to the IGW.

>[!note] Doing this is more logical in general
>The routing goes directly between VPCs and doesn't have to cross the IGW first => reducing latency => makes more sense.
>
>Imagine living next to your friend's house but you decide to take the train to the central station then back home just to meet your friend. Like why bro?

# NAT Gateway
[NAT Gateway routing help](https://stackoverflow.com/questions/66415539/aws-vpc-cant-access-internet-despite-configuring-nat-internet-gateway-accordin)

# IPv6
An IPv6 address contains 128 bits (4 times more than IPv4), so ideally this SHOULD be a way better system than IPv4, BUT NOOOOOOOOOO, hUmANs arE ScAREd Of CHanGe.

Whatever. Take these 128 bits, cut them into 8 equal parts. Each of these will have 16 bits. These 16 bits can be represented by 4 characters, which of course have 16 configurations. So we represent that with 4 hex characters.

You can compress these numbers by squishing THE FIRST series of only-zero blocks into a colon. Any only-zero blocks afterwards will be compressed into a single zero. E.g.
`2607:0000:0000:0000:1234:0000:0000:0000` is equivalent to `2607::1234:0:0:0`.

For historical reasons, we STILL HAVE TO FUCKING SUBNET A SYSTEM THAT CAN OUTLAST THE HUMAN RACE. So we use the last 4 blocks (64 bits) for the host. Then the 40 bits prior to that are used for subnetting. The first 24 bits are for networking.

The second block of the first 24 bits is actually split in half, that's why it's technically (16 + 8) + (8 + 32) + 64. The second hanging 8 there is used to define regions. So you can tell where the region of the subnet is. Then for every region, it chunks the next 20 bits for VPCs.

Look up IPv6 subnetting for more information.