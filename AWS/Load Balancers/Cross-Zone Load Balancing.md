# Overview
## Thought problem
Let's say you have 2 LBs on 2 different AZs, like so:

![[Pasted image 20250921011910.png]]

You see that on AZ1, there's not that many instances, but AZ2, sheesh. What can you do here?

Well, Amazon already came up with a solution, which is **Cross-Zone Load Balancing**.
## How does it work?
I think this diagram explains it pretty nicely.

![[Pasted image 20250921012202.png]]

![[Pasted image 20250921012322.png]]

Simply put, with CZLB, the traffic is evenly distributed between ALL **connected** LBs and its EC2 instances, leading to a more even spread, even across regions.

Without CZLB, traffic is only evenly distributed within the AZs of the each LB, so some instances will receive more traffic than others. 

Is this absolutely necessary for you? NO.
This, as well as all other AWS provided services, are optional. Use if you want.

# Availability
- [[Application Load Balancer (v2)|ALBs]]
	- Enabled by default (can be disabled at the TG level)
	- No charges for inter-AZ data
- [[Network Load Balancer (v2)|NLBs]] & [[Gateway Load Balancer|GWLBs]]
	- Disabled by default
	- You pay charges for inter-AZ data if enabled
- CLBs
	- Disabled by default
	- No charges for inter-AZ data