---
aliases:
  - EC2
  - AWS EC2
  - Amazon EC2
---

# Introduction
EC2 (Elastic Compute Cloud) is one of the most popular of AWS's offering. It is a way to do [[concepts/compsci/cloud/Cloud Computing Models#Infrastructure as a Service - IaaS|IaaS]] on AWS.

There are lots of things you can do with EC2, namely:
- Rent [[Virtual Machine|virtual machines]] (EC2 instances)
- Store data on virtual drives ([[Elastic Block Store|EBS]] Volumes)
- Distribute load across machines ([[AWS Elastic Load Balancer|ELB]])
- Scaling the services using an auto-scaling group ([[AWS Auto-Scaling Group|ASG]])

Knowing ECS is fundamental to understand how the Cloud works (Main basis of cloud is renting virtual machines, duh)

# EC2 Sizing & Configuration Options
- Operating System ([[Operating Systems]]): [[Linux]], [[Windows]], or [[MacOS]]
- How much compute power & number of cores ([[CPU]])
- How much random-access memory ([[RAM]])
- How much storage space:
	- Network-attached (EBS & [[EFS]])
	- Hardware (EC2 Instance Store)
- Network card: speed of the card, public IP address
- Firewall rules: [[EC2 Security Group|Security Groups]]
- Bootstrap script (configure at first launch): EC2 User Data

# EC2 User Data
It is possible to [[bootstrap]] our instances using an EC2 User Data script.

Bootstrapping in this case means launching commands when a machine starts, either through a provided script, or commands pasted in a provided text area. The script runs only once at the instance first start (first initialization).

It is used to automate boot tasks such as:
- Installing updates
- Installing software
- Downloading common files from the internet
- Anything, really...

Just know that the more you add, the slower it boots up because it has to do all those tasks.

The EC2 User Data Script runs with the root user, aka `sudo`.

