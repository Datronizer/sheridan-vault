---
aliases:
  - ELB
  - Elastic Load Balancer
  - AWS ELB
---
# What is Load Balancing?
A Load Balancer is a server that forwards traffic to multiple servers (EC2 instances) downstream.

Example:
3 users are trying to connect to an Elastic Load Balancer that has 3 EC2 instances hooked up to it.

1. User A accessing the ELB will be routed to the 1st EC2 instance. 
2. User B accessing the site after user A will have their traffic calculated by the ELB. 
3. The ELB sees that the load is unbalanced (2nd and 3rd still empty)
4. It sends user B to the 2nd EC2 instance. 
5. Similarly, user C goes to the 3rd instance.

It's important to note this is not exactly how the ELB works as there are other algorithms that measure load.

# Why use a Load Balancer?
For one, it is useful more managing traffic. It can spread load across multiple downstream instances to prevent overloading.

It also provides a single point of access ([[DNS]]) to your apps, meaning you don't need multiple DNSes for different [[Elastic Compute Cloud (EC2)|EC2]] instances. 

It can seamlessly handle failures of downstream instances, and route traffic to healthy instances instead. Which also means it can do regular health checks to your instances to make sure they're still alive.

You can also provide [[SSL]] termination ([[HTTPS]]) for your websites, enforce stickiness with cookies, ensure high availability across zones, and separate public traffic from private traffic. There are lots of ways to make your load balancer work for you.

# Why use an Elastic Load Balancer?
An Elastic Load Balancer is a managed load balancer:
- AWS guarantees that it will be working
- AWS takes care of upgrades, maintenance, and high availability
- AWS provides only a few configuration knobs

It costs less to setup your own load balancer, but will take up a lot more effort, also it might not be scalable.

ELBs are integrates with many AWS offerings, e.g.:
- EC2, [[AWS Auto-Scaling Group|EC2 Auto Scaling Groups]], [[Amazon ECS]]
- [[AWS Certificate Manager]], [[CloudWatch]]
- [[Route 53]], [[AWS WAF]], [[AWS Global Accelerator]]

# Health Checks
Your ELB will occasionally check if your EC2 instances are healthy because it will not send traffic to unhealthy instances otherwise.

They enable the LB to know if instances it forwards traffic to are available to reply to requests, and it is done on a port and a route (`/health` is common).

Example:
```mermaid.js
flowchart LR
ELB[Elastic Load Balancer] -- "`**Protocol**: HTTP
**Port**: 4567
**Endpoint**: */health*`" --> EC2[EC2 Instance]
```

If the response is not a 200 (OK), then the instance is unhealthy and no traffic will be sent there.

# Types of load balancers on AWS
There are 4 kinds of LBs managed by AWS:
- (*Deprecated*) Classic LB (v1 - old generation) - 2009 - CLB
	- HTTP, HTTPS, TCP, SSL (secure TCP)
- Application Load Balancer (v2 - new generation) - 2016 - ALB
	- HTTP, HTTPS, WebSocket
- Network Load Balancer (v2 - new generation) - 2017 - NLB
	- TCP, TLS (secure TCP), UDP
- Gateway Load Balancer - 2020 - GWLB
	- Operates at layer 3 (Network layer) - IP Protocol

It is almost always recommended to use the newer generation LBs as they provide more features. Some LBs can be set up as **internal** (private) or **external** (public) ELBS.

# Load Balancer Security Groups
The user can access your LB using HTTP and HTTPS anywhere, as such, your Load Balancer SG will look like so:

| Type  | Protocol | Port Range | Source    | Description               |
| ----- | -------- | ---------- | --------- | ------------------------- |
| HTTP  | TCP      | 80         | 0.0.0.0/0 | Allow HTTP from anywhere  |
| HTTPS | TCP      | 443        | 0.0.0.0/0 | Allow HTTPS from anywhere |
But the application itself should ONLY allow traffic from the LB and should NOT allow any other access to it.

| Type | Protocol | Port Range | Source                               | Description                           |
| ---- | -------- | ---------- | ------------------------------------ | ------------------------------------- |
| HTTP | TCP      | 80         | sg-902n2j0mg02930 (load-balancer-sg) | Allow traffic only from Load Balancer |

