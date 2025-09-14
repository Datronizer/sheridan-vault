---
aliases:
  - SG
  - Security Groups
  - EC2 SG
  - Security Group
  - SGs
---
# Introduction
Security Groups (SG's) are the fundamentals of network security in AWS. They control how traffic flows in an out of our [[Elastic Compute Cloud (EC2)|EC2]] Instances (anything really, it's the first line of defense).

> [!important]
> SG's only contain **Allow** rules.
> SG's rules can reference by IP or by another SG

## Example of how the SG works conceptually:
We are on our PC connecting to an EC2 Instance with an SG attached. Let's say the SG allows some kind of inbound traffic, and allows some kind of outbound traffic. Then only the allowed inbound traffic will makes its way to the EC2 instance. Conversely, only the allowed outbound traffic will make it to you

# Deeper Dive
SGs act as a firewall on EC2 instances. They regulate:
- Access to Ports
- Authorized IP ranges, both [[IPv4]] and [[IPv6]]
- Controls inbound network (traffic *to* the instance)
- Controls outbound network (traffic *from* the instance)

![[{34B75872-6FE2-461E-A84B-5179DE783E4E}.png]]

This diagram shows some possible configuration for an example SG:
- Allows all HTTP traffic (0.0.0.0/0)
- Only allow SSH traffic from 122.149.196.95/32
- Allows all traffic to port 4567 (custom TCP rule, noted as Java app in description)

# Good to knows
- An SG can be attached to multiple instances
- An SG is locked down to a region / VPC combination
- Lives outside the EC2 collection. Meaning, if traffic is blocked, the EC2 instance won't see it. 
	- SG's are literally the Firewall to your apps. If SG blocks it, it will never make it to any apps.
- It's a good idea to maintain 1 separate SG for SSH access
	- SSH access is the most complicated thing to do, so it's a good idea to isolate it
- **Common errors:**
	- If your app isn't accessible (time out), it's probably an SG issue
	- If your app throws a connection refused error, then it's an app error instead, or the instance didn't start
- **By default:**
	- All inbound traffic are **blocked** by default
	- All outbound traffic are **authorized** by default

# Referencing SGs from other SGs
This is easier explained with an example.

Suppose you have 4 EC2 instances:
- Instance1
- Instance2
- Instance3
- Instance4

For Instance1, let's create an SG called SG1. Let's do the same for Instance2 with SG2.
For Instance3, we create an SG3, and for inbound traffic, we will authorize SG1 and SG2.

In this case, Instance1 can send traffic to Instance3 because SG3 allows access for SG1. Same thing applies to SG2. This is really cool because it allows access based only on SG, meaning you won't have to wrestle around with IPs and ports. Just assign an Instance with a relevant SG and it will be allowed through.

Instance4, in our example, uses SG4. Because SG4 wasn't authorized in SG1, inbound traffic from SG4 will be rejected.

# Classic Ports to know
Here are some important, commonly used ports to remember:
- 22 = SSH (Secure Shell) - connect remotely using shell (Linux & Mac, Windows 11 just added this)
- 21 = FTP (File Transfer Protocol) - upload files into a file share
- 22 = SFTP (Secure File Transfer Protocol) - upload files using SSH (yes same port as SSH)
- 80 = HTTP - access unsecured websites
- 443 = HTTPS - access secured websites
- 3389 = RDP (Remote Desktop Protocol) - log into a Windows instance