# EC2 Instance Types
You can use many different types of EC2 instances that are optimized for different use cases (https://aws.amazon.com/ec2/instance-types)

For now there are 7 main types of EC2 instances:
- General Purpose
- Compute Optimized
- Memory Optimized
- Accelerated Computing
- Storage Optimized
- Instance Features
- Measuring Instance Performance

And within each of these, they are further categorized, for example, in General Purpose:
- Mac
- T4g
- T3
- T3a
- T2
- M6g
- etc.

There are a lot of these, so do your research and choose whichever is appropriate for your use case. There is a way to read this however, for example `m5.2xlarge`:
- `m`: instance class
- `5`: generation of instance class (`m4, m5, m6, etc.)
- `2xlarge`: size within the instance class
## General Purpose
Great for a diversity of workloads such as web servers or code repos. Strikes good balance between *Compute*, *Memory*, and *Networking*. For the course, we will use `t2.micro` which is a general purpose EC2 instance, that is part of the free tier.

## Compute Optimized
Great for compute-intensive tasks that require high-performance processors:
- Batch processing workloads
- Media transcoding
- High performance web servers
- High performance computing (HPC)
- Scientific modeling & [[ML]]
- Dedicated Gaming Servers

Mostly things that require tons of CPU power. For now, all their names start with `C`, e.g., `C5, C6gn, C6, etc.`

## Memory Optimized
Fast performance for workloads that process large datasets in memory (high RAM usage):
- High performance, relational/non-relational DBs
- Distributed web scale cache stores
- In-memory databases optimized for BI (Business Intelligence)
- Applications performing real-time processing of big unstructured data

Most of their names start with an `R` (`R6g, R5, R5a,...)`, but they also have some `X`, `Z`, and `High Memory`. Fuck these names man.

## Storage Optimized
Great for accessing large datasets, or storage-sensitive tasks that require high, sequential read/write access to large datasets on local storage.
- High frequency Online Transaction Processing (OLTP) systems
- Relational & NoSQL databases
- Cache for in-memory databases (e.g. Redis)
- Data warehousing applications
- Distributed file systems

Fuck the names, dw, it's like `i, H` or whatever.

## Examples:
![[{60C201E3-BD3D-483D-9AB4-53FB16636701}.png]]

Look at `t2.micro` and `t2.xlarge`. You can see that everything is much bigger for the `xlarge`, including CPU, RAM, Network, etc.

All the other ones are, in order: Compute-Optimized, Memory-Optimized, and... actually idk wtf that last one is, but it looks huge.

More information on all available instances can be found [here](https://instances.vantage.sh/)

# EC2 Instances Purchasing Options
You can optimize your spending by purchasing the instance types that work for your use case.
- On-demand instances (the one we're using) - short workload, predictable pricing, pay by second
- Reserved Instances (1 & 3 years)
	- Reserved Instances - used for long workloads
	- Convertible Reserved Instances - long workloads with flexible instances (allows changing type over time)
- Savings Plans (1 & 3 years) - commit to an amount of usage (in $) rather than a specific instance type, long workloads
- Spot Instances - very short workloads, very cheap, but can lose instances (less reliable)
- Dedicated Hosts - book an entire physical server, control instance placement (expensive af)
- Dedicated Instances - no other customer shares your hardware (also expensive af)
- Capacity Reservations - Reserve capacity in a specific AZ for any duration

## EC2 On Demand
- You basically pay for what you use
	- Linux / Windows - billing every second, after the first minute
	- Everything else - billing per hour
- Highest cost buuuuut... no upfront payment
- No long-term commitments

Recommended for short-term and uninterrupted workloads where you can't predict how the app will behave.

## EC2 Reserved Instances
### Reserved Instance
- Up to 72% cheaper vs On-Demand (value of discount can change)
- Reserve a specific instance attribute (Instance Type, Region, Tenancy, OS)
- Reservation period: 1 year (+discount) or 3 years (+++discount)
- Payment options: no upfront (+), partial upfront (++), all upfront (+++)
- Reserved Instance's Scope: Regional or Zonal (reserve capacity in an AZ)

Recommended for steady-state usage application (like DBs). You can sell and buy reserved instances in the Reserved Instance Marketplace

### Convertible Reserved Instance
- Can change EC2 instance type, family, OS, scope, and tenancy
- Up to 66% discount (value may vary)

## EC2 Savings Plans
- Get a discount for long-term use (up to 72% - same as RIs)
- Commit to a certain type of usage ($10/hour for 1 to 3 years)
- Usage beyond EC2 Savings Plans is billed at On-Demand price
 
- Locked to specific instance family & AWS region (e.g `M5` in `us-east-1`)
- Flexible across:
	- Instance Size (e.g., `m5.xlarge`, `m5.2xlarge`)
	- OS (e.g. Linux, Windows)
	- Tenancy (Host, Dedicated, Default)

## EC2 Spot Instances
- Can get huuuuuge discounts up to 90% (values may vary) compared to On-demand
- Instances that you can "lose" at any point if your max price is less than the current spot price
	- You're basically putting out a bid, and if the current bid is higher than yours, you're booted
- MOST cost-efficient instances in AWS

Useful for workloads resilient to failure
- Batch jobs
- Data analysis
- Image processing
- Any distributed workloads
- Workloads with flexible start and end time

Not suitable for critical jobs or databases

## EC2 Dedicated Hosts
- Physical server with EC2 instance capacity fully dedicated to your use 
- Allows you to address compliance reqs and use your existing server-bound software licenses (e.g. billing per-socket, per-core, VM software licenses)
- Purchasing options:
	- On-demand - pay per second for active Dedicated Host
	- Reserved - 1 or 3 years (No Upfront, Partial Upfront, All Upfront)
- The most expensive option

Useful for software that have complicated licensing model (BYOL - Bring your own license). Or for companies with strong regulatory or compliance needs.

## EC2 Dedicated Instances
- Instances that run on hardware dedicated to you. Not to be confused with Dedicated Hosts.
- May share hardware with other instances in the same account
- No control over instance placements (can move hardware after Stop / Start)

![[{26163270-9A42-4506-AE5A-77AA1276BC67}.png]]

Basically you're reserving an instance in a physical machine vs the entire machine itself. Since you're just renting an instance, they just reserve what you need, and thus you will probably still be sharing the tower with other instances. But your slot is yours and no one can take it.

Dedicated hosts on the other hand, rents the entire tower/machine that hosts your instances. Obviously with the entire machine, you have full control over the sockets, cores, etc. With an instance, you just pay per instance. With the whole tower, well... you get the idea.

tldr: It's like renting an instance with static IP forever vs renting the entire server tower.

## EC2 Capacity Reservation
Reserve *On-Demand* instances capacity in a specific AZ for any duration. In that way, you get access to the EC2 capacity whenever you need it.

There are no time commitments (create/cancel anytime), but no billing discounts. You're basically just telling them you're reserving space for your instances. 

If you do want discounts, you should pair this with Regional Reserved Instances & Savings Plans. And you'll be charged at On-Demand rates whether you run instances or not, soooo... think about it.

Suitable for short term, uninterrupted workloads that needs to be in a specific AZ.

## Which one works for me?
- On-Demand: Use whenever you like? Pay full price for the convenience
- Reserved: Planning ahead to use long term? You'll get a "loyalty" discount.
- Savings Plan: Pay a certain amount per hour for a specified amount of time, and use whatever you want within that limit
- Spot Instances: Bid for empty instances, highest bidder gets the instance spot and you get booted. Pretty cheap because they sell way under market price due to the volatility.
- Dedicated host: Get the entire server for yourself.
- Capacity Reservation: Book an instance, pay full price even if you don't live in it.

Example pricing model, for `m4.large` at `us-east-1`:
![[{E834D91E-53DB-47E7-BE6B-E456F61B9E40}.png]]

