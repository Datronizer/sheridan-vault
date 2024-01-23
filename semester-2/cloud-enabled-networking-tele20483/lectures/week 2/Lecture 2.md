So you know how we can spin up a VM and run it from the cloud? Well, clouds are super secure, and your PC might not be. How do we access the server?

There are 3 ways to do so:
- AWS GUI
- AWS CLI
- Python script

But these are just ways to develop. To actually access the server, you need to pass the [[firewall]]. To do so, you need to be allowed into a security group, think of it as a security badge. You have a badge, you can come in.

For exercise 1a, we need to allow all access (0.0.0.0) rather than a specific IP. Obviously this is to save you from the hassle of dynamic IP, and of course this is **NOT SECURE**. Bu for our temporary use case, it's all good :D.

# The cloud and the datacenter
The so-called cloud is actually a BUNCH of **computing & networking resources** located in multiple datacenters
The cloud provides an interface for users/developers accessing their networks.
## Location
As we've discussed, the location for these datacenters are important. Usually we want to place our centers somewhere cold, somewhere cheap, and somewhere politically stable. Of course this means Europe and North America most of the time. 

The locations of these servers are also strategically placed to piggyback off already available systems. For example, Seattle is a main hub for Canada and US, so as New York!

The location of a service might be determined by the traffic interests. Let's say Netflix. You can't have your favorite show have so much latency no?

The default region for AWS is U.S. East North Virginia. There are 48 availability zones (datacenters) there. It's also super close to the government who use these services also. 
## Physical setup
The datacenter usually prefers having their own electrical energy generation. It's mostly for quality purposes. Can't have the server die because the local government feels like it, yknow?
HVAC and fire supression is also required. You can probably guess why.
## Data Layer
The so called AWS **data layer** are rows and rows of computing and networking equipment. We're talking thousands of servers and computers hooked up to hundreds of switches.

Here's how they do it: 
Imagine a server tower. Okay, this tower has tons of computers stacked on top of each other. All the way at the top is a switch. These tower switches are called **leaves**. They're connected to switches hanging on the ceiling called **spines**. All leaves connect to spines and vice versa to maintain connectivity in case you own multiple VMs.
## Availablity Zones
An availability zone is one or more datacenters with redundant power, networking, and connectivity inside an AWS region.

The main idea is to provide redundancy and load distribution. If one server fails, we would still have a backup (for a price).
## AWS Regions
An AWS region is a geographical cluster of availability zones. As of Dec 2022, there are 22 in the world. 2023 now has 25. AND CALGARY STILL DOESN'T HAVE ONE AHAHAHA (Jan 2024).

It's good to imagine this as such. 3 datacenters in Viriginia are connected to each other, this is an availability zone. Now I hook 3 of these AZs up, that's an AWS region. 

## Extension of the availability zone concept
AWS wants
%% Fill in with powerpoint notes  %%

AWS local zones are extentions of Amazon AWS that deploys AWS compute, storage, database, resources, and services in proximity to some large population, industries and centers.

## AWS Outpost
Let's say you want to connect to the AWS server and you have own your own datacenter. Well, Amazon could through a tower your way that will connect their shit to your shit. Now you have redundancy which is good.

# Chapter 3
## Virtual Machine
A virtual machine (VM) is the emulation of a computer device running on another machine.
Even though the VM appears as a real computer to the user; it is mostly code running on the host.

More information available [[virtual machine]] %% Is this link missing? %%

## Chipset
