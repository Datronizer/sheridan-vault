# Load balancing
## Introduction
A powerful technique used in server farms. Of course the name already tells you what it does: it balances workload, duh. "But how, Chien?" you ask. "Well, I don't fuckin know." I answer.

The way it actually does this is it will **split up the workload evenly to smaller instances to process load**. Here's how it works in detail.

Let's say you're Google with the IP 8.8.8.8, and the DNS `google.com`. You want global reach so you would set up multiple DNS identical server farms around the globe. But since each of these servers are different with different IPs, we need to use Anycast to cast your DNS `www.google.com` to these IPs to allow users from all over the world to access your site, regardless of their region. Since there are so many redundant server farms, assuming 1 dies, you'd still have a ton more to carry the load.

> [!important] Any server you can think of can have a load balancer. They're fundamentally the same, just different names and tools that do the same thing. 
## Definition
In the simplest sense possible: a load balancer balances workload/requests by splitting and sending them to smaller webservers based on where they need to go.
## Example
Let's say I own an AWS account with 3 webservers. Here's what I want:
- I allow HTTP (80) and HTTPS (443). 
- I want to send these requests to the appropriate webservers based on user request protocols. 
- I want the workload to be balanced.

I would set up 2 load balancers A and B. 
- A will check my webservers and see where it can send this new load so that it's all balanced. 
- B will check if this request is 80 or 443 and send it accordingly. 
- These two will intertwine and make sure your servers are never overloading (in theory) and will optimize where things go.
## AWS Elastic Load Balancer
For AWS, there is a thing called **Elastic Load Balancer** which automatically scales your server up and down based on use case; if it detects a dead instance, it terminates it and spins a new instance in its place. That's pretty sick actually.

This is probably why when you make a load balancer, you assign multiple IPs to it and it gives you back a DNS name. When you access this DNS, it routes you to each IP every time you refresh the page (which means it's working--this is the load balancer attempting to send you to a different IP each time to balance the workload).
## Load balancing HTTP
To do load balancing for HTTP, the Load Balancer would change the Proxy Forwarded Fields of the HTTP request as such. It modifies the X-Host, X-Proto, X-For fields of the request and sends it down to the appropriate webservers for processing. 
## Load balancing HTTPS
Same as HTTP but worse. Way worse. The biggest issue is because HTTPS is encrypted so this is done differently. 

HTTPS uses Security Certificates to prove the authenticiy of the web services and negotiate a secured TLS (Transport Layer Security) between client and webserver. There are 2 ways to do this:
- Pass HTTPS traffic through to the backend unaltered
- Terminate secure channel after verification => traffic between LB and server becomes cleartext. Requires the LB to have security certificates to access the request itself. 

Usually having the LB be the "security guard" is worse since it takes away the processing step from the servers and will be better for the individual servers, but it will tank LB performance since it now has to do double the work (balancing + deciphering).
## Health Checking
Since we want these load balancers to stay alive, we probably want them to stay alive. Thus **health checking** is another crucial component for this. The health check is surprisingly simple in theory. Send an HTTP request, and if an error (code 500 Cannot be reached) is returned, the server is considered dead. Else (code 200 OK) it's healthy. 

For a typical LB, if it sees a dead instance, it removes it from the pool of resources until it passes the health check. For AWS ELB, it kills that instance and replaces it with the new
## Decision Algorithms
### Round Robin
Let's say you have 3 servers A, B, and C. I use A, next person will be assigned B, then next next person will be assigned C, then it loops back to A for the next next next person. 

This is the default setup for AWS. Drawback is that it assumes everyone has the same length and communication volume, so it doesn't actually balance shit. It just sends you to the next available queue, like Ontario DriveTest (fuck DriveTest).
### Least Connection Algorithm
Checks each webserver for their current volume. If it's too heavy, send traffic to different server.

Fixes the length and volume of communication issue from **round robin**. Unfortunately is a huge waste of resources because it has to keep checking the volume
### Source IP checking
Keeps track of source IP of client to provide same server for different sessions. Can use cookies to provision webservers to client.
### Hash checking
Same as IP checking, but keeps track of a hash generated directly into the URL. If it sees that particular URL, it routes whatever user that was to the same session they had last time.

Example: I go to `urmom.com`. The site generates a token and puts it in the URL like `urmom.com/#/token-123abc`. Next time I go to the site using that token, it automatically routes me to my last session.
## Redundancy
Give 2 LBs, each its own IP, and link them together (logically, not physically ofc). Then give them a "shared" virtual IP. Make one of these the "master" load balancer. Ideally when you access the website, it goes to the virtual IP, then from there, it sends it to either LBs (with their own IPs). Then these LBs would do their job as usual.

Assuming the master LB dies, the other one would know (because it realizes the master one did not respond to health checks), so it turns itself into the master LB instead and takes over the workload from the other one. This allows for more stable uptime while your cloud engineer fixes the issue (aka doing his fucking job).